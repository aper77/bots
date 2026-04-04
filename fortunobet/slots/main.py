"""
FortunoBet — PRODUCTION VERSION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Install: pip install aiogram
Run:     python3 bot.py

ECONOMY:
  1 spin = $0.01 = 0.002 TON
  200 spins = $2.00 = 0.4 TON  <- min withdrawal
  Buy packages: choose how many Stars to spend (min 10)

RTP 99%:
  777 Jackpot  = bet x 15   (1/64)
  BAR win      = bet x 4    (1/64)
  Fruit win    = bet x 1.5  (2/64)
  Near miss    = bet x 0.8  (56/64)
  Full loss    = bet x 0    (4/64)

ADMIN COMMANDS:
  /admin              main dashboard
  /stats7             last 7 days
  /pay [id]           Tonkeeper payout link
  /reject [id]        reject withdrawal, return spins
  /gift [id] [amount] give free spins
  /userinfo [id]      full user profile
  /ban [id]           ban user
  /unban [id]         unban user
  /broadcast [msg]    message all users

FEATURES:
  Early-bird: first 5 unique players each day get +5 free spins
  Referral: when your friend joins via your link, YOU get +5 spins
  Multi-package buy: user picks 10/25/50/100 Stars
  Withdraw reject: admin can reject and spins auto-return to user
"""

import logging
import asyncio
import json
import os
from datetime import date, timedelta
from urllib.parse import quote
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import Command, CommandObject
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import (
    LabeledPrice, PreCheckoutQuery, Message,
    InlineKeyboardButton, InlineKeyboardMarkup
)

# =========================================================
#  CONFIGURATION — only edit this section
# =========================================================
TOKEN             = "8785716937:AAHi1QULuw-OGhCVAhYOXg_aO6QpMkdmr_Y"
ADMIN_ID          = 8612272966
TONCENTER_API_KEY = "a4e8dd9e0111177cb876e4b0559e8a58b5eeb4b6acdbd981ad4f7b6123acad9c"
ADMIN_WALLET      = "UQDlWJTEIwwGt7vai3T6s5MXgULmXk4ojhseU_UxxL7SY2DK"

SPIN_USD     = 0.01    # 1 spin = $0.01
SPIN_TO_TON  = 0.002   # 1 spin = 0.002 TON
MIN_WITHDRAW = 200     # minimum spins to withdraw = $2.00

JACKPOT_VALUE    = 43
BAR_VALUE        = 1
FRUIT_VALUES     = {22, 64}
FULL_LOSS_VALUES = {10, 20, 30, 40}

JACKPOT_MULT  = 15
BAR_MULT      = 4
FRUIT_MULT    = 1.5
MINI_WIN_MULT = 0.8

BET_OPTIONS = [1, 5, 10, 25, 50]

# Buy packages: (stars, spins, label)
# Minimum is always 10 Stars (first package)
# User picks which package they want
STAR_PACKAGES = [
    (10,   100,  "Starter"),
    (25,   250,  "Popular ⭐"),
    (50,   500,  "Big Win"),
    (100, 1000,  "Whale 🐋"),
]

DATA_FILE  = "user_data.json"
STATS_FILE = "stats.json"
BOT_NAME   = "FortunoSlotsbot"

DAILY_EARLY_BIRD_LIMIT = 5
DAILY_EARLY_BIRD_SPINS = 5
# =========================================================

bot = Bot(token=TOKEN)
dp  = Dispatcher(storage=MemoryStorage())

class WithdrawStates(StatesGroup):
    waiting_amount = State()
    waiting_wallet = State()

# ── Persistence ───────────────────────────────────────────
def _load(fp) -> dict:
    if os.path.exists(fp):
        try:
            with open(fp, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {}

def _save(data, fp):
    tmp = fp + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    os.replace(tmp, fp)

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
        "total_mini_wins":    0,
        "total_losses":       0,
        "total_ton_paid":     0.0,
        "total_depositors":   0,
        "daily_active":       {},
        "daily_first_five":   {},
        "daily_new_players":  {},
        "daily_purchases":    {},
        "daily_depositors":   {},
        "daily_stars_spent":  {},
        "daily_spins_played": {},
        "daily_revenue_spins":{},
    }

# Backfill missing keys for existing stats files
_DEFAULTS = {
    "total_depositors":   0,
    "daily_first_five":   {},
    "daily_new_players":  {},
    "daily_purchases":    {},
    "daily_depositors":   {},
    "daily_stars_spent":  {},
    "daily_spins_played": {},
    "daily_revenue_spins":{},
}
for _k, _v in _DEFAULTS.items():
    if _k not in stats:
        stats[_k] = _v

def save_all():
    _save(user_data, DATA_FILE)
    _save(stats,     STATS_FILE)

def get_user(uid: int) -> dict:
    k = str(uid)
    if k not in user_data:
        user_data[k] = {
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
            "total_lost":         0,
            "purchases":          0,
            "ever_deposited":     False,
            "banned":             False,
            "bet_size":           1,
            "biggest_win":        0,
        }
        stats["total_players"] += 1
        today = str(date.today())
        stats["daily_new_players"][today] = stats["daily_new_players"].get(today, 0) + 1
        save_all()
    if "ever_deposited" not in user_data[k]:
        user_data[k]["ever_deposited"] = user_data[k].get("purchases", 0) > 0
    return user_data[k]

def track_daily(uid: int):
    today = str(date.today())
    if today not in stats["daily_active"]:
        stats["daily_active"][today] = []
    k = str(uid)
    if k not in stats["daily_active"][today]:
        stats["daily_active"][today].append(k)

def check_early_bird(uid: int) -> bool:
    """
    Award +5 spins to first 5 DIFFERENT users who open the bot today.
    Max 5 unique people per day. Each person claims ONCE per day.
    Resets automatically at midnight.
    """
    today   = str(date.today())
    winners = stats["daily_first_five"].setdefault(today, [])
    k       = str(uid)
    if k in winners:
        return False
    if len(winners) >= DAILY_EARLY_BIRD_LIMIT:
        return False
    winners.append(k)
    u = get_user(uid)
    u["spins"] += DAILY_EARLY_BIRD_SPINS
    save_all()
    return True

