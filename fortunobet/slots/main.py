import logging
import asyncio
import json
import os
from datetime import datetime, date
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import Command, CommandObject
from aiogram.types import (
    LabeledPrice, PreCheckoutQuery, Message,
    InlineKeyboardButton, InlineKeyboardMarkup
)

# ─────────────────────────────────────────────
TOKEN    = "8767986301:AAHpaeLqV0RG-2I5rYn3T18o9LFSOJoGqfI"
ADMIN_ID = 7627990095
# ─────────────────────────────────────────────

JACKPOT_VALUE  = 43
BAR_VALUE      = 1
FRUIT_VALUES   = {22, 64}

JACKPOT_PAYOUT = 150
BAR_PAYOUT     = 40
FRUIT_PAYOUT   = 5
WITHDRAW_MIN   = 500

DATA_FILE  = "user_data.json"
STATS_FILE = "stats.json"

bot = Bot(token=TOKEN)
dp  = Dispatcher()

# ── Persistence ──────────────────────────────

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

# Initialize stats if empty
if not stats:
    stats = {
        "total_players":   0,
        "total_spins_bought": 0,
        "total_referrals": 0,
        "total_spins_played": 0,
        "total_jackpots":  0,
        "total_bar_wins":  0,
        "total_fruit_wins":0,
        "daily_active":    {},   # { "2024-01-01": [user_id, ...] }
        "purchases":       [],   # list of { user_id, amount, date }
    }

def save_all():
    _save(user_data, DATA_FILE)
    _save(stats, STATS_FILE)

def get_user(user_id: int) -> dict:
    uid = str(user_id)
    if uid not in user_data:
        user_data[uid] = {
            "spins":               0,
            "ever_started":        False,
            "pending_withdrawal":  False,
            "pending_spins":       0,
            "referrals":           0,      # how many friends this user invited
            "referred_by":         None,   # who invited this user
            "joined_date":         str(date.today()),
            "total_spins_played":  0,
            "total_won":           0,
            "purchases":           0,      # how many times bought spins
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

# ── Keyboards ────────────────────────────────

def main_kb(user_id: int) -> InlineKeyboardMarkup:
    ref_link = f"https://t.me/FortunoSlotsbot?start={user_id}"
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🎰 SPIN (1 Credit)", callback_data="spin")],
        [InlineKeyboardButton(text="💎 BUY 100 SPINS — 10 Stars", callback_data="buy")],
        [InlineKeyboardButton(text="💸 WITHDRAW WINNINGS", callback_data="withdraw_req")],
        [InlineKeyboardButton(text="📊 MY STATS", callback_data="my_stats")],
        [InlineKeyboardButton(text="📢 INVITE FOR 5 SPINS", url=f"https://t.me/share/url?url={ref_link}")],
    ])

def no_spins_kb(user_id: int) -> InlineKeyboardMarkup:
    """Special keyboard shown when user runs out of spins."""
    ref_link = f"https://t.me/FortunoSlotsbot?start={user_id}"
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💎 BUY 100 SPINS — 10 Stars", callback_data="buy")],
        [InlineKeyboardButton(text="📢 INVITE A FRIEND (+5 SPINS)", url=f"https://t.me/share/url?url={ref_link}")],
        [InlineKeyboardButton(text="📊 SEE MY STATS", callback_data="my_stats")],
    ])

spin_again_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🎰 SPIN AGAIN", callback_data="spin")],
    [InlineKeyboardButton(text="💎 BUY SPINS",  callback_data="buy")],
])

# ── /start ───────────────────────────────────

@dp.message(Command("start"))
async def cmd_start(message: Message, command: CommandObject):
    user_id = message.from_user.id
    user    = get_user(user_id)

    is_new = not user.get("ever_started", False)
    if is_new:
        user["spins"]        = 10
        user["ever_started"] = True

    # Referral bonus
    if command.args and is_new:
        try:
            ref_id = int(command.args)
            if ref_id != user_id:
                ref = get_user(ref_id)
                ref["spins"]     += 5
                ref["referrals"] += 1
                user["referred_by"] = ref_id
                stats["total_referrals"] += 1
                save_all()
                await bot.send_message(
                    ref_id,
                    f"🎊 *Bonus!* A friend joined using your link!\n"
                    f"*+5 FREE SPINS* added to your balance!\n"
                    f"💰 Your balance: {ref['spins']} spins\n\n"
                    f"You have invited *{ref['referrals']}* friend(s) total!",
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
        f"{'🆕 You got 10 FREE spins to start!' if is_new else ''}",
        reply_markup=main_kb(user_id),
        parse_mode="Markdown",
    )

