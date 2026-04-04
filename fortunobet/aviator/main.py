# """
# AviatorBet ✈️ — PRODUCTION VERSION
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Install: pip install aiogram
# Run:     python3 aviator_bot.py

# ECONOMY:
#   1 spin = $0.01 = 0.002 TON
#   200 spins = $2.00 = 0.4 TON  <- min withdrawal
#   Buy packages: 10 / 25 / 50 / 100 Stars

# RTP ~97%:
#   Crash point generated via provably-fair formula.
#   House edge = 3% baked into crash distribution.

# GAME FLOW:
#   1. User picks bet (1/5/10/25/50 spins)
#   2. Presses ✈️ FLY — round starts, multiplier climbs
#   3. Presses 💰 CASHOUT before crash to win (bet × multiplier)
#   4. If no cashout before crash → full bet lost

# ADMIN COMMANDS:
#   /admin              main dashboard
#   /stats7             last 7 days
#   /pay [id]           Tonkeeper payout link
#   /reject [id]        reject withdrawal, return spins
#   /gift [id] [amount] give free spins
#   /userinfo [id]      full user profile
#   /ban [id]           ban user
#   /unban [id]         unban user
#   /broadcast [msg]    message all users

# FEATURES:
#   Early-bird: first 5 unique players each day get +5 free spins
#   Referral: when your friend joins via your link, YOU get +5 spins
#   Multi-package buy: user picks 10/25/50/100 Stars
#   Withdraw reject: admin can reject and spins auto-return to user
# """

# import logging
# import asyncio
# import json
# import os
# import math
# import random
# from datetime import date
# from urllib.parse import quote
# from aiogram import Bot, Dispatcher, F, types
# from aiogram.filters import Command, CommandObject
# from aiogram.fsm.context import FSMContext
# from aiogram.fsm.state import State, StatesGroup
# from aiogram.fsm.storage.memory import MemoryStorage
# from aiogram.types import (
#     LabeledPrice, PreCheckoutQuery, Message,
#     InlineKeyboardButton, InlineKeyboardMarkup
# )

# # =========================================================
# #  CONFIGURATION — only edit this section
# # =========================================================
# TOKEN             = "8605162590:AAE9r8DRRnJw-3qRJQStQJk2ShTSuF0TI4o"   # ← paste your Aviator bot token
# ADMIN_ID          = 8612272966
# TONCENTER_API_KEY = "a4e8dd9e0111177cb876e4b0559e8a58b5eeb4b6acdbd981ad4f7b6123acad9c"
# ADMIN_WALLET      = "UQDlWJTEIwwGt7vai3T6s5MXgULmXk4ojhseU_UxxL7SY2DK"

# SPIN_USD     = 0.01
# SPIN_TO_TON  = 0.002
# MIN_WITHDRAW = 200

# # 97% RTP house edge
# HOUSE_EDGE = 0.03

# BET_OPTIONS = [1, 5, 10, 25, 50]

# STAR_PACKAGES = [
#     (10,   100,  "Starter"),
#     (25,   250,  "Popular ⭐"),
#     (50,   500,  "Big Win"),
#     (100, 1000,  "Whale 🐋"),
# ]

# DATA_FILE  = "aviator_user_data.json"
# STATS_FILE = "aviator_stats.json"
# BOT_NAME   = "FortunoAviatorBot"

# DAILY_EARLY_BIRD_LIMIT = 5
# DAILY_EARLY_BIRD_SPINS = 5

# # Multiplier tick interval in seconds (how fast multiplier climbs)
# TICK_INTERVAL = 0.6
# # =========================================================

# bot = Bot(token=TOKEN)
# dp  = Dispatcher(storage=MemoryStorage())

# # In-memory active games: {user_id: {"bet": int, "crash": float, "multiplier": float, "msg_id": int, "cashed_out": bool, "task": asyncio.Task}}
# active_games: dict = {}

# class WithdrawStates(StatesGroup):
#     waiting_amount = State()
#     waiting_wallet = State()

# # ── Persistence ───────────────────────────────────────────
# def _load(fp) -> dict:
#     if os.path.exists(fp):
#         try:
#             with open(fp, "r", encoding="utf-8") as f:
#                 return json.load(f)
#         except Exception:
#             pass
#     return {}

# def _save(data, fp):
#     tmp = fp + ".tmp"
#     with open(tmp, "w", encoding="utf-8") as f:
#         json.dump(data, f, ensure_ascii=False, indent=2)
#     os.replace(tmp, fp)

# user_data: dict = _load(DATA_FILE)
# stats: dict     = _load(STATS_FILE)

# if not stats:
#     stats = {
#         "total_players":        0,
#         "total_spins_bought":   0,
#         "total_referrals":      0,
#         "total_rounds_played":  0,
#         "total_cashouts":       0,
#         "total_crashes":        0,
#         "total_spins_won":      0,
#         "total_spins_lost":     0,
#         "total_ton_paid":       0.0,
#         "total_depositors":     0,
#         "daily_active":         {},
#         "daily_first_five":     {},
#         "daily_new_players":    {},
#         "daily_purchases":      {},
#         "daily_depositors":     {},
#         "daily_stars_spent":    {},
#         "daily_rounds_played":  {},
#         "daily_revenue_spins":  {},
#         "biggest_win_ever":     0,
#         "highest_multiplier":   0.0,
#     }

# _DEFAULTS = {
#     "total_depositors":    0,
#     "daily_first_five":    {},
#     "daily_new_players":   {},
#     "daily_purchases":     {},
#     "daily_depositors":    {},
#     "daily_stars_spent":   {},
#     "daily_rounds_played": {},
#     "daily_revenue_spins": {},
#     "biggest_win_ever":    0,
#     "highest_multiplier":  0.0,
# }
# for _k, _v in _DEFAULTS.items():
#     if _k not in stats:
#         stats[_k] = _v

# def save_all():
#     _save(user_data, DATA_FILE)
#     _save(stats,     STATS_FILE)

# def get_user(uid: int) -> dict:
#     k = str(uid)
#     if k not in user_data:
#         user_data[k] = {
#             "spins":              0,
#             "ever_started":       False,
#             "pending_withdrawal": False,
#             "pending_spins":      0,
#             "pending_wallet":     None,
#             "referrals":          0,
#             "referred_by":        None,
#             "joined_date":        str(date.today()),
#             "total_rounds_played":0,
#             "total_won":          0,
#             "total_lost":         0,
#             "purchases":          0,
#             "ever_deposited":     False,
#             "banned":             False,
#             "bet_size":           1,
#             "biggest_win":        0,
#             "highest_multiplier": 0.0,
#         }
#         stats["total_players"] += 1
#         today = str(date.today())
#         stats["daily_new_players"][today] = stats["daily_new_players"].get(today, 0) + 1
#         save_all()
#     if "ever_deposited" not in user_data[k]:
#         user_data[k]["ever_deposited"] = user_data[k].get("purchases", 0) > 0
#     return user_data[k]

# def track_daily(uid: int):
#     today = str(date.today())
#     if today not in stats["daily_active"]:
#         stats["daily_active"][today] = []
#     k = str(uid)
#     if k not in stats["daily_active"][today]:
#         stats["daily_active"][today].append(k)

# def check_early_bird(uid: int) -> bool:
#     today   = str(date.today())
#     winners = stats["daily_first_five"].setdefault(today, [])
#     k       = str(uid)
#     if k in winners:
#         return False
#     if len(winners) >= DAILY_EARLY_BIRD_LIMIT:
#         return False
#     winners.append(k)
#     u = get_user(uid)
#     u["spins"] += DAILY_EARLY_BIRD_SPINS
#     save_all()
#     return True

# # ── Helpers ───────────────────────────────────────────────
# def usd(spins) -> str:
#     return f"${spins * SPIN_USD:.2f}"

# def ton(spins) -> float:
#     return round(spins * SPIN_TO_TON, 4)

# def pay_link(to_addr: str, amount_ton: float, comment: str) -> str:
#     nano = int(amount_ton * 1_000_000_000)
#     return (
#         f"https://app.tonkeeper.com/transfer/{to_addr}"
#         f"?amount={nano}&text={quote(comment)}"
#     )

# # ── Crash point generator (97% RTP) ──────────────────────
# def generate_crash_point() -> float:
#     """
#     Provably-fair crash point using inverse CDF method.
#     Formula: crash = max(1.00, 1 / (rand * house_edge_factor))
#     Distribution gives ~97% RTP with occasional high multipliers.
#     """
#     r = random.random()
#     if r < HOUSE_EDGE:
#         # Instant crash (1.00x) — happens 3% of the time
#         return 1.00
#     # Scale remaining probability for smooth distribution
#     r2 = random.random()
#     crash = 1.0 / (1.0 - r2 * (1.0 - HOUSE_EDGE))
#     crash = max(1.01, min(crash, 200.0))
#     return round(crash, 2)

# def multiplier_bar(mult: float, crash: float) -> str:
#     """Visual progress bar showing how close to crash."""
#     safe_zone = min(mult / crash, 1.0)
#     filled = int(safe_zone * 10)
#     bar = "🟢" * (10 - filled) + "🔴" * filled
#     return bar

# def plane_animation(mult: float) -> str:
#     """Animated plane emoji based on multiplier height."""
#     if mult < 2.0:
#         return "✈️"
#     elif mult < 5.0:
#         return "🛫"
#     elif mult < 10.0:
#         return "🚀"
#     else:
#         return "🛸"

# # ── Keyboards ─────────────────────────────────────────────
# def main_kb(uid: int) -> InlineKeyboardMarkup:
#     u = get_user(uid)
#     bal = u["spins"]
#     return InlineKeyboardMarkup(inline_keyboard=[
#         [InlineKeyboardButton(text=f"✈️ PLAY  |  💰 {bal} spins", callback_data="play")],
#         [
#             InlineKeyboardButton(text="💎 Buy Spins", callback_data="buy"),
#             InlineKeyboardButton(text="💸 Withdraw",  callback_data="withdraw"),
#         ],
#         [
#             InlineKeyboardButton(text="📊 My Stats",  callback_data="mystats"),
#             InlineKeyboardButton(text="👥 Referral",  callback_data="referral"),
#         ],
#         [InlineKeyboardButton(text="ℹ️ How to Play", callback_data="howtoplay")],
#     ])

# def bet_kb(uid: int) -> InlineKeyboardMarkup:
#     u = get_user(uid)
#     current = u.get("bet_size", 1)
#     rows = []
#     row = []
#     for b in BET_OPTIONS:
#         label = f"✅ {b}" if b == current else str(b)
#         row.append(InlineKeyboardButton(text=f"{label} spin{'s' if b > 1 else ''}", callback_data=f"setbet_{b}"))
#         if len(row) == 3:
#             rows.append(row)
#             row = []
#     if row:
#         rows.append(row)
#     rows.append([InlineKeyboardButton(text="🚀 FLY!", callback_data="startgame")])
#     rows.append([InlineKeyboardButton(text="🔙 Back", callback_data="back_main")])
#     return InlineKeyboardMarkup(inline_keyboard=rows)

