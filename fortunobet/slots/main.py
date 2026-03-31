import logging
import asyncio
import json
import os
from datetime import date
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import Command, CommandObject
from aiogram.types import (
    LabeledPrice, PreCheckoutQuery, Message,
    InlineKeyboardButton, InlineKeyboardMarkup
)

# ─────────────────────────────────────────────────────────────────
#  CONFIGURATION  — only edit this section
# ─────────────────────────────────────────────────────────────────
TOKEN    = "8767986301:AAHpaeLqV0RG-2I5rYn3T18o9LFSOJoGqfI"
ADMIN_ID = 7627990095

# YOUR NEW WALLET 24 WORDS — replace each word with your new wallet words
# Example shown below — replace with YOUR new wallet mnemonic!
MNEMONIC = [
    "lawsuit",  "paddle",  "skull",  "autumn",  "embrace",  "urge",
    "wrist",  "spell",  "easily",  "vast", "poet", "clarify",
    "behind", "style", "icon", "oak", "recipe", "method",
    "coast", "gun", "family", "crop", "wrestle", "budget",
]
# Example (DO NOT USE — this is just to show format):
# MNEMONIC = [
#     "lawsuit", "paddle",  "skull",   "autumn", "embrace", "urge",
#     "wrist",   "spell",   "easily",  "vast",   "poet",    "clarify",
#     "behind",  "style",   "icon",    "oak",    "recipe",  "method",
#     "coast",   "gun",     "family",  "crop",   "wrestle", "budget",
# ]

# Exchange rate — how much TON per 500 spins
# Ideal rate explanation:
#   10 Stars = 100 spins (purchase price)
#   1 Telegram Star ≈ $0.013 USD
#   10 Stars ≈ $0.13 USD for 100 spins
#   500 spins = 5x that = ~$0.65 USD
#   1 TON ≈ $5 USD  →  500 spins = 0.13 TON  (good for players)
#   Use 0.1 TON per 500 spins to keep it attractive and profitable
SPINS_PER_TON = 500        # 500 spins = 1 TON  (you can change this)
MIN_WITHDRAW  = 500        # minimum spins to withdraw

# Slot win values (Telegram dice 1–64)
JACKPOT_VALUE  = 43        # shows 777 animation
BAR_VALUE      = 1         # shows BAR animation
FRUIT_VALUES   = {22, 64}  # shows fruit animation

# Win payouts in spins
JACKPOT_PAYOUT = 150
BAR_PAYOUT     = 40
FRUIT_PAYOUT   = 5

# Spin multiplier options (players can bet more at once)
BET_OPTIONS = [1, 5, 10, 25, 50]   # available bet sizes

DATA_FILE  = "user_data.json"
STATS_FILE = "stats.json"
# ─────────────────────────────────────────────────────────────────

bot = Bot(token=TOKEN)
dp  = Dispatcher()

# ── TON auto-payment setup ────────────────────────────────────────
try:
    from pytonlib import TonlibClient
    from tonsdk.crypto import mnemonic_to_wallet_key
    from tonsdk.contract.wallet import Wallets, WalletVersionEnum
    TON_AVAILABLE = True
except ImportError:
    TON_AVAILABLE = False
    logging.warning("pytonlib/tonsdk not installed — auto TON payment disabled. Run: pip install pytonlib tonsdk")

async def send_ton(to_address: str, amount_ton: float) -> bool:
    """Send TON automatically from admin wallet to user wallet."""
    if not TON_AVAILABLE:
        logging.error("TON libraries not installed!")
        return False
    try:
        mnemonics    = MNEMONIC
        pub_k, priv_k = mnemonic_to_wallet_key(mnemonics)
        _wallet_cls, _, _, wallet = Wallets.from_mnemonics(
            mnemonics, WalletVersionEnum.v4r2, workchain=0
        )
        # amount in nanoTON (1 TON = 1,000,000,000 nanoTON)
        nano_amount = int(amount_ton * 1_000_000_000)

        client = TonlibClient()
        await client.init()
        seqno = await client.run_get_method(
            address=wallet.address.to_string(True, True, True),
            method="seqno", stack=[]
        )
        query = wallet.create_transfer_message(
            to_addr=to_address,
            amount=nano_amount,
            seqno=int(seqno["stack"][0][1], 16),
            payload="FortunoBet Payout",
        )
        await client.raw_send_message(query["message"].to_boc(False))
        await client.close()
        return True
    except Exception as e:
        logging.error(f"TON send failed: {e}")
        return False