# ── Helpers ───────────────────────────────────────────────
def usd(spins) -> str:
    return f"${spins * SPIN_USD:.2f}"

def ton(spins) -> float:
    return round(spins * SPIN_TO_TON, 4)

def pay_link(to_addr: str, amount_ton: float, comment: str) -> str:
    nano = int(amount_ton * 1_000_000_000)
    return (
        f"https://app.tonkeeper.com/transfer/{to_addr}"
        f"?amount={nano}&text={quote(comment)}"
    )

# ── Win engine (99% RTP) ──────────────────────────────────
def calc_win(dice: int, bet: int) -> tuple[int, str, str]:
    """
    Dice 1-64 distribution:
      43       → JACKPOT 777  (bet x 15)
      1        → BAR win      (bet x 4)
      22, 64   → FRUIT win    (bet x 1.5)
      10,20,30,40 → FULL LOSS (0)
      all others (56/64) → NEAR MISS (bet x 0.8) ← gives 99% RTP
    """
    if dice == JACKPOT_VALUE:
        w = int(bet * JACKPOT_MULT)
        return w, f"🔥 *JACKPOT! 7️⃣7️⃣7️⃣*\n+{w} spins · {usd(w)}\n\n🏆 *LEGEND!*", "jackpot"

    if dice == BAR_VALUE:
        w = int(bet * BAR_MULT)
        return w, f"💎 *BAR WIN!*\n+{w} spins · {usd(w)}", "bar"

    if dice in FRUIT_VALUES:
        w = int(bet * FRUIT_MULT)
        return w, f"🍋 *FRUIT WIN!*\n+{w} spins · {usd(w)}", "fruit"

    if dice in FULL_LOSS_VALUES:
        return 0, "💨 *No match.* Try again!", "loss"

    # Near miss — 56 out of 64 values → 80% of bet returned
    w = int(bet * MINI_WIN_MULT)
    return w, f"⚡ *Near miss!*\n+{w} spins back", "mini"

# ── Keyboards ─────────────────────────────────────────────
def main_kb(uid: int) -> InlineKeyboardMarkup:
    u        = get_user(uid)
    bet      = int(u.get("bet_size", 1))
    ref_link = f"https://t.me/{BOT_NAME}?start={uid}"
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(
            text=f"🎰 SPIN  ·  {bet} spin{'s' if bet>1 else ''} = {usd(bet)}",
            callback_data="spin"
        )],
        [InlineKeyboardButton(text="🎲 Change Bet", callback_data="change_bet"),
         InlineKeyboardButton(text="📊 My Stats",   callback_data="my_stats")],
        [InlineKeyboardButton(text="💎 Buy Spins",       callback_data="buy")],
        [InlineKeyboardButton(text="💸 Withdraw to TON", callback_data="withdraw_req")],
        [InlineKeyboardButton(
            text="📢 Invite friend → +5 spins for you",
            url=f"https://t.me/share/url?url={ref_link}"
        )],
    ])

def buy_kb() -> InlineKeyboardMarkup:
    """Show all spin packages. User picks how many Stars to spend."""
    rows = []
    for stars, spins, label in STAR_PACKAGES:
        rows.append([InlineKeyboardButton(
            text=f"💎 {label} — {spins} spins · {stars} ⭐ (${stars * 0.013:.2f})",
            callback_data=f"buypack_{stars}_{spins}"
        )])
    rows.append([InlineKeyboardButton(text="🔙 Back", callback_data="back_main")])
    return InlineKeyboardMarkup(inline_keyboard=rows)

def bet_kb(uid: int) -> InlineKeyboardMarkup:
    u   = get_user(uid)
    bal = u.get("spins", 0)
    rows = []
    for b in BET_OPTIONS:
        ok      = "✅" if bal >= b else "❌"
        jackpot = int(b * JACKPOT_MULT)
        net_nm  = int(b * MINI_WIN_MULT) - b
        rows.append([InlineKeyboardButton(
            text=f"{ok} {b}x · jackpot +{jackpot} · near miss {net_nm:+}",
            callback_data=f"bet_{b}"
        )])
    rows.append([InlineKeyboardButton(text="🔙 Back", callback_data="back_main")])
    return InlineKeyboardMarkup(inline_keyboard=rows)

def no_spins_kb(uid: int) -> InlineKeyboardMarkup:
    ref_link = f"https://t.me/{BOT_NAME}?start={uid}"
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💎 Buy Spins", callback_data="buy")],
        [InlineKeyboardButton(
            text="📢 Invite friend → +5 free spins",
            url=f"https://t.me/share/url?url={ref_link}"
        )],
        [InlineKeyboardButton(text="🎲 Lower my bet", callback_data="change_bet")],
    ])

def spin_again_kb(bet_size: int) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(
            text=f"🎰 Spin Again  ·  {bet_size}x = {usd(bet_size)}",
            callback_data="spin"
        )],
        [InlineKeyboardButton(text="🎲 Change Bet", callback_data="change_bet"),
         InlineKeyboardButton(text="💎 Buy Spins",  callback_data="buy")],
    ])