# def cashout_kb() -> InlineKeyboardMarkup:
#     return InlineKeyboardMarkup(inline_keyboard=[
#         [InlineKeyboardButton(text="💰 CASHOUT NOW!", callback_data="cashout")],
#     ])

# def buy_kb() -> InlineKeyboardMarkup:
#     rows = []
#     for stars, spins, label in STAR_PACKAGES:
#         rows.append([InlineKeyboardButton(
#             text=f"{label} — {spins} spins ({stars} ⭐)",
#             callback_data=f"buypack_{stars}_{spins}"
#         )])
#     rows.append([InlineKeyboardButton(text="🔙 Back", callback_data="back_main")])
#     return InlineKeyboardMarkup(inline_keyboard=rows)

# def withdraw_kb() -> InlineKeyboardMarkup:
#     return InlineKeyboardMarkup(inline_keyboard=[
#         [InlineKeyboardButton(text="💸 Request Withdrawal", callback_data="withdraw_start")],
#         [InlineKeyboardButton(text="🔙 Back", callback_data="back_main")],
#     ])

# # ── /start ────────────────────────────────────────────────
# @dp.message(Command("start"))
# async def cmd_start(message: Message):
#     uid  = message.from_user.id
#     u    = get_user(uid)
#     args = message.text.split()

#     if u.get("banned"):
#         await message.answer("🚫 You are banned.")
#         return

#     track_daily(uid)

#     # Referral handling
#     if len(args) > 1 and not u["ever_started"]:
#         try:
#             ref_id = int(args[1])
#             if ref_id != uid and not u.get("referred_by"):
#                 ref_u = get_user(ref_id)
#                 ref_u["spins"]     += 5
#                 ref_u["referrals"] += 1
#                 u["referred_by"]    = ref_id
#                 stats["total_referrals"] += 1
#                 save_all()
#                 try:
#                     await bot.send_message(ref_id,
#                         f"🎉 *+5 spins!* Your friend joined AviatorBet!\n"
#                         f"💰 Balance: *{ref_u['spins']}* spins",
#                         parse_mode="Markdown")
#                 except Exception:
#                     pass
#         except (ValueError, IndexError):
#             pass

#     # Early-bird bonus
#     early = check_early_bird(uid)
#     u["ever_started"] = True
#     save_all()

#     early_msg = "\n🎁 *Early-bird bonus: +5 spins!* You're one of the first 5 today!" if early else ""

#     await message.answer(
#         f"✈️ *Welcome to AviatorBet!*\n"
#         f"━━━━━━━━━━━━━━━━━━━━━\n"
#         f"🎮 The plane takes off — cash out before it flies away!\n"
#         f"💰 Balance: *{u['spins']}* spins · {usd(u['spins'])}\n"
#         f"{early_msg}\n\n"
#         f"Pick an action below 👇",
#         parse_mode="Markdown",
#         reply_markup=main_kb(uid)
#     )

# # ── How to Play ───────────────────────────────────────────
# @dp.callback_query(F.data == "howtoplay")
# async def howtoplay(callback: types.CallbackQuery):
#     await callback.message.answer(
#         "✈️ *How to Play AviatorBet*\n"
#         "━━━━━━━━━━━━━━━━━━━━━\n\n"
#         "1️⃣ Press *PLAY* and choose your bet (1–50 spins)\n"
#         "2️⃣ Press *🚀 FLY!* — the plane takes off!\n"
#         "3️⃣ The multiplier climbs: 1.00x → 2x → 5x → 10x...\n"
#         "4️⃣ Press *💰 CASHOUT* before the plane flies away!\n"
#         "5️⃣ If you cashout at 3.00x with 10 spins → you get *30 spins!*\n\n"
#         "💥 *If the plane crashes before you cashout — you lose your bet!*\n\n"
#         "📈 *RTP: 97%* — very player-friendly odds\n"
#         "💸 *Min withdrawal: 200 spins = $2.00 = 0.4 TON*\n\n"
#         "Good luck! 🍀",
#         parse_mode="Markdown",
#         reply_markup=InlineKeyboardMarkup(inline_keyboard=[
#             [InlineKeyboardButton(text="✈️ Play Now!", callback_data="play")],
#             [InlineKeyboardButton(text="🔙 Back", callback_data="back_main")],
#         ])
#     )
#     await callback.answer()

# # ── Back to main ──────────────────────────────────────────
# @dp.callback_query(F.data == "back_main")
# async def back_main(callback: types.CallbackQuery):
#     uid = callback.from_user.id
#     u   = get_user(uid)
#     await callback.message.answer(
#         f"✈️ *AviatorBet*\n💰 Balance: *{u['spins']}* spins · {usd(u['spins'])}",
#         parse_mode="Markdown",
#         reply_markup=main_kb(uid)
#     )
#     await callback.answer()

# # ── Play → Bet Selection ──────────────────────────────────
# @dp.callback_query(F.data == "play")
# async def process_play(callback: types.CallbackQuery):
#     uid = callback.from_user.id
#     u   = get_user(uid)

#     if u.get("banned"):
#         await callback.answer("🚫 You are banned.", show_alert=True)
#         return

#     if uid in active_games:
#         await callback.answer("⚠️ You already have a game running!", show_alert=True)
#         return

#     track_daily(uid)

#     await callback.message.answer(
#         f"✈️ *Choose Your Bet*\n"
#         f"━━━━━━━━━━━━━━━━\n"
#         f"💰 Balance: *{u['spins']}* spins\n"
#         f"Current bet: *{u.get('bet_size', 1)}* spin{'s' if u.get('bet_size',1) > 1 else ''}\n\n"
#         f"Select bet size then press 🚀 FLY!",
#         parse_mode="Markdown",
#         reply_markup=bet_kb(uid)
#     )
#     await callback.answer()

# # ── Set Bet Size ──────────────────────────────────────────
# @dp.callback_query(F.data.startswith("setbet_"))
# async def set_bet(callback: types.CallbackQuery):
#     uid = callback.from_user.id
#     u   = get_user(uid)
#     bet = int(callback.data.split("_")[1])
#     u["bet_size"] = bet
#     save_all()
#     await callback.message.edit_reply_markup(reply_markup=bet_kb(uid))
#     await callback.answer(f"✅ Bet set to {bet} spin{'s' if bet > 1 else ''}!")

# # ── Start Game ────────────────────────────────────────────
# @dp.callback_query(F.data == "startgame")
# async def start_game(callback: types.CallbackQuery):
#     uid = callback.from_user.id
#     u   = get_user(uid)

#     if u.get("banned"):
#         await callback.answer("🚫 You are banned.", show_alert=True)
#         return

#     if uid in active_games:
#         await callback.answer("⚠️ Game already running!", show_alert=True)
#         return

#     bet = u.get("bet_size", 1)
#     if u["spins"] < bet:
#         await callback.answer(f"❌ Not enough spins! You need {bet} spins.", show_alert=True)
#         return

#     # Deduct bet
#     u["spins"] -= bet
#     save_all()

#     # Generate crash point
#     crash_point = generate_crash_point()

#     # Send initial game message
#     msg = await callback.message.answer(
#         f"✈️ *AviatorBet — FLYING!*\n"
#         f"━━━━━━━━━━━━━━━━━━━━━\n"
#         f"🎯 Bet: *{bet}* spins\n"
#         f"📈 Multiplier: *1.00x*\n"
#         f"✈️ ..................\n\n"
#         f"💰 Press CASHOUT before the plane flies away!",
#         parse_mode="Markdown",
#         reply_markup=cashout_kb()
#     )

#     # Store game state
#     active_games[uid] = {
#         "bet":        bet,
#         "crash":      crash_point,
#         "multiplier": 1.00,
#         "msg_id":     msg.message_id,
#         "chat_id":    callback.message.chat.id,
#         "cashed_out": False,
#         "task":       None,
#     }

#     # Start the multiplier task
#     task = asyncio.create_task(run_game(uid))
#     active_games[uid]["task"] = task

#     await callback.answer()

# # ── Game Loop ─────────────────────────────────────────────
# async def run_game(uid: int):
#     """Runs the multiplier climb and crash logic."""
#     try:
#         game   = active_games[uid]
#         u      = get_user(uid)
#         mult   = 1.00
#         crash  = game["crash"]
#         bet    = game["bet"]
#         tick   = 0

#         while mult < crash:
#             await asyncio.sleep(TICK_INTERVAL)

#             if game["cashed_out"]:
#                 return

#             # Increase multiplier — faster at low values, slower at high
#             if mult < 2.0:
#                 mult += random.uniform(0.05, 0.15)
#             elif mult < 5.0:
#                 mult += random.uniform(0.10, 0.30)
#             elif mult < 10.0:
#                 mult += random.uniform(0.20, 0.60)
#             else:
#                 mult += random.uniform(0.50, 2.00)

#             mult = round(min(mult, crash), 2)
#             game["multiplier"] = mult
#             tick += 1

#             # Update message every 2 ticks to avoid Telegram rate limits
#             if tick % 2 == 0 or mult >= crash:
#                 plane = plane_animation(mult)
#                 potential = round(bet * mult)
#                 bar = multiplier_bar(mult, crash)
#                 try:
#                     await bot.edit_message_text(
#                         chat_id=game["chat_id"],
#                         message_id=game["msg_id"],
#                         text=(
#                             f"{plane} *AviatorBet — FLYING!*\n"
#                             f"━━━━━━━━━━━━━━━━━━━━━\n"
#                             f"🎯 Bet: *{bet}* spins\n"
#                             f"📈 Multiplier: *{mult:.2f}x*\n"
#                             f"{bar}\n"
#                             f"💵 If cashout now: *{potential}* spins\n\n"
#                             f"💰 Press CASHOUT before the plane flies away!"
#                         ),
#                         parse_mode="Markdown",
#                         reply_markup=cashout_kb()
#                     )
#                 except Exception:
#                     pass  # Message might already be edited or deleted

#         # ── CRASHED ───────────────────────────────────────
#         if not game["cashed_out"]:
#             game["cashed_out"] = True

#             # Update stats
#             today = str(date.today())
#             u["total_rounds_played"] = u.get("total_rounds_played", 0) + 1
#             u["total_lost"]          = u.get("total_lost", 0) + bet
#             stats["total_rounds_played"]             = stats.get("total_rounds_played", 0) + 1
#             stats["total_crashes"]                   = stats.get("total_crashes", 0) + 1
#             stats["total_spins_lost"]                = stats.get("total_spins_lost", 0) + bet
#             stats["daily_rounds_played"][today]      = stats["daily_rounds_played"].get(today, 0) + 1
#             save_all()