# ── Persistence ───────────────────────────────────────────────────

def _load(filepath) -> dict:
    if os.path.exists(filepath):
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {}

def _save(data: dict, filepath: str) -> None:
    tmp = filepath + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    os.replace(tmp, filepath)

user_data: dict = _load(DATA_FILE)
stats: dict     = _load(STATS_FILE)

if not stats:
    stats = {
        "total_players":      0,
        "total_spins_bought": 0,
        "total_referrals":    0,
        "total_spins_played": 0,
        "total_jackpots":     0,
        "total_bar_wins":     0,
        "total_fruit_wins":   0,
        "total_ton_paid":     0.0,
        "daily_active":       {},
        "purchases":          [],
    }

def save_all():
    _save(user_data, DATA_FILE)
    _save(stats,     STATS_FILE)

def get_user(user_id: int) -> dict:
    uid = str(user_id)
    if uid not in user_data:
        user_data[uid] = {
            "spins":              0,
            "ever_started":       False,
            "pending_withdrawal": False,
            "pending_spins":      0,
            "pending_wallet":     None,
            "referrals":          0,
            "referred_by":        None,
            "joined_date":        str(date.today()),
            "total_spins_played": 0,
            "total_won":          0,
            "purchases":          0,
            "banned":             False,
            "bet_size":           1,       # default bet = 1 spin
        }
        stats["total_players"] += 1
        save_all()
    return user_data[uid]

def track_daily(user_id: int):
    today = str(date.today())
    if today not in stats["daily_active"]:
        stats["daily_active"][today] = []
    uid = str(user_id)
    if uid not in stats["daily_active"][today]:
        stats["daily_active"][today].append(uid)

def spins_to_ton(spins: int) -> float:
    """Convert spins to TON amount."""
    return round(spins / SPINS_PER_TON, 4)

# ── Keyboards ─────────────────────────────────────────────────────

def main_kb(user_id: int) -> InlineKeyboardMarkup:
    ref_link = f"https://t.me/FortunoSlotsbot?start={user_id}"
    user     = get_user(user_id)
    bet      = user.get("bet_size", 1)
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"🎰 SPIN  (Bet: {bet} spin{'s' if bet > 1 else ''})", callback_data="spin")],
        [InlineKeyboardButton(text="🎲 CHANGE BET", callback_data="change_bet")],
        [InlineKeyboardButton(text="💎 BUY 100 SPINS — 10 Stars", callback_data="buy")],
        [InlineKeyboardButton(text="💸 WITHDRAW WINNINGS", callback_data="withdraw_req")],
        [InlineKeyboardButton(text="📊 MY STATS", callback_data="my_stats")],
        [InlineKeyboardButton(text="📢 INVITE FOR 5 SPINS", url=f"https://t.me/share/url?url={ref_link}")],
    ])

def no_spins_kb(user_id: int) -> InlineKeyboardMarkup:
    ref_link = f"https://t.me/FortunoSlotsbot?start={user_id}"
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💎 BUY 100 SPINS — 10 Stars", callback_data="buy")],
        [InlineKeyboardButton(text="📢 INVITE A FRIEND (+5 SPINS)", url=f"https://t.me/share/url?url={ref_link}")],
        [InlineKeyboardButton(text="📊 MY STATS", callback_data="my_stats")],
    ])

def bet_kb() -> InlineKeyboardMarkup:
    buttons = []
    for bet in BET_OPTIONS:
        buttons.append(InlineKeyboardButton(
            text=f"{'⚡' if bet >= 25 else '🎯' if bet >= 10 else '🎲'} {bet} Spin{'s' if bet > 1 else ''}  {'(x'+str(bet)+' win)' if bet > 1 else '(normal)'}",
            callback_data=f"bet_{bet}"
        ))
    return InlineKeyboardMarkup(inline_keyboard=[[b] for b in buttons] + [
        [InlineKeyboardButton(text="🔙 BACK", callback_data="back_main")]
    ])

spin_again_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🎰 SPIN AGAIN", callback_data="spin")],
    [InlineKeyboardButton(text="🎲 CHANGE BET", callback_data="change_bet")],
    [InlineKeyboardButton(text="💎 BUY SPINS",  callback_data="buy")],
])

# ── /start ────────────────────────────────────────────────────────