# ── /balance ─────────────────────────────────

@dp.message(Command("balance"))
async def cmd_balance(message: Message):
    user = get_user(message.from_user.id)
    track_daily(message.from_user.id)
    save_all()
    await message.answer(
        f"💰 *Your Balance:* {user['spins']} Spins",
        parse_mode="Markdown",
        reply_markup=main_kb(message.from_user.id),
    )

# ── My Stats ─────────────────────────────────

@dp.callback_query(F.data == "my_stats")
async def my_stats(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user    = get_user(user_id)
    ref_link = f"https://t.me/FortunoSlotsbot?start={user_id}"

    await callback.message.answer(
        f"📊 *YOUR STATS*\n\n"
        f"💰 Balance: *{user['spins']}* spins\n"
        f"🎰 Total spins played: *{user.get('total_spins_played', 0)}*\n"
        f"🏆 Total spins won: *{user.get('total_won', 0)}*\n"
        f"👥 Friends invited: *{user.get('referrals', 0)}*\n"
        f"💎 Purchases made: *{user.get('purchases', 0)}*\n"
        f"📅 Joined: *{user.get('joined_date', 'N/A')}*\n\n"
        f"🔗 *Your invite link:*\n`{ref_link}`\n\n"
        f"_Invite friends and get +5 spins per friend!_",
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="📢 SHARE MY LINK", url=f"https://t.me/share/url?url={ref_link}")],
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

# ── Spin ─────────────────────────────────────

@dp.callback_query(F.data == "spin")
async def play_slots(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user    = get_user(user_id)

    # ── NO SPINS — show special offer screen ──
    if user["spins"] < 1:
        await callback.message.answer(
            "😢 *You ran out of spins!*\n\n"
            "Don't stop now — you could be one spin away from the JACKPOT! 🔥\n\n"
            "👇 *Get more spins:*\n"
            "💎 Buy 100 spins for just *10 Telegram Stars*\n"
            "📢 Invite a friend and get *+5 FREE spins*",
            reply_markup=no_spins_kb(user_id),
            parse_mode="Markdown",
        )
        await callback.answer("❌ No spins left!", show_alert=False)
        return

    user["spins"] -= 1
    user["total_spins_played"] = user.get("total_spins_played", 0) + 1
    stats["total_spins_played"] = stats.get("total_spins_played", 0) + 1
    track_daily(user_id)
    save_all()

    msg   = await callback.message.answer_dice(emoji="🎰")
    value = msg.dice.value
    await asyncio.sleep(2.5)

    if value == JACKPOT_VALUE:
        win_amount = JACKPOT_PAYOUT
        win_text   = f"🔥 *JACKPOT! 7️⃣7️⃣7️⃣*\n+{JACKPOT_PAYOUT} SPINS!"
        stats["total_jackpots"] = stats.get("total_jackpots", 0) + 1
    elif value == BAR_VALUE:
        win_amount = BAR_PAYOUT
        win_text   = f"💎 *BAR WIN!*\n+{BAR_PAYOUT} SPINS!"
        stats["total_bar_wins"] = stats.get("total_bar_wins", 0) + 1
    elif value in FRUIT_VALUES:
        win_amount = FRUIT_PAYOUT
        win_text   = f"✨ *FRUIT WIN!*\n+{FRUIT_PAYOUT} SPINS!"
        stats["total_fruit_wins"] = stats.get("total_fruit_wins", 0) + 1
    else:
        win_amount = 0
        win_text   = "❌ *No win.* Try again!"

    user["spins"]     += win_amount
    user["total_won"]  = user.get("total_won", 0) + win_amount
    save_all()

    await callback.message.answer(
        f"{win_text}\n\n💰 *Balance:* {user['spins']} Spins",
        reply_markup=spin_again_kb,
        parse_mode="Markdown",
    )
    await callback.answer()

# ── Withdraw ─────────────────────────────────

@dp.callback_query(F.data == "withdraw_req")
async def withdraw_info(callback: types.CallbackQuery):
    user = get_user(callback.from_user.id)

    if user["spins"] < WITHDRAW_MIN:
        needed = WITHDRAW_MIN - user["spins"]
        await callback.message.answer(
            f"💸 *WITHDRAWAL*\n\n"
            f"❌ You need *{WITHDRAW_MIN} spins* to withdraw.\n\n"
            f"Your balance: *{user['spins']}* spins\n"
            f"You need *{needed}* more spins!\n\n"
            f"Keep spinning or invite friends to reach the limit! 💪",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="🎰 KEEP SPINNING", callback_data="spin")],
                [InlineKeyboardButton(text="💎 BUY SPINS", callback_data="buy")],
            ])
        )
        await callback.answer()
        return

    if user.get("pending_withdrawal"):
        await callback.answer(
            "⏳ You already have a pending withdrawal. Please wait for admin approval.",
            show_alert=True,
        )
        return

    await callback.message.answer(
        "💸 *WITHDRAWAL REQUEST*\n\n"
        f"✅ Your balance: *{user['spins']} spins*\n\n"
        "Please send your *TON Wallet Address* below.\n"
        "_(Starts with UQ, EQ, or 0Q)_\n\n"
        "Admin will process your payment within 24 hours.",
        parse_mode="Markdown",
    )
    await callback.answer()