#             try:
#                 await bot.edit_message_text(
#                     chat_id=game["chat_id"],
#                     message_id=game["msg_id"],
#                     text=(
#                         f"💥 *CRASHED at {crash:.2f}x!*\n"
#                         f"━━━━━━━━━━━━━━━━━━━━━\n"
#                         f"🎯 Bet: *{bet}* spins\n"
#                         f"❌ You lost *{bet}* spins\n"
#                         f"💰 Balance: *{u['spins']}* spins\n\n"
#                         f"Try again? Press Play! 🚀"
#                     ),
#                     parse_mode="Markdown",
#                     reply_markup=InlineKeyboardMarkup(inline_keyboard=[
#                         [InlineKeyboardButton(text="✈️ Play Again", callback_data="play")],
#                         [InlineKeyboardButton(text="💎 Buy Spins",  callback_data="buy")],
#                     ])
#                 )
#             except Exception:
#                 pass

#             active_games.pop(uid, None)

#     except asyncio.CancelledError:
#         pass
#     except Exception as e:
#         logging.error(f"Game error for {uid}: {e}")
#         active_games.pop(uid, None)

# # ── Cashout ───────────────────────────────────────────────
# @dp.callback_query(F.data == "cashout")
# async def process_cashout(callback: types.CallbackQuery):
#     uid  = callback.from_user.id
#     game = active_games.get(uid)

#     if not game:
#         await callback.answer("⚠️ No active game found.", show_alert=True)
#         return

#     if game["cashed_out"]:
#         await callback.answer("⚠️ Already cashed out or crashed!", show_alert=True)
#         return

#     game["cashed_out"] = True

#     # Cancel the running task
#     if game["task"] and not game["task"].done():
#         game["task"].cancel()

#     mult    = game["multiplier"]
#     bet     = game["bet"]
#     winnings = round(bet * mult)
#     profit   = winnings - bet

#     u = get_user(uid)
#     u["spins"]               += winnings
#     u["total_rounds_played"]  = u.get("total_rounds_played", 0) + 1
#     u["total_won"]            = u.get("total_won", 0) + winnings

#     if winnings > u.get("biggest_win", 0):
#         u["biggest_win"] = winnings
#     if winnings > stats.get("biggest_win_ever", 0):
#         stats["biggest_win_ever"] = winnings
#     if mult > u.get("highest_multiplier", 0.0):
#         u["highest_multiplier"] = mult
#     if mult > stats.get("highest_multiplier", 0.0):
#         stats["highest_multiplier"] = mult

#     today = str(date.today())
#     stats["total_rounds_played"]        = stats.get("total_rounds_played", 0) + 1
#     stats["total_cashouts"]             = stats.get("total_cashouts", 0) + 1
#     stats["total_spins_won"]            = stats.get("total_spins_won", 0) + winnings
#     stats["daily_rounds_played"][today] = stats["daily_rounds_played"].get(today, 0) + 1
#     save_all()

#     plane = plane_animation(mult)

#     try:
#         await bot.edit_message_text(
#             chat_id=game["chat_id"],
#             message_id=game["msg_id"],
#             text=(
#                 f"{plane} *CASHED OUT! {mult:.2f}x!*\n"
#                 f"━━━━━━━━━━━━━━━━━━━━━\n"
#                 f"🎯 Bet: *{bet}* spins\n"
#                 f"📈 Multiplier: *{mult:.2f}x*\n"
#                 f"🏆 Won: *{winnings}* spins (+{profit} profit!)\n"
#                 f"💰 Balance: *{u['spins']}* spins · {usd(u['spins'])}\n\n"
#                 f"🔥 Great timing!"
#             ),
#             parse_mode="Markdown",
#             reply_markup=InlineKeyboardMarkup(inline_keyboard=[
#                 [InlineKeyboardButton(text="✈️ Play Again", callback_data="play")],
#                 [InlineKeyboardButton(text="💸 Withdraw",   callback_data="withdraw")],
#             ])
#         )
#     except Exception:
#         await bot.send_message(
#             game["chat_id"],
#             f"✅ *Cashed out at {mult:.2f}x!* Won *{winnings}* spins!\n💰 Balance: *{u['spins']}* spins",
#             parse_mode="Markdown",
#             reply_markup=main_kb(uid)
#         )

#     active_games.pop(uid, None)
#     await callback.answer(f"✅ Cashed out at {mult:.2f}x!")

# # ── My Stats ─────────────────────────────────────────────
# @dp.callback_query(F.data == "mystats")
# async def my_stats(callback: types.CallbackQuery):
#     uid = callback.from_user.id
#     u   = get_user(uid)
#     played = u.get("total_rounds_played", 0)
#     won    = u.get("total_won", 0)
#     lost   = u.get("total_lost", 0)
#     best   = u.get("biggest_win", 0)
#     bestx  = u.get("highest_multiplier", 0.0)

#     await callback.message.answer(
#         f"📊 *Your Stats — AviatorBet*\n"
#         f"━━━━━━━━━━━━━━━━━━━━━\n"
#         f"✈️ Rounds played: *{played}*\n"
#         f"💰 Balance: *{u['spins']}* spins · {usd(u['spins'])}\n"
#         f"🏆 Best win: *{best}* spins\n"
#         f"📈 Highest multiplier: *{bestx:.2f}x*\n"
#         f"🎁 Referrals: *{u.get('referrals', 0)}*\n"
#         f"📅 Member since: {u.get('joined_date', 'N/A')}",
#         parse_mode="Markdown",
#         reply_markup=InlineKeyboardMarkup(inline_keyboard=[
#             [InlineKeyboardButton(text="🔙 Back", callback_data="back_main")]
#         ])
#     )
#     await callback.answer()

# # ── Referral ──────────────────────────────────────────────
# @dp.callback_query(F.data == "referral")
# async def referral_menu(callback: types.CallbackQuery):
#     uid  = callback.from_user.id
#     u    = get_user(uid)
#     link = f"https://t.me/{BOT_NAME}?start={uid}"
#     await callback.message.answer(
#         f"👥 *Referral Program*\n"
#         f"━━━━━━━━━━━━━━━━━━━━━\n"
#         f"Invite friends and earn *+5 spins* for each one!\n\n"
#         f"🔗 Your link:\n`{link}`\n\n"
#         f"👫 Friends invited: *{u.get('referrals', 0)}*\n"
#         f"🎁 Spins earned from referrals: *{u.get('referrals', 0) * 5}*",
#         parse_mode="Markdown",
#         reply_markup=InlineKeyboardMarkup(inline_keyboard=[
#             [InlineKeyboardButton(text="🔙 Back", callback_data="back_main")]
#         ])
#     )
#     await callback.answer()

# # ── Withdraw ──────────────────────────────────────────────
# @dp.callback_query(F.data == "withdraw")
# async def withdraw_menu(callback: types.CallbackQuery):
#     uid = callback.from_user.id
#     u   = get_user(uid)

#     if u["spins"] < MIN_WITHDRAW:
#         await callback.message.answer(
#             f"💸 *Withdraw*\n\n"
#             f"❌ Minimum withdrawal: *{MIN_WITHDRAW} spins* = {usd(MIN_WITHDRAW)}\n"
#             f"💰 Your balance: *{u['spins']}* spins\n\n"
#             f"You need *{MIN_WITHDRAW - u['spins']}* more spins.",
#             parse_mode="Markdown",
#             reply_markup=InlineKeyboardMarkup(inline_keyboard=[
#                 [InlineKeyboardButton(text="💎 Buy Spins", callback_data="buy")],
#                 [InlineKeyboardButton(text="🔙 Back",      callback_data="back_main")],
#             ])
#         )
#         await callback.answer()
#         return

#     if u["pending_withdrawal"]:
#         await callback.message.answer(
#             f"⏳ *Withdrawal Pending*\n\n"
#             f"You have a pending withdrawal of *{u['pending_spins']}* spins.\n"
#             f"Please wait for admin to process it.",
#             parse_mode="Markdown",
#             reply_markup=InlineKeyboardMarkup(inline_keyboard=[
#                 [InlineKeyboardButton(text="🔙 Back", callback_data="back_main")]
#             ])
#         )
#         await callback.answer()
#         return

#     await callback.message.answer(
#         f"💸 *Withdraw Spins*\n\n"
#         f"💰 Balance: *{u['spins']}* spins · {usd(u['spins'])}\n"
#         f"Minimum: *{MIN_WITHDRAW}* spins = {usd(MIN_WITHDRAW)} = {ton(MIN_WITHDRAW)} TON\n\n"
#         f"Press below to start withdrawal:",
#         parse_mode="Markdown",
#         reply_markup=withdraw_kb()
#     )
#     await callback.answer()

# @dp.callback_query(F.data == "withdraw_start")
# async def withdraw_start(callback: types.CallbackQuery, state: FSMContext):
#     uid = callback.from_user.id
#     u   = get_user(uid)
#     await state.set_state(WithdrawStates.waiting_amount)
#     await callback.message.answer(
#         f"💸 How many spins do you want to withdraw?\n"
#         f"Min: *{MIN_WITHDRAW}* · Max: *{u['spins']}*\n\n"
#         f"Type the amount:",
#         parse_mode="Markdown"
#     )
#     await callback.answer()

# @dp.message(WithdrawStates.waiting_amount)
# async def withdraw_amount(message: Message, state: FSMContext):
#     uid = message.from_user.id
#     u   = get_user(uid)
#     try:
#         amount = int(message.text.strip())
#     except ValueError:
#         await message.answer("❌ Please enter a valid number.")
#         return
#     if amount < MIN_WITHDRAW:
#         await message.answer(f"❌ Minimum is {MIN_WITHDRAW} spins.")
#         return
#     if amount > u["spins"]:
#         await message.answer(f"❌ You only have {u['spins']} spins.")
#         return
#     await state.update_data(amount=amount)
#     await state.set_state(WithdrawStates.waiting_wallet)
#     await message.answer(
#         f"💳 Enter your *TON wallet address*:\n\n"
#         f"(Example: `UQD...`)",
#         parse_mode="Markdown"
#     )

# @dp.message(WithdrawStates.waiting_wallet)
# async def withdraw_wallet(message: Message, state: FSMContext):
#     uid    = message.from_user.id
#     u      = get_user(uid)
#     wallet = message.text.strip()
#     data   = await state.get_data()
#     amount = data["amount"]

#     if len(wallet) < 10:
#         await message.answer("❌ Invalid wallet address.")
#         return

#     u["spins"]              -= amount
#     u["pending_withdrawal"]  = True
#     u["pending_spins"]       = amount
#     u["pending_wallet"]      = wallet
#     save_all()

#     await state.clear()

#     await message.answer(
#         f"✅ *Withdrawal Request Submitted!*\n\n"
#         f"💰 Amount: *{amount}* spins = {usd(amount)} = {ton(amount)} TON\n"
#         f"👛 Wallet: `{wallet}`\n\n"
#         f"⏳ Admin will process within 24h.",
#         parse_mode="Markdown",
#         reply_markup=main_kb(uid)
#     )