@dp.message(Command("start"))
async def cmd_start(message: Message, command: CommandObject):
    user_id = message.from_user.id
    user    = get_user(user_id)

    is_new = not user.get("ever_started", False)
    if is_new:
        user["spins"]        = 10
        user["ever_started"] = True

    if command.args and is_new:
        try:
            ref_id = int(command.args)
            if ref_id != user_id:
                ref = get_user(ref_id)
                ref["spins"]        += 5
                ref["referrals"]    += 1
                user["referred_by"]  = ref_id
                stats["total_referrals"] += 1
                save_all()
                await bot.send_message(
                    ref_id,
                    f"🎊 *Friend joined using your link!*\n"
                    f"*+5 FREE SPINS* added!\n"
                    f"💰 Your balance: *{ref['spins']}* spins\n"
                    f"👥 Total friends invited: *{ref['referrals']}*",
                    parse_mode="Markdown"
                )
        except (ValueError, TypeError):
            pass

    track_daily(user_id)
    save_all()

    await message.answer(
        "🎰 *WELCOME TO FORTUNOBET* 🎰\n\n"
        "High RTP Slots | Instant TON Payouts\n\n"
        f"💰 *Your Balance:* {user['spins']} Spins\n"
        f"{'🆕 *You got 10 FREE spins to start!* 🎁' if is_new else ''}\n\n"
        f"📌 *How it works:*\n"
        f"🎰 Spin to win spins\n"
        f"🏆 Reach {MIN_WITHDRAW} spins → Withdraw as TON\n"
        f"📢 Invite friends → Get +5 spins each\n"
        f"🎲 Change your bet size for bigger wins!",
        reply_markup=main_kb(user_id),
        parse_mode="Markdown",
    )

# ── Change bet ────────────────────────────────────────────────────

@dp.callback_query(F.data == "change_bet")
async def change_bet_menu(callback: types.CallbackQuery):
    user = get_user(callback.from_user.id)
    await callback.message.answer(
        "🎲 *SELECT YOUR BET SIZE*\n\n"
        "Higher bet = more spins used per spin BUT wins are multiplied!\n\n"
        f"Your balance: *{user['spins']}* spins\n\n"
        "Example with 10x bet:\n"
        "❌ Lose = -10 spins\n"
        f"✨ Fruit win = +{FRUIT_PAYOUT * 10} spins\n"
        f"💎 Bar win = +{BAR_PAYOUT * 10} spins\n"
        f"🔥 Jackpot = +{JACKPOT_PAYOUT * 10} spins",
        reply_markup=bet_kb(),
        parse_mode="Markdown",
    )
    await callback.answer()

@dp.callback_query(F.data.startswith("bet_"))
async def set_bet(callback: types.CallbackQuery):
    user     = get_user(callback.from_user.id)
    bet_size = int(callback.data.split("_")[1])
    user["bet_size"] = bet_size
    save_all()
    await callback.message.answer(
        f"✅ *Bet set to {bet_size} spin{'s' if bet_size > 1 else ''}!*\n\n"
        f"💰 Your balance: *{user['spins']}* spins\n"
        f"🎰 Each spin costs *{bet_size}* spins\n"
        f"🔥 Jackpot win = *+{JACKPOT_PAYOUT * bet_size}* spins\n"
        f"💎 Bar win = *+{BAR_PAYOUT * bet_size}* spins\n"
        f"✨ Fruit win = *+{FRUIT_PAYOUT * bet_size}* spins",
        reply_markup=main_kb(callback.from_user.id),
        parse_mode="Markdown",
    )
    await callback.answer(f"Bet set to {bet_size}x!")

# ── Spin ──────────────────────────────────────────────────────────