@dp.message(F.text.regexp(r"^(UQ|EQ|0Q)[\w-]{46,}$"))
async def handle_wallet(message: Message):
    user_id = message.from_user.id
    user    = get_user(user_id)

    if user["spins"] < WITHDRAW_MIN:
        return

    if user.get("pending_withdrawal"):
        await message.answer("⏳ You already have a pending withdrawal. Please wait.")
        return

    user["pending_withdrawal"] = True
    user["pending_spins"]      = user["spins"]
    save_all()

    await bot.send_message(
        ADMIN_ID,
        f"🚨 *PAYOUT NEEDED!*\n"
        f"User ID: `{user_id}`\n"
        f"Name: {message.from_user.full_name}\n"
        f"Balance: `{user['spins']}` spins\n"
        f"Wallet: `{message.text}`\n\n"
        f"Use `/pay {user_id}` to confirm payment.",
        parse_mode="Markdown",
    )
    await message.answer(
        "✅ *Request received!*\n"
        "Admin is reviewing your balance. You will receive your TON within 24 hours.",
        parse_mode="Markdown",
    )

# ── HIDDEN ADMIN DASHBOARD (/admin) ──────────

@dp.message(Command("admin"))
async def admin_dashboard(message: Message):
    if message.from_user.id != ADMIN_ID:
        return   # invisible to non-admins — no reply at all

    today     = str(date.today())
    active_today = len(stats["daily_active"].get(today, []))

    # Calculate total pending withdrawals
    pending = [
        (uid, u) for uid, u in user_data.items()
        if u.get("pending_withdrawal")
    ]

    # Top 5 players by balance
    top_players = sorted(
        user_data.items(),
        key=lambda x: x[1].get("spins", 0),
        reverse=True
    )[:5]

    # Top 5 by referrals
    top_referrers = sorted(
        user_data.items(),
        key=lambda x: x[1].get("referrals", 0),
        reverse=True
    )[:5]

    top_text = ""
    for i, (uid, u) in enumerate(top_players, 1):
        top_text += f"  {i}. ID `{uid}` — {u.get('spins', 0)} spins\n"

    ref_text = ""
    for i, (uid, u) in enumerate(top_referrers, 1):
        ref_text += f"  {i}. ID `{uid}` — {u.get('referrals', 0)} referrals\n"

    pending_text = ""
    for uid, u in pending:
        pending_text += f"  • ID `{uid}` — {u.get('pending_spins', 0)} spins\n"
    if not pending_text:
        pending_text = "  None pending ✅\n"

    await message.answer(
        f"🔐 *ADMIN DASHBOARD*\n"
        f"━━━━━━━━━━━━━━━━━━━━\n\n"
        f"👥 *PLAYERS*\n"
        f"  Total players: *{stats['total_players']}*\n"
        f"  Active today: *{active_today}*\n"
        f"  Total referrals: *{stats['total_referrals']}*\n\n"
        f"🎰 *SPINS*\n"
        f"  Total spins played: *{stats.get('total_spins_played', 0)}*\n"
        f"  Jackpots hit: *{stats.get('total_jackpots', 0)}*\n"
        f"  Bar wins: *{stats.get('total_bar_wins', 0)}*\n"
        f"  Fruit wins: *{stats.get('total_fruit_wins', 0)}*\n\n"
        f"💎 *PURCHASES*\n"
        f"  Total spins bought: *{stats.get('total_spins_bought', 0)}*\n\n"
        f"💸 *PENDING WITHDRAWALS*\n"
        f"{pending_text}\n"
        f"🏆 *TOP 5 PLAYERS (by balance)*\n"
        f"{top_text}\n"
        f"📢 *TOP 5 REFERRERS*\n"
        f"{ref_text}\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"🛠 *ADMIN COMMANDS*\n"
        f"`/gift [id] [amount]` — give spins\n"
        f"`/pay [id]` — confirm withdrawal\n"
        f"`/ban [id]` — ban a user\n"
        f"`/unban [id]` — unban a user\n"
        f"`/broadcast [msg]` — message all users",
        parse_mode="Markdown",
    )