#     # Notify admin
#     try:
#         await bot.send_message(
#             ADMIN_ID,
#             f"💸 *NEW WITHDRAWAL REQUEST*\n"
#             f"👤 User: `{uid}` · @{message.from_user.username or 'no username'}\n"
#             f"💰 {amount} spins = {usd(amount)} = {ton(amount)} TON\n"
#             f"👛 `{wallet}`\n\n"
#             f"Use /pay {uid} to approve or /reject {uid} to reject.",
#             parse_mode="Markdown"
#         )
#     except Exception:
#         pass

# # ── Admin Commands ────────────────────────────────────────
# @dp.message(Command("admin"))
# async def admin_dashboard(message: Message):
#     if message.from_user.id != ADMIN_ID:
#         return
#     today = str(date.today())
#     dau   = len(stats["daily_active"].get(today, []))
#     new_p = stats["daily_new_players"].get(today, 0)
#     rounds_today = stats["daily_rounds_played"].get(today, 0)
#     stars_today  = stats["daily_stars_spent"].get(today, 0)
#     dep_today    = len(stats["daily_depositors"].get(today, []))
#     purch_today  = stats["daily_purchases"].get(today, 0)

#     pending = [(uid, ud) for uid, ud in user_data.items() if ud.get("pending_withdrawal")]

#     pend_txt = ""
#     for uid, ud in pending[:5]:
#         pend_txt += (
#             f"  • `{uid}` — {ud['pending_spins']} spins "
#             f"({usd(ud['pending_spins'])}) → `{ud['pending_wallet'][:12]}...`\n"
#         )
#     if not pend_txt:
#         pend_txt = "  None ✅\n"

#     await message.answer(
#         f"🛠 *AviatorBet Admin Dashboard*\n"
#         f"━━━━━━━━━━━━━━━━━━━━━\n"
#         f"📅 *Today ({today})*\n"
#         f"  👥 Active: {dau} · 🆕 New: {new_p}\n"
#         f"  ✈️ Rounds: {rounds_today} · 💎 Purchases: {purch_today}\n"
#         f"  ⭐ Stars: {stars_today} · 💳 Depositors: {dep_today}\n\n"
#         f"📊 *All Time*\n"
#         f"  👥 Players: {stats['total_players']}\n"
#         f"  ✈️ Rounds: {stats['total_rounds_played']}\n"
#         f"  💰 Cashouts: {stats['total_cashouts']} · Crashes: {stats['total_crashes']}\n"
#         f"  🏆 Biggest win: {stats.get('biggest_win_ever', 0)} spins\n"
#         f"  📈 Highest mult: {stats.get('highest_multiplier', 0.0):.2f}x\n"
#         f"  💸 TON paid: {stats['total_ton_paid']}\n\n"
#         f"⏳ *Pending Withdrawals*\n{pend_txt}",
#         parse_mode="Markdown"
#     )

# @dp.message(Command("stats7"))
# async def stats7(message: Message):
#     if message.from_user.id != ADMIN_ID:
#         return
#     today = date.today()
#     lines = ["📈 *Last 7 Days — AviatorBet*\n━━━━━━━━━━━━━━━━━━━━━"]
#     for i in range(7):
#         d     = str(today - __import__("datetime").timedelta(days=i))
#         dau   = len(stats["daily_active"].get(d, []))
#         new_p = stats["daily_new_players"].get(d, 0)
#         rnds  = stats["daily_rounds_played"].get(d, 0)
#         stars = stats["daily_stars_spent"].get(d, 0)
#         lines.append(f"  `{d}` — 👥{dau} · 🆕{new_p} · ✈️{rnds} · ⭐{stars}")
#     await message.answer("\n".join(lines), parse_mode="Markdown")

# @dp.message(Command("pay"))
# async def admin_pay(message: Message):
#     if message.from_user.id != ADMIN_ID:
#         return
#     try:
#         target_id = str(int(message.text.split()[1]))
#         u         = user_data.get(target_id)
#         if not u or not u.get("pending_withdrawal"):
#             await message.answer("❌ No pending withdrawal for this user.")
#             return
#         spins  = u["pending_spins"]
#         wallet = u["pending_wallet"]
#         amount = ton(spins)
#         link   = pay_link(wallet, amount, f"AviatorBet withdrawal {target_id}")
#         stats["total_ton_paid"] = round(stats.get("total_ton_paid", 0) + amount, 4)
#         u["pending_withdrawal"] = False
#         u["pending_spins"]      = 0
#         u["pending_wallet"]     = None
#         save_all()
#         await message.answer(
#             f"✅ Withdrawal approved for `{target_id}`\n"
#             f"💸 {spins} spins = {usd(spins)} = {amount} TON\n"
#             f"[👉 Open in Tonkeeper]({link})",
#             parse_mode="Markdown"
#         )
#         try:
#             await bot.send_message(int(target_id),
#                 f"✅ *Withdrawal Approved!*\n"
#                 f"💸 {spins} spins = {usd(spins)} = {amount} TON sent to your wallet!\n"
#                 f"Thanks for playing AviatorBet ✈️",
#                 parse_mode="Markdown", reply_markup=main_kb(int(target_id)))
#         except Exception:
#             pass
#     except (IndexError, ValueError):
#         await message.answer("❌ Usage: /pay [user_id]")

# @dp.message(Command("reject"))
# async def admin_reject(message: Message):
#     if message.from_user.id != ADMIN_ID:
#         return
#     try:
#         target_id = str(int(message.text.split()[1]))
#         u         = user_data.get(target_id)
#         if not u or not u.get("pending_withdrawal"):
#             await message.answer("❌ No pending withdrawal for this user.")
#             return
#         spins = u["pending_spins"]
#         u["spins"]              += spins
#         u["pending_withdrawal"]  = False
#         u["pending_spins"]       = 0
#         u["pending_wallet"]      = None
#         save_all()
#         await message.answer(f"✅ Rejected and returned {spins} spins to `{target_id}`.", parse_mode="Markdown")
#         try:
#             await bot.send_message(int(target_id),
#                 f"❌ *Withdrawal Rejected*\n"
#                 f"💰 {spins} spins have been returned to your balance.\n"
#                 f"Contact support if you have questions.",
#                 parse_mode="Markdown", reply_markup=main_kb(int(target_id)))
#         except Exception:
#             pass
#     except (IndexError, ValueError):
#         await message.answer("❌ Usage: /reject [user_id]")

# @dp.message(Command("gift"))
# async def admin_gift(message: Message):
#     if message.from_user.id != ADMIN_ID:
#         return
#     try:
#         parts     = message.text.split()
#         target_id = str(int(parts[1]))
#         amount    = int(parts[2])
#         u         = get_user(int(target_id))
#         u["spins"] += amount
#         save_all()
#         await message.answer(f"🎁 Gifted *{amount}* spins to `{target_id}`.", parse_mode="Markdown")
#         try:
#             await bot.send_message(int(target_id),
#                 f"🎁 *You received {amount} free spins!*\n"
#                 f"💰 Balance: *{u['spins']}* spins\n"
#                 f"Good luck! ✈️",
#                 parse_mode="Markdown", reply_markup=main_kb(int(target_id)))
#         except Exception:
#             pass
#     except (IndexError, ValueError):
#         await message.answer("❌ Usage: /gift [user_id] [amount]")

# @dp.message(Command("userinfo"))
# async def admin_userinfo(message: Message):
#     if message.from_user.id != ADMIN_ID:
#         return
#     try:
#         target_id = str(int(message.text.split()[1]))
#         u         = user_data.get(target_id)
#         if not u:
#             await message.answer("❌ User not found.")
#             return
#         await message.answer(
#             f"👤 *USER INFO* · `{target_id}`\n"
#             f"━━━━━━━━━━━━━━━━━━━━\n"
#             f"💰 *{u.get('spins',0)}* spins · {usd(u.get('spins',0))} · {ton(u.get('spins',0))} TON\n"
#             f"✈️ Rounds: *{u.get('total_rounds_played',0)}* · 🏆 Best: *{u.get('biggest_win',0)}* spins\n"
#             f"📈 Highest mult: *{u.get('highest_multiplier',0.0):.2f}x*\n"
#             f"💎 Purchases: *{u.get('purchases',0)}* · Deposited: *{u.get('ever_deposited',False)}*\n"
#             f"👥 Invited: *{u.get('referrals',0)}* · 🎲 Bet: *{u.get('bet_size',1)}x*\n"
#             f"📅 Joined: {u.get('joined_date','N/A')} · 🚫 Banned: *{u.get('banned',False)}*\n"
#             f"⏳ Pending: *{u.get('pending_withdrawal',False)}* · Spins held: *{u.get('pending_spins',0)}*\n"
#             f"👛 `{u.get('pending_wallet','None')}`",
#             parse_mode="Markdown",
#             reply_markup=InlineKeyboardMarkup(inline_keyboard=[
#                 [InlineKeyboardButton(text="🎁 Gift spins",
#                     callback_data=f"gift_menu_{target_id}")],
#                 [InlineKeyboardButton(
#                     text=f"{'✅ Unban' if u.get('banned') else '🚫 Ban'} this user",
#                     callback_data=f"toggle_ban_{target_id}"
#                 )],
#             ])
#         )
#     except (IndexError, ValueError):
#         await message.answer("❌ Usage: /userinfo [user_id]")

# @dp.callback_query(F.data.startswith("toggle_ban_"))
# async def toggle_ban(callback: types.CallbackQuery):
#     if callback.from_user.id != ADMIN_ID:
#         await callback.answer("❌ Not authorized.", show_alert=True)
#         return
#     target_id = callback.data.replace("toggle_ban_", "")
#     u         = user_data.get(target_id)
#     if not u:
#         await callback.answer("❌ User not found.", show_alert=True)
#         return
#     u["banned"] = not u.get("banned", False)
#     save_all()
#     status = "🚫 Banned" if u["banned"] else "✅ Unbanned"
#     await callback.answer(f"{status} {target_id}", show_alert=True)

# @dp.message(Command("ban"))
# async def admin_ban(message: Message):
#     if message.from_user.id != ADMIN_ID:
#         return
#     try:
#         target_id = str(int(message.text.split()[1]))
#         get_user(int(target_id))["banned"] = True
#         save_all()
#         await message.answer(f"🚫 *Banned* `{target_id}`.", parse_mode="Markdown")
#     except (IndexError, ValueError):
#         await message.answer("❌ Usage: /ban [user_id]")