@dp.callback_query(F.data == "spin")
async def play_slots(callback: types.CallbackQuery):
    user_id  = callback.from_user.id
    user     = get_user(user_id)
    bet_size = user.get("bet_size", 1)

    if user.get("banned"):
        await callback.answer("🚫 You are banned.", show_alert=True)
        return

    # Not enough spins
    if user["spins"] < bet_size:
        await callback.message.answer(
            f"😢 *You ran out of spins!*\n\n"
            f"Your balance: *{user['spins']}* spins\n"
            f"Your bet: *{bet_size}* spins\n\n"
            f"Don't stop now — you could be one spin away from the JACKPOT! 🔥\n\n"
            f"👇 *Get more spins:*\n"
            f"💎 Buy 100 spins for just *10 Telegram Stars*\n"
            f"📢 Invite a friend → get *+5 FREE spins*",
            reply_markup=no_spins_kb(user_id),
            parse_mode="Markdown",
        )
        await callback.answer("❌ Not enough spins!", show_alert=False)
        return

    # Deduct bet
    user["spins"]             -= bet_size
    user["total_spins_played"] = user.get("total_spins_played", 0) + bet_size
    stats["total_spins_played"] = stats.get("total_spins_played", 0) + bet_size
    track_daily(user_id)
    save_all()

    msg   = await callback.message.answer_dice(emoji="🎰")
    value = msg.dice.value
    await asyncio.sleep(2.5)

    if value == JACKPOT_VALUE:
        win_amount = JACKPOT_PAYOUT * bet_size
        win_text   = f"🔥 *JACKPOT! 7️⃣7️⃣7️⃣*\n+{win_amount} SPINS!"
        stats["total_jackpots"] = stats.get("total_jackpots", 0) + 1
    elif value == BAR_VALUE:
        win_amount = BAR_PAYOUT * bet_size
        win_text   = f"💎 *BAR WIN!*\n+{win_amount} SPINS!"
        stats["total_bar_wins"] = stats.get("total_bar_wins", 0) + 1
    elif value in FRUIT_VALUES:
        win_amount = FRUIT_PAYOUT * bet_size
        win_text   = f"✨ *FRUIT WIN!*\n+{win_amount} SPINS!"
        stats["total_fruit_wins"] = stats.get("total_fruit_wins", 0) + 1
    else:
        win_amount = 0
        win_text   = "❌ *No win.* Try again!"

    user["spins"]    += win_amount
    user["total_won"] = user.get("total_won", 0) + win_amount
    save_all()

    # Show withdraw hint when close to minimum
    withdraw_hint = ""
    if MIN_WITHDRAW - 50 <= user["spins"] < MIN_WITHDRAW:
        withdraw_hint = f"\n\n🔥 *Almost there!* You need {MIN_WITHDRAW - user['spins']} more spins to withdraw!"
    elif user["spins"] >= MIN_WITHDRAW:
        withdraw_hint = f"\n\n💸 *You can withdraw now!* Press WITHDRAW WINNINGS!"

    await callback.message.answer(
        f"{win_text}\n\n"
        f"💰 *Balance:* {user['spins']} Spins"
        f"{withdraw_hint}",
        reply_markup=spin_again_kb,
        parse_mode="Markdown",
    )
    await callback.answer()

# ── My Stats ──────────────────────────────────────────────────────

@dp.callback_query(F.data == "my_stats")
async def my_stats(callback: types.CallbackQuery):
    user_id  = callback.from_user.id
    user     = get_user(user_id)
    ref_link = f"https://t.me/FortunoSlotsbot?start={user_id}"
    ton_value = spins_to_ton(user["spins"])

    await callback.message.answer(
        f"📊 *YOUR STATS*\n\n"
        f"💰 Balance: *{user['spins']}* spins (~*{ton_value} TON*)\n"
        f"🎰 Total spins played: *{user.get('total_spins_played', 0)}*\n"
        f"🏆 Total spins won: *{user.get('total_won', 0)}*\n"
        f"🎲 Current bet size: *{user.get('bet_size', 1)}x*\n"
        f"👥 Friends invited: *{user.get('referrals', 0)}*\n"
        f"💎 Purchases made: *{user.get('purchases', 0)}*\n"
        f"📅 Joined: *{user.get('joined_date', 'N/A')}*\n\n"
        f"📌 *Withdraw at {MIN_WITHDRAW} spins = {spins_to_ton(MIN_WITHDRAW)} TON*\n"
        f"You need *{max(0, MIN_WITHDRAW - user['spins'])}* more spins!\n\n"
        f"🔗 *Your invite link:*\n`{ref_link}`",
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="📢 SHARE MY INVITE LINK", url=f"https://t.me/share/url?url={ref_link}")],
            [InlineKeyboardButton(text="🔙 BACK", callback_data="back_main")],
        ])
    )
    await callback.answer()

@dp.callback_query(F.data == "back_main")
async def back_main(callback: types.CallbackQuery):
    user = get_user(callback.from_user.id)
    await callback.message.answer(
        f"🎰 *FORTUNOBET*\n\n💰 *Balance:* {user['spins']} Spins",
        reply_markup=main_kb(callback.from_user.id),
        parse_mode="Markdown",
    )
    await callback.answer()