# ── /start ────────────────────────────────────────────────
@dp.message(Command("start"))
async def cmd_start(message: Message, command: CommandObject):
    uid    = message.from_user.id
    user   = get_user(uid)
    is_new = not user.get("ever_started", False)

    if is_new:
        user["spins"]        = 10
        user["ever_started"] = True

    # Early-bird: first 5 unique players each day get +5 spins
    early_bird_won = check_early_bird(uid)

    # Referral: inviter gets +5 when NEW friend joins
    if command.args and is_new:
        try:
            ref_id = int(command.args)
            if ref_id != uid:
                ref = get_user(ref_id)
                ref["spins"]     += 5
                ref["referrals"] += 1
                user["referred_by"] = ref_id
                stats["total_referrals"] += 1
                save_all()
                await bot.send_message(
                    ref_id,
                    f"🎊 *Friend joined!* +5 spins credited!\n"
                    f"💰 Balance: *{ref['spins']}* spins · 👥 Invited: *{ref['referrals']}*",
                    parse_mode="Markdown"
                )
        except (ValueError, TypeError):
            pass

    track_daily(uid)
    save_all()

    bal    = user["spins"]
    extras = ""
    if early_bird_won:
        pos    = len(stats["daily_first_five"].get(str(date.today()), []))
        extras = f"\n🌅 *Early Bird #{pos}!* +{DAILY_EARLY_BIRD_SPINS} free spins!\n"

    welcome = "🎁 *Welcome gift: 10 free spins!*" if is_new else "👋 *Welcome back!*"

    await message.answer(
        f"🎰 *FortunoBet* — Real TON Payouts\n\n"
        f"{welcome}{extras}\n"
        f"💰 Balance: *{bal} spins* · {usd(bal)}\n\n"
        f"🏆 Win up to x15 · 99% RTP\n"
        f"💸 Withdraw from {MIN_WITHDRAW} spins = {usd(MIN_WITHDRAW)}",
        reply_markup=main_kb(uid),
        parse_mode="Markdown",
    )

# ── /balance ──────────────────────────────────────────────
@dp.message(Command("balance"))
async def cmd_balance(message: Message):
    u = get_user(message.from_user.id)
    await message.answer(
        f"💰 *{u['spins']}* spins · {usd(u['spins'])} · {ton(u['spins'])} TON",
        parse_mode="Markdown",
        reply_markup=main_kb(message.from_user.id)
    )

# ── Change bet ────────────────────────────────────────────
@dp.callback_query(F.data == "change_bet")
async def change_bet_menu(callback: types.CallbackQuery):
    u = get_user(callback.from_user.id)
    await callback.message.answer(
        f"🎲 *Select Bet Size*\n"
        f"💰 Balance: *{u['spins']}* spins\n\n"
        f"Near miss = 80% back · Higher bet = bigger jackpot",
        reply_markup=bet_kb(callback.from_user.id),
        parse_mode="Markdown"
    )
    await callback.answer()

@dp.callback_query(F.data.startswith("bet_"))
async def set_bet(callback: types.CallbackQuery):
    u        = get_user(callback.from_user.id)
    bet_size = int(callback.data.split("_")[1])
    if u["spins"] < bet_size:
        await callback.answer(f"❌ Need {bet_size} spins!", show_alert=True)
        return
    u["bet_size"] = bet_size
    save_all()

    jw = int(bet_size * JACKPOT_MULT)
    bw = int(bet_size * BAR_MULT)
    fw = int(bet_size * FRUIT_MULT)
    mw = int(bet_size * MINI_WIN_MULT)

    await callback.message.answer(
        f"✅ *Bet: {bet_size}x* ({usd(bet_size)} per spin)\n\n"
        f"🔥 Jackpot → +{jw} (net +{jw-bet_size})\n"
        f"💎 Bar     → +{bw} (net +{bw-bet_size})\n"
        f"🍋 Fruit   → +{fw} (net +{fw-bet_size})\n"
        f"⚡ Near miss→ +{mw} back (net {mw-bet_size:+})\n"
        f"💨 Loss    → 0 (net -{bet_size})",
        reply_markup=main_kb(callback.from_user.id),
        parse_mode="Markdown",
    )
    await callback.answer(f"Bet set to {bet_size}x!")

# ── Spin ──────────────────────────────────────────────────
@dp.callback_query(F.data == "spin")
async def play_slots(callback: types.CallbackQuery):
    uid      = callback.from_user.id
    u        = get_user(uid)
    bet_size = int(u.get("bet_size", 1))

    if u.get("banned"):
        await callback.answer("🚫 You are banned.", show_alert=True)
        return

    if u["spins"] < bet_size:
        await callback.message.answer(
            f"❌ *Not enough spins!*\n"
            f"Balance: *{u['spins']}* · Need: *{bet_size}*",
            reply_markup=no_spins_kb(uid),
            parse_mode="Markdown",
        )
        await callback.answer("❌ Not enough spins!")
        return

    # Deduct bet before spin
    u["spins"]              -= bet_size
    u["total_spins_played"]  = u.get("total_spins_played", 0) + bet_size
    stats["total_spins_played"] = stats.get("total_spins_played", 0) + bet_size
    today = str(date.today())
    stats["daily_spins_played"][today] = stats["daily_spins_played"].get(today, 0) + bet_size
    track_daily(uid)
    save_all()

    # Roll the dice
    msg  = await callback.message.answer_dice(emoji="🎰")
    dice = msg.dice.value
    await asyncio.sleep(2.5)   # wait for animation

    win_spins, win_text, win_type = calc_win(dice, bet_size)

    # Add winnings
    u["spins"]    += win_spins
    u["total_won"] = u.get("total_won", 0) + win_spins
    if win_spins > u.get("biggest_win", 0):
        u["biggest_win"] = win_spins

    net     = win_spins - bet_size
    net_str = f"+{net}" if net >= 0 else str(net)

    if win_type == "jackpot":
        stats["total_jackpots"]   = stats.get("total_jackpots", 0) + 1
    elif win_type == "bar":
        stats["total_bar_wins"]   = stats.get("total_bar_wins", 0) + 1
    elif win_type == "fruit":
        stats["total_fruit_wins"] = stats.get("total_fruit_wins", 0) + 1
    elif win_type == "mini":
        stats["total_mini_wins"]  = stats.get("total_mini_wins", 0) + 1
    else:
        stats["total_losses"]     = stats.get("total_losses", 0) + 1

    save_all()

    hint = ""
    if u["spins"] >= MIN_WITHDRAW:
        hint = f"\n\n💸 *Ready to withdraw!* Tap below 🚀"
    elif 0 < MIN_WITHDRAW - u["spins"] <= 30:
        hint = f"\n\n🔥 Only *{MIN_WITHDRAW - u['spins']}* more spins to withdraw!"

    await callback.message.answer(
        f"{win_text}\n\n"
        f"Bet *{bet_size}* · Got *{win_spins}* back · Net *{net_str}*\n"
        f"💰 *{u['spins']}* spins · {usd(u['spins'])}"
        f"{hint}",
        reply_markup=spin_again_kb(bet_size),
        parse_mode="Markdown",
    )
    await callback.answer()