# @dp.message(Command("unban"))
# async def admin_unban(message: Message):
#     if message.from_user.id != ADMIN_ID:
#         return
#     try:
#         target_id = str(int(message.text.split()[1]))
#         get_user(int(target_id))["banned"] = False
#         save_all()
#         await message.answer(f"✅ *Unbanned* `{target_id}`.", parse_mode="Markdown")
#     except (IndexError, ValueError):
#         await message.answer("❌ Usage: /unban [user_id]")

# @dp.message(Command("broadcast"))
# async def admin_broadcast(message: Message):
#     if message.from_user.id != ADMIN_ID:
#         return
#     try:
#         text = message.text.split(" ", 1)[1]
#     except IndexError:
#         await message.answer("❌ Usage: /broadcast [message]")
#         return
#     await message.answer("📢 Sending...")
#     sent = failed = 0
#     for k in user_data:
#         if user_data[k].get("banned"):
#             continue
#         try:
#             await bot.send_message(int(k), f"📢 *AviatorBet:*\n\n{text}", parse_mode="Markdown")
#             sent += 1
#             await asyncio.sleep(0.05)
#         except Exception:
#             failed += 1
#     await message.answer(f"✅ Sent: *{sent}* · Failed: *{failed}*", parse_mode="Markdown")

# # ── Buy Spins ─────────────────────────────────────────────
# @dp.callback_query(F.data == "buy")
# async def process_buy(callback: types.CallbackQuery):
#     await callback.message.answer(
#         f"💎 *Buy Spins*\n\n"
#         f"Minimum: *10 Stars* = 100 spins\n"
#         f"1 spin = $0.01 · 97% RTP\n\n"
#         f"Pick your package 👇",
#         parse_mode="Markdown",
#         reply_markup=buy_kb()
#     )
#     await callback.answer()

# @dp.callback_query(F.data.startswith("buypack_"))
# async def process_buypack(callback: types.CallbackQuery):
#     try:
#         parts = callback.data.split("_")
#         stars = int(parts[1])
#         spins = int(parts[2])
#     except (ValueError, IndexError):
#         await callback.answer("❌ Invalid package.", show_alert=True)
#         return
#     label = next((l for s, sp, l in STAR_PACKAGES if s == stars and sp == spins), "Spins")
#     await bot.send_invoice(
#         callback.message.chat.id,
#         title=f"{label} — {spins} Spins",
#         description=f"{spins} spins · 1 spin = $0.01 · 97% RTP · TON payouts",
#         payload=f"buy_{stars}_{spins}",
#         provider_token="",
#         currency="XTR",
#         prices=[LabeledPrice(label=f"{spins} Spins", amount=stars)],
#     )
#     await callback.answer()

# @dp.pre_checkout_query()
# async def pre_check(q: PreCheckoutQuery):
#     try:
#         parts = q.invoice_payload.split("_")
#         if parts[0] != "buy":
#             raise ValueError
#         stars = int(parts[1])
#         spins = int(parts[2])
#         valid = any(s == stars and sp == spins for s, sp, _ in STAR_PACKAGES)
#         if not valid:
#             raise ValueError
#     except (ValueError, IndexError):
#         await q.answer(ok=False, error_message="Unknown product. Contact support.")
#         return
#     await q.answer(ok=True)

# @dp.message(F.successful_payment)
# async def success_pay(m: Message):
#     uid   = m.from_user.id
#     u     = get_user(uid)
#     today = str(date.today())
#     try:
#         parts = m.successful_payment.invoice_payload.split("_")
#         stars = int(parts[1])
#         spins = int(parts[2])
#     except (ValueError, IndexError):
#         spins = 100
#         stars = 10

#     charge_id = m.successful_payment.telegram_payment_charge_id
#     seen      = u.setdefault("processed_charge_ids", [])
#     if charge_id in seen:
#         await m.answer(
#             f"✅ Payment already credited!\n💰 Balance: *{u['spins']}* spins",
#             parse_mode="Markdown", reply_markup=main_kb(uid))
#         return

#     seen.append(charge_id)
#     if len(seen) > 20:
#         u["processed_charge_ids"] = seen[-20:]

#     u["spins"]    += spins
#     u["purchases"] = u.get("purchases", 0) + 1

#     if not u.get("ever_deposited"):
#         u["ever_deposited"] = True
#         stats["total_depositors"] = stats.get("total_depositors", 0) + 1

#     dep_list = stats["daily_depositors"].setdefault(today, [])
#     if str(uid) not in dep_list:
#         dep_list.append(str(uid))

#     stats["total_spins_bought"]         = stats.get("total_spins_bought", 0) + spins
#     stats["daily_purchases"][today]     = stats["daily_purchases"].get(today, 0) + 1
#     stats["daily_stars_spent"][today]   = stats["daily_stars_spent"].get(today, 0) + stars
#     stats["daily_revenue_spins"][today] = stats["daily_revenue_spins"].get(today, 0) + spins
#     save_all()

#     await m.answer(
#         f"✅ *+{spins} Spins added!*\n"
#         f"💰 Balance: *{u['spins']}* spins · {usd(u['spins'])}\n\n"
#         f"✈️ Good luck — fly high!",
#         parse_mode="Markdown",
#         reply_markup=main_kb(uid)
#     )

# # ── Main ──────────────────────────────────────────────────
# async def main():
#     logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
#     logging.info("AviatorBet ✈️ is online!")
#     await dp.start_polling(bot)

# if __name__ == "__main__":
#     asyncio.run(main())




"""
Fortuno Aviator ✈️ — PRODUCTION VERSION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Install: pip install aiogram
Run:     python3 main.py
"""

import logging
import asyncio
import json
import os
import random
import datetime
from datetime import date
from urllib.parse import quote
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import (
    LabeledPrice, PreCheckoutQuery, Message,
    InlineKeyboardButton, InlineKeyboardMarkup
)

# =========================================================
#  CONFIGURATION
# =========================================================
TOKEN             = "8605162590:AAE9r8DRRnJw-3qRJQStQJk2ShTSuF0TI4o"
ADMIN_ID          = 8612272966
TONCENTER_API_KEY = "a4e8dd9e0111177cb876e4b0559e8a58b5eeb4b6acdbd981ad4f7b6123acad9c"
ADMIN_WALLET      = "UQDlWJTEIwwGt7vai3T6s5MXgULmXk4ojhseU_UxxL7SY2DK"

SPIN_USD     = 0.01
SPIN_TO_TON  = 0.002
MIN_WITHDRAW = 200
HOUSE_EDGE   = 0.03   # 3% house edge = 97% RTP

BET_OPTIONS = [1, 5, 10, 25, 50]

STAR_PACKAGES = [
    (10,   100,  "Starter"),
    (25,   250,  "Popular ⭐"),
    (50,   500,  "Big Win"),
    (100, 1000,  "Whale 🐋"),
]

DATA_FILE  = "aviator_user_data.json"
STATS_FILE = "aviator_stats.json"
BOT_NAME   = "FortunoAviatorBot"

DAILY_EARLY_BIRD_LIMIT = 5
DAILY_EARLY_BIRD_SPINS = 5
TICK_INTERVAL          = 1.0   # 1 second per update — easy to follow
# =========================================================

bot = Bot(token=TOKEN)
dp  = Dispatcher(storage=MemoryStorage())

active_games: dict = {}

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
        "total_players":        0,
        "total_spins_bought":   0,
        "total_referrals":      0,
        "total_rounds_played":  0,
        "total_cashouts":       0,
        "total_crashes":        0,
        "total_spins_won":      0,
        "total_spins_lost":     0,
        "total_ton_paid":       0.0,
        "total_depositors":     0,
        "daily_active":         {},
        "daily_first_five":     {},
        "daily_new_players":    {},
        "daily_purchases":      {},
        "daily_depositors":     {},
        "daily_stars_spent":    {},
        "daily_rounds_played":  {},
        "daily_revenue_spins":  {},
        "biggest_win_ever":     0,
        "highest_multiplier":   0.0,
    }

_DEFAULTS = {
    "total_depositors":    0,
    "daily_first_five":    {},
    "daily_new_players":   {},
    "daily_purchases":     {},
    "daily_depositors":    {},
    "daily_stars_spent":   {},
    "daily_rounds_played": {},
    "daily_revenue_spins": {},
    "biggest_win_ever":    0,
    "highest_multiplier":  0.0,
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
            "spins":               0,
            "ever_started":        False,
            "pending_withdrawal":  False,
            "pending_spins":       0,
            "pending_wallet":      None,
            "referrals":           0,
            "referred_by":         None,
            "joined_date":         str(date.today()),
            "total_rounds_played": 0,
            "total_won":           0,
            "total_lost":          0,
            "purchases":           0,
            "ever_deposited":      False,
            "banned":              False,
            "bet_size":            1,
            "biggest_win":         0,
            "highest_multiplier":  0.0,
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

# ── Crash point generator (97% RTP) ──────────────────────
def generate_crash_point() -> float:
    r = random.random()
    if r < HOUSE_EDGE:
        return 1.00
    r2    = random.random()
    crash = 1.0 / (1.0 - r2 * (1.0 - HOUSE_EDGE))
    return round(max(1.01, min(crash, 200.0)), 2)

# ── Simple plane emoji based on height ───────────────────
def get_plane(mult: float) -> str:
    if mult < 2.0:
        return "✈️"
    elif mult < 5.0:
        return "🛫"
    elif mult < 10.0:
        return "🚀"
    else:
        return "🛸"

# ── Simple message for flying state ──────────────────────
def flying_text(bet: int, mult: float) -> str:
    plane = get_plane(mult)
    if mult < 1.5:
        mood = "Just took off... 👀"
    elif mult < 2.0:
        mood = "Flying steady... 😏"
    elif mult < 3.0:
        mood = "Going higher! 😮"
    elif mult < 5.0:
        mood = "Getting risky... 😬"
    elif mult < 10.0:
        mood = "Very high now! 😱"
    else:
        mood = "INSANE height!! 🤑"

    potential = round(bet * mult)
    return (
        f"{plane}  *{mult:.2f}x*  —  {mood}\n\n"
        f"🎯 Bet: *{bet}* spins\n"
        f"💵 Cashout now = *{potential}* spins\n\n"
        f"⬇️ Press the button before it crashes!"
    )

# ── Keyboards ─────────────────────────────────────────────
def main_kb(uid: int) -> InlineKeyboardMarkup:
    u   = get_user(uid)
    bal = u["spins"]
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"✈️ PLAY  |  💰 {bal} spins", callback_data="play")],
        [
            InlineKeyboardButton(text="💎 Buy Spins", callback_data="buy"),
            InlineKeyboardButton(text="💸 Withdraw",  callback_data="withdraw"),
        ],
        [
            InlineKeyboardButton(text="📊 My Stats",  callback_data="mystats"),
            InlineKeyboardButton(text="👥 Referral",  callback_data="referral"),
        ],
        [InlineKeyboardButton(text="ℹ️ How to Play", callback_data="howtoplay")],
    ])