# ── Withdraw ──────────────────────────────────────────────────────

@dp.callback_query(F.data == "withdraw_req")
async def withdraw_info(callback: types.CallbackQuery):
    user     = get_user(callback.from_user.id)
    ton_val  = spins_to_ton(user["spins"])

    if user["spins"] < MIN_WITHDRAW:
        needed = MIN_WITHDRAW - user["spins"]
        await callback.message.answer(
            f"💸 *WITHDRAWAL*\n\n"
            f"❌ You need *{MIN_WITHDRAW} spins* to withdraw.\n\n"
            f"Your balance: *{user['spins']}* spins\n"
            f"You need *{needed}* more spins!\n\n"
            f"*{MIN_WITHDRAW} spins = {spins_to_ton(MIN_WITHDRAW)} TON*\n\n"
            f"Keep spinning or invite friends! 💪",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="🎰 KEEP SPINNING", callback_data="spin")],
                [InlineKeyboardButton(text="💎 BUY SPINS", callback_data="buy")],
            ])
        )
        await callback.answer()
        return

    if user.get("pending_withdrawal"):
        await callback.answer("⏳ You already have a pending withdrawal!", show_alert=True)
        return

    await callback.message.answer(
        f"💸 *WITHDRAWAL REQUEST*\n\n"
        f"✅ Your balance: *{user['spins']} spins*\n"
        f"💎 You will receive: *{ton_val} TON*\n\n"
        f"Please send your *TON Wallet Address* below.\n"
        f"_(Starts with UQ, EQ, or 0Q)_",
        parse_mode="Markdown",
    )
    await callback.answer()

@dp.message(F.text.regexp(r"^(UQ|EQ|0Q)[\w-]{46,}$"))
async def handle_wallet(message: Message):
    user_id = message.from_user.id
    user    = get_user(user_id)

    if user["spins"] < MIN_WITHDRAW or user.get("pending_withdrawal"):
        return

    ton_amount = spins_to_ton(user["spins"])
    user["pending_withdrawal"] = True
    user["pending_spins"]      = user["spins"]
    user["pending_wallet"]     = message.text
    save_all()

    await bot.send_message(
        ADMIN_ID,
        f"🚨 *PAYOUT NEEDED!*\n"
        f"User: {message.from_user.full_name}\n"
        f"ID: `{user_id}`\n"
        f"Spins: *{user['spins']}*\n"
        f"TON amount: *{ton_amount} TON*\n"
        f"Wallet: `{message.text}`\n\n"
        f"Type `/pay {user_id}` to send TON automatically!",
        parse_mode="Markdown",
    )
    await message.answer(
        f"✅ *Request received!*\n"
        f"Amount: *{ton_amount} TON*\n"
        f"Processing within 24 hours. 🙏",
        parse_mode="Markdown",
    )

# ── Admin: /pay (AUTO TON SEND) ───────────────────────────────────

@dp.message(Command("pay"))
async def admin_pay(message: Message):
    if message.from_user.id != ADMIN_ID:
        return
    try:
        target_id = str(int(message.text.split()[1]))
        user      = user_data.get(target_id)
        if not user:
            await message.answer("❌ User not found.")
            return
        if not user.get("pending_withdrawal"):
            await message.answer("❌ No pending withdrawal for this user.")
            return

        wallet     = user.get("pending_wallet")
        ton_amount = spins_to_ton(user.get("pending_spins", 0))

        if not wallet:
            await message.answer("❌ No wallet address found for this user.")
            return

        await message.answer(
            f"⏳ Sending *{ton_amount} TON* to `{wallet}`...",
            parse_mode="Markdown"
        )

        # AUTO SEND TON
        success = await send_ton(wallet, ton_amount)

        if success:
            user["spins"]             -= user.get("pending_spins", 0)
            user["pending_withdrawal"] = False
            user["pending_spins"]      = 0
            user["pending_wallet"]     = None
            stats["total_ton_paid"]    = stats.get("total_ton_paid", 0) + ton_amount
            save_all()

            await message.answer(
                f"✅ *Payment sent!*\n"
                f"Amount: *{ton_amount} TON*\n"
                f"Wallet: `{wallet}`",
                parse_mode="Markdown"
            )
            await bot.send_message(
                int(target_id),
                f"💸 *Your withdrawal is complete!*\n"
                f"*{ton_amount} TON* has been sent to your wallet!\n"
                f"Thank you for playing FortunoBet! 🎰",
                parse_mode="Markdown",
            )
        else:
            await message.answer(
                f"❌ *Auto payment failed!*\n\n"
                f"Please send manually:\n"
                f"Amount: *{ton_amount} TON*\n"
                f"Wallet: `{wallet}`\n\n"
                f"Then type `/paydone {target_id}` to confirm.",
                parse_mode="Markdown"
            )
    except (IndexError, ValueError):
        await message.answer("Usage: `/pay [user_id]`", parse_mode="Markdown")

