import logging
import asyncio
import json
import os
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import Command, CommandObject
from aiogram.types import (
    LabeledPrice, PreCheckoutQuery, Message,
    InlineKeyboardButton, InlineKeyboardMarkup
)

# ─────────────────────────────────────────────
# CONFIGURATION  ← only edit this section
# ─────────────────────────────────────────────
TOKEN    = "YOUR_BOT_TOKEN_HERE"
ADMIN_ID = 123456789          # ← your real Telegram ID (use @userinfobot to find it)

# Telegram slot-machine dice: value 1–64
# These are the REAL dice values that show the matching animation:
#   1  = BAR BAR BAR  (cherries / bar win)
#   22 = LEMON LEMON LEMON
#   43 = SEVEN SEVEN SEVEN  ← jackpot
#   64 = GRAPE GRAPE GRAPE
# Other values = mixed reels (no win)
JACKPOT_VALUE = 43          # true 777 jackpot animation
BAR_VALUE     = 1           # bar/cherry win animation
FRUIT_VALUES  = {22, 64}    # matching fruit (lemon / grape)

# Payout in spins
JACKPOT_PAYOUT = 150
BAR_PAYOUT     = 40
FRUIT_PAYOUT   = 5

# Minimum spins required to request a withdrawal
WITHDRAW_MIN = 500

# Persistence file – survives bot restarts
DATA_FILE = "user_data.json"
# ─────────────────────────────────────────────

bot = Bot(token=TOKEN)
dp  = Dispatcher()

# ── Persistence helpers ──────────────────────

def _load() -> dict:
    """Load user data from disk, return empty dict on first run."""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            pass
    return {}

def _save(data: dict) -> None:
    """Persist user data to disk atomically (write-then-rename)."""
    tmp = DATA_FILE + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    os.replace(tmp, DATA_FILE)

# Load once at startup; all handlers mutate this dict and call _save()
user_data: dict = _load()


def get_user(user_id: int) -> dict:
    """Return the user's record, creating a default one if absent."""
    uid = str(user_id)           # JSON keys are always strings
    if uid not in user_data:
        user_data[uid] = {
            "spins": 0,
            "pending_withdrawal": False,   # True while awaiting admin payout
        }
    return user_data[uid]


# ── Keyboards ────────────────────────────────

def main_kb(user_id: int) -> InlineKeyboardMarkup:
    ref_link = f"https://t.me/FortunoSlotsbot?start={user_id}"
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🎰 SPIN (1 Credit)", callback_data="spin")],
        [InlineKeyboardButton(text="💎 BUY 100 SPINS — 10 Stars", callback_data="buy")],
        [InlineKeyboardButton(text="💸 WITHDRAW WINNINGS", callback_data="withdraw_req")],
        [InlineKeyboardButton(
            text="📢 INVITE FOR 5 SPINS",
            url=f"https://t.me/share/url?url={ref_link}"
        )],
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

    # Give 10 free spins only if this is a brand-new user
    is_new = user["spins"] == 0 and not user.get("ever_started")
    if is_new:
        user["spins"] = 10
        user["ever_started"] = True

    # Referral bonus
    if command.args and is_new:
        try:
            ref_id = int(command.args)
            ref    = get_user(ref_id)
            if ref_id != user_id:
                ref["spins"] += 5
                _save(user_data)
                await bot.send_message(ref_id, "🎊 *Bonus!* Your referral joined — +5 FREE SPINS!", parse_mode="Markdown")
        except (ValueError, TypeError):
            pass

    _save(user_data)
    await message.answer(
        "🎰 *WELCOME TO FORTUNOBET* 🎰\n\n"
        "High RTP Slots | Instant TON Payouts\n\n"
        f"💰 *Your Balance:* {user['spins']} Spins",
        reply_markup=main_kb(user_id),
        parse_mode="Markdown",
    )


# ── /balance ─────────────────────────────────

@dp.message(Command("balance"))
async def cmd_balance(message: Message):
    user = get_user(message.from_user.id)
    await message.answer(
        f"💰 *Your Balance:* {user['spins']} Spins",
        parse_mode="Markdown",
        reply_markup=main_kb(message.from_user.id),
    )


# ── Spin ─────────────────────────────────────