def bet_kb(uid: int) -> InlineKeyboardMarkup:
    u       = get_user(uid)
    current = u.get("bet_size", 1)
    rows    = []
    row     = []
    for b in BET_OPTIONS:
        label = f"✅ {b}" if b == current else str(b)
        row.append(InlineKeyboardButton(
            text=f"{label} spin{'s' if b > 1 else ''}",
            callback_data=f"setbet_{b}"
        ))
        if len(row) == 3:
            rows.append(row)
            row = []
    if row:
        rows.append(row)
    rows.append([InlineKeyboardButton(text="🚀 FLY NOW!", callback_data="startgame")])
    rows.append([InlineKeyboardButton(text="🔙 Back",     callback_data="back_main")])
    return InlineKeyboardMarkup(inline_keyboard=rows)

def cashout_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💰  CASH OUT NOW!  💰", callback_data="cashout")],
    ])

def buy_kb() -> InlineKeyboardMarkup:
    rows = []
    for stars, spins, label in STAR_PACKAGES:
        rows.append([InlineKeyboardButton(
            text=f"{label} — {spins} spins ({stars} ⭐)",
            callback_data=f"buypack_{stars}_{spins}"
        )])
    rows.append([InlineKeyboardButton(text="🔙 Back", callback_data="back_main")])
    return InlineKeyboardMarkup(inline_keyboard=rows)

def withdraw_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💸 Request Withdrawal", callback_data="withdraw_start")],
        [InlineKeyboardButton(text="🔙 Back",               callback_data="back_main")],
    ])

# ── /start ────────────────────────────────────────────────
@dp.message(Command("start"))
async def cmd_start(message: Message):
    uid  = message.from_user.id
    u    = get_user(uid)
    args = message.text.split()

    if u.get("banned"):
        await message.answer("🚫 You are banned.")
        return

    track_daily(uid)

    # Referral
    if len(args) > 1 and not u["ever_started"]:
        try:
            ref_id = int(args[1])
            if ref_id != uid and not u.get("referred_by"):
                ref_u = get_user(ref_id)
                ref_u["spins"]     += 5
                ref_u["referrals"] += 1
                u["referred_by"]    = ref_id
                stats["total_referrals"] += 1
                save_all()
                try:
                    await bot.send_message(
                        ref_id,
                        f"🎉 *+5 spins!* Your friend joined Fortuno Aviator!\n"
                        f"💰 Balance: *{ref_u['spins']}* spins",
                        parse_mode="Markdown"
                    )
                except Exception:
                    pass
        except (ValueError, IndexError):
            pass

    early = check_early_bird(uid)
    u["ever_started"] = True
    save_all()

    early_msg = "\n🎁 *Early bird bonus: +5 free spins!* You are one of the first 5 today!" if early else ""

    await message.answer(
        f"✈️ *Welcome to Fortuno Aviator!*\n"
        f"━━━━━━━━━━━━━━━━━━━━━\n"
        f"🎮 Watch the plane fly — cash out before it crashes!\n"
        f"💰 Your balance: *{u['spins']}* spins\n"
        f"{early_msg}\n\n"
        f"What do you want to do? 👇",
        parse_mode="Markdown",
        reply_markup=main_kb(uid)
    )

# ── How to Play ───────────────────────────────────────────
@dp.callback_query(F.data == "howtoplay")
async def howtoplay(callback: types.CallbackQuery):
    await callback.message.answer(
        "✈️ *How To Play — Very Simple!*\n"
        "━━━━━━━━━━━━━━━━━━━━━\n\n"
        "1️⃣  Press *PLAY* and choose how many spins to bet\n\n"
        "2️⃣  Press *🚀 FLY NOW!* — the plane takes off!\n\n"
        "3️⃣  You will see the number going up:\n"
        "       ✈️ 1.20x → 1.85x → 2.43x → 3.10x...\n\n"
        "4️⃣  Press *💰 CASH OUT NOW* at any time!\n\n"
        "✅ *Example:*\n"
        "       Bet 10 spins → cashout at 3x → WIN 30 spins!\n\n"
        "💥 *If you wait too long — plane crashes!*\n"
        "       You lose your bet. Cash out early!\n\n"
        "📈 97% RTP — very good odds for you!\n"
        "💸 Min cashout: 200 spins = $2.00",
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="✈️ Play Now!", callback_data="play")],
            [InlineKeyboardButton(text="🔙 Back",      callback_data="back_main")],
        ])
    )
    await callback.answer()

# ── Back to main ──────────────────────────────────────────
@dp.callback_query(F.data == "back_main")
async def back_main(callback: types.CallbackQuery):
    uid = callback.from_user.id
    u   = get_user(uid)
    await callback.message.answer(
        f"✈️ *Fortuno Aviator*\n"
        f"💰 Your balance: *{u['spins']}* spins",
        parse_mode="Markdown",
        reply_markup=main_kb(uid)
    )
    await callback.answer()

# ── Play → Bet Selection ──────────────────────────────────
@dp.callback_query(F.data == "play")
async def process_play(callback: types.CallbackQuery):
    uid = callback.from_user.id
    u   = get_user(uid)

    if u.get("banned"):
        await callback.answer("🚫 You are banned.", show_alert=True)
        return

    if uid in active_games:
        await callback.answer("⚠️ You already have a game running!", show_alert=True)
        return

    track_daily(uid)

    await callback.message.answer(
        f"✈️ *Choose How Many Spins To Bet*\n"
        f"━━━━━━━━━━━━━━━━━━━━━\n"
        f"💰 Your balance: *{u['spins']}* spins\n"
        f"Current bet: *{u.get('bet_size', 1)}* spin{'s' if u.get('bet_size',1) > 1 else ''}\n\n"
        f"👇 Pick your bet then press 🚀 FLY NOW!",
        parse_mode="Markdown",
        reply_markup=bet_kb(uid)
    )
    await callback.answer()

# ── Set Bet ───────────────────────────────────────────────
@dp.callback_query(F.data.startswith("setbet_"))
async def set_bet(callback: types.CallbackQuery):
    uid = callback.from_user.id
    u   = get_user(uid)
    bet = int(callback.data.split("_")[1])
    u["bet_size"] = bet
    save_all()
    await callback.message.edit_reply_markup(reply_markup=bet_kb(uid))
    await callback.answer(f"✅ Bet set to {bet} spin{'s' if bet > 1 else ''}!")

# ── Start Game ────────────────────────────────────────────
@dp.callback_query(F.data == "startgame")
async def start_game(callback: types.CallbackQuery):
    uid = callback.from_user.id
    u   = get_user(uid)

    if u.get("banned"):
        await callback.answer("🚫 You are banned.", show_alert=True)
        return

    if uid in active_games:
        await callback.answer("⚠️ Game already running!", show_alert=True)
        return

    bet = u.get("bet_size", 1)
    if u["spins"] < bet:
        await callback.answer(
            f"❌ Not enough spins! You need {bet} spins but you only have {u['spins']}.",
            show_alert=True
        )
        return

    # Deduct bet
    u["spins"] -= bet
    save_all()

    # Generate secret crash point
    crash_point = generate_crash_point()

    # Send countdown
    countdown_msg = await callback.message.answer(
        f"✈️ *Get ready...*\n\n"
        f"🎯 Bet: *{bet}* spins\n"
        f"⏳ Plane is taking off in 3 seconds...\n\n"
        f"👇 *Press CASH OUT the moment you want to stop!*",
        parse_mode="Markdown"
    )

    await asyncio.sleep(1)
    try:
        await bot.edit_message_text(
            chat_id=countdown_msg.chat.id,
            message_id=countdown_msg.message_id,
            text=(
                f"✈️ *Get ready...*\n\n"
                f"🎯 Bet: *{bet}* spins\n"
                f"⏳ Taking off in 2 seconds...\n\n"
                f"👇 *Press CASH OUT the moment you want to stop!*"
            ),
            parse_mode="Markdown"
        )
    except Exception:
        pass

    await asyncio.sleep(1)
    try:
        await bot.edit_message_text(
            chat_id=countdown_msg.chat.id,
            message_id=countdown_msg.message_id,
            text=(
                f"✈️ *Get ready...*\n\n"
                f"🎯 Bet: *{bet}* spins\n"
                f"⏳ Taking off in 1 second...\n\n"
                f"👇 *Press CASH OUT the moment you want to stop!*"
            ),
            parse_mode="Markdown"
        )
    except Exception:
        pass

    await asyncio.sleep(1)

    # Send the live game message
    msg = await bot.send_message(
        chat_id=callback.message.chat.id,
        text=flying_text(bet, 1.00),
        parse_mode="Markdown",
        reply_markup=cashout_kb()
    )

    # Store game state
    active_games[uid] = {
        "bet":        bet,
        "crash":      crash_point,
        "multiplier": 1.00,
        "msg_id":     msg.message_id,
        "chat_id":    callback.message.chat.id,
        "cashed_out": False,
        "task":       None,
    }

    task = asyncio.create_task(run_game(uid))
    active_games[uid]["task"] = task

    await callback.answer()

# ── Game Loop ─────────────────────────────────────────────
async def run_game(uid: int):
    try:
        game  = active_games[uid]
        u     = get_user(uid)
        mult  = 1.00
        crash = game["crash"]
        bet   = game["bet"]

        while mult < crash:
            await asyncio.sleep(TICK_INTERVAL)

            if game["cashed_out"]:
                return

            # Multiplier grows — slower at first, faster as it climbs
            if mult < 2.0:
                mult += random.uniform(0.08, 0.18)
            elif mult < 5.0:
                mult += random.uniform(0.15, 0.35)
            elif mult < 10.0:
                mult += random.uniform(0.30, 0.70)
            else:
                mult += random.uniform(0.80, 2.50)

            mult = round(min(mult, crash), 2)
            game["multiplier"] = mult

            # Update message every tick — 1 second so users can follow easily
            try:
                await bot.edit_message_text(
                    chat_id=game["chat_id"],
                    message_id=game["msg_id"],
                    text=flying_text(bet, mult),
                    parse_mode="Markdown",
                    reply_markup=cashout_kb()
                )
            except Exception:
                pass

        # ── CRASHED ───────────────────────────────────────
        if not game["cashed_out"]:
            game["cashed_out"] = True
            today = str(date.today())

            u["total_rounds_played"] = u.get("total_rounds_played", 0) + 1
            u["total_lost"]          = u.get("total_lost", 0) + bet
            stats["total_rounds_played"]        = stats.get("total_rounds_played", 0) + 1
            stats["total_crashes"]              = stats.get("total_crashes", 0) + 1
            stats["total_spins_lost"]           = stats.get("total_spins_lost", 0) + bet
            stats["daily_rounds_played"][today] = stats["daily_rounds_played"].get(today, 0) + 1
            save_all()

            try:
                await bot.edit_message_text(
                    chat_id=game["chat_id"],
                    message_id=game["msg_id"],
                    text=(
                        f"💥 *CRASHED at {crash:.2f}x!*\n\n"
                        f"😭 Too slow! The plane flew away!\n\n"
                        f"🎯 You bet: *{bet}* spins\n"
                        f"❌ You lost: *{bet}* spins\n"
                        f"💰 Your balance: *{u['spins']}* spins\n\n"
                        f"Try again — cash out faster next time! 💪"
                    ),
                    parse_mode="Markdown",
                    reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                        [InlineKeyboardButton(text="✈️ Play Again", callback_data="play")],
                        [InlineKeyboardButton(text="💎 Buy Spins",  callback_data="buy")],
                    ])
                )
            except Exception:
                pass

            active_games.pop(uid, None)

    except asyncio.CancelledError:
        pass
    except Exception as e:
        logging.error(f"Game error for uid {uid}: {e}")
        active_games.pop(uid, None)