# ── My Stats ──────────────────────────────────────────────
@dp.callback_query(F.data == "my_stats")
async def my_stats(callback: types.CallbackQuery):
    uid      = callback.from_user.id
    u        = get_user(uid)
    ref_link = f"https://t.me/{BOT_NAME}?start={uid}"
    needed   = max(0, MIN_WITHDRAW - u["spins"])
    status   = "✅ *Ready to withdraw!*" if needed == 0 else f"Need *{needed}* more spins ({usd(needed)})"

    await callback.message.answer(
        f"📊 *Your Stats*\n\n"
        f"💰 *{u['spins']}* spins · {usd(u['spins'])} · {ton(u['spins'])} TON\n"
        f"🎰 Played: *{u.get('total_spins_played',0)}* · 🏆 Best win: *{u.get('biggest_win',0)}*\n"
        f"🎲 Bet: *{u.get('bet_size',1)}x* · 👥 Invited: *{u.get('referrals',0)}*\n"
        f"💎 Purchases: *{u.get('purchases',0)}* · 📅 Joined: {u.get('joined_date','N/A')}\n\n"
        f"🏁 Withdraw: need {MIN_WITHDRAW} spins = {usd(MIN_WITHDRAW)}\n"
        f"{status}\n\n"
        f"🔗 Invite link:\n`{ref_link}`",
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(
                text="📢 Share Invite Link",
                url=f"https://t.me/share/url?url={ref_link}"
            )],
            [InlineKeyboardButton(text="🔙 Back", callback_data="back_main")],
        ])
    )
    await callback.answer()

@dp.callback_query(F.data == "back_main")
async def back_main(callback: types.CallbackQuery):
    u = get_user(callback.from_user.id)
    await callback.message.answer(
        f"🎰 *FortunoBet*\n💰 *{u['spins']}* spins · {usd(u['spins'])}",
        reply_markup=main_kb(callback.from_user.id),
        parse_mode="Markdown",
    )
    await callback.answer()

# ── Withdraw ──────────────────────────────────────────────
@dp.callback_query(F.data == "withdraw_req")
async def withdraw_start(callback: types.CallbackQuery, state: FSMContext):
    u = get_user(callback.from_user.id)

    if u["spins"] < MIN_WITHDRAW:
        needed = MIN_WITHDRAW - u["spins"]
        await callback.message.answer(
            f"💸 *Withdrawal*\n\n"
            f"❌ Minimum: *{MIN_WITHDRAW} spins* ({usd(MIN_WITHDRAW)})\n"
            f"You have: *{u['spins']}* · Need *{needed}* more",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="🎰 Keep Spinning", callback_data="spin")],
                [InlineKeyboardButton(text="💎 Buy Spins",     callback_data="buy")],
            ])
        )
        await callback.answer()
        return

    if u.get("pending_withdrawal"):
        await callback.answer("⏳ Withdrawal in progress! Check back in 2 hours.", show_alert=True)
        return

    await state.set_state(WithdrawStates.waiting_amount)
    await callback.message.answer(
        f"💸 *Withdrawal*\n\n"
        f"💰 *{u['spins']}* spins = {ton(u['spins'])} TON = {usd(u['spins'])}\n\n"
        f"How many spins? (min {MIN_WITHDRAW})\nType a number or tap button 👇",
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(
                text=f"💰 Withdraw All — {u['spins']} spins = {ton(u['spins'])} TON",
                callback_data="withdraw_all"
            )],
            [InlineKeyboardButton(text="❌ Cancel", callback_data="cancel_withdraw")],
        ])
    )
    await callback.answer()

@dp.message(WithdrawStates.waiting_amount)
async def withdraw_amount(message: Message, state: FSMContext):
    u = get_user(message.from_user.id)
    try:
        amount = int(message.text.strip())
    except ValueError:
        await message.answer(f"❌ Type a number. Example: `{MIN_WITHDRAW}`", parse_mode="Markdown")
        return
    if amount < MIN_WITHDRAW:
        await message.answer(f"❌ Minimum is *{MIN_WITHDRAW}* spins ({usd(MIN_WITHDRAW)}).", parse_mode="Markdown")
        return
    if amount > u["spins"]:
        await message.answer(f"❌ You only have *{u['spins']}* spins.", parse_mode="Markdown")
        return

    await state.update_data(withdraw_amount=amount)
    await state.set_state(WithdrawStates.waiting_wallet)
    await message.answer(
        f"✅ *{amount} spins* = {ton(amount)} TON = {usd(amount)}\n\n"
        f"Send your TON wallet address:\n_(starts with UQ, EQ, or 0Q)_",
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="❌ Cancel", callback_data="cancel_withdraw")]
        ])
    )

@dp.callback_query(F.data == "withdraw_all")
async def withdraw_all(callback: types.CallbackQuery, state: FSMContext):
    u      = get_user(callback.from_user.id)
    amount = u["spins"]
    await state.update_data(withdraw_amount=amount)
    await state.set_state(WithdrawStates.waiting_wallet)
    await callback.message.answer(
        f"✅ *{amount} spins* = {ton(amount)} TON = {usd(amount)}\n\n"
        f"Send your TON wallet address:\n_(starts with UQ, EQ, or 0Q)_",
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="❌ Cancel", callback_data="cancel_withdraw")]
        ])
    )
    await callback.answer()