@dp.callback_query(F.data == "spin")
async def play_slots(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user    = get_user(user_id)

    if user["spins"] < 1:
        await callback.answer("❌ Out of spins! Buy more or invite friends.", show_alert=True)
        return

    # Deduct spin first — prevents double-spin exploits
    user["spins"] -= 1
    _save(user_data)

    msg   = await callback.message.answer_dice(emoji="🎰")
    value = msg.dice.value
    await asyncio.sleep(2.5)   # wait for dice animation to finish

    # ── Win logic (based on verified Telegram dice values) ──
    if value == JACKPOT_VALUE:
        win_amount = JACKPOT_PAYOUT
        win_text   = f"🔥 *JACKPOT!* +{JACKPOT_PAYOUT} SPINS!"
    elif value == BAR_VALUE:
        win_amount = BAR_PAYOUT
        win_text   = f"💎 *BAR WIN!* +{BAR_PAYOUT} SPINS!"
    elif value in FRUIT_VALUES:
        win_amount = FRUIT_PAYOUT
        win_text   = f"✨ *FRUIT WIN!* +{FRUIT_PAYOUT} SPINS!"
    else:
        win_amount = 0
        win_text   = "❌ No win. Try again!"

    user["spins"] += win_amount
    _save(user_data)

    await callback.message.answer(
        f"{win_text}\n💰 *Balance:* {user['spins']} Spins",
        reply_markup=spin_again_kb,
        parse_mode="Markdown",
    )
    await callback.answer()   # dismiss the loading indicator


# ── Withdraw request ─────────────────────────

@dp.callback_query(F.data == "withdraw_req")
async def withdraw_info(callback: types.CallbackQuery):
    user = get_user(callback.from_user.id)

    if user["spins"] < WITHDRAW_MIN:
        await callback.answer(
            f"❌ Minimum withdrawal is {WITHDRAW_MIN} Spins. "
            f"You have {user['spins']}.",
            show_alert=True,
        )
        return

    if user.get("pending_withdrawal"):
        await callback.answer(
            "⏳ You already have a pending withdrawal. Please wait for admin approval.",
            show_alert=True,
        )
        return

    await callback.message.answer(
        "💸 *WITHDRAWAL REQUEST*\n\n"
        "Please send your *TON Wallet Address* below.\n"
        "_(It starts with UQ, EQ, or 0Q)_\n\n"
        "Admin will process your payment within 24 hours.",
        parse_mode="Markdown",
    )
    await callback.answer()


# ── Wallet address handler ────────────────────

@dp.message(F.text.regexp(r"^(UQ|EQ|0Q)[\w-]{46,}$"))
async def handle_wallet(message: Message):
    user_id = message.from_user.id
    user    = get_user(user_id)

    if user["spins"] < WITHDRAW_MIN:
        return   # silently ignore — shouldn't happen normally

    if user.get("pending_withdrawal"):
        await message.answer("⏳ You already have a pending withdrawal. Please wait.")
        return

    # Lock the balance so they can't spend these spins while waiting
    user["pending_withdrawal"] = True
    user["pending_spins"]      = user["spins"]   # snapshot the amount owed
    _save(user_data)

    await bot.send_message(
        ADMIN_ID,
        f"🚨 *PAYOUT NEEDED!*\n"
        f"User ID: `{user_id}`\n"
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


# ── Admin: /pay [user_id] — confirm withdrawal ──

@dp.message(Command("pay"))
async def admin_pay(message: Message):
    if message.from_user.id != ADMIN_ID:
        return

    try:
        target_id = str(message.text.split()[1])
        user      = user_data.get(target_id)
        if not user:
            await message.answer("❌ User not found.")
            return

        amount = user.get("pending_spins", 0)
        user["spins"]              -= amount
        user["pending_withdrawal"]  = False
        user["pending_spins"]       = 0
        _save(user_data)

        await message.answer(f"✅ Marked as paid. Deducted {amount} spins from user {target_id}.")
        await bot.send_message(
            int(target_id),
            "💸 *Your withdrawal has been processed!* "
            "Check your TON wallet. Thank you for playing FortunoBet! 🎰",
            parse_mode="Markdown",
        )
    except (IndexError, ValueError):
        await message.answer("Usage: `/pay [user_id]`", parse_mode="Markdown")


# ── Admin: /gift [user_id] [amount] ──────────

@dp.message(Command("gift"))
async def admin_gift(message: Message):
    if message.from_user.id != ADMIN_ID:
        return

    try:
        parts     = message.text.split()
        target_id = str(int(parts[1]))   # normalise to string key
        amount    = int(parts[2])
        user      = get_user(int(target_id))
        user["spins"] += amount
        _save(user_data)
        await message.answer(f"✅ Added {amount} spins to user {target_id}. New balance: {user['spins']}.")
    except (IndexError, ValueError):
        await message.answer("Usage: `/gift [user_id] [amount]`", parse_mode="Markdown")


# ── Stars payment ─────────────────────────────

@dp.callback_query(F.data == "buy")
async def process_buy(callback: types.CallbackQuery):
    await bot.send_invoice(
        callback.message.chat.id,
        title="100 Spins",
        description="100 credits for FortunoBet slots",
        payload="buy_100",
        provider_token="",      # empty = Telegram Stars
        currency="XTR",
        prices=[LabeledPrice(label="100 Spins", amount=10)],
    )
    await callback.answer()

@dp.pre_checkout_query()
async def pre_check(q: PreCheckoutQuery):
    await q.answer(ok=True)

@dp.message(F.successful_payment)
async def success_pay(m: Message):
    user        = get_user(m.from_user.id)
    user["spins"] += 100
    _save(user_data)
    await m.answer(
        "✅ *Success!* 100 Spins added to your account.\n"
        f"💰 New Balance: {user['spins']} Spins",
        parse_mode="Markdown",
    )


# ── Entry point ───────────────────────────────

async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
    )
    logging.info("FortunoBet is online.")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())