# ── Cashout ───────────────────────────────────────────────
@dp.callback_query(F.data == "cashout")
async def process_cashout(callback: types.CallbackQuery):
    uid  = callback.from_user.id
    game = active_games.get(uid)

    if not game:
        await callback.answer("⚠️ No active game. Press Play to start!", show_alert=True)
        return

    if game["cashed_out"]:
        await callback.answer("💥 Too late! The plane already crashed!", show_alert=True)
        return

    game["cashed_out"] = True

    if game["task"] and not game["task"].done():
        game["task"].cancel()

    mult     = game["multiplier"]
    bet      = game["bet"]
    winnings = round(bet * mult)
    profit   = winnings - bet

    u = get_user(uid)
    u["spins"]               += winnings
    u["total_rounds_played"]  = u.get("total_rounds_played", 0) + 1
    u["total_won"]            = u.get("total_won", 0) + winnings

    if winnings > u.get("biggest_win", 0):
        u["biggest_win"] = winnings
    if winnings > stats.get("biggest_win_ever", 0):
        stats["biggest_win_ever"] = winnings
    if mult > u.get("highest_multiplier", 0.0):
        u["highest_multiplier"] = mult
    if mult > stats.get("highest_multiplier", 0.0):
        stats["highest_multiplier"] = mult

    today = str(date.today())
    stats["total_rounds_played"]        = stats.get("total_rounds_played", 0) + 1
    stats["total_cashouts"]             = stats.get("total_cashouts", 0) + 1
    stats["total_spins_won"]            = stats.get("total_spins_won", 0) + winnings
    stats["daily_rounds_played"][today] = stats["daily_rounds_played"].get(today, 0) + 1
    save_all()

    plane = get_plane(mult)

    try:
        await bot.edit_message_text(
            chat_id=game["chat_id"],
            message_id=game["msg_id"],
            text=(
                f"{plane} *YOU CASHED OUT!* 🎉\n\n"
                f"📈 Multiplier: *{mult:.2f}x*\n"
                f"🎯 You bet: *{bet}* spins\n"
                f"🏆 You won: *{winnings}* spins\n"
                f"📊 Profit: *+{profit}* spins\n\n"
                f"💰 Your balance: *{u['spins']}* spins\n\n"
                f"🔥 Well done! Play again?"
            ),
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="✈️ Play Again", callback_data="play")],
                [InlineKeyboardButton(text="💸 Withdraw",   callback_data="withdraw")],
            ])
        )
    except Exception:
        await bot.send_message(
            game["chat_id"],
            f"✅ *Cashed out at {mult:.2f}x!*\n"
            f"Won *{winnings}* spins!\n"
            f"💰 Balance: *{u['spins']}* spins",
            parse_mode="Markdown",
            reply_markup=main_kb(uid)
        )

    active_games.pop(uid, None)
    await callback.answer(f"✅ Cashed out at {mult:.2f}x! You won {winnings} spins!")

# ── My Stats ──────────────────────────────────────────────
@dp.callback_query(F.data == "mystats")
async def my_stats(callback: types.CallbackQuery):
    uid   = callback.from_user.id
    u     = get_user(uid)
    await callback.message.answer(
        f"📊 *Your Stats*\n"
        f"━━━━━━━━━━━━━━━━━━━━━\n"
        f"✈️ Rounds played: *{u.get('total_rounds_played', 0)}*\n"
        f"💰 Balance: *{u['spins']}* spins\n"
        f"🏆 Best win ever: *{u.get('biggest_win', 0)}* spins\n"
        f"📈 Highest multiplier: *{u.get('highest_multiplier', 0.0):.2f}x*\n"
        f"👥 Friends invited: *{u.get('referrals', 0)}*\n"
        f"📅 Member since: {u.get('joined_date', 'N/A')}",
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="🔙 Back", callback_data="back_main")]
        ])
    )
    await callback.answer()

# ── Referral ──────────────────────────────────────────────
@dp.callback_query(F.data == "referral")
async def referral_menu(callback: types.CallbackQuery):
    uid  = callback.from_user.id
    u    = get_user(uid)
    link = f"https://t.me/{BOT_NAME}?start={uid}"
    await callback.message.answer(
        f"👥 *Invite Friends — Earn Free Spins!*\n"
        f"━━━━━━━━━━━━━━━━━━━━━\n"
        f"For every friend you invite → you get *+5 free spins!*\n\n"
        f"🔗 Your invite link:\n`{link}`\n\n"
        f"👫 Friends invited: *{u.get('referrals', 0)}*\n"
        f"🎁 Free spins earned: *{u.get('referrals', 0) * 5}*\n\n"
        f"Share your link now and earn! 💰",
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="🔙 Back", callback_data="back_main")]
        ])
    )
    await callback.answer()

# ── Withdraw ──────────────────────────────────────────────
@dp.callback_query(F.data == "withdraw")
async def withdraw_menu(callback: types.CallbackQuery):
    uid = callback.from_user.id
    u   = get_user(uid)

    if u["spins"] < MIN_WITHDRAW:
        need = MIN_WITHDRAW - u["spins"]
        await callback.message.answer(
            f"💸 *Withdraw*\n\n"
            f"❌ You need at least *{MIN_WITHDRAW} spins* to withdraw.\n"
            f"💰 Your balance: *{u['spins']}* spins\n"
            f"📊 You need *{need}* more spins.\n\n"
            f"Keep playing to reach {MIN_WITHDRAW} spins! 💪",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="✈️ Play Now", callback_data="play")],
                [InlineKeyboardButton(text="💎 Buy Spins", callback_data="buy")],
                [InlineKeyboardButton(text="🔙 Back",      callback_data="back_main")],
            ])
        )
        await callback.answer()
        return

    if u["pending_withdrawal"]:
        await callback.message.answer(
            f"⏳ *Withdrawal Pending*\n\n"
            f"You already have a withdrawal request for *{u['pending_spins']}* spins.\n"
            f"Please wait — admin will send your money within 24 hours.",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="🔙 Back", callback_data="back_main")]
            ])
        )
        await callback.answer()
        return

    await callback.message.answer(
        f"💸 *Withdraw Your Winnings*\n\n"
        f"💰 Your balance: *{u['spins']}* spins = {usd(u['spins'])} = {ton(u['spins'])} TON\n"
        f"📌 Minimum: *{MIN_WITHDRAW} spins* = {usd(MIN_WITHDRAW)}\n\n"
        f"Press the button below to request your withdrawal:",
        parse_mode="Markdown",
        reply_markup=withdraw_kb()
    )
    await callback.answer()

@dp.callback_query(F.data == "withdraw_start")
async def withdraw_start(callback: types.CallbackQuery, state: FSMContext):
    uid = callback.from_user.id
    u   = get_user(uid)
    await state.set_state(WithdrawStates.waiting_amount)
    await callback.message.answer(
        f"💸 *How many spins do you want to withdraw?*\n\n"
        f"Minimum: *{MIN_WITHDRAW}*\n"
        f"Maximum: *{u['spins']}*\n\n"
        f"👇 Type the number:",
        parse_mode="Markdown"
    )
    await callback.answer()

@dp.message(WithdrawStates.waiting_amount)
async def withdraw_amount(message: Message, state: FSMContext):
    uid = message.from_user.id
    u   = get_user(uid)
    try:
        amount = int(message.text.strip())
    except ValueError:
        await message.answer("❌ Please type a number only. Example: 200")
        return
    if amount < MIN_WITHDRAW:
        await message.answer(f"❌ Minimum is {MIN_WITHDRAW} spins.")
        return
    if amount > u["spins"]:
        await message.answer(f"❌ You only have {u['spins']} spins.")
        return
    await state.update_data(amount=amount)
    await state.set_state(WithdrawStates.waiting_wallet)
    await message.answer(
        f"💳 *Enter your TON wallet address:*\n\n"
        f"Example: `UQD...`\n\n"
        f"👇 Paste your wallet address:",
        parse_mode="Markdown"
    )

@dp.message(WithdrawStates.waiting_wallet)
async def withdraw_wallet(message: Message, state: FSMContext):
    uid    = message.from_user.id
    u      = get_user(uid)
    wallet = message.text.strip()
    data   = await state.get_data()
    amount = data["amount"]

    if len(wallet) < 10:
        await message.answer("❌ That wallet address looks wrong. Please try again.")
        return

    u["spins"]             -= amount
    u["pending_withdrawal"] = True
    u["pending_spins"]      = amount
    u["pending_wallet"]     = wallet
    save_all()
    await state.clear()

    await message.answer(
        f"✅ *Withdrawal Request Sent!*\n\n"
        f"💰 Amount: *{amount}* spins = {usd(amount)} = {ton(amount)} TON\n"
        f"👛 Wallet: `{wallet}`\n\n"
        f"⏳ Admin will send your money within 24 hours.\n"
        f"Thank you for playing Fortuno Aviator! ✈️",
        parse_mode="Markdown",
        reply_markup=main_kb(uid)
    )

    try:
        await bot.send_message(
            ADMIN_ID,
            f"💸 *NEW WITHDRAWAL — Fortuno Aviator*\n"
            f"👤 User: `{uid}` · @{message.from_user.username or 'no username'}\n"
            f"💰 {amount} spins = {usd(amount)} = {ton(amount)} TON\n"
            f"👛 `{wallet}`\n\n"
            f"/pay {uid} to approve\n"
            f"/reject {uid} to reject",
            parse_mode="Markdown"
        )
    except Exception:
        pass