@dp.callback_query(F.data == "cancel_withdraw")
async def cancel_withdraw(callback: types.CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.message.answer("❌ Withdrawal cancelled.", reply_markup=main_kb(callback.from_user.id))
    await callback.answer()

@dp.message(WithdrawStates.waiting_wallet)
async def withdraw_wallet(message: Message, state: FSMContext):
    wallet = message.text.strip()
    uid    = message.from_user.id
    u      = get_user(uid)
    data   = await state.get_data()
    amount = data.get("withdraw_amount", 0)

    if not (wallet.startswith(("UQ", "EQ", "0Q")) and len(wallet) >= 48):
        await message.answer(
            "❌ *Invalid wallet!*\nMust start with UQ, EQ, or 0Q — 48+ characters.\n"
            "Open Tonkeeper → copy address → paste here.",
            parse_mode="Markdown"
        )
        return

    if amount > u["spins"]:
        await message.answer(f"❌ Balance changed. You have *{u['spins']}* spins.", parse_mode="Markdown")
        await state.clear()
        return

    ton_amount = ton(amount)

    # Deduct spins immediately — held until admin confirms or rejects
    u["spins"]             -= amount
    u["pending_withdrawal"] = True
    u["pending_spins"]      = amount
    u["pending_wallet"]     = wallet
    save_all()
    await state.clear()

    link = pay_link(wallet, ton_amount, f"FortunoBet payout {uid}")
    await bot.send_message(
        ADMIN_ID,
        f"🚨 *PAYOUT REQUEST*\n\n"
        f"👤 {message.from_user.full_name} · `{uid}`\n"
        f"🎰 {amount} spins · 💎 {ton_amount} TON · 💵 {usd(amount)}\n"
        f"👛 `{wallet}`\n\n"
        f"✅ CONFIRM = payment sent, spins stay deducted\n"
        f"❌ REJECT  = spins returned to user automatically",
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text=f"💎 PAY {ton_amount} TON via Tonkeeper", url=link)],
            [InlineKeyboardButton(text="✅ CONFIRM — PAYMENT SENT",  callback_data=f"confirm_pay_{uid}")],
            [InlineKeyboardButton(text="❌ REJECT — RETURN SPINS",   callback_data=f"reject_pay_{uid}")],
        ])
    )

    await message.answer(
        f"✅ *Withdrawal submitted!*\n\n"
        f"🎰 {amount} spins → 💎 {ton_amount} TON\n"
        f"⏱ Up to 2 hours. You'll be notified! 🔔",
        parse_mode="Markdown",
        reply_markup=main_kb(uid)
    )

@dp.callback_query(F.data.startswith("confirm_pay_"))
async def confirm_payment(callback: types.CallbackQuery):
    if callback.from_user.id != ADMIN_ID:
        await callback.answer("❌ Not authorized.", show_alert=True)
        return

    target_id = str(callback.data.replace("confirm_pay_", ""))
    u         = user_data.get(target_id)

    if not u or not u.get("pending_withdrawal"):
        await callback.answer("❌ No pending withdrawal.", show_alert=True)
        return

    amount     = u.get("pending_spins", 0)
    ton_amount = ton(amount)
    wallet     = u.get("pending_wallet")

    # Spins already deducted at request time — just clear pending status
    u["pending_withdrawal"] = False
    u["pending_spins"]      = 0
    u["pending_wallet"]     = None
    stats["total_ton_paid"] = round(stats.get("total_ton_paid", 0) + ton_amount, 4)
    save_all()

    await callback.message.edit_reply_markup(reply_markup=None)
    await callback.message.answer(
        f"✅ *Payment confirmed!*\n`{target_id}` · {ton_amount} TON · `{wallet}`",
        parse_mode="Markdown"
    )
    await bot.send_message(
        int(target_id),
        f"💸 *Withdrawal complete!*\n\n"
        f"{ton_amount} TON sent to your wallet!\n"
        f"Check Tonkeeper now 🎉",
        parse_mode="Markdown",
        reply_markup=main_kb(int(target_id))
    )
    await callback.answer("✅ Payment confirmed!")

@dp.callback_query(F.data.startswith("reject_pay_"))
async def reject_payment_button(callback: types.CallbackQuery):
    if callback.from_user.id != ADMIN_ID:
        await callback.answer("❌ Not authorized.", show_alert=True)
        return

    target_id = str(callback.data.replace("reject_pay_", ""))
    u         = user_data.get(target_id)

    if not u or not u.get("pending_withdrawal"):
        await callback.answer("❌ No pending withdrawal found.", show_alert=True)
        return

    amount = u.get("pending_spins", 0)

    # Return spins to user
    u["spins"]             += amount
    u["pending_withdrawal"] = False
    u["pending_spins"]      = 0
    u["pending_wallet"]     = None
    save_all()

    await callback.message.edit_reply_markup(reply_markup=None)
    await callback.message.answer(
        f"❌ *Withdrawal rejected.*\n"
        f"User `{target_id}` — *{amount} spins* returned.",
        parse_mode="Markdown"
    )
    await bot.send_message(
        int(target_id),
        f"❌ *Withdrawal not approved.*\n\n"
        f"Your *{amount} spins* have been returned.\n"
        f"💰 Balance: *{u['spins']}* spins\n\n"
        f"Contact support if you have questions.",
        parse_mode="Markdown",
        reply_markup=main_kb(int(target_id))
    )
    await callback.answer("❌ Withdrawal rejected, spins returned.")

# /reject [user_id] — manually reject without original message
# Example: /reject 773227767
@dp.message(Command("reject"))
async def admin_reject(message: Message):
    if message.from_user.id != ADMIN_ID:
        return
    try:
        target_id = str(int(message.text.split()[1]))
        u         = user_data.get(target_id)

        if not u or not u.get("pending_withdrawal"):
            await message.answer(f"❌ No pending withdrawal for `{target_id}`.", parse_mode="Markdown")
            return

        amount = u.get("pending_spins", 0)
        u["spins"]             += amount
        u["pending_withdrawal"] = False
        u["pending_spins"]      = 0
        u["pending_wallet"]     = None
        save_all()

        await message.answer(
            f"❌ *Rejected.* `{target_id}` — *{amount} spins* returned. Balance: *{u['spins']}*",
            parse_mode="Markdown"
        )
        await bot.send_message(
            int(target_id),
            f"❌ *Withdrawal not approved.*\n\n"
            f"Your *{amount} spins* have been returned.\n"
            f"💰 Balance: *{u['spins']}* spins",
            parse_mode="Markdown",
            reply_markup=main_kb(int(target_id))
        )
    except (IndexError, ValueError):
        await message.answer("❌ Usage: `/reject [user_id]`", parse_mode="Markdown")

# =========================================================
#  ADMIN COMMANDS
# =========================================================

# /admin — full dashboard
@dp.message(Command("admin"))
async def admin_dashboard(message: Message):
    if message.from_user.id != ADMIN_ID:
        return

    today        = str(date.today())
    active_today = len(stats["daily_active"].get(today, []))
    early_today  = len(stats["daily_first_five"].get(today, []))
    new_today    = stats["daily_new_players"].get(today, 0)
    dep_today    = len(stats["daily_depositors"].get(today, []))
    purch_today  = stats["daily_purchases"].get(today, 0)
    stars_today  = stats["daily_stars_spent"].get(today, 0)
    rev_today    = stats["daily_revenue_spins"].get(today, 0) * SPIN_USD

    total_depositors = sum(1 for v in user_data.values() if v.get("ever_deposited"))

    pending     = [(k, v) for k, v in user_data.items() if v.get("pending_withdrawal")]
    top_players = sorted(user_data.items(), key=lambda x: x[1].get("spins", 0), reverse=True)[:5]
    top_refs    = sorted(user_data.items(), key=lambda x: x[1].get("referrals", 0), reverse=True)[:5]
    top_winners = sorted(user_data.items(), key=lambda x: x[1].get("biggest_win", 0), reverse=True)[:3]

    top_text  = "\n".join([f"  {i+1}. `{k}` — {v.get('spins',0)} spins ({usd(v.get('spins',0))})" for i,(k,v) in enumerate(top_players)])
    ref_text  = "\n".join([f"  {i+1}. `{k}` — {v.get('referrals',0)} referrals" for i,(k,v) in enumerate(top_refs)])
    win_text  = "\n".join([f"  {i+1}. `{k}` — {v.get('biggest_win',0)} spins ({usd(v.get('biggest_win',0))})" for i,(k,v) in enumerate(top_winners)])
    pend_text = "\n".join([f"  • `{k}` — {ton(v.get('pending_spins',0))} TON ({usd(v.get('pending_spins',0))})" for k,v in pending]) or "  None ✅"

    spins_sold = stats.get("total_spins_bought", 0)
    revenue    = spins_sold * SPIN_USD

    await message.answer(
        f"🔐 *ADMIN DASHBOARD*\n"
        f"━━━━━━━━━━━━━━━━━━━━\n\n"
        f"👥 *PLAYERS*\n"
        f"  Total: *{stats['total_players']}*\n"
        f"  Active today: *{active_today}*\n"
        f"  New today: *{new_today}*\n"
        f"  Early-bird today: *{early_today}/{DAILY_EARLY_BIRD_LIMIT}*\n"
        f"  Total referrals: *{stats['total_referrals']}*\n\n"
        f"💰 *DEPOSITORS*\n"
        f"  All-time: *{total_depositors}* / {stats['total_players']} players\n"
        f"  Today: *{dep_today}* · Purchases: *{purch_today}* · ⭐ Stars: *{stars_today}*\n"
        f"  Revenue today: *${rev_today:.2f}*\n\n"
        f"🎰 *GAME (ALL TIME)*\n"
        f"  Spins played: *{stats.get('total_spins_played',0)}*\n"
        f"  Jackpots: *{stats.get('total_jackpots',0)}* · Bar: *{stats.get('total_bar_wins',0)}*\n"
        f"  Fruit: *{stats.get('total_fruit_wins',0)}* · Near miss: *{stats.get('total_mini_wins',0)}*\n"
        f"  Full losses: *{stats.get('total_losses',0)}*\n\n"
        f"💵 *REVENUE (ALL TIME)*\n"
        f"  Spins sold: *{spins_sold}* → *${revenue:.2f}*\n"
        f"  TON paid out: *{stats.get('total_ton_paid',0)} TON*\n\n"
        f"⏳ *PENDING PAYOUTS*\n{pend_text}\n\n"
        f"🏆 *TOP 5 BALANCE*\n{top_text}\n\n"
        f"📢 *TOP 5 REFERRERS*\n{ref_text}\n\n"
        f"🥇 *TOP 3 BIGGEST WINS*\n{win_text}\n\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"🛠 `/pay` `/reject` `/gift` `/userinfo` `/ban` `/unban` `/broadcast` `/stats7`",
        parse_mode="Markdown",
    )

# /stats7 — last 7 days breakdown
@dp.message(Command("stats7"))
async def admin_stats7(message: Message):
    if message.from_user.id != ADMIN_ID:
        return

    lines  = []
    totals = dict(new=0, active=0, purchases=0, depositors=0, stars=0, rev=0, spins=0)

    for i in range(6, -1, -1):
        d          = str(date.today() - timedelta(days=i))
        label      = "TODAY" if i == 0 else ("YESTERDAY" if i == 1 else d)
        new_p      = stats["daily_new_players"].get(d, 0)
        active     = len(stats["daily_active"].get(d, []))
        purchases  = stats["daily_purchases"].get(d, 0)
        depositors = len(stats["daily_depositors"].get(d, []))
        stars      = stats["daily_stars_spent"].get(d, 0)
        rev_spins  = stats["daily_revenue_spins"].get(d, 0)
        spins_pl   = stats["daily_spins_played"].get(d, 0)
        revenue    = rev_spins * SPIN_USD

        totals["new"]        += new_p
        totals["active"]     += active
        totals["purchases"]  += purchases
        totals["depositors"] += depositors
        totals["stars"]      += stars
        totals["rev"]        += rev_spins
        totals["spins"]      += spins_pl

        lines.append(
            f"📅 *{label}*\n"
            f"  👤 New: *{new_p}* · Active: *{active}*\n"
            f"  💎 Depositors: *{depositors}* · Purchases: *{purchases}* · ⭐ Stars: *{stars}*\n"
            f"  💵 Revenue: *${revenue:.2f}* · 🎰 Spins: *{spins_pl}*"
        )

    await message.answer(
        f"📈 *LAST 7 DAYS*\n"
        f"━━━━━━━━━━━━━━━━━━━━\n\n"
        + "\n\n".join(lines)
        + f"\n\n━━━━━━━━━━━━━━━━━━━━\n"
        f"📊 *7-DAY TOTALS*\n"
        f"  👤 New: *{totals['new']}* · Active: *{totals['active']}*\n"
        f"  💎 Depositors: *{totals['depositors']}* · Purchases: *{totals['purchases']}*\n"
        f"  ⭐ Stars: *{totals['stars']}* · 💵 Revenue: *${totals['rev']*SPIN_USD:.2f}*\n"
        f"  🎰 Spins played: *{totals['spins']}*",
        parse_mode="Markdown",
    )