# ── Admin: /paydone (manual confirm fallback) ─────────────────────

@dp.message(Command("paydone"))
async def admin_paydone(message: Message):
    if message.from_user.id != ADMIN_ID:
        return
    try:
        target_id = str(int(message.text.split()[1]))
        user      = user_data.get(target_id)
        if not user:
            await message.answer("❌ User not found.")
            return
        ton_amount = spins_to_ton(user.get("pending_spins", 0))
        user["spins"]             -= user.get("pending_spins", 0)
        user["pending_withdrawal"] = False
        user["pending_spins"]      = 0
        user["pending_wallet"]     = None
        stats["total_ton_paid"]    = stats.get("total_ton_paid", 0) + ton_amount
        save_all()
        await message.answer(f"✅ Marked as paid manually. {ton_amount} TON for user {target_id}.")
        await bot.send_message(
            int(target_id),
            f"💸 *Your withdrawal is complete!*\n"
            f"*{ton_amount} TON* sent to your wallet!\n"
            f"Thank you for playing! 🎰",
            parse_mode="Markdown",
        )
    except (IndexError, ValueError):
        await message.answer("Usage: `/paydone [user_id]`", parse_mode="Markdown")

# ── Admin: /admin dashboard ───────────────────────────────────────

@dp.message(Command("admin"))
async def admin_dashboard(message: Message):
    if message.from_user.id != ADMIN_ID:
        return

    today        = str(date.today())
    active_today = len(stats["daily_active"].get(today, []))
    pending      = [(uid, u) for uid, u in user_data.items() if u.get("pending_withdrawal")]

    top_players = sorted(user_data.items(), key=lambda x: x[1].get("spins", 0), reverse=True)[:5]
    top_refs    = sorted(user_data.items(), key=lambda x: x[1].get("referrals", 0), reverse=True)[:5]

    top_text = "\n".join([f"  {i+1}. `{uid}` — {u.get('spins',0)} spins" for i, (uid, u) in enumerate(top_players)])
    ref_text = "\n".join([f"  {i+1}. `{uid}` — {u.get('referrals',0)} referrals" for i, (uid, u) in enumerate(top_refs)])
    pend_text = "\n".join([f"  • `{uid}` — {spins_to_ton(u.get('pending_spins',0))} TON" for uid, u in pending]) or "  None ✅"

    await message.answer(
        f"🔐 *ADMIN DASHBOARD*\n"
        f"━━━━━━━━━━━━━━━━━━━━\n\n"
        f"👥 *PLAYERS*\n"
        f"  Total: *{stats['total_players']}*\n"
        f"  Active today: *{active_today}*\n"
        f"  Total referrals: *{stats['total_referrals']}*\n\n"
        f"🎰 *GAME STATS*\n"
        f"  Spins played: *{stats.get('total_spins_played', 0)}*\n"
        f"  Jackpots: *{stats.get('total_jackpots', 0)}*\n"
        f"  Bar wins: *{stats.get('total_bar_wins', 0)}*\n"
        f"  Fruit wins: *{stats.get('total_fruit_wins', 0)}*\n\n"
        f"💎 *MONEY*\n"
        f"  Spins sold: *{stats.get('total_spins_bought', 0)}*\n"
        f"  TON paid out: *{stats.get('total_ton_paid', 0)} TON*\n\n"
        f"💸 *PENDING PAYOUTS*\n{pend_text}\n\n"
        f"🏆 *TOP 5 PLAYERS*\n{top_text}\n\n"
        f"📢 *TOP 5 REFERRERS*\n{ref_text}\n\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"🛠 *COMMANDS*\n"
        f"`/pay [id]` — auto send TON\n"
        f"`/paydone [id]` — manual confirm\n"
        f"`/gift [id] [spins]` — give spins\n"
        f"`/ban [id]` — ban user\n"
        f"`/unban [id]` — unban user\n"
        f"`/broadcast [msg]` — message all",
        parse_mode="Markdown",
    )