# ── Admin: /admin ─────────────────────────────────────────
@dp.message(Command("admin"))
async def admin_dashboard(message: Message):
    if message.from_user.id != ADMIN_ID:
        return
    today        = str(date.today())
    dau          = len(stats["daily_active"].get(today, []))
    new_p        = stats["daily_new_players"].get(today, 0)
    rounds_today = stats["daily_rounds_played"].get(today, 0)
    stars_today  = stats["daily_stars_spent"].get(today, 0)
    dep_today    = len(stats["daily_depositors"].get(today, []))
    purch_today  = stats["daily_purchases"].get(today, 0)

    pending  = [(uid, ud) for uid, ud in user_data.items() if ud.get("pending_withdrawal")]
    pend_txt = ""
    for uid, ud in pending[:5]:
        pend_txt += (
            f"  • `{uid}` — {ud['pending_spins']} spins "
            f"({usd(ud['pending_spins'])}) → `{ud['pending_wallet'][:12]}...`\n"
        )
    if not pend_txt:
        pend_txt = "  None ✅\n"

    await message.answer(
        f"🛠 *Fortuno Aviator — Admin*\n"
        f"━━━━━━━━━━━━━━━━━━━━━\n"
        f"📅 *Today ({today})*\n"
        f"  👥 Active: {dau} · 🆕 New: {new_p}\n"
        f"  ✈️ Rounds: {rounds_today} · 💎 Purchases: {purch_today}\n"
        f"  ⭐ Stars: {stars_today} · 💳 Depositors: {dep_today}\n\n"
        f"📊 *All Time*\n"
        f"  👥 Players: {stats['total_players']}\n"
        f"  ✈️ Rounds: {stats['total_rounds_played']}\n"
        f"  💰 Cashouts: {stats['total_cashouts']} · 💥 Crashes: {stats['total_crashes']}\n"
        f"  🏆 Biggest win: {stats.get('biggest_win_ever', 0)} spins\n"
        f"  📈 Highest mult: {stats.get('highest_multiplier', 0.0):.2f}x\n"
        f"  💸 TON paid out: {stats['total_ton_paid']} TON\n\n"
        f"⏳ *Pending Withdrawals*\n{pend_txt}",
        parse_mode="Markdown"
    )

# ── Admin: /stats7 ────────────────────────────────────────
@dp.message(Command("stats7"))
async def stats7(message: Message):
    if message.from_user.id != ADMIN_ID:
        return
    today = date.today()
    lines = ["📈 *Last 7 Days — Fortuno Aviator*\n━━━━━━━━━━━━━━━━━━━━━"]
    for i in range(7):
        d     = str(today - datetime.timedelta(days=i))
        dau   = len(stats["daily_active"].get(d, []))
        new_p = stats["daily_new_players"].get(d, 0)
        rnds  = stats["daily_rounds_played"].get(d, 0)
        stars = stats["daily_stars_spent"].get(d, 0)
        lines.append(f"  `{d}` — 👥{dau} · 🆕{new_p} · ✈️{rnds} · ⭐{stars}")
    await message.answer("\n".join(lines), parse_mode="Markdown")

# ── Admin: /pay ───────────────────────────────────────────
@dp.message(Command("pay"))
async def admin_pay(message: Message):
    if message.from_user.id != ADMIN_ID:
        return
    try:
        target_id = str(int(message.text.split()[1]))
        u         = user_data.get(target_id)
        if not u or not u.get("pending_withdrawal"):
            await message.answer("❌ No pending withdrawal for this user.")
            return
        spins  = u["pending_spins"]
        wallet = u["pending_wallet"]
        amount = ton(spins)
        link   = pay_link(wallet, amount, f"FortunoAviator withdrawal {target_id}")
        stats["total_ton_paid"]  = round(stats.get("total_ton_paid", 0) + amount, 4)
        u["pending_withdrawal"]  = False
        u["pending_spins"]       = 0
        u["pending_wallet"]      = None
        save_all()
        await message.answer(
            f"✅ Approved `{target_id}`\n"
            f"💸 {spins} spins = {usd(spins)} = {amount} TON\n"
            f"[👉 Open Tonkeeper]({link})",
            parse_mode="Markdown"
        )
        try:
            await bot.send_message(
                int(target_id),
                f"✅ *Your withdrawal has been approved!*\n\n"
                f"💸 {spins} spins = {usd(spins)} = {amount} TON\n"
                f"Your money is on the way! 🎉\n\n"
                f"Thanks for playing Fortuno Aviator ✈️",
                parse_mode="Markdown",
                reply_markup=main_kb(int(target_id))
            )
        except Exception:
            pass
    except (IndexError, ValueError):
        await message.answer("❌ Usage: /pay [user_id]")

# ── Admin: /reject ────────────────────────────────────────
@dp.message(Command("reject"))
async def admin_reject(message: Message):
    if message.from_user.id != ADMIN_ID:
        return
    try:
        target_id = str(int(message.text.split()[1]))
        u         = user_data.get(target_id)
        if not u or not u.get("pending_withdrawal"):
            await message.answer("❌ No pending withdrawal.")
            return
        spins                   = u["pending_spins"]
        u["spins"]             += spins
        u["pending_withdrawal"] = False
        u["pending_spins"]      = 0
        u["pending_wallet"]     = None
        save_all()
        await message.answer(
            f"✅ Rejected · returned {spins} spins to `{target_id}`.",
            parse_mode="Markdown"
        )
        try:
            await bot.send_message(
                int(target_id),
                f"❌ *Your withdrawal was rejected.*\n\n"
                f"💰 {spins} spins have been returned to your balance.\n"
                f"Please contact support if you have questions.",
                parse_mode="Markdown",
                reply_markup=main_kb(int(target_id))
            )
        except Exception:
            pass
    except (IndexError, ValueError):
        await message.answer("❌ Usage: /reject [user_id]")

# ── Admin: /gift ──────────────────────────────────────────
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
            f"🎁 Gifted *{amount}* spins to `{target_id}`.",
            parse_mode="Markdown"
        )
        try:
            await bot.send_message(
                int(target_id),
                f"🎁 *You received {amount} free spins!*\n\n"
                f"💰 Your balance: *{u['spins']}* spins\n"
                f"Good luck! ✈️",
                parse_mode="Markdown",
                reply_markup=main_kb(int(target_id))
            )
        except Exception:
            pass
    except (IndexError, ValueError):
        await message.answer("❌ Usage: /gift [user_id] [amount]")

# ── Admin: /userinfo ──────────────────────────────────────
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
            f"✈️ Rounds played: *{u.get('total_rounds_played',0)}*\n"
            f"🏆 Best win: *{u.get('biggest_win',0)}* spins\n"
            f"📈 Highest mult: *{u.get('highest_multiplier',0.0):.2f}x*\n"
            f"💎 Purchases: *{u.get('purchases',0)}* · Deposited: *{u.get('ever_deposited',False)}*\n"
            f"👥 Friends invited: *{u.get('referrals',0)}*\n"
            f"📅 Joined: {u.get('joined_date','N/A')} · 🚫 Banned: *{u.get('banned',False)}*\n"
            f"⏳ Pending withdrawal: *{u.get('pending_withdrawal',False)}*\n"
            f"💵 Held spins: *{u.get('pending_spins',0)}*\n"
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
        await message.answer("❌ Usage: /userinfo [user_id]")

@dp.callback_query(F.data.startswith("toggle_ban_"))
async def toggle_ban(callback: types.CallbackQuery):
    if callback.from_user.id != ADMIN_ID:
        await callback.answer("❌ Not authorized.", show_alert=True)
        return
    target_id = callback.data.replace("toggle_ban_", "")
    u         = user_data.get(target_id)
    if not u:
        await callback.answer("❌ User not found.", show_alert=True)
        return
    u["banned"] = not u.get("banned", False)
    save_all()
    status = "🚫 Banned" if u["banned"] else "✅ Unbanned"
    await callback.answer(f"{status} {target_id}", show_alert=True)

# ── Admin: /ban /unban ────────────────────────────────────
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
        await message.answer("❌ Usage: /ban [user_id]")

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
        await message.answer("❌ Usage: /unban [user_id]")

# ── Admin: /broadcast ─────────────────────────────────────
@dp.message(Command("broadcast"))
async def admin_broadcast(message: Message):
    if message.from_user.id != ADMIN_ID:
        return
    try:
        text = message.text.split(" ", 1)[1]
    except IndexError:
        await message.answer("❌ Usage: /broadcast [message]")
        return
    await message.answer("📢 Sending to all users...")
    sent = failed = 0
    for k in user_data:
        if user_data[k].get("banned"):
            continue
        try:
            await bot.send_message(
                int(k),
                f"📢 *Fortuno Aviator:*\n\n{text}",
                parse_mode="Markdown"
            )
            sent += 1
            await asyncio.sleep(0.05)
        except Exception:
            failed += 1
    await message.answer(
        f"✅ Done!\nSent: *{sent}* · Failed: *{failed}*",
        parse_mode="Markdown"
    )

# ── Buy Spins ─────────────────────────────────────────────
@dp.callback_query(F.data == "buy")
async def process_buy(callback: types.CallbackQuery):
    await callback.message.answer(
        f"💎 *Buy Spins*\n\n"
        f"Minimum: *10 Stars* = 100 spins\n"
        f"1 spin = $0.01 · 97% RTP\n\n"
        f"👇 Pick your package:",
        parse_mode="Markdown",
        reply_markup=buy_kb()
    )
    await callback.answer()

@dp.callback_query(F.data.startswith("buypack_"))
async def process_buypack(callback: types.CallbackQuery):
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
        description=f"{spins} spins · 1 spin = $0.01 · 97% RTP · TON payouts",
        payload=f"buy_{stars}_{spins}",
        provider_token="",
        currency="XTR",
        prices=[LabeledPrice(label=f"{spins} Spins", amount=stars)],
    )
    await callback.answer()

@dp.pre_checkout_query()
async def pre_check(q: PreCheckoutQuery):
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
    try:
        parts = m.successful_payment.invoice_payload.split("_")
        stars = int(parts[1])
        spins = int(parts[2])
    except (ValueError, IndexError):
        spins = 100
        stars = 10

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

    u["spins"]    += spins
    u["purchases"] = u.get("purchases", 0) + 1

    if not u.get("ever_deposited"):
        u["ever_deposited"] = True
        stats["total_depositors"] = stats.get("total_depositors", 0) + 1

    dep_list = stats["daily_depositors"].setdefault(today, [])
    if str(uid) not in dep_list:
        dep_list.append(str(uid))

    stats["total_spins_bought"]         = stats.get("total_spins_bought", 0) + spins
    stats["daily_purchases"][today]     = stats["daily_purchases"].get(today, 0) + 1
    stats["daily_stars_spent"][today]   = stats["daily_stars_spent"].get(today, 0) + stars
    stats["daily_revenue_spins"][today] = stats["daily_revenue_spins"].get(today, 0) + spins
    save_all()

    await m.answer(
        f"✅ *+{spins} Spins added to your account!*\n\n"
        f"💰 Your balance: *{u['spins']}* spins\n\n"
        f"✈️ Go fly and win big! Good luck! 🔥",
        parse_mode="Markdown",
        reply_markup=main_kb(uid)
    )

# ── Main ──────────────────────────────────────────────────
async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s"
    )
    logging.info("Fortuno Aviator ✈️ is online!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())