# ── Admin: /pay ───────────────────────────────

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
        amount                     = user.get("pending_spins", 0)
        user["spins"]             -= amount
        user["pending_withdrawal"] = False
        user["pending_spins"]      = 0
        save_all()
        await message.answer(f"✅ Paid! Deducted {amount} spins from user {target_id}.")
        await bot.send_message(
            int(target_id),
            "💸 *Your withdrawal has been processed!*\n"
            "Check your TON wallet. Thank you for playing! 🎰",
            parse_mode="Markdown",
        )
    except (IndexError, ValueError):
        await message.answer("Usage: `/pay [user_id]`", parse_mode="Markdown")

# ── Admin: /gift ──────────────────────────────

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
        await message.answer(
            f"✅ Added *{amount}* spins to `{target_id}`.\n"
            f"New balance: *{user['spins']}* spins.",
            parse_mode="Markdown",
        )
        await bot.send_message(
            int(target_id),
            f"🎁 *You received {amount} free spins!*\n"
            f"💰 Your balance: {user['spins']} spins\n\n"
            f"Good luck! 🎰",
            parse_mode="Markdown",
        )
    except (IndexError, ValueError):
        await message.answer("Usage: `/gift [user_id] [amount]`", parse_mode="Markdown")

# ── Admin: /ban & /unban ──────────────────────

@dp.message(Command("ban"))
async def admin_ban(message: Message):
    if message.from_user.id != ADMIN_ID:
        return
    try:
        target_id = str(int(message.text.split()[1]))
        user      = get_user(int(target_id))
        user["banned"] = True
        save_all()
        await message.answer(f"🚫 User `{target_id}` has been banned.", parse_mode="Markdown")
        await bot.send_message(int(target_id), "🚫 You have been banned from FortunoBet.")
    except (IndexError, ValueError):
        await message.answer("Usage: `/ban [user_id]`", parse_mode="Markdown")

@dp.message(Command("unban"))
async def admin_unban(message: Message):
    if message.from_user.id != ADMIN_ID:
        return
    try:
        target_id = str(int(message.text.split()[1]))
        user      = get_user(int(target_id))
        user["banned"] = False
        save_all()
        await message.answer(f"✅ User `{target_id}` has been unbanned.", parse_mode="Markdown")
        await bot.send_message(int(target_id), "✅ You have been unbanned from FortunoBet. Welcome back!")
    except (IndexError, ValueError):
        await message.answer("Usage: `/unban [user_id]`", parse_mode="Markdown")

# ── Admin: /broadcast ────────────────────────

@dp.message(Command("broadcast"))
async def admin_broadcast(message: Message):
    if message.from_user.id != ADMIN_ID:
        return
    try:
        text = message.text.split(" ", 1)[1]
    except IndexError:
        await message.answer("Usage: `/broadcast [message]`", parse_mode="Markdown")
        return

    sent    = 0
    failed  = 0
    for uid in user_data:
        if user_data[uid].get("banned"):
            continue
        try:
            await bot.send_message(
                int(uid),
                f"📢 *Message from FortunoBet:*\n\n{text}",
                parse_mode="Markdown",
            )
            sent += 1
            await asyncio.sleep(0.05)   # avoid hitting Telegram rate limit
        except Exception:
            failed += 1

    await message.answer(
        f"✅ Broadcast done!\n"
        f"Sent: *{sent}* | Failed: *{failed}*",
        parse_mode="Markdown",
    )

# ── Stars payment ─────────────────────────────

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
    user["spins"]     += 100
    user["purchases"]  = user.get("purchases", 0) + 1
    stats["total_spins_bought"] = stats.get("total_spins_bought", 0) + 100
    stats["purchases"].append({
        "user_id": str(m.from_user.id),
        "amount":  100,
        "date":    str(date.today()),
    })
    save_all()
    await m.answer(
        f"✅ *Success!* 100 Spins added!\n"
        f"💰 New Balance: *{user['spins']}* Spins\n\n"
        f"Good luck! 🎰",
        parse_mode="Markdown",
    )

# ── Main ──────────────────────────────────────

async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s"
    )
    logging.info("FortunoBet UPGRADED is online.")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

    
# /gift 7627990095 50
# /admin — full dashboard
# /broadcast [message] — send a message to ALL users at once
# /ban [user_id] — ban a cheater
# /unban [user_id] — unban them
# /gift and /pay — same as before