# ── Admin: /gift ──────────────────────────────────────────────────

@dp.message(Command("gift"))
async def admin_gift(message: Message):
    if message.from_user.id != ADMIN_ID:
        return
    try:
        parts     = message.text.split()
        target_id = str(int(parts[1]))
        amount    = int(parts[2])
        user      = get_user(int(target_id))
        user["spins"] += amount
        save_all()
        await message.answer(f"✅ Added *{amount}* spins to `{target_id}`. New balance: *{user['spins']}*.", parse_mode="Markdown")
        await bot.send_message(int(target_id), f"🎁 *You received {amount} free spins!*\n💰 Balance: {user['spins']} spins\nGood luck! 🎰", parse_mode="Markdown")
    except (IndexError, ValueError):
        await message.answer("Usage: `/gift [user_id] [amount]`", parse_mode="Markdown")

# ── Admin: /ban /unban ────────────────────────────────────────────

@dp.message(Command("ban"))
async def admin_ban(message: Message):
    if message.from_user.id != ADMIN_ID:
        return
    try:
        target_id = str(int(message.text.split()[1]))
        user = get_user(int(target_id))
        user["banned"] = True
        save_all()
        await message.answer(f"🚫 User `{target_id}` banned.", parse_mode="Markdown")
    except (IndexError, ValueError):
        await message.answer("Usage: `/ban [user_id]`", parse_mode="Markdown")

@dp.message(Command("unban"))
async def admin_unban(message: Message):
    if message.from_user.id != ADMIN_ID:
        return
    try:
        target_id = str(int(message.text.split()[1]))
        user = get_user(int(target_id))
        user["banned"] = False
        save_all()
        await message.answer(f"✅ User `{target_id}` unbanned.", parse_mode="Markdown")
    except (IndexError, ValueError):
        await message.answer("Usage: `/unban [user_id]`", parse_mode="Markdown")

# ── Admin: /broadcast ─────────────────────────────────────────────

@dp.message(Command("broadcast"))
async def admin_broadcast(message: Message):
    if message.from_user.id != ADMIN_ID:
        return
    try:
        text = message.text.split(" ", 1)[1]
    except IndexError:
        await message.answer("Usage: `/broadcast [message]`", parse_mode="Markdown")
        return

    sent = failed = 0
    for uid in user_data:
        if user_data[uid].get("banned"):
            continue
        try:
            await bot.send_message(int(uid), f"📢 *FortunoBet:*\n\n{text}", parse_mode="Markdown")
            sent += 1
            await asyncio.sleep(0.05)
        except Exception:
            failed += 1

    await message.answer(f"✅ Sent: *{sent}* | Failed: *{failed}*", parse_mode="Markdown")

# ── Stars payment ──────────────────────────────────────────────────

@dp.callback_query(F.data == "buy")
async def process_buy(callback: types.CallbackQuery):
    await bot.send_invoice(
        callback.message.chat.id,
        title="100 Spins",
        description="100 credits for FortunoBet slots",
        payload="buy_100",
        provider_token="",
        currency="XTR",
        prices=[LabeledPrice(label="100 Spins", amount=10)],
    )
    await callback.answer()

@dp.pre_checkout_query()
async def pre_check(q: PreCheckoutQuery):
    await q.answer(ok=True)

@dp.message(F.successful_payment)
async def success_pay(m: Message):
    user = get_user(m.from_user.id)
    user["spins"]    += 100
    user["purchases"] = user.get("purchases", 0) + 1
    stats["total_spins_bought"] = stats.get("total_spins_bought", 0) + 100
    save_all()
    await m.answer(
        f"✅ *100 Spins added!*\n💰 Balance: *{user['spins']}* spins\nGood luck! 🎰",
        parse_mode="Markdown",
    )

# ── Main ───────────────────────────────────────────────────────────

async def main():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
    logging.info("FortunoBet FULL VERSION is online.")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

    
# /gift 7627990095 50
# /admin — full dashboard
# /broadcast [message] — send a message to ALL users at once
# /ban [user_id] — ban a cheater
# /unban [user_id] — unban them
# /gift and /pay — same as before