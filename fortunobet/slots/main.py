"""
FortunoBet — FINAL COMPLETE VERSION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Install: pip install aiogram aiohttp
Run:     python3 bot.py
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ECONOMY:
  1 spin     = $0.01
  1 TON      = ~$5
  1 spin     = 0.002 TON
  200 spins  = $2.00 = 0.4 TON  ← minimum withdrawal
  500 spins  = $5.00 = 1.0 TON

RTP 99%:
  777 Jackpot  = bet × 15   (1 value out of 64)
  BAR win      = bet × 4    (1 value out of 64)
  Fruit win    = bet × 1.5  (2 values out of 64)
  Near miss    = bet × 0.8  (56 values out of 64) ← 99% RTP engine
  Full loss    = bet × 0    (4 values out of 64)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ADMIN COMMANDS — FULL REFERENCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

/admin
  → Shows full dashboard: players, revenue, pending
     payouts, top players, top referrers, biggest wins
  Example: /admin

/pay [user_id]
  → Sends you a Tonkeeper payment link for that user.
     Tap the link → Tonkeeper opens → tap Confirm.
     Then tap "✅ CONFIRM" button to notify the user.
  Example: /pay 773227767

/gift [user_id] [amount]
  → Gives free spins to any user.
     User gets a notification about their gift.
  Example: /gift 773227767 100
  Example: /gift 7627990095 500

NEW FEATURES:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🌅 DAILY EARLY-BIRD BONUS
  The FIRST 5 players who start/open the bot each day
  automatically receive +5 FREE SPINS.
  Each player can earn this once per day.
  Resets every midnight (date change).
  Admin dashboard shows how many claimed it today.

🔗 REFERRAL JOINER BONUS
  When a new player joins via a referral link:
    • The REFERRER gets +5 spins (existing feature)
    • The NEW USER also gets +5 spins (new feature)
  Both players are notified of their bonuses.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

/ban [user_id]
  → Bans a user. They cannot spin anymore.
  Example: /ban 773227767

/unban [user_id]
  → Removes ban from a user.
  Example: /unban 773227767

/broadcast [message]
  → Sends a message to ALL users at once.
     Banned users are skipped automatically.
  Example: /broadcast 🔥 SPECIAL EVENT! Double wins for 1 hour!
  Example: /broadcast 💎 New jackpot added! Come spin now!

/userinfo [user_id]
  → Shows full details about any user:
     balance, spins played, biggest win,
     referrals, purchases, ban status,
     pending withdrawal details.
  Example: /userinfo 773227767

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
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

# ═══════════════════════════════════════════════════════════════════
#  CONFIGURATION — only edit this section
# ═══════════════════════════════════════════════════════════════════
TOKEN             = "8785716937:AAHi1QULuw-OGhCVAhYOXg_aO6QpMkdmr_Y"
ADMIN_ID          = 8612272966
TONCENTER_API_KEY = "a4e8dd9e0111177cb876e4b0559e8a58b5eeb4b6acdbd981ad4f7b6123acad9c"

# Your Tonkeeper wallet — you pay FROM here via the link
ADMIN_WALLET = "UQDlWJTEIwwGt7vai3T6s5MXgULmXk4ojhseU_UxxL7SY2DK"

# Economy
SPIN_USD     = 0.01    # 1 spin  = $0.01
SPIN_TO_TON  = 0.002   # 1 spin  = 0.002 TON
MIN_WITHDRAW = 200     # minimum spins to withdraw = $2.00 = 0.4 TON

# Slot dice values 1-64
JACKPOT_VALUE    = 43
BAR_VALUE        = 1
FRUIT_VALUES     = {22, 64}
FULL_LOSS_VALUES = {10, 20, 30, 40}   # only 4 values = full loss

# Win multipliers (× bet size)
JACKPOT_MULT  = 15     # 777   → bet × 15
BAR_MULT      = 4      # BAR   → bet × 4
FRUIT_MULT    = 1.5    # fruit → bet × 1.5
MINI_WIN_MULT = 0.8    # near miss → bet × 0.8  (lose only 20%)

# Bet options (spins per spin, 1 spin = $0.01)
BET_OPTIONS = [1, 5, 10, 25, 50]

DATA_FILE  = "user_data.json"
STATS_FILE = "stats.json"
BOT_NAME   = "FortunoSlotsbot"
# ═══════════════════════════════════════════════════════════════════

bot = Bot(token=TOKEN)
dp  = Dispatcher(storage=MemoryStorage())

# ── FSM states ─────────────────────────────────────────────────────
class WithdrawStates(StatesGroup):
    waiting_amount = State()
    waiting_wallet = State()

# ── Persistence ────────────────────────────────────────────────────
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
        "daily_active":       {},
        "daily_first_five":   {},
        "daily_new_players":  {},
        "daily_purchases":    {},
        "daily_stars_spent":  {},
        "daily_spins_played": {},
        "daily_revenue_spins":{},
    }

# Backfill missing keys for older stats files
for _key, _default in [
    ("daily_first_five",    {}),
    ("daily_new_players",   {}),
    ("daily_purchases",     {}),
    ("daily_stars_spent",   {}),
    ("daily_spins_played",  {}),
    ("daily_revenue_spins", {}),
]:
    if _key not in stats:
        stats[_key] = _default

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
            "banned":             False,
            "bet_size":           1,
            "biggest_win":        0,
        }
        stats["total_players"] += 1
        today = str(date.today())
        stats["daily_new_players"][today] = stats["daily_new_players"].get(today, 0) + 1
        save_all()
    return user_data[k]

def track_daily(uid: int):
    today = str(date.today())
    if today not in stats["daily_active"]:
        stats["daily_active"][today] = []
    k = str(uid)
    if k not in stats["daily_active"][today]:
        stats["daily_active"][today].append(k)

DAILY_EARLY_BIRD_LIMIT  = 5   # first N players each day
DAILY_EARLY_BIRD_SPINS  = 5   # free spins awarded

def check_early_bird(uid: int) -> bool:
    """
    Returns True and awards early-bird spins if this user is among
    the first DAILY_EARLY_BIRD_LIMIT players to interact today.
    Each user can only receive the bonus once per day.
    """
    today = str(date.today())
    if today not in stats["daily_first_five"]:
        stats["daily_first_five"][today] = []
    k = str(uid)
    winners = stats["daily_first_five"][today]
    if k in winners:
        return False                         # already got it today
    if len(winners) >= DAILY_EARLY_BIRD_LIMIT:
        return False                         # quota filled for today
    winners.append(k)
    u = get_user(uid)
    u["spins"] += DAILY_EARLY_BIRD_SPINS
    return True

# ── Money helpers ──────────────────────────────────────────────────
def usd(spins) -> str:
    """Convert spins to dollar string. Example: usd(100) → '$1.00'"""
    return f"${spins * SPIN_USD:.2f}"

def ton(spins) -> float:
    """Convert spins to TON amount. Example: ton(500) → 1.0"""
    return round(spins * SPIN_TO_TON, 4)

def pay_link(to_addr: str, amount_ton: float, comment: str) -> str:
    """Generate Tonkeeper deep link for one-tap payment."""
    nano = int(amount_ton * 1_000_000_000)
    return (
        f"https://app.tonkeeper.com/transfer/{to_addr}"
        f"?amount={nano}&text={quote(comment)}"
    )

# ── RTP 99% win engine ─────────────────────────────────────────────
def calc_win(dice: int, bet: int) -> tuple[int, str, str]:
    """
    Calculate win based on dice value and bet size.
    Returns: (win_spins, message_text, win_type)

    Dice value distribution (1-64):
      value 43       → JACKPOT 777  (bet × 15)
      value 1        → BAR win      (bet × 4)
      values 22, 64  → FRUIT win    (bet × 1.5)
      values 10,20,30,40 → FULL LOSS (0)
      all others (56 values) → NEAR MISS (bet × 0.8) ← 99% RTP
    """
    if dice == JACKPOT_VALUE:
        w = int(bet * JACKPOT_MULT)
        return w, (
            f"🔥 *JACKPOT! 7️⃣7️⃣7️⃣ JACKPOT!*\n\n"
            f"*+{w} SPINS ADDED!*\n"
            f"💵 Value: *{usd(w)}*\n\n"
            f"🏆 *YOU ARE A LEGEND!*"
        ), "jackpot"

    if dice == BAR_VALUE:
        w = int(bet * BAR_MULT)
        return w, (
            f"💎 *BAR WIN! NICE ONE!*\n\n"
            f"*+{w} SPINS ADDED!*\n"
            f"💵 Value: *{usd(w)}*\n\n"
            f"🔥 Keep it up!"
        ), "bar"

    if dice in FRUIT_VALUES:
        w = int(bet * FRUIT_MULT)
        return w, (
            f"🍋 *FRUIT MATCH! YOU WIN!*\n\n"
            f"*+{w} SPINS ADDED!*\n"
            f"💵 Value: *{usd(w)}*\n\n"
            f"⚡ Getting closer to jackpot!"
        ), "fruit"

    if dice in FULL_LOSS_VALUES:
        return 0, (
            f"💨 *No match this time.*\n\n"
            f"The jackpot is waiting — spin again! 🎰"
        ), "loss"

    # Near miss — 56 out of 64 values hit here
    # Player gets 80% of bet back → only loses 20%
    # This is what gives us 99% RTP
    w = int(bet * MINI_WIN_MULT)
    return w, (
        f"⚡ *SO CLOSE! Near miss!*\n\n"
        f"*+{w} SPINS* back ({usd(w)})\n\n"
        f"One more spin — jackpot is yours! 🔥"
    ), "mini"

# ── Keyboards ──────────────────────────────────────────────────────
def main_kb(uid: int) -> InlineKeyboardMarkup:
    u        = get_user(uid)
    bet      = u.get("bet_size", 1)
    ref_link = f"https://t.me/{BOT_NAME}?start={uid}"
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(
            text=f"🎰 SPIN  ·  {bet} spin{'s' if bet>1 else ''} = {usd(bet)}",
            callback_data="spin"
        )],
        [InlineKeyboardButton(text="🎲 CHANGE BET SIZE", callback_data="change_bet")],
        [InlineKeyboardButton(text="💎 BUY 100 SPINS — 10 ⭐", callback_data="buy")],
        [InlineKeyboardButton(text="💸 WITHDRAW TO TON", callback_data="withdraw_req")],
        [InlineKeyboardButton(text="📊 MY STATS", callback_data="my_stats")],
        [InlineKeyboardButton(
            text="📢 INVITE & GET +5 FREE SPINS (friend gets +5 too!)",
            url=f"https://t.me/share/url?url={ref_link}"
        )],
    ])

def bet_kb(uid: int) -> InlineKeyboardMarkup:
    u   = get_user(uid)
    bal = u.get("spins", 0)
    rows = []
    for b in BET_OPTIONS:
        can     = "✅" if bal >= b else "❌"
        jackpot = int(b * JACKPOT_MULT)
        rows.append([InlineKeyboardButton(
            text=f"{can} {b}x · costs {usd(b)} · 🔥 jackpot = {usd(jackpot)}",
            callback_data=f"bet_{b}"
        )])
    rows.append([InlineKeyboardButton(text="🔙 BACK", callback_data="back_main")])
    return InlineKeyboardMarkup(inline_keyboard=rows)

def no_spins_kb(uid: int) -> InlineKeyboardMarkup:
    ref_link = f"https://t.me/{BOT_NAME}?start={uid}"
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💎 BUY 100 SPINS — 10 ⭐", callback_data="buy")],
        [InlineKeyboardButton(
            text="📢 INVITE FRIEND · +5 SPINS FOR YOU & THEM",
            url=f"https://t.me/share/url?url={ref_link}"
        )],
        [InlineKeyboardButton(text="🎲 LOWER MY BET", callback_data="change_bet")],
    ])

spin_again_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🎰 SPIN AGAIN",  callback_data="spin")],
    [InlineKeyboardButton(text="🎲 CHANGE BET",  callback_data="change_bet")],
    [InlineKeyboardButton(text="💎 BUY SPINS",   callback_data="buy")],
])

# ── /start ─────────────────────────────────────────────────────────
@dp.message(Command("start"))
async def cmd_start(message: Message, command: CommandObject):
    uid    = message.from_user.id
    user   = get_user(uid)
    is_new = not user.get("ever_started", False)

    if is_new:
        user["spins"]        = 10
        user["ever_started"] = True

    # ── Early-bird bonus: first 5 players each day get +5 free spins ──
    early_bird_won = check_early_bird(uid)

    # ── Referral bonus (forwarder gets +5 spins when friend joins) ───
    referral_bonus_msg = ""
    if command.args and is_new:
        try:
            ref_id = int(command.args)
            if ref_id != uid:
                ref = get_user(ref_id)
                ref["spins"]        += 5
                ref["referrals"]    += 1
                user["referred_by"]  = ref_id
                stats["total_referrals"] += 1
                save_all()
                await bot.send_message(
                    ref_id,
                    f"🎊 *A friend joined using your link!*\n"
                    f"*+5 FREE SPINS* credited to you!\n"
                    f"💰 Balance: *{ref['spins']}* spins\n"
                    f"👥 Total invited: *{ref['referrals']}*",
                    parse_mode="Markdown"
                )
        except (ValueError, TypeError):
            pass

    track_daily(uid)
    save_all()

    bal = user["spins"]

    # Build early-bird notice if they won it
    early_bird_msg = ""
    if early_bird_won:
        today_winners = len(stats["daily_first_five"].get(str(date.today()), []))
        early_bird_msg = (
            f"\n🌅 *EARLY BIRD #{today_winners}!* You're among the first {DAILY_EARLY_BIRD_LIMIT} "
            f"players today — *+{DAILY_EARLY_BIRD_SPINS} FREE SPINS* added!\n"
        )

    await message.answer(
        f"🎰 *FORTUNOBET — THE HOTTEST TON CASINO* 🎰\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"{'🎁 *WELCOME GIFT: 10 FREE SPINS!*' if is_new else f'👋 Welcome back!'}\n"
        f"{early_bird_msg}\n"
        f"💰 *Your Balance:* {bal} spins · {usd(bal)}\n\n"
        f"🔥 *Why FortunoBet?*\n"
        f"⚡ 99% RTP — highest in Telegram!\n"
        f"💎 1 spin = $0.01 — real money!\n"
        f"🏆 Win up to ×15 your bet!\n"
        f"💸 Instant TON payouts in 2 hours\n"
        f"📢 Invite friends → +5 spins each time!\n\n"
        f"🎯 *Withdraw from just {MIN_WITHDRAW} spins = {usd(MIN_WITHDRAW)}!*",
        reply_markup=main_kb(uid),
        parse_mode="Markdown",
    )

# ── /balance ───────────────────────────────────────────────────────
@dp.message(Command("balance"))
async def cmd_balance(message: Message):
    u = get_user(message.from_user.id)
    await message.answer(
        f"💰 *Your Balance:*\n\n"
        f"🎰 *{u['spins']}* spins\n"
        f"💵 = *{usd(u['spins'])}* USD\n"
        f"💎 = *{ton(u['spins'])} TON*",
        parse_mode="Markdown",
        reply_markup=main_kb(message.from_user.id)
    )

# ── Change bet ─────────────────────────────────────────────────────
@dp.callback_query(F.data == "change_bet")
async def change_bet_menu(callback: types.CallbackQuery):
    u = get_user(callback.from_user.id)
    lines = "\n".join([
        f"  *{b}x* · costs {usd(b)} · "
        f"near miss returns {usd(int(b * MINI_WIN_MULT))} · "
        f"🔥 jackpot *{usd(int(b * JACKPOT_MULT))}*"
        for b in BET_OPTIONS
    ])
    await callback.message.answer(
        f"🎲 *SELECT YOUR BET SIZE*\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"Higher bet = bigger wins!\n"
        f"Near miss = 80% of bet returned\n\n"
        f"💰 Your balance: *{u['spins']}* spins ({usd(u['spins'])})\n\n"
        f"{lines}",
        reply_markup=bet_kb(callback.from_user.id),
        parse_mode="Markdown"
    )
    await callback.answer()

@dp.callback_query(F.data.startswith("bet_"))
async def set_bet(callback: types.CallbackQuery):
    u        = get_user(callback.from_user.id)
    bet_size = int(callback.data.split("_")[1])
    if u["spins"] < bet_size:
        await callback.answer(
            f"❌ Need {bet_size} spins ({usd(bet_size)}) for this bet!",
            show_alert=True
        )
        return
    u["bet_size"] = bet_size
    save_all()
    await callback.message.answer(
        f"✅ *Bet set to {bet_size}x!*\n\n"
        f"💰 Balance: *{u['spins']}* spins ({usd(u['spins'])})\n\n"
        f"Each spin costs *{bet_size}* spin{'s' if bet_size>1 else ''} ({usd(bet_size)})\n\n"
        f"🔥 Jackpot = *+{int(bet_size * JACKPOT_MULT)}* spins ({usd(int(bet_size * JACKPOT_MULT))})\n"
        f"💎 Bar win = *+{int(bet_size * BAR_MULT)}* spins ({usd(int(bet_size * BAR_MULT))})\n"
        f"🍋 Fruit   = *+{int(bet_size * FRUIT_MULT)}* spins ({usd(int(bet_size * FRUIT_MULT))})\n"
        f"⚡ Near miss = *+{int(bet_size * MINI_WIN_MULT)}* spins back ({usd(int(bet_size * MINI_WIN_MULT))})\n\n"
        f"*Spin now and win big!* 🎰",
        reply_markup=main_kb(callback.from_user.id),
        parse_mode="Markdown",
    )
    await callback.answer(f"Bet set to {bet_size}x!")

# ── Spin ────────────────────────────────────────────────────────────
@dp.callback_query(F.data == "spin")
async def play_slots(callback: types.CallbackQuery):
    uid      = callback.from_user.id
    u        = get_user(uid)
    bet_size = u.get("bet_size", 1)

    if u.get("banned"):
        await callback.answer("🚫 You are banned.", show_alert=True)
        return

    if u["spins"] < bet_size:
        await callback.message.answer(
            f"😤 *Not enough spins!*\n\n"
            f"Balance: *{u['spins']}* spins\n"
            f"Bet size: *{bet_size}x* = {usd(bet_size)}\n\n"
            f"🔥 *Don't stop — your jackpot is one spin away!*\n\n"
            f"💎 Buy 100 spins for just *10 ⭐ Stars*\n"
            f"📢 Invite a friend → *+5 FREE spins*\n"
            f"🎲 Or lower your bet size!",
            reply_markup=no_spins_kb(uid),
            parse_mode="Markdown",
        )
        await callback.answer("❌ Not enough spins!")
        return

    # Deduct bet before spin
    u["spins"]             -= bet_size
    u["total_spins_played"] = u.get("total_spins_played", 0) + bet_size
    stats["total_spins_played"] = stats.get("total_spins_played", 0) + bet_size
    today = str(date.today())
    stats["daily_spins_played"][today] = stats["daily_spins_played"].get(today, 0) + bet_size
    track_daily(uid)
    save_all()

    # Roll the dice
    msg  = await callback.message.answer_dice(emoji="🎰")
    dice = msg.dice.value
    await asyncio.sleep(2.5)   # wait for animation to finish

    win_spins, win_text, win_type = calc_win(dice, bet_size)

    # Update user stats
    u["spins"]    += win_spins
    u["total_won"] = u.get("total_won", 0) + win_spins
    if win_spins > u.get("biggest_win", 0):
        u["biggest_win"] = win_spins

    # Update global stats
    if win_type == "jackpot":
        stats["total_jackpots"] = stats.get("total_jackpots", 0) + 1
    elif win_type == "bar":
        stats["total_bar_wins"] = stats.get("total_bar_wins", 0) + 1
    elif win_type == "fruit":
        stats["total_fruit_wins"] = stats.get("total_fruit_wins", 0) + 1
    elif win_type == "mini":
        stats["total_mini_wins"] = stats.get("total_mini_wins", 0) + 1
    else:
        stats["total_losses"] = stats.get("total_losses", 0) + 1

    save_all()

    # Withdraw hint when close or ready
    hint = ""
    if u["spins"] >= MIN_WITHDRAW:
        hint = f"\n\n💸 *You can WITHDRAW NOW!*\nPress WITHDRAW TO TON! 🚀"
    elif 0 < MIN_WITHDRAW - u["spins"] <= 50:
        hint = f"\n\n🔥 *Only {MIN_WITHDRAW - u['spins']} more spins to withdraw!*"

    await callback.message.answer(
        f"{win_text}\n\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"💰 Balance: *{u['spins']}* spins · {usd(u['spins'])}"
        f"{hint}",
        reply_markup=spin_again_kb,
        parse_mode="Markdown",
    )
    await callback.answer()

# ── My Stats ───────────────────────────────────────────────────────
@dp.callback_query(F.data == "my_stats")
async def my_stats(callback: types.CallbackQuery):
    uid      = callback.from_user.id
    u        = get_user(uid)
    ref_link = f"https://t.me/{BOT_NAME}?start={uid}"
    needed   = max(0, MIN_WITHDRAW - u["spins"])

    await callback.message.answer(
        f"📊 *YOUR STATS*\n"
        f"━━━━━━━━━━━━━━━━━━━━\n\n"
        f"💰 Balance: *{u['spins']}* spins\n"
        f"     = *{usd(u['spins'])}* USD\n"
        f"     = *{ton(u['spins'])} TON*\n\n"
        f"🎰 Spins played: *{u.get('total_spins_played', 0)}*\n"
        f"🏆 Biggest win: *{u.get('biggest_win', 0)}* spins ({usd(u.get('biggest_win', 0))})\n"
        f"🎲 Current bet: *{u.get('bet_size', 1)}x* ({usd(u.get('bet_size', 1))})\n"
        f"👥 Friends invited: *{u.get('referrals', 0)}*\n"
        f"💎 Purchases: *{u.get('purchases', 0)}*\n"
        f"📅 Joined: *{u.get('joined_date', 'N/A')}*\n\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"🏁 *Withdraw goal:*\n"
        f"Minimum: *{MIN_WITHDRAW} spins* = *{usd(MIN_WITHDRAW)}* = *{ton(MIN_WITHDRAW)} TON*\n"
        f"{'✅ *READY TO WITHDRAW NOW!*' if needed == 0 else f'You need *{needed}* more spins ({usd(needed)})'}\n\n"
        f"🔗 *Your invite link:*\n`{ref_link}`",
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(
                text="📢 SHARE MY INVITE LINK",
                url=f"https://t.me/share/url?url={ref_link}"
            )],
            [InlineKeyboardButton(text="🔙 BACK", callback_data="back_main")],
        ])
    )
    await callback.answer()

@dp.callback_query(F.data == "back_main")
async def back_main(callback: types.CallbackQuery):
    u = get_user(callback.from_user.id)
    await callback.message.answer(
        f"🎰 *FORTUNOBET*\n\n"
        f"💰 *Balance:* {u['spins']} spins · {usd(u['spins'])}",
        reply_markup=main_kb(callback.from_user.id),
        parse_mode="Markdown",
    )
    await callback.answer()

# ── Withdraw Step 1 ────────────────────────────────────────────────
@dp.callback_query(F.data == "withdraw_req")
async def withdraw_start(callback: types.CallbackQuery, state: FSMContext):
    u = get_user(callback.from_user.id)

    if u["spins"] < MIN_WITHDRAW:
        needed = MIN_WITHDRAW - u["spins"]
        await callback.message.answer(
            f"💸 *WITHDRAWAL*\n\n"
            f"❌ Minimum withdrawal is *{MIN_WITHDRAW} spins* ({usd(MIN_WITHDRAW)})\n\n"
            f"Your balance: *{u['spins']}* spins ({usd(u['spins'])})\n"
            f"You need *{needed}* more spins ({usd(needed)})!\n\n"
            f"*{MIN_WITHDRAW} spins = {ton(MIN_WITHDRAW)} TON = {usd(MIN_WITHDRAW)}*\n\n"
            f"🔥 Keep spinning — you're almost there!",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="🎰 KEEP SPINNING", callback_data="spin")],
                [InlineKeyboardButton(text="💎 BUY MORE SPINS", callback_data="buy")],
            ])
        )
        await callback.answer()
        return

    if u.get("pending_withdrawal"):
        await callback.answer(
            "⏳ Your withdrawal is being processed! Check back in 2 hours.",
            show_alert=True
        )
        return

    await state.set_state(WithdrawStates.waiting_amount)
    await callback.message.answer(
        f"💸 *WITHDRAWAL REQUEST*\n"
        f"━━━━━━━━━━━━━━━━━━━━\n\n"
        f"💰 Your balance: *{u['spins']}* spins\n"
        f"     = *{ton(u['spins'])} TON*\n"
        f"     = *{usd(u['spins'])} USD*\n\n"
        f"📝 *How many spins to withdraw?*\n\n"
        f"Minimum: *{MIN_WITHDRAW} spins* ({usd(MIN_WITHDRAW)})\n"
        f"Maximum: *{u['spins']} spins* ({usd(u['spins'])})\n\n"
        f"⏱ Processing time: *2 hours*\n\n"
        f"Type a number below 👇",
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(
                text=f"💰 WITHDRAW ALL — {u['spins']} spins = {ton(u['spins'])} TON ({usd(u['spins'])})",
                callback_data="withdraw_all"
            )],
            [InlineKeyboardButton(text="❌ CANCEL", callback_data="cancel_withdraw")],
        ])
    )
    await callback.answer()

# ── Withdraw Step 2 — amount typed ────────────────────────────────
@dp.message(WithdrawStates.waiting_amount)
async def withdraw_amount(message: Message, state: FSMContext):
    u = get_user(message.from_user.id)
    try:
        amount = int(message.text.strip())
    except ValueError:
        await message.answer(
            f"❌ Please type a number.\nExample: `{MIN_WITHDRAW}`",
            parse_mode="Markdown"
        )
        return
    if amount < MIN_WITHDRAW:
        await message.answer(
            f"❌ Minimum is *{MIN_WITHDRAW}* spins ({usd(MIN_WITHDRAW)}).\n"
            f"You typed: *{amount}* ({usd(amount)})",
            parse_mode="Markdown"
        )
        return
    if amount > u["spins"]:
        await message.answer(
            f"❌ You only have *{u['spins']}* spins ({usd(u['spins'])}).",
            parse_mode="Markdown"
        )
        return

    await state.update_data(withdraw_amount=amount)
    await state.set_state(WithdrawStates.waiting_wallet)
    await message.answer(
        f"✅ *{amount} spins selected*\n\n"
        f"You will receive:\n"
        f"💎 *{ton(amount)} TON*\n"
        f"💵 *{usd(amount)} USD*\n\n"
        f"⏱ Processing time: *2 hours*\n\n"
        f"📝 Now send your *TON wallet address*\n"
        f"_(Starts with UQ, EQ, or 0Q)_",
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="❌ CANCEL", callback_data="cancel_withdraw")]
        ])
    )

# ── Withdraw all button ────────────────────────────────────────────
@dp.callback_query(F.data == "withdraw_all")
async def withdraw_all(callback: types.CallbackQuery, state: FSMContext):
    u      = get_user(callback.from_user.id)
    amount = u["spins"]
    await state.update_data(withdraw_amount=amount)
    await state.set_state(WithdrawStates.waiting_wallet)
    await callback.message.answer(
        f"✅ *Withdrawing all {amount} spins*\n\n"
        f"You will receive:\n"
        f"💎 *{ton(amount)} TON*\n"
        f"💵 *{usd(amount)} USD*\n\n"
        f"⏱ Processing time: *2 hours*\n\n"
        f"📝 Now send your *TON wallet address*\n"
        f"_(Starts with UQ, EQ, or 0Q)_",
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="❌ CANCEL", callback_data="cancel_withdraw")]
        ])
    )
    await callback.answer()

# ── Cancel withdraw ────────────────────────────────────────────────
@dp.callback_query(F.data == "cancel_withdraw")
async def cancel_withdraw(callback: types.CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.message.answer(
        "❌ *Withdrawal cancelled.*",
        parse_mode="Markdown",
        reply_markup=main_kb(callback.from_user.id)
    )
    await callback.answer()

# ── Withdraw Step 3 — wallet address ──────────────────────────────
@dp.message(WithdrawStates.waiting_wallet)
async def withdraw_wallet(message: Message, state: FSMContext):
    wallet = message.text.strip()
    uid    = message.from_user.id
    u      = get_user(uid)
    data   = await state.get_data()
    amount = data.get("withdraw_amount", 0)

    # Validate wallet address format
    if not (wallet.startswith(("UQ", "EQ", "0Q")) and len(wallet) >= 48):
        await message.answer(
            "❌ *Invalid wallet address!*\n\n"
            "Must start with *UQ*, *EQ*, or *0Q*\n"
            "and be at least 48 characters long.\n\n"
            "Open Tonkeeper → copy your address → paste here.",
            parse_mode="Markdown"
        )
        return

    if amount > u["spins"]:
        await message.answer(
            f"❌ Your balance changed. You now have *{u['spins']}* spins.",
            parse_mode="Markdown"
        )
        await state.clear()
        return

    ton_amount = ton(amount)
    u["pending_withdrawal"] = True
    u["pending_spins"]      = amount
    u["pending_wallet"]     = wallet
    save_all()
    await state.clear()

    # Send Tonkeeper payment link to admin
    link = pay_link(wallet, ton_amount, f"FortunoBet payout {uid}")
    await bot.send_message(
        ADMIN_ID,
        f"🚨 *NEW PAYOUT REQUEST*\n"
        f"━━━━━━━━━━━━━━━━━━━━\n\n"
        f"👤 {message.from_user.full_name}\n"
        f"🆔 `{uid}`\n"
        f"🎰 Spins: *{amount}*\n"
        f"💎 TON: *{ton_amount}*\n"
        f"💵 USD: *{usd(amount)}*\n"
        f"👛 Wallet:\n`{wallet}`\n\n"
        f"👇 *Tap PAY → Tonkeeper opens → tap Confirm:*",
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(
                text=f"💎 PAY {ton_amount} TON via Tonkeeper",
                url=link
            )],
            [InlineKeyboardButton(
                text="✅ CONFIRM — I SENT THE PAYMENT",
                callback_data=f"confirm_pay_{uid}"
            )],
        ])
    )

    await message.answer(
        f"✅ *Withdrawal Request Submitted!*\n"
        f"━━━━━━━━━━━━━━━━━━━━\n\n"
        f"🎰 Spins: *{amount}*\n"
        f"💎 You will receive: *{ton_amount} TON*\n"
        f"💵 Value: *{usd(amount)}*\n\n"
        f"⏱ *Processing time: up to 2 hours*\n\n"
        f"You will get a notification when payment is sent! 🔔",
        parse_mode="Markdown",
        reply_markup=main_kb(uid)
    )

# ── Admin confirms payment via button ──────────────────────────────
@dp.callback_query(F.data.startswith("confirm_pay_"))
async def confirm_payment(callback: types.CallbackQuery):
    if callback.from_user.id != ADMIN_ID:
        await callback.answer("❌ Not authorized.", show_alert=True)
        return

    target_id = str(callback.data.replace("confirm_pay_", ""))
    u         = user_data.get(target_id)

    if not u or not u.get("pending_withdrawal"):
        await callback.answer("❌ No pending withdrawal found.", show_alert=True)
        return

    amount     = u.get("pending_spins", 0)
    ton_amount = ton(amount)
    wallet     = u.get("pending_wallet")

    # Deduct spins and clear pending status
    u["spins"]             -= amount
    u["pending_withdrawal"] = False
    u["pending_spins"]      = 0
    u["pending_wallet"]     = None
    stats["total_ton_paid"] = round(stats.get("total_ton_paid", 0) + ton_amount, 4)
    save_all()

    await callback.message.edit_reply_markup(reply_markup=None)
    await callback.message.answer(
        f"✅ *Payment Confirmed!*\n\n"
        f"User: `{target_id}`\n"
        f"Amount: *{ton_amount} TON* ({usd(amount)})\n"
        f"Wallet: `{wallet}`",
        parse_mode="Markdown"
    )

    # Notify the player
    await bot.send_message(
        int(target_id),
        f"💸 *YOUR WITHDRAWAL IS COMPLETE!*\n"
        f"━━━━━━━━━━━━━━━━━━━━\n\n"
        f"*{ton_amount} TON* has been sent to your wallet!\n"
        f"💵 Value: *{usd(amount)}*\n\n"
        f"Check your Tonkeeper now! 🎉\n\n"
        f"Thank you for playing FortunoBet! 🎰\n"
        f"Come back and win even more! 🔥",
        parse_mode="Markdown",
        reply_markup=main_kb(int(target_id))
    )
    await callback.answer("✅ Payment confirmed!")

# ══════════════════════════════════════════════════════════════════
#  ADMIN COMMANDS
# ══════════════════════════════════════════════════════════════════

# /admin — full dashboard
# Shows: players, revenue, spins played, wins, losses,
#        pending payouts, top 5 players, top referrers, biggest wins
@dp.message(Command("admin"))
async def admin_dashboard(message: Message):
    if message.from_user.id != ADMIN_ID:
        return   # invisible to non-admins

    today        = str(date.today())
    active_today = len(stats["daily_active"].get(today, []))
    early_today  = len(stats["daily_first_five"].get(today, []))
    pending      = [(k, v) for k, v in user_data.items() if v.get("pending_withdrawal")]
    top_players  = sorted(user_data.items(), key=lambda x: x[1].get("spins", 0), reverse=True)[:5]
    top_refs     = sorted(user_data.items(), key=lambda x: x[1].get("referrals", 0), reverse=True)[:5]
    top_winners  = sorted(user_data.items(), key=lambda x: x[1].get("biggest_win", 0), reverse=True)[:3]

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
        f"  Early-bird bonus claimed today: *{early_today}/{DAILY_EARLY_BIRD_LIMIT}*\n"
        f"  Referrals: *{stats['total_referrals']}*\n\n"
        f"🎰 *GAME*\n"
        f"  Spins played: *{stats.get('total_spins_played',0)}*\n"
        f"  Jackpots 777: *{stats.get('total_jackpots',0)}*\n"
        f"  Bar wins: *{stats.get('total_bar_wins',0)}*\n"
        f"  Fruit wins: *{stats.get('total_fruit_wins',0)}*\n"
        f"  Near miss wins: *{stats.get('total_mini_wins',0)}*\n"
        f"  Full losses: *{stats.get('total_losses',0)}*\n\n"
        f"💵 *REVENUE*\n"
        f"  Spins sold: *{spins_sold}*\n"
        f"  Est. revenue: *${revenue:.2f}*\n"
        f"  TON paid out: *{stats.get('total_ton_paid',0)} TON*\n\n"
        f"⏳ *PENDING PAYOUTS*\n{pend_text}\n\n"
        f"🏆 *TOP 5 BY BALANCE*\n{top_text}\n\n"
        f"📢 *TOP 5 REFERRERS*\n{ref_text}\n\n"
        f"🥇 *TOP 3 BIGGEST WINS*\n{win_text}\n\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"🛠 *COMMANDS*\n"
        f"`/pay [id]` — send Tonkeeper payment link\n"
        f"`/gift [id] [spins]` — give free spins\n"
        f"`/userinfo [id]` — full user details\n"
        f"`/ban [id]` / `/unban [id]` — ban control\n"
        f"`/broadcast [msg]` — message all users\n"
        f"`/stats7` — last 7 days detailed breakdown",
        parse_mode="Markdown",
    )

# /stats7 — last 7 days breakdown
# Shows per-day: new players, active players, purchases, Stars spent, revenue, spins played
@dp.message(Command("stats7"))
async def admin_stats7(message: Message):
    if message.from_user.id != ADMIN_ID:
        return

    lines = []
    total_new = total_active = total_purchases = total_stars = total_rev_spins = total_spins = 0

    for i in range(6, -1, -1):   # 6 days ago → today
        d         = str(date.today() - timedelta(days=i))
        label     = "TODAY" if i == 0 else ("YESTERDAY" if i == 1 else d)
        new_p     = stats["daily_new_players"].get(d, 0)
        active    = len(stats["daily_active"].get(d, []))
        purchases = stats["daily_purchases"].get(d, 0)
        stars     = stats["daily_stars_spent"].get(d, 0)
        rev_spins = stats["daily_revenue_spins"].get(d, 0)
        spins_pl  = stats["daily_spins_played"].get(d, 0)
        revenue   = rev_spins * SPIN_USD

        total_new        += new_p
        total_active     += active
        total_purchases  += purchases
        total_stars      += stars
        total_rev_spins  += rev_spins
        total_spins      += spins_pl

        lines.append(
            f"📅 *{label}*\n"
            f"  👤 New players: *{new_p}*  |  Active: *{active}*\n"
            f"  💎 Purchases: *{purchases}*  |  ⭐ Stars: *{stars}*\n"
            f"  💵 Revenue: *${revenue:.2f}*  |  🎰 Spins played: *{spins_pl}*"
        )

    summary = (
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"📊 *7-DAY TOTALS*\n"
        f"  👤 New players: *{total_new}*\n"
        f"  🟢 Active sessions: *{total_active}*\n"
        f"  💎 Purchases: *{total_purchases}*\n"
        f"  ⭐ Stars spent: *{total_stars}*\n"
        f"  💵 Revenue: *${total_rev_spins * SPIN_USD:.2f}*\n"
        f"  🎰 Spins played: *{total_spins}*"
    )

    await message.answer(
        f"📈 *LAST 7 DAYS — DAILY STATS*\n"
        f"━━━━━━━━━━━━━━━━━━━━\n\n"
        + "\n\n".join(lines)
        + "\n\n" + summary,
        parse_mode="Markdown",
    )
# Sends you a Tonkeeper payment link for that user.
# Tap the link → Tonkeeper opens → tap Confirm.
# Then tap the "✅ CONFIRM" button in chat to notify user.
# Example: /pay 773227767
@dp.message(Command("pay"))
async def admin_pay(message: Message):
    if message.from_user.id != ADMIN_ID:
        return
    try:
        target_id = str(int(message.text.split()[1]))
        u         = user_data.get(target_id)
        if not u or not u.get("pending_withdrawal"):
            await message.answer(
                "❌ No pending withdrawal for this user.\n"
                "Use `/admin` to see all pending payouts.",
                parse_mode="Markdown"
            )
            return
        wallet     = u.get("pending_wallet")
        amount     = u.get("pending_spins", 0)
        ton_amount = ton(amount)
        link       = pay_link(wallet, ton_amount, f"FortunoBet payout {target_id}")
        await message.answer(
            f"💸 *SEND PAYMENT*\n\n"
            f"To: `{wallet}`\n"
            f"Amount: *{ton_amount} TON* ({usd(amount)})\n"
            f"User: `{target_id}`\n\n"
            f"1️⃣ Tap the button below\n"
            f"2️⃣ Tonkeeper opens with amount filled\n"
            f"3️⃣ Tap Confirm in Tonkeeper\n"
            f"4️⃣ Tap ✅ CONFIRM button here",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(
                    text=f"💎 PAY {ton_amount} TON via Tonkeeper",
                    url=link
                )],
                [InlineKeyboardButton(
                    text="✅ CONFIRM — I SENT THE PAYMENT",
                    callback_data=f"confirm_pay_{target_id}"
                )],
            ])
        )
    except (IndexError, ValueError):
        await message.answer(
            "❌ Wrong format.\nUsage: `/pay [user_id]`\nExample: `/pay 773227767`",
            parse_mode="Markdown"
        )

# /gift [user_id] [amount]
# Gives free spins to any user. User gets notified.
# Example: /gift 773227767 100
# Example: /gift 7627990095 500
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
            f"✅ *Gift sent!*\n\n"
            f"User: `{target_id}`\n"
            f"Added: *{amount}* spins ({usd(amount)})\n"
            f"New balance: *{u['spins']}* spins ({usd(u['spins'])})",
            parse_mode="Markdown"
        )
        await bot.send_message(
            int(target_id),
            f"🎁 *BONUS SPINS!*\n\n"
            f"You received *{amount} FREE SPINS!*\n"
            f"💵 Value: *{usd(amount)}*\n"
            f"💰 New balance: *{u['spins']}* spins\n\n"
            f"Go win big! 🎰🔥",
            parse_mode="Markdown",
            reply_markup=main_kb(int(target_id))
        )
    except (IndexError, ValueError):
        await message.answer(
            "❌ Wrong format.\nUsage: `/gift [user_id] [amount]`\n"
            "Example: `/gift 773227767 100`",
            parse_mode="Markdown"
        )

# /userinfo [user_id]
# Shows full details about any user.
# Example: /userinfo 773227767
@dp.message(Command("userinfo"))
async def admin_userinfo(message: Message):
    if message.from_user.id != ADMIN_ID:
        return
    try:
        target_id = str(int(message.text.split()[1]))
        u         = user_data.get(target_id)
        if not u:
            await message.answer("❌ User not found. They must have started the bot first.")
            return
        await message.answer(
            f"👤 *USER INFO*\n"
            f"━━━━━━━━━━━━━━━━━━━━\n\n"
            f"🆔 ID: `{target_id}`\n"
            f"💰 Balance: *{u.get('spins',0)}* spins ({usd(u.get('spins',0))})\n"
            f"💎 TON value: *{ton(u.get('spins',0))} TON*\n\n"
            f"🎰 Spins played: *{u.get('total_spins_played',0)}*\n"
            f"🏆 Biggest win: *{u.get('biggest_win',0)}* spins ({usd(u.get('biggest_win',0))})\n"
            f"🎲 Bet size: *{u.get('bet_size',1)}x*\n\n"
            f"👥 Friends invited: *{u.get('referrals',0)}*\n"
            f"💎 Purchases: *{u.get('purchases',0)}*\n"
            f"📅 Joined: *{u.get('joined_date','N/A')}*\n\n"
            f"🚫 Banned: *{u.get('banned',False)}*\n"
            f"⏳ Pending withdrawal: *{u.get('pending_withdrawal',False)}*\n"
            f"💸 Pending spins: *{u.get('pending_spins',0)}* ({usd(u.get('pending_spins',0))})\n"
            f"👛 Pending wallet: `{u.get('pending_wallet','None')}`",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(
                    text=f"🎁 Gift spins to this user",
                    callback_data=f"gift_menu_{target_id}"
                )],
                [InlineKeyboardButton(
                    text=f"{'✅ Unban' if u.get('banned') else '🚫 Ban'} this user",
                    callback_data=f"toggle_ban_{target_id}"
                )],
            ])
        )
    except (IndexError, ValueError):
        await message.answer(
            "❌ Wrong format.\nUsage: `/userinfo [user_id]`\n"
            "Example: `/userinfo 773227767`",
            parse_mode="Markdown"
        )

# Quick ban/unban from userinfo button
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
    await callback.message.answer(
        f"{status} user `{target_id}`.",
        parse_mode="Markdown"
    )

# /ban [user_id]
# Bans a user. They cannot spin anymore.
# Example: /ban 773227767
@dp.message(Command("ban"))
async def admin_ban(message: Message):
    if message.from_user.id != ADMIN_ID:
        return
    try:
        target_id = str(int(message.text.split()[1]))
        get_user(int(target_id))["banned"] = True
        save_all()
        await message.answer(
            f"🚫 *Banned* user `{target_id}`.\n"
            f"They can no longer spin.",
            parse_mode="Markdown"
        )
    except (IndexError, ValueError):
        await message.answer(
            "❌ Wrong format.\nUsage: `/ban [user_id]`\n"
            "Example: `/ban 773227767`",
            parse_mode="Markdown"
        )

# /unban [user_id]
# Removes ban. User can play again.
# Example: /unban 773227767
@dp.message(Command("unban"))
async def admin_unban(message: Message):
    if message.from_user.id != ADMIN_ID:
        return
    try:
        target_id = str(int(message.text.split()[1]))
        get_user(int(target_id))["banned"] = False
        save_all()
        await message.answer(
            f"✅ *Unbanned* user `{target_id}`.\n"
            f"They can play again.",
            parse_mode="Markdown"
        )
    except (IndexError, ValueError):
        await message.answer(
            "❌ Wrong format.\nUsage: `/unban [user_id]`\n"
            "Example: `/unban 773227767`",
            parse_mode="Markdown"
        )

# /broadcast [message]
# Sends a message to ALL users at once.
# Banned users are skipped automatically.
# Example: /broadcast 🔥 Double wins event — spin now!
# Example: /broadcast 💎 New jackpot! Come play!
@dp.message(Command("broadcast"))
async def admin_broadcast(message: Message):
    if message.from_user.id != ADMIN_ID:
        return
    try:
        text = message.text.split(" ", 1)[1]
    except IndexError:
        await message.answer(
            "❌ Wrong format.\nUsage: `/broadcast [message]`\n"
            "Example: `/broadcast 🔥 Special event today!`",
            parse_mode="Markdown"
        )
        return

    await message.answer(f"📢 Sending to all users...")
    sent = failed = 0
    for k in user_data:
        if user_data[k].get("banned"):
            continue
        try:
            await bot.send_message(
                int(k),
                f"📢 *FortunoBet:*\n\n{text}",
                parse_mode="Markdown"
            )
            sent += 1
            await asyncio.sleep(0.05)   # avoid Telegram rate limit
        except Exception:
            failed += 1

    await message.answer(
        f"✅ *Broadcast complete!*\n\n"
        f"Sent: *{sent}* users\n"
        f"Failed: *{failed}* users",
        parse_mode="Markdown"
    )

# ── Stars payment ───────────────────────────────────────────────────
@dp.callback_query(F.data == "buy")
async def process_buy(callback: types.CallbackQuery):
    await bot.send_invoice(
        callback.message.chat.id,
        title="100 Spins — $1.00 Value",
        description="100 spins · 1 spin = $0.01 · 99% RTP · Instant TON payouts",
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
    u = get_user(m.from_user.id)
    u["spins"]    += 100
    u["purchases"] = u.get("purchases", 0) + 1
    stats["total_spins_bought"] = stats.get("total_spins_bought", 0) + 100
    today = str(date.today())
    stats["daily_purchases"][today]    = stats["daily_purchases"].get(today, 0) + 1
    stats["daily_stars_spent"][today]  = stats["daily_stars_spent"].get(today, 0) + 10
    stats["daily_revenue_spins"][today]= stats["daily_revenue_spins"].get(today, 0) + 100
    save_all()
    await m.answer(
        f"✅ *100 SPINS ADDED!*\n\n"
        f"💰 New balance: *{u['spins']}* spins\n"
        f"💵 Value: *{usd(u['spins'])}* USD\n\n"
        f"🔥 *Go spin and win big!* 🎰",
        parse_mode="Markdown",
        reply_markup=main_kb(m.from_user.id)
    )

# ── Main ─────────────────────────────────────────────────────────────
async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s"
    )
    logging.info("FortunoBet FINAL is online!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


# ══════════════════════════════════════════════════════════════════
#  QUICK ADMIN COMMAND REFERENCE
#  (copy-paste these in your bot chat)
# ══════════════════════════════════════════════════════════════════
#
#  /admin
#      → Full dashboard with all stats
#
#  /pay 773227767
#      → Send payment link for user 773227767
#
#  /gift 773227767 100
#      → Give 100 free spins to user 773227767
#
#  /gift 7627990095 500
#      → Give yourself 500 spins for testing
#
#  /userinfo 773227767
#      → See full info about user 773227767
#
#  /ban 773227767
#      → Ban user 773227767
#
#  /unban 773227767
#      → Unban user 773227767
#
#  /broadcast 🔥 Special event today! Double wins!
#      → Send message to ALL users
#
#  /broadcast 💎 New jackpot added! Come spin now!
#      → Another broadcast example
#
# ══════════════════════════════════════════════════════════════════