# /pay [user_id] — send Tonkeeper payment link
# Example: /pay 773227767
@dp.message(Command("pay"))
async def admin_pay(message: Message):
    if message.from_user.id != ADMIN_ID:
        return
    try:
        target_id = str(int(message.text.split()[1]))
        u         = user_data.get(target_id)
        if not u or not u.get("pending_withdrawal"):
            await message.answer("❌ No pending withdrawal for this user.", parse_mode="Markdown")
            return
        wallet     = u.get("pending_wallet")
        amount     = u.get("pending_spins", 0)
        ton_amount = ton(amount)
        link       = pay_link(wallet, ton_amount, f"FortunoBet payout {target_id}")
        await message.answer(
            f"💸 *Send Payment*\n\n"
            f"To: `{wallet}`\n"
            f"Amount: *{ton_amount} TON* ({usd(amount)})\n"
            f"User: `{target_id}`\n\n"
            f"1️⃣ Tap button → Tonkeeper opens\n"
            f"2️⃣ Confirm in Tonkeeper\n"
            f"3️⃣ Tap CONFIRM here\n\n"
            f"Or tap REJECT to cancel and return spins.",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text=f"💎 PAY {ton_amount} TON via Tonkeeper", url=link)],
                [InlineKeyboardButton(text="✅ CONFIRM — PAYMENT SENT",  callback_data=f"confirm_pay_{target_id}")],
                [InlineKeyboardButton(text="❌ REJECT — RETURN SPINS",   callback_data=f"reject_pay_{target_id}")],
            ])
        )
    except (IndexError, ValueError):
        await message.answer("❌ Usage: `/pay [user_id]`\nExample: `/pay 773227767`", parse_mode="Markdown")

# /gift [user_id] [amount] — give free spins
# Example: /gift 773227767 100
@dp.message(Command("gift"))
async def admin_gift(message: Message):
    if message.from_user.id != ADMIN_ID:
        return
    try:
        parts     = message.text.split()
        target_id = str(int(parts[1]))
        amount    = int(parts[2])
        u         = get_user(int(target_id))
        u["spins"] += amount
        save_all()
        await message.answer(
            f"✅ Gift sent! `{target_id}` +{amount} spins → balance: *{u['spins']}*",
            parse_mode="Markdown"
        )
        await bot.send_message(
            int(target_id),
            f"🎁 *{amount} FREE SPINS!*\n"
            f"💰 Balance: *{u['spins']}* spins · {usd(u['spins'])}\n\n"
            f"Go win big! 🎰",
            parse_mode="Markdown",
            reply_markup=main_kb(int(target_id))
        )
    except (IndexError, ValueError):
        await message.answer("❌ Usage: `/gift [user_id] [amount]`\nExample: `/gift 773227767 100`", parse_mode="Markdown")

# /userinfo [user_id] — full user profile
# Example: /userinfo 773227767
@dp.message(Command("userinfo"))
async def admin_userinfo(message: Message):
    if message.from_user.id != ADMIN_ID:
        return
    try:
        target_id = str(int(message.text.split()[1]))
        u         = user_data.get(target_id)
        if not u:
            await message.answer("❌ User not found.")
            return
        await message.answer(
            f"👤 *USER INFO* · `{target_id}`\n"
            f"━━━━━━━━━━━━━━━━━━━━\n"
            f"💰 *{u.get('spins',0)}* spins · {usd(u.get('spins',0))} · {ton(u.get('spins',0))} TON\n"
            f"🎰 Played: *{u.get('total_spins_played',0)}* · 🏆 Best: *{u.get('biggest_win',0)}* spins\n"
            f"🎲 Bet: *{u.get('bet_size',1)}x* · 👥 Invited: *{u.get('referrals',0)}*\n"
            f"💎 Purchases: *{u.get('purchases',0)}* · Deposited: *{u.get('ever_deposited',False)}*\n"
            f"📅 Joined: {u.get('joined_date','N/A')} · 🚫 Banned: *{u.get('banned',False)}*\n"
            f"⏳ Pending: *{u.get('pending_withdrawal',False)}* · "
            f"Spins held: *{u.get('pending_spins',0)}*\n"
            f"👛 `{u.get('pending_wallet','None')}`",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="🎁 Gift spins", callback_data=f"gift_menu_{target_id}")],
                [InlineKeyboardButton(
                    text=f"{'✅ Unban' if u.get('banned') else '🚫 Ban'} this user",
                    callback_data=f"toggle_ban_{target_id}"
                )],
            ])
        )
    except (IndexError, ValueError):
        await message.answer("❌ Usage: `/userinfo [user_id]`", parse_mode="Markdown")

@dp.callback_query(F.data.startswith("toggle_ban_"))
async def toggle_ban(callback: types.CallbackQuery):
    if callback.from_user.id != ADMIN_ID:
        await callback.answer("❌ Not authorized.", show_alert=True)
        return
    target_id = str(callback.data.replace("toggle_ban_", ""))
    u         = user_data.get(target_id)
    if not u:
        await callback.answer("❌ User not found.", show_alert=True)
        return
    u["banned"] = not u.get("banned", False)
    save_all()
    status = "🚫 Banned" if u["banned"] else "✅ Unbanned"
    await callback.answer(f"{status} user {target_id}", show_alert=True)
    await callback.message.answer(f"{status} user `{target_id}`.", parse_mode="Markdown")

# /ban [user_id]
# Example: /ban 773227767
@dp.message(Command("ban"))
async def admin_ban(message: Message):
    if message.from_user.id != ADMIN_ID:
        return
    try:
        target_id = str(int(message.text.split()[1]))
        get_user(int(target_id))["banned"] = True
        save_all()
        await message.answer(f"🚫 *Banned* `{target_id}`.", parse_mode="Markdown")
    except (IndexError, ValueError):
        await message.answer("❌ Usage: `/ban [user_id]`", parse_mode="Markdown")

# /unban [user_id]
# Example: /unban 773227767
@dp.message(Command("unban"))
async def admin_unban(message: Message):
    if message.from_user.id != ADMIN_ID:
        return
    try:
        target_id = str(int(message.text.split()[1]))
        get_user(int(target_id))["banned"] = False
        save_all()
        await message.answer(f"✅ *Unbanned* `{target_id}`.", parse_mode="Markdown")
    except (IndexError, ValueError):
        await message.answer("❌ Usage: `/unban [user_id]`", parse_mode="Markdown")

# /broadcast [message] — send to all users
# Example: /broadcast 🔥 Double wins today!
@dp.message(Command("broadcast"))
async def admin_broadcast(message: Message):
    if message.from_user.id != ADMIN_ID:
        return
    try:
        text = message.text.split(" ", 1)[1]
    except IndexError:
        await message.answer("❌ Usage: `/broadcast [message]`", parse_mode="Markdown")
        return

    await message.answer("📢 Sending...")
    sent = failed = 0
    for k in user_data:
        if user_data[k].get("banned"):
            continue
        try:
            await bot.send_message(int(k), f"📢 *FortunoBet:*\n\n{text}", parse_mode="Markdown")
            sent += 1
            await asyncio.sleep(0.05)
        except Exception:
            failed += 1

    await message.answer(f"✅ Sent: *{sent}* · Failed: *{failed}*", parse_mode="Markdown")

# =========================================================
#  BUY SPINS — multi-package Stars payment
# =========================================================

@dp.callback_query(F.data == "buy")
async def process_buy(callback: types.CallbackQuery):
    """Show spin package selection menu. Minimum 10 Stars."""
    await callback.message.answer(
        f"💎 *Buy Spins*\n\n"
        f"Minimum: *10 Stars* = 100 spins\n"
        f"1 spin = $0.01 · 99% RTP\n\n"
        f"Pick your package 👇",
        parse_mode="Markdown",
        reply_markup=buy_kb()
    )
    await callback.answer()

@dp.callback_query(F.data.startswith("buypack_"))
async def process_buypack(callback: types.CallbackQuery):
    """Send invoice for chosen package."""
    try:
        parts = callback.data.split("_")
        stars = int(parts[1])
        spins = int(parts[2])
    except (ValueError, IndexError):
        await callback.answer("❌ Invalid package.", show_alert=True)
        return

    label = next((l for s, sp, l in STAR_PACKAGES if s == stars and sp == spins), "Spins")

    await bot.send_invoice(
        callback.message.chat.id,
        title=f"{label} — {spins} Spins",
        description=f"{spins} spins · 1 spin = $0.01 · 99% RTP · TON payouts",
        payload=f"buy_{stars}_{spins}",
        provider_token="",
        currency="XTR",
        prices=[LabeledPrice(label=f"{spins} Spins", amount=stars)],
    )
    await callback.answer()

@dp.pre_checkout_query()
async def pre_check(q: PreCheckoutQuery):
    """Verify payload is a valid package before approving payment."""
    try:
        parts = q.invoice_payload.split("_")
        if parts[0] != "buy":
            raise ValueError
        stars = int(parts[1])
        spins = int(parts[2])
        valid = any(s == stars and sp == spins for s, sp, _ in STAR_PACKAGES)
        if not valid:
            raise ValueError
    except (ValueError, IndexError):
        await q.answer(ok=False, error_message="Unknown product. Contact support.")
        return
    await q.answer(ok=True)

@dp.message(F.successful_payment)
async def success_pay(m: Message):
    uid   = m.from_user.id
    u     = get_user(uid)
    today = str(date.today())

    # Parse spins from payload
    try:
        parts = m.successful_payment.invoice_payload.split("_")
        stars = int(parts[1])
        spins = int(parts[2])
    except (ValueError, IndexError):
        spins = 100
        stars = 10

    # Guard against duplicate payment events
    charge_id = m.successful_payment.telegram_payment_charge_id
    seen      = u.setdefault("processed_charge_ids", [])
    if charge_id in seen:
        await m.answer(
            f"✅ Payment already credited!\n💰 Balance: *{u['spins']}* spins",
            parse_mode="Markdown",
            reply_markup=main_kb(uid)
        )
        return

    seen.append(charge_id)
    if len(seen) > 20:
        u["processed_charge_ids"] = seen[-20:]

    # Credit spins
    u["spins"]    += spins
    u["purchases"] = u.get("purchases", 0) + 1

    # Track first-time depositor
    if not u.get("ever_deposited"):
        u["ever_deposited"] = True
        stats["total_depositors"] = stats.get("total_depositors", 0) + 1

    # Track unique daily depositors
    dep_list = stats["daily_depositors"].setdefault(today, [])
    if str(uid) not in dep_list:
        dep_list.append(str(uid))

    # Revenue stats
    stats["total_spins_bought"]         = stats.get("total_spins_bought", 0) + spins
    stats["daily_purchases"][today]     = stats["daily_purchases"].get(today, 0) + 1
    stats["daily_stars_spent"][today]   = stats["daily_stars_spent"].get(today, 0) + stars
    stats["daily_revenue_spins"][today] = stats["daily_revenue_spins"].get(today, 0) + spins
    save_all()

    await m.answer(
        f"✅ *+{spins} Spins added!*\n"
        f"💰 Balance: *{u['spins']}* spins · {usd(u['spins'])}\n\n"
        f"Good luck! 🎰🔥",
        parse_mode="Markdown",
        reply_markup=main_kb(uid)
    )

# ── Main ──────────────────────────────────────────────────
async def main():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
    logging.info("FortunoBet is online!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())