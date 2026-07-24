# """
# Fortuno Aviator ✈️ — PRODUCTION VERSION
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Install: pip install aiogram
# Run:     python3 main.py
# """

# import logging
# import asyncio
# import json
# import os
# import random
# import datetime
# from datetime import date
# from urllib.parse import quote
# from aiogram import Bot, Dispatcher, F, types
# from aiogram.filters import Command
# from aiogram.fsm.context import FSMContext
# from aiogram.fsm.state import State, StatesGroup
# from aiogram.fsm.storage.memory import MemoryStorage
# from aiogram.types import (
#     LabeledPrice, PreCheckoutQuery, Message,
#     InlineKeyboardButton, InlineKeyboardMarkup
# )

# # =========================================================
# #  CONFIGURATION
# # =========================================================
# TOKEN             = "8605162590:AAGg7lk-K8fqedcpQP9w8JdHrbdVO2X39wQ"
# ADMIN_ID          = 8612272966
# TONCENTER_API_KEY = "a4e8dd9e0111177cb876e4b0559e8a58b5eeb4b6acdbd981ad4f7b6123acad9c"
# ADMIN_WALLET      = "UQDlWJTEIwwGt7vai3T6s5MXgULmXk4ojhseU_UxxL7SY2DK"

# SPIN_USD     = 0.01
# SPIN_TO_TON  = 0.002
# MIN_WITHDRAW = 200
# HOUSE_EDGE   = 0.03   # 3% house edge = 97% RTP

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
# TICK_INTERVAL          = 1.0   # 1 second per tick
# # =========================================================

# bot = Bot(token=TOKEN)
# dp  = Dispatcher(storage=MemoryStorage())

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
#             "spins":               0,
#             "ever_started":        False,
#             "pending_withdrawal":  False,
#             "pending_spins":       0,
#             "pending_wallet":      None,
#             "referrals":           0,
#             "referred_by":         None,
#             "joined_date":         str(date.today()),
#             "total_rounds_played": 0,
#             "total_won":           0,
#             "total_lost":          0,
#             "purchases":           0,
#             "ever_deposited":      False,
#             "banned":              False,
#             "bet_size":            1,
#             "biggest_win":         0,
#             "highest_multiplier":  0.0,
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
#     r = random.random()
#     if r < HOUSE_EDGE:
#         return 1.00
#     r2    = random.random()
#     crash = 1.0 / (1.0 - r2 * (1.0 - HOUSE_EDGE))
#     return round(max(1.01, min(crash, 200.0)), 2)

# # ── Plane emoji based on multiplier ──────────────────────
# def get_plane(mult: float) -> str:
#     if mult < 2.0:
#         return "✈️"
#     elif mult < 5.0:
#         return "🛫"
#     elif mult < 10.0:
#         return "🚀"
#     else:
#         return "🛸"

# # ── Mood text based on multiplier ────────────────────────
# def get_mood(mult: float) -> str:
#     if mult < 1.5:
#         return "Just took off... 👀"
#     elif mult < 2.0:
#         return "Flying steady... 😏"
#     elif mult < 3.0:
#         return "Going higher! 😮"
#     elif mult < 5.0:
#         return "Getting risky... 😬"
#     elif mult < 10.0:
#         return "Very high now! 😱"
#     else:
#         return "INSANE height!! 🤑"

# # ── DANGER BAR — connected to real crash logic ────────────
# # The bar fills with 🟥 as you get CLOSER to the crash point.
# # All green = safe zone. All red = about to crash!
# # Formula: how far through the danger zone are you?
# #
# #   safe  ──────────────────────────────►  crash
# #   1.00x                               crash_point
# #
# # Each 🟩 = safe distance remaining
# # Each 🟥 = danger — crash is getting close!
# #
# def danger_bar(mult: float, crash: float) -> str:
#     BAR_SIZE = 10

#     # How close to crash are we? 0.0 = just started, 1.0 = crashed
#     # We use a logarithmic scale so the bar moves meaningfully
#     # even at low multipliers (1x→2x feels as dangerous as 5x→10x)
#     if crash <= 1.0:
#         pct = 1.0
#     else:
#         log_progress = (mult - 1.0) / (crash - 1.0)
#         pct = max(0.0, min(log_progress, 1.0))

#     red   = int(round(pct * BAR_SIZE))
#     green = BAR_SIZE - red

#     bar = "🟩" * green + "🟥" * red

#     # Label below the bar
#     if pct < 0.3:
#         label = "SAFE ZONE ✅"
#     elif pct < 0.6:
#         label = "BE CAREFUL ⚠️"
#     elif pct < 0.85:
#         label = "DANGER! 🔴"
#     else:
#         label = "CRASH COMING!! 💥"

#     return f"{bar}\n{label}"

# # ── Full flying message ───────────────────────────────────
# def flying_text(bet: int, mult: float, crash: float) -> str:
#     plane     = get_plane(mult)
#     mood      = get_mood(mult)
#     potential = round(bet * mult)
#     bar       = danger_bar(mult, crash)

#     return (
#         f"{plane}  *{mult:.2f}x*  —  {mood}\n\n"
#         f"{bar}\n\n"
#         f"🎯 Bet: *{bet}* spins\n"
#         f"💵 Cashout now = *{potential}* spins\n\n"
#         f"⬇️ Press the button before it crashes!"
#     )

# # ── Keyboards ─────────────────────────────────────────────
# def main_kb(uid: int) -> InlineKeyboardMarkup:
#     u   = get_user(uid)
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
#     u       = get_user(uid)
#     current = u.get("bet_size", 1)
#     rows    = []
#     row     = []
#     for b in BET_OPTIONS:
#         label = f"✅ {b}" if b == current else str(b)
#         row.append(InlineKeyboardButton(
#             text=f"{label} spin{'s' if b > 1 else ''}",
#             callback_data=f"setbet_{b}"
#         ))
#         if len(row) == 3:
#             rows.append(row)
#             row = []
#     if row:
#         rows.append(row)
#     rows.append([InlineKeyboardButton(text="🚀 FLY NOW!", callback_data="startgame")])
#     rows.append([InlineKeyboardButton(text="🔙 Back",     callback_data="back_main")])
#     return InlineKeyboardMarkup(inline_keyboard=rows)

# def cashout_kb() -> InlineKeyboardMarkup:
#     return InlineKeyboardMarkup(inline_keyboard=[
#         [InlineKeyboardButton(text="💰  CASH OUT NOW!  💰", callback_data="cashout")],
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
#         [InlineKeyboardButton(text="🔙 Back",               callback_data="back_main")],
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
#                     await bot.send_message(
#                         ref_id,
#                         f"🎉 *+5 spins!* Your friend joined Fortuno Aviator!\n"
#                         f"💰 Balance: *{ref_u['spins']}* spins",
#                         parse_mode="Markdown"
#                     )
#                 except Exception:
#                     pass
#         except (ValueError, IndexError):
#             pass

#     early = check_early_bird(uid)
#     u["ever_started"] = True
#     save_all()

#     early_msg = "\n🎁 *Early bird bonus: +5 free spins!* You are one of the first 5 today!" if early else ""

#     await message.answer(
#         f"✈️ *Welcome to Fortuno Aviator!*\n"
#         f"━━━━━━━━━━━━━━━━━━━━━\n"
#         f"🎮 Watch the plane fly — cash out before it crashes!\n"
#         f"💰 Your balance: *{u['spins']}* spins\n"
#         f"{early_msg}\n\n"
#         f"What do you want to do? 👇",
#         parse_mode="Markdown",
#         reply_markup=main_kb(uid)
#     )

# # ── How to Play ───────────────────────────────────────────
# @dp.callback_query(F.data == "howtoplay")
# async def howtoplay(callback: types.CallbackQuery):
#     await callback.message.answer(
#         "✈️ *How To Play — Very Simple!*\n"
#         "━━━━━━━━━━━━━━━━━━━━━\n\n"
#         "1️⃣  Press *PLAY* and choose how many spins to bet\n\n"
#         "2️⃣  Press *🚀 FLY NOW!* — the plane takes off!\n\n"
#         "3️⃣  Watch the multiplier go up:\n"
#         "       ✈️ 1.20x → 1.85x → 2.43x → 3.10x...\n\n"
#         "4️⃣  Watch the safety bar:\n"
#         "       🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩 = Very safe\n"
#         "       🟩🟩🟩🟩🟩🟥🟥🟥🟥🟥 = Getting risky!\n"
#         "       🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥 = CRASH COMING!!\n\n"
#         "5️⃣  Press *💰 CASH OUT NOW* before bar goes all red!\n\n"
#         "✅ *Example:*\n"
#         "       Bet 10 spins → cashout at 3x → WIN 30 spins!\n\n"
#         "💥 *If bar goes full red — plane crashes! You lose!*\n\n"
#         "📈 97% RTP — very good odds!\n"
#         "💸 Min cashout: 200 spins = $2.00",
#         parse_mode="Markdown",
#         reply_markup=InlineKeyboardMarkup(inline_keyboard=[
#             [InlineKeyboardButton(text="✈️ Play Now!", callback_data="play")],
#             [InlineKeyboardButton(text="🔙 Back",      callback_data="back_main")],
#         ])
#     )
#     await callback.answer()

# # ── Back to main ──────────────────────────────────────────
# @dp.callback_query(F.data == "back_main")
# async def back_main(callback: types.CallbackQuery):
#     uid = callback.from_user.id
#     u   = get_user(uid)
#     await callback.message.answer(
#         f"✈️ *Fortuno Aviator*\n"
#         f"💰 Your balance: *{u['spins']}* spins",
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
#         f"✈️ *Choose How Many Spins To Bet*\n"
#         f"━━━━━━━━━━━━━━━━━━━━━\n"
#         f"💰 Your balance: *{u['spins']}* spins\n"
#         f"Current bet: *{u.get('bet_size', 1)}* spin{'s' if u.get('bet_size',1) > 1 else ''}\n\n"
#         f"👇 Pick your bet then press 🚀 FLY NOW!",
#         parse_mode="Markdown",
#         reply_markup=bet_kb(uid)
#     )
#     await callback.answer()

# # ── Set Bet ───────────────────────────────────────────────
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
#         await callback.answer(
#             f"❌ Not enough spins! You need {bet} but have {u['spins']}.",
#             show_alert=True
#         )
#         return

#     u["spins"] -= bet
#     save_all()

#     crash_point = generate_crash_point()

#     # 3 second countdown
#     countdown_msg = await callback.message.answer(
#         f"✈️ *Plane is taking off!*\n\n"
#         f"🎯 Bet: *{bet}* spins\n"
#         f"⏳ *3...*\n\n"
#         f"Get your finger ready on CASH OUT! 👇",
#         parse_mode="Markdown"
#     )

#     await asyncio.sleep(1)
#     try:
#         await bot.edit_message_text(
#             chat_id=countdown_msg.chat.id,
#             message_id=countdown_msg.message_id,
#             text=(
#                 f"✈️ *Plane is taking off!*\n\n"
#                 f"🎯 Bet: *{bet}* spins\n"
#                 f"⏳ *2...*\n\n"
#                 f"Get your finger ready on CASH OUT! 👇"
#             ),
#             parse_mode="Markdown"
#         )
#     except Exception:
#         pass

#     await asyncio.sleep(1)
#     try:
#         await bot.edit_message_text(
#             chat_id=countdown_msg.chat.id,
#             message_id=countdown_msg.message_id,
#             text=(
#                 f"✈️ *Plane is taking off!*\n\n"
#                 f"🎯 Bet: *{bet}* spins\n"
#                 f"⏳ *1...*\n\n"
#                 f"Get your finger ready on CASH OUT! 👇"
#             ),
#             parse_mode="Markdown"
#         )
#     except Exception:
#         pass

#     await asyncio.sleep(1)

#     # Send live game message
#     msg = await bot.send_message(
#         chat_id=callback.message.chat.id,
#         text=flying_text(bet, 1.00, crash_point),
#         parse_mode="Markdown",
#         reply_markup=cashout_kb()
#     )

#     active_games[uid] = {
#         "bet":        bet,
#         "crash":      crash_point,
#         "multiplier": 1.00,
#         "msg_id":     msg.message_id,
#         "chat_id":    callback.message.chat.id,
#         "cashed_out": False,
#         "task":       None,
#     }

#     task = asyncio.create_task(run_game(uid))
#     active_games[uid]["task"] = task

#     await callback.answer()

# # ── Game Loop ─────────────────────────────────────────────
# async def run_game(uid: int):
#     try:
#         game  = active_games[uid]
#         u     = get_user(uid)
#         mult  = 1.00
#         crash = game["crash"]
#         bet   = game["bet"]

#         while mult < crash:
#             await asyncio.sleep(TICK_INTERVAL)

#             if game["cashed_out"]:
#                 return

#             # Multiplier grows naturally
#             if mult < 2.0:
#                 mult += random.uniform(0.08, 0.18)
#             elif mult < 5.0:
#                 mult += random.uniform(0.15, 0.35)
#             elif mult < 10.0:
#                 mult += random.uniform(0.30, 0.70)
#             else:
#                 mult += random.uniform(0.80, 2.50)

#             mult = round(min(mult, crash), 2)
#             game["multiplier"] = mult

#             # Update message — bar fills with red as crash approaches
#             try:
#                 await bot.edit_message_text(
#                     chat_id=game["chat_id"],
#                     message_id=game["msg_id"],
#                     text=flying_text(bet, mult, crash),
#                     parse_mode="Markdown",
#                     reply_markup=cashout_kb()
#                 )
#             except Exception:
#                 pass

#         # ── CRASHED ───────────────────────────────────────
#         if not game["cashed_out"]:
#             game["cashed_out"] = True
#             today = str(date.today())

#             u["total_rounds_played"] = u.get("total_rounds_played", 0) + 1
#             u["total_lost"]          = u.get("total_lost", 0) + bet
#             stats["total_rounds_played"]        = stats.get("total_rounds_played", 0) + 1
#             stats["total_crashes"]              = stats.get("total_crashes", 0) + 1
#             stats["total_spins_lost"]           = stats.get("total_spins_lost", 0) + bet
#             stats["daily_rounds_played"][today] = stats["daily_rounds_played"].get(today, 0) + 1
#             save_all()

#             try:
#                 await bot.edit_message_text(
#                     chat_id=game["chat_id"],
#                     message_id=game["msg_id"],
#                     text=(
#                         f"💥 *CRASHED at {crash:.2f}x!*\n\n"
#                         f"🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥\n"
#                         f"TOO LATE! 😭\n\n"
#                         f"🎯 You bet: *{bet}* spins\n"
#                         f"❌ You lost: *{bet}* spins\n"
#                         f"💰 Your balance: *{u['spins']}* spins\n\n"
#                         f"Cash out faster next time! 💪"
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
#         logging.error(f"Game error for uid {uid}: {e}")
#         active_games.pop(uid, None)

# # ── Cashout ───────────────────────────────────────────────
# @dp.callback_query(F.data == "cashout")
# async def process_cashout(callback: types.CallbackQuery):
#     uid  = callback.from_user.id
#     game = active_games.get(uid)

#     if not game:
#         await callback.answer("⚠️ No active game. Press Play to start!", show_alert=True)
#         return

#     if game["cashed_out"]:
#         await callback.answer("💥 Too late! The plane already crashed!", show_alert=True)
#         return

#     game["cashed_out"] = True

#     if game["task"] and not game["task"].done():
#         game["task"].cancel()

#     mult     = game["multiplier"]
#     bet      = game["bet"]
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

#     plane = get_plane(mult)

#     try:
#         await bot.edit_message_text(
#             chat_id=game["chat_id"],
#             message_id=game["msg_id"],
#             text=(
#                 f"{plane} *YOU CASHED OUT!* 🎉\n\n"
#                 f"🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩\n"
#                 f"PERFECT TIMING! ✅\n\n"
#                 f"📈 Multiplier: *{mult:.2f}x*\n"
#                 f"🎯 You bet: *{bet}* spins\n"
#                 f"🏆 You won: *{winnings}* spins\n"
#                 f"📊 Profit: *+{profit}* spins\n\n"
#                 f"💰 Your balance: *{u['spins']}* spins\n\n"
#                 f"🔥 Well done! Play again?"
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
#             f"✅ *Cashed out at {mult:.2f}x!*\n"
#             f"Won *{winnings}* spins!\n"
#             f"💰 Balance: *{u['spins']}* spins",
#             parse_mode="Markdown",
#             reply_markup=main_kb(uid)
#         )

#     active_games.pop(uid, None)
#     await callback.answer(f"✅ Cashed out at {mult:.2f}x! You won {winnings} spins!")

# # ── My Stats ──────────────────────────────────────────────
# @dp.callback_query(F.data == "mystats")
# async def my_stats(callback: types.CallbackQuery):
#     uid = callback.from_user.id
#     u   = get_user(uid)
#     await callback.message.answer(
#         f"📊 *Your Stats*\n"
#         f"━━━━━━━━━━━━━━━━━━━━━\n"
#         f"✈️ Rounds played: *{u.get('total_rounds_played', 0)}*\n"
#         f"💰 Balance: *{u['spins']}* spins\n"
#         f"🏆 Best win ever: *{u.get('biggest_win', 0)}* spins\n"
#         f"📈 Highest multiplier: *{u.get('highest_multiplier', 0.0):.2f}x*\n"
#         f"👥 Friends invited: *{u.get('referrals', 0)}*\n"
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
#         f"👥 *Invite Friends — Earn Free Spins!*\n"
#         f"━━━━━━━━━━━━━━━━━━━━━\n"
#         f"For every friend you invite → you get *+5 free spins!*\n\n"
#         f"🔗 Your invite link:\n`{link}`\n\n"
#         f"👫 Friends invited: *{u.get('referrals', 0)}*\n"
#         f"🎁 Free spins earned: *{u.get('referrals', 0) * 5}*\n\n"
#         f"Share your link now and earn! 💰",
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
#         need = MIN_WITHDRAW - u["spins"]
#         await callback.message.answer(
#             f"💸 *Withdraw*\n\n"
#             f"❌ You need at least *{MIN_WITHDRAW} spins* to withdraw.\n"
#             f"💰 Your balance: *{u['spins']}* spins\n"
#             f"📊 You need *{need}* more spins.\n\n"
#             f"Keep playing to reach {MIN_WITHDRAW} spins! 💪",
#             parse_mode="Markdown",
#             reply_markup=InlineKeyboardMarkup(inline_keyboard=[
#                 [InlineKeyboardButton(text="✈️ Play Now",  callback_data="play")],
#                 [InlineKeyboardButton(text="💎 Buy Spins", callback_data="buy")],
#                 [InlineKeyboardButton(text="🔙 Back",      callback_data="back_main")],
#             ])
#         )
#         await callback.answer()
#         return

#     if u["pending_withdrawal"]:
#         await callback.message.answer(
#             f"⏳ *Withdrawal Pending*\n\n"
#             f"You already requested *{u['pending_spins']}* spins withdrawal.\n"
#             f"Admin will send your money within 24 hours.",
#             parse_mode="Markdown",
#             reply_markup=InlineKeyboardMarkup(inline_keyboard=[
#                 [InlineKeyboardButton(text="🔙 Back", callback_data="back_main")]
#             ])
#         )
#         await callback.answer()
#         return

#     await callback.message.answer(
#         f"💸 *Withdraw Your Winnings*\n\n"
#         f"💰 Balance: *{u['spins']}* spins = {usd(u['spins'])} = {ton(u['spins'])} TON\n"
#         f"📌 Minimum: *{MIN_WITHDRAW} spins* = {usd(MIN_WITHDRAW)}\n\n"
#         f"Press below to request:",
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
#         f"💸 *How many spins to withdraw?*\n\n"
#         f"Minimum: *{MIN_WITHDRAW}*\n"
#         f"Maximum: *{u['spins']}*\n\n"
#         f"👇 Type the number:",
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
#         await message.answer("❌ Please type a number only. Example: 200")
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
#         f"💳 *Enter your TON wallet address:*\n\n"
#         f"Example: `UQD...`\n\n"
#         f"👇 Paste your wallet:",
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
#         await message.answer("❌ That wallet address looks wrong. Try again.")
#         return

#     u["spins"]             -= amount
#     u["pending_withdrawal"] = True
#     u["pending_spins"]      = amount
#     u["pending_wallet"]     = wallet
#     save_all()
#     await state.clear()

#     await message.answer(
#         f"✅ *Withdrawal Request Sent!*\n\n"
#         f"💰 Amount: *{amount}* spins = {usd(amount)} = {ton(amount)} TON\n"
#         f"👛 Wallet: `{wallet}`\n\n"
#         f"⏳ Admin will send your money within 24 hours.\n"
#         f"Thank you! ✈️",
#         parse_mode="Markdown",
#         reply_markup=main_kb(uid)
#     )

#     try:
#         await bot.send_message(
#             ADMIN_ID,
#             f"💸 *NEW WITHDRAWAL — Fortuno Aviator*\n"
#             f"👤 User: `{uid}` · @{message.from_user.username or 'no username'}\n"
#             f"💰 {amount} spins = {usd(amount)} = {ton(amount)} TON\n"
#             f"👛 `{wallet}`\n\n"
#             f"/pay {uid} to approve\n"
#             f"/reject {uid} to reject",
#             parse_mode="Markdown"
#         )
#     except Exception:
#         pass

# # ── Admin: /admin ─────────────────────────────────────────
# @dp.message(Command("admin"))
# async def admin_dashboard(message: Message):
#     if message.from_user.id != ADMIN_ID:
#         return
#     today        = str(date.today())
#     dau          = len(stats["daily_active"].get(today, []))
#     new_p        = stats["daily_new_players"].get(today, 0)
#     rounds_today = stats["daily_rounds_played"].get(today, 0)
#     stars_today  = stats["daily_stars_spent"].get(today, 0)
#     dep_today    = len(stats["daily_depositors"].get(today, []))
#     purch_today  = stats["daily_purchases"].get(today, 0)
#     pending      = [(uid, ud) for uid, ud in user_data.items() if ud.get("pending_withdrawal")]
#     pend_txt     = ""
#     for uid, ud in pending[:5]:
#         pend_txt += (
#             f"  • `{uid}` — {ud['pending_spins']} spins "
#             f"({usd(ud['pending_spins'])}) → `{ud['pending_wallet'][:12]}...`\n"
#         )
#     if not pend_txt:
#         pend_txt = "  None ✅\n"

#     await message.answer(
#         f"🛠 *Fortuno Aviator — Admin*\n"
#         f"━━━━━━━━━━━━━━━━━━━━━\n"
#         f"📅 *Today ({today})*\n"
#         f"  👥 Active: {dau} · 🆕 New: {new_p}\n"
#         f"  ✈️ Rounds: {rounds_today} · 💎 Purchases: {purch_today}\n"
#         f"  ⭐ Stars: {stars_today} · 💳 Depositors: {dep_today}\n\n"
#         f"📊 *All Time*\n"
#         f"  👥 Players: {stats['total_players']}\n"
#         f"  ✈️ Rounds: {stats['total_rounds_played']}\n"
#         f"  💰 Cashouts: {stats['total_cashouts']} · 💥 Crashes: {stats['total_crashes']}\n"
#         f"  🏆 Biggest win: {stats.get('biggest_win_ever', 0)} spins\n"
#         f"  📈 Highest mult: {stats.get('highest_multiplier', 0.0):.2f}x\n"
#         f"  💸 TON paid: {stats['total_ton_paid']} TON\n\n"
#         f"⏳ *Pending Withdrawals*\n{pend_txt}",
#         parse_mode="Markdown"
#     )

# # ── Admin: /stats7 ────────────────────────────────────────
# @dp.message(Command("stats7"))
# async def stats7(message: Message):
#     if message.from_user.id != ADMIN_ID:
#         return
#     today = date.today()
#     lines = ["📈 *Last 7 Days — Fortuno Aviator*\n━━━━━━━━━━━━━━━━━━━━━"]
#     for i in range(7):
#         d     = str(today - datetime.timedelta(days=i))
#         dau   = len(stats["daily_active"].get(d, []))
#         new_p = stats["daily_new_players"].get(d, 0)
#         rnds  = stats["daily_rounds_played"].get(d, 0)
#         stars = stats["daily_stars_spent"].get(d, 0)
#         lines.append(f"  `{d}` — 👥{dau} · 🆕{new_p} · ✈️{rnds} · ⭐{stars}")
#     await message.answer("\n".join(lines), parse_mode="Markdown")

# # ── Admin: /pay ───────────────────────────────────────────
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
#         link   = pay_link(wallet, amount, f"FortunoAviator withdrawal {target_id}")
#         stats["total_ton_paid"] = round(stats.get("total_ton_paid", 0) + amount, 4)
#         u["pending_withdrawal"] = False
#         u["pending_spins"]      = 0
#         u["pending_wallet"]     = None
#         save_all()
#         await message.answer(
#             f"✅ Approved `{target_id}`\n"
#             f"💸 {spins} spins = {usd(spins)} = {amount} TON\n"
#             f"[👉 Open Tonkeeper]({link})",
#             parse_mode="Markdown"
#         )
#         try:
#             await bot.send_message(
#                 int(target_id),
#                 f"✅ *Withdrawal Approved!*\n\n"
#                 f"💸 {spins} spins = {usd(spins)} = {amount} TON sent!\n"
#                 f"Thanks for playing Fortuno Aviator ✈️",
#                 parse_mode="Markdown",
#                 reply_markup=main_kb(int(target_id))
#             )
#         except Exception:
#             pass
#     except (IndexError, ValueError):
#         await message.answer("❌ Usage: /pay [user_id]")

# # ── Admin: /reject ────────────────────────────────────────
# @dp.message(Command("reject"))
# async def admin_reject(message: Message):
#     if message.from_user.id != ADMIN_ID:
#         return
#     try:
#         target_id = str(int(message.text.split()[1]))
#         u         = user_data.get(target_id)
#         if not u or not u.get("pending_withdrawal"):
#             await message.answer("❌ No pending withdrawal.")
#             return
#         spins                   = u["pending_spins"]
#         u["spins"]             += spins
#         u["pending_withdrawal"] = False
#         u["pending_spins"]      = 0
#         u["pending_wallet"]     = None
#         save_all()
#         await message.answer(f"✅ Rejected · returned {spins} spins to `{target_id}`.", parse_mode="Markdown")
#         try:
#             await bot.send_message(
#                 int(target_id),
#                 f"❌ *Withdrawal Rejected*\n\n"
#                 f"💰 {spins} spins returned to your balance.\n"
#                 f"Contact support if you have questions.",
#                 parse_mode="Markdown",
#                 reply_markup=main_kb(int(target_id))
#             )
#         except Exception:
#             pass
#     except (IndexError, ValueError):
#         await message.answer("❌ Usage: /reject [user_id]")

# # ── Admin: /gift ──────────────────────────────────────────
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
#             await bot.send_message(
#                 int(target_id),
#                 f"🎁 *You received {amount} free spins!*\n\n"
#                 f"💰 Balance: *{u['spins']}* spins\nGood luck! ✈️",
#                 parse_mode="Markdown",
#                 reply_markup=main_kb(int(target_id))
#             )
#         except Exception:
#             pass
#     except (IndexError, ValueError):
#         await message.answer("❌ Usage: /gift [user_id] [amount]")

# # ── Admin: /userinfo ──────────────────────────────────────
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
#             f"✈️ Rounds: *{u.get('total_rounds_played',0)}*\n"
#             f"🏆 Best win: *{u.get('biggest_win',0)}* spins\n"
#             f"📈 Highest mult: *{u.get('highest_multiplier',0.0):.2f}x*\n"
#             f"💎 Purchases: *{u.get('purchases',0)}* · Deposited: *{u.get('ever_deposited',False)}*\n"
#             f"👥 Invited: *{u.get('referrals',0)}*\n"
#             f"📅 Joined: {u.get('joined_date','N/A')} · 🚫 Banned: *{u.get('banned',False)}*\n"
#             f"⏳ Pending: *{u.get('pending_withdrawal',False)}* · Held: *{u.get('pending_spins',0)}*\n"
#             f"👛 `{u.get('pending_wallet','None')}`",
#             parse_mode="Markdown",
#             reply_markup=InlineKeyboardMarkup(inline_keyboard=[
#                 [InlineKeyboardButton(text="🎁 Gift spins", callback_data=f"gift_menu_{target_id}")],
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

# # ── Admin: /ban /unban ────────────────────────────────────
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

# # ── Admin: /broadcast ─────────────────────────────────────
# @dp.message(Command("broadcast"))
# async def admin_broadcast(message: Message):
#     if message.from_user.id != ADMIN_ID:
#         return
#     try:
#         text = message.text.split(" ", 1)[1]
#     except IndexError:
#         await message.answer("❌ Usage: /broadcast [message]")
#         return
#     await message.answer("📢 Sending to all users...")
#     sent = failed = 0
#     for k in user_data:
#         if user_data[k].get("banned"):
#             continue
#         try:
#             await bot.send_message(
#                 int(k),
#                 f"📢 *Fortuno Aviator:*\n\n{text}",
#                 parse_mode="Markdown"
#             )
#             sent += 1
#             await asyncio.sleep(0.05)
#         except Exception:
#             failed += 1
#     await message.answer(f"✅ Done! Sent: *{sent}* · Failed: *{failed}*", parse_mode="Markdown")

# # ── Buy Spins ─────────────────────────────────────────────
# @dp.callback_query(F.data == "buy")
# async def process_buy(callback: types.CallbackQuery):
#     await callback.message.answer(
#         f"💎 *Buy Spins*\n\n"
#         f"Minimum: *10 Stars* = 100 spins\n"
#         f"1 spin = $0.01 · 97% RTP\n\n"
#         f"👇 Pick your package:",
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
#             f"✅ Already credited!\n💰 Balance: *{u['spins']}* spins",
#             parse_mode="Markdown",
#             reply_markup=main_kb(uid)
#         )
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
#         f"✅ *+{spins} Spins added!*\n\n"
#         f"💰 Your balance: *{u['spins']}* spins\n\n"
#         f"✈️ Fly high and win big! 🔥",
#         parse_mode="Markdown",
#         reply_markup=main_kb(uid)
#     )

# # ── Main ──────────────────────────────────────────────────
# async def main():
#     logging.basicConfig(
#         level=logging.INFO,
#         format="%(asctime)s [%(levelname)s] %(message)s"
#     )
#     logging.info("Fortuno Aviator ✈️ is online!")
#     await dp.start_polling(bot)

# if __name__ == "__main__":
#     asyncio.run(main())

# """
# Fortuno Aviator ✈️ — PRODUCTION VERSION
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Install: pip install aiogram
# Run:     python3 main.py
# """

# import logging
# import asyncio
# import json
# import os
# import random
# import datetime
# from datetime import date
# from urllib.parse import quote
# from aiogram import Bot, Dispatcher, F, types
# from aiogram.filters import Command
# from aiogram.fsm.context import FSMContext
# from aiogram.fsm.state import State, StatesGroup
# from aiogram.fsm.storage.memory import MemoryStorage
# from aiogram.types import (
#     LabeledPrice, PreCheckoutQuery, Message,
#     InlineKeyboardButton, InlineKeyboardMarkup
# )

# # =========================================================
# #  CONFIGURATION
# # =========================================================
# TOKEN             = "8605162590:AAE9r8DRRnJw-3qRJQStQJk2ShTSuF0TI4o"
# ADMIN_ID          = 8612272966
# TONCENTER_API_KEY = "a4e8dd9e0111177cb876e4b0559e8a58b5eeb4b6acdbd981ad4f7b6123acad9c"
# ADMIN_WALLET      = "UQDlWJTEIwwGt7vai3T6s5MXgULmXk4ojhseU_UxxL7SY2DK"

# SPIN_USD     = 0.01
# SPIN_TO_TON  = 0.002
# MIN_WITHDRAW = 200
# HOUSE_EDGE   = 0.03   # 3% house edge = 97% RTP

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
# TICK_INTERVAL          = 1.0   # 1 second per update — easy to follow
# # =========================================================

# bot = Bot(token=TOKEN)
# dp  = Dispatcher(storage=MemoryStorage())

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
#             "spins":               0,
#             "ever_started":        False,
#             "pending_withdrawal":  False,
#             "pending_spins":       0,
#             "pending_wallet":      None,
#             "referrals":           0,
#             "referred_by":         None,
#             "joined_date":         str(date.today()),
#             "total_rounds_played": 0,
#             "total_won":           0,
#             "total_lost":          0,
#             "purchases":           0,
#             "ever_deposited":      False,
#             "banned":              False,
#             "bet_size":            1,
#             "biggest_win":         0,
#             "highest_multiplier":  0.0,
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
#     r = random.random()
#     if r < HOUSE_EDGE:
#         return 1.00
#     r2    = random.random()
#     crash = 1.0 / (1.0 - r2 * (1.0 - HOUSE_EDGE))
#     return round(max(1.01, min(crash, 200.0)), 2)

# # ── Simple plane emoji based on height ───────────────────
# def get_plane(mult: float) -> str:
#     if mult < 2.0:
#         return "✈️"
#     elif mult < 5.0:
#         return "🛫"
#     elif mult < 10.0:
#         return "🚀"
#     else:
#         return "🛸"

# # ── Simple message for flying state ──────────────────────
# def flying_text(bet: int, mult: float) -> str:
#     plane = get_plane(mult)
#     if mult < 1.5:
#         mood = "Just took off... 👀"
#     elif mult < 2.0:
#         mood = "Flying steady... 😏"
#     elif mult < 3.0:
#         mood = "Going higher! 😮"
#     elif mult < 5.0:
#         mood = "Getting risky... 😬"
#     elif mult < 10.0:
#         mood = "Very high now! 😱"
#     else:
#         mood = "INSANE height!! 🤑"

#     potential = round(bet * mult)
#     return (
#         f"{plane}  *{mult:.2f}x*  —  {mood}\n\n"
#         f"🎯 Bet: *{bet}* spins\n"
#         f"💵 Cashout now = *{potential}* spins\n\n"
#         f"⬇️ Press the button before it crashes!"
#     )

# # ── Keyboards ─────────────────────────────────────────────
# def main_kb(uid: int) -> InlineKeyboardMarkup:
#     u   = get_user(uid)
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
#     u       = get_user(uid)
#     current = u.get("bet_size", 1)
#     rows    = []
#     row     = []
#     for b in BET_OPTIONS:
#         label = f"✅ {b}" if b == current else str(b)
#         row.append(InlineKeyboardButton(
#             text=f"{label} spin{'s' if b > 1 else ''}",
#             callback_data=f"setbet_{b}"
#         ))
#         if len(row) == 3:
#             rows.append(row)
#             row = []
#     if row:
#         rows.append(row)
#     rows.append([InlineKeyboardButton(text="🚀 FLY NOW!", callback_data="startgame")])
#     rows.append([InlineKeyboardButton(text="🔙 Back",     callback_data="back_main")])
#     return InlineKeyboardMarkup(inline_keyboard=rows)

# def cashout_kb() -> InlineKeyboardMarkup:
#     return InlineKeyboardMarkup(inline_keyboard=[
#         [InlineKeyboardButton(text="💰  CASH OUT NOW!  💰", callback_data="cashout")],
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
#         [InlineKeyboardButton(text="🔙 Back",               callback_data="back_main")],
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

#     # Referral
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
#                     await bot.send_message(
#                         ref_id,
#                         f"🎉 *+5 spins!* Your friend joined Fortuno Aviator!\n"
#                         f"💰 Balance: *{ref_u['spins']}* spins",
#                         parse_mode="Markdown"
#                     )
#                 except Exception:
#                     pass
#         except (ValueError, IndexError):
#             pass

#     early = check_early_bird(uid)
#     u["ever_started"] = True
#     save_all()

#     early_msg = "\n🎁 *Early bird bonus: +5 free spins!* You are one of the first 5 today!" if early else ""

#     await message.answer(
#         f"✈️ *Welcome to Fortuno Aviator!*\n"
#         f"━━━━━━━━━━━━━━━━━━━━━\n"
#         f"🎮 Watch the plane fly — cash out before it crashes!\n"
#         f"💰 Your balance: *{u['spins']}* spins\n"
#         f"{early_msg}\n\n"
#         f"What do you want to do? 👇",
#         parse_mode="Markdown",
#         reply_markup=main_kb(uid)
#     )

# # ── How to Play ───────────────────────────────────────────
# @dp.callback_query(F.data == "howtoplay")
# async def howtoplay(callback: types.CallbackQuery):
#     await callback.message.answer(
#         "✈️ *How To Play — Very Simple!*\n"
#         "━━━━━━━━━━━━━━━━━━━━━\n\n"
#         "1️⃣  Press *PLAY* and choose how many spins to bet\n\n"
#         "2️⃣  Press *🚀 FLY NOW!* — the plane takes off!\n\n"
#         "3️⃣  You will see the number going up:\n"
#         "       ✈️ 1.20x → 1.85x → 2.43x → 3.10x...\n\n"
#         "4️⃣  Press *💰 CASH OUT NOW* at any time!\n\n"
#         "✅ *Example:*\n"
#         "       Bet 10 spins → cashout at 3x → WIN 30 spins!\n\n"
#         "💥 *If you wait too long — plane crashes!*\n"
#         "       You lose your bet. Cash out early!\n\n"
#         "📈 97% RTP — very good odds for you!\n"
#         "💸 Min cashout: 200 spins = $2.00",
#         parse_mode="Markdown",
#         reply_markup=InlineKeyboardMarkup(inline_keyboard=[
#             [InlineKeyboardButton(text="✈️ Play Now!", callback_data="play")],
#             [InlineKeyboardButton(text="🔙 Back",      callback_data="back_main")],
#         ])
#     )
#     await callback.answer()

# # ── Back to main ──────────────────────────────────────────
# @dp.callback_query(F.data == "back_main")
# async def back_main(callback: types.CallbackQuery):
#     uid = callback.from_user.id
#     u   = get_user(uid)
#     await callback.message.answer(
#         f"✈️ *Fortuno Aviator*\n"
#         f"💰 Your balance: *{u['spins']}* spins",
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
#         f"✈️ *Choose How Many Spins To Bet*\n"
#         f"━━━━━━━━━━━━━━━━━━━━━\n"
#         f"💰 Your balance: *{u['spins']}* spins\n"
#         f"Current bet: *{u.get('bet_size', 1)}* spin{'s' if u.get('bet_size',1) > 1 else ''}\n\n"
#         f"👇 Pick your bet then press 🚀 FLY NOW!",
#         parse_mode="Markdown",
#         reply_markup=bet_kb(uid)
#     )
#     await callback.answer()

# # ── Set Bet ───────────────────────────────────────────────
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
#         await callback.answer(
#             f"❌ Not enough spins! You need {bet} spins but you only have {u['spins']}.",
#             show_alert=True
#         )
#         return

#     # Deduct bet
#     u["spins"] -= bet
#     save_all()

#     # Generate secret crash point
#     crash_point = generate_crash_point()

#     # Send countdown
#     countdown_msg = await callback.message.answer(
#         f"✈️ *Get ready...*\n\n"
#         f"🎯 Bet: *{bet}* spins\n"
#         f"⏳ Plane is taking off in 3 seconds...\n\n"
#         f"👇 *Press CASH OUT the moment you want to stop!*",
#         parse_mode="Markdown"
#     )

#     await asyncio.sleep(1)
#     try:
#         await bot.edit_message_text(
#             chat_id=countdown_msg.chat.id,
#             message_id=countdown_msg.message_id,
#             text=(
#                 f"✈️ *Get ready...*\n\n"
#                 f"🎯 Bet: *{bet}* spins\n"
#                 f"⏳ Taking off in 2 seconds...\n\n"
#                 f"👇 *Press CASH OUT the moment you want to stop!*"
#             ),
#             parse_mode="Markdown"
#         )
#     except Exception:
#         pass

#     await asyncio.sleep(1)
#     try:
#         await bot.edit_message_text(
#             chat_id=countdown_msg.chat.id,
#             message_id=countdown_msg.message_id,
#             text=(
#                 f"✈️ *Get ready...*\n\n"
#                 f"🎯 Bet: *{bet}* spins\n"
#                 f"⏳ Taking off in 1 second...\n\n"
#                 f"👇 *Press CASH OUT the moment you want to stop!*"
#             ),
#             parse_mode="Markdown"
#         )
#     except Exception:
#         pass

#     await asyncio.sleep(1)

#     # Send the live game message
#     msg = await bot.send_message(
#         chat_id=callback.message.chat.id,
#         text=flying_text(bet, 1.00),
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

#     task = asyncio.create_task(run_game(uid))
#     active_games[uid]["task"] = task

#     await callback.answer()

# # ── Game Loop ─────────────────────────────────────────────
# async def run_game(uid: int):
#     try:
#         game  = active_games[uid]
#         u     = get_user(uid)
#         mult  = 1.00
#         crash = game["crash"]
#         bet   = game["bet"]

#         while mult < crash:
#             await asyncio.sleep(TICK_INTERVAL)

#             if game["cashed_out"]:
#                 return

#             # Multiplier grows — slower at first, faster as it climbs
#             if mult < 2.0:
#                 mult += random.uniform(0.08, 0.18)
#             elif mult < 5.0:
#                 mult += random.uniform(0.15, 0.35)
#             elif mult < 10.0:
#                 mult += random.uniform(0.30, 0.70)
#             else:
#                 mult += random.uniform(0.80, 2.50)

#             mult = round(min(mult, crash), 2)
#             game["multiplier"] = mult

#             # Update message every tick — 1 second so users can follow easily
#             try:
#                 await bot.edit_message_text(
#                     chat_id=game["chat_id"],
#                     message_id=game["msg_id"],
#                     text=flying_text(bet, mult),
#                     parse_mode="Markdown",
#                     reply_markup=cashout_kb()
#                 )
#             except Exception:
#                 pass

#         # ── CRASHED ───────────────────────────────────────
#         if not game["cashed_out"]:
#             game["cashed_out"] = True
#             today = str(date.today())

#             u["total_rounds_played"] = u.get("total_rounds_played", 0) + 1
#             u["total_lost"]          = u.get("total_lost", 0) + bet
#             stats["total_rounds_played"]        = stats.get("total_rounds_played", 0) + 1
#             stats["total_crashes"]              = stats.get("total_crashes", 0) + 1
#             stats["total_spins_lost"]           = stats.get("total_spins_lost", 0) + bet
#             stats["daily_rounds_played"][today] = stats["daily_rounds_played"].get(today, 0) + 1
#             save_all()

#             try:
#                 await bot.edit_message_text(
#                     chat_id=game["chat_id"],
#                     message_id=game["msg_id"],
#                     text=(
#                         f"💥 *CRASHED at {crash:.2f}x!*\n\n"
#                         f"😭 Too slow! The plane flew away!\n\n"
#                         f"🎯 You bet: *{bet}* spins\n"
#                         f"❌ You lost: *{bet}* spins\n"
#                         f"💰 Your balance: *{u['spins']}* spins\n\n"
#                         f"Try again — cash out faster next time! 💪"
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
#         logging.error(f"Game error for uid {uid}: {e}")
#         active_games.pop(uid, None)

# # ── Cashout ───────────────────────────────────────────────
# @dp.callback_query(F.data == "cashout")
# async def process_cashout(callback: types.CallbackQuery):
#     uid  = callback.from_user.id
#     game = active_games.get(uid)

#     if not game:
#         await callback.answer("⚠️ No active game. Press Play to start!", show_alert=True)
#         return

#     if game["cashed_out"]:
#         await callback.answer("💥 Too late! The plane already crashed!", show_alert=True)
#         return

#     game["cashed_out"] = True

#     if game["task"] and not game["task"].done():
#         game["task"].cancel()

#     mult     = game["multiplier"]
#     bet      = game["bet"]
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

#     plane = get_plane(mult)

#     try:
#         await bot.edit_message_text(
#             chat_id=game["chat_id"],
#             message_id=game["msg_id"],
#             text=(
#                 f"{plane} *YOU CASHED OUT!* 🎉\n\n"
#                 f"📈 Multiplier: *{mult:.2f}x*\n"
#                 f"🎯 You bet: *{bet}* spins\n"
#                 f"🏆 You won: *{winnings}* spins\n"
#                 f"📊 Profit: *+{profit}* spins\n\n"
#                 f"💰 Your balance: *{u['spins']}* spins\n\n"
#                 f"🔥 Well done! Play again?"
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
#             f"✅ *Cashed out at {mult:.2f}x!*\n"
#             f"Won *{winnings}* spins!\n"
#             f"💰 Balance: *{u['spins']}* spins",
#             parse_mode="Markdown",
#             reply_markup=main_kb(uid)
#         )

#     active_games.pop(uid, None)
#     await callback.answer(f"✅ Cashed out at {mult:.2f}x! You won {winnings} spins!")

# # ── My Stats ──────────────────────────────────────────────
# @dp.callback_query(F.data == "mystats")
# async def my_stats(callback: types.CallbackQuery):
#     uid   = callback.from_user.id
#     u     = get_user(uid)
#     await callback.message.answer(
#         f"📊 *Your Stats*\n"
#         f"━━━━━━━━━━━━━━━━━━━━━\n"
#         f"✈️ Rounds played: *{u.get('total_rounds_played', 0)}*\n"
#         f"💰 Balance: *{u['spins']}* spins\n"
#         f"🏆 Best win ever: *{u.get('biggest_win', 0)}* spins\n"
#         f"📈 Highest multiplier: *{u.get('highest_multiplier', 0.0):.2f}x*\n"
#         f"👥 Friends invited: *{u.get('referrals', 0)}*\n"
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
#         f"👥 *Invite Friends — Earn Free Spins!*\n"
#         f"━━━━━━━━━━━━━━━━━━━━━\n"
#         f"For every friend you invite → you get *+5 free spins!*\n\n"
#         f"🔗 Your invite link:\n`{link}`\n\n"
#         f"👫 Friends invited: *{u.get('referrals', 0)}*\n"
#         f"🎁 Free spins earned: *{u.get('referrals', 0) * 5}*\n\n"
#         f"Share your link now and earn! 💰",
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
#         need = MIN_WITHDRAW - u["spins"]
#         await callback.message.answer(
#             f"💸 *Withdraw*\n\n"
#             f"❌ You need at least *{MIN_WITHDRAW} spins* to withdraw.\n"
#             f"💰 Your balance: *{u['spins']}* spins\n"
#             f"📊 You need *{need}* more spins.\n\n"
#             f"Keep playing to reach {MIN_WITHDRAW} spins! 💪",
#             parse_mode="Markdown",
#             reply_markup=InlineKeyboardMarkup(inline_keyboard=[
#                 [InlineKeyboardButton(text="✈️ Play Now", callback_data="play")],
#                 [InlineKeyboardButton(text="💎 Buy Spins", callback_data="buy")],
#                 [InlineKeyboardButton(text="🔙 Back",      callback_data="back_main")],
#             ])
#         )
#         await callback.answer()
#         return

#     if u["pending_withdrawal"]:
#         await callback.message.answer(
#             f"⏳ *Withdrawal Pending*\n\n"
#             f"You already have a withdrawal request for *{u['pending_spins']}* spins.\n"
#             f"Please wait — admin will send your money within 24 hours.",
#             parse_mode="Markdown",
#             reply_markup=InlineKeyboardMarkup(inline_keyboard=[
#                 [InlineKeyboardButton(text="🔙 Back", callback_data="back_main")]
#             ])
#         )
#         await callback.answer()
#         return

#     await callback.message.answer(
#         f"💸 *Withdraw Your Winnings*\n\n"
#         f"💰 Your balance: *{u['spins']}* spins = {usd(u['spins'])} = {ton(u['spins'])} TON\n"
#         f"📌 Minimum: *{MIN_WITHDRAW} spins* = {usd(MIN_WITHDRAW)}\n\n"
#         f"Press the button below to request your withdrawal:",
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
#         f"💸 *How many spins do you want to withdraw?*\n\n"
#         f"Minimum: *{MIN_WITHDRAW}*\n"
#         f"Maximum: *{u['spins']}*\n\n"
#         f"👇 Type the number:",
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
#         await message.answer("❌ Please type a number only. Example: 200")
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
#         f"💳 *Enter your TON wallet address:*\n\n"
#         f"Example: `UQD...`\n\n"
#         f"👇 Paste your wallet address:",
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
#         await message.answer("❌ That wallet address looks wrong. Please try again.")
#         return

#     u["spins"]             -= amount
#     u["pending_withdrawal"] = True
#     u["pending_spins"]      = amount
#     u["pending_wallet"]     = wallet
#     save_all()
#     await state.clear()

#     await message.answer(
#         f"✅ *Withdrawal Request Sent!*\n\n"
#         f"💰 Amount: *{amount}* spins = {usd(amount)} = {ton(amount)} TON\n"
#         f"👛 Wallet: `{wallet}`\n\n"
#         f"⏳ Admin will send your money within 24 hours.\n"
#         f"Thank you for playing Fortuno Aviator! ✈️",
#         parse_mode="Markdown",
#         reply_markup=main_kb(uid)
#     )

#     try:
#         await bot.send_message(
#             ADMIN_ID,
#             f"💸 *NEW WITHDRAWAL — Fortuno Aviator*\n"
#             f"👤 User: `{uid}` · @{message.from_user.username or 'no username'}\n"
#             f"💰 {amount} spins = {usd(amount)} = {ton(amount)} TON\n"
#             f"👛 `{wallet}`\n\n"
#             f"/pay {uid} to approve\n"
#             f"/reject {uid} to reject",
#             parse_mode="Markdown"
#         )
#     except Exception:
#         pass

# # ── Admin: /admin ─────────────────────────────────────────
# @dp.message(Command("admin"))
# async def admin_dashboard(message: Message):
#     if message.from_user.id != ADMIN_ID:
#         return
#     today        = str(date.today())
#     dau          = len(stats["daily_active"].get(today, []))
#     new_p        = stats["daily_new_players"].get(today, 0)
#     rounds_today = stats["daily_rounds_played"].get(today, 0)
#     stars_today  = stats["daily_stars_spent"].get(today, 0)
#     dep_today    = len(stats["daily_depositors"].get(today, []))
#     purch_today  = stats["daily_purchases"].get(today, 0)

#     pending  = [(uid, ud) for uid, ud in user_data.items() if ud.get("pending_withdrawal")]
#     pend_txt = ""
#     for uid, ud in pending[:5]:
#         pend_txt += (
#             f"  • `{uid}` — {ud['pending_spins']} spins "
#             f"({usd(ud['pending_spins'])}) → `{ud['pending_wallet'][:12]}...`\n"
#         )
#     if not pend_txt:
#         pend_txt = "  None ✅\n"

#     await message.answer(
#         f"🛠 *Fortuno Aviator — Admin*\n"
#         f"━━━━━━━━━━━━━━━━━━━━━\n"
#         f"📅 *Today ({today})*\n"
#         f"  👥 Active: {dau} · 🆕 New: {new_p}\n"
#         f"  ✈️ Rounds: {rounds_today} · 💎 Purchases: {purch_today}\n"
#         f"  ⭐ Stars: {stars_today} · 💳 Depositors: {dep_today}\n\n"
#         f"📊 *All Time*\n"
#         f"  👥 Players: {stats['total_players']}\n"
#         f"  ✈️ Rounds: {stats['total_rounds_played']}\n"
#         f"  💰 Cashouts: {stats['total_cashouts']} · 💥 Crashes: {stats['total_crashes']}\n"
#         f"  🏆 Biggest win: {stats.get('biggest_win_ever', 0)} spins\n"
#         f"  📈 Highest mult: {stats.get('highest_multiplier', 0.0):.2f}x\n"
#         f"  💸 TON paid out: {stats['total_ton_paid']} TON\n\n"
#         f"⏳ *Pending Withdrawals*\n{pend_txt}",
#         parse_mode="Markdown"
#     )

# # ── Admin: /stats7 ────────────────────────────────────────
# @dp.message(Command("stats7"))
# async def stats7(message: Message):
#     if message.from_user.id != ADMIN_ID:
#         return
#     today = date.today()
#     lines = ["📈 *Last 7 Days — Fortuno Aviator*\n━━━━━━━━━━━━━━━━━━━━━"]
#     for i in range(7):
#         d     = str(today - datetime.timedelta(days=i))
#         dau   = len(stats["daily_active"].get(d, []))
#         new_p = stats["daily_new_players"].get(d, 0)
#         rnds  = stats["daily_rounds_played"].get(d, 0)
#         stars = stats["daily_stars_spent"].get(d, 0)
#         lines.append(f"  `{d}` — 👥{dau} · 🆕{new_p} · ✈️{rnds} · ⭐{stars}")
#     await message.answer("\n".join(lines), parse_mode="Markdown")

# # ── Admin: /pay ───────────────────────────────────────────
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
#         link   = pay_link(wallet, amount, f"FortunoAviator withdrawal {target_id}")
#         stats["total_ton_paid"]  = round(stats.get("total_ton_paid", 0) + amount, 4)
#         u["pending_withdrawal"]  = False
#         u["pending_spins"]       = 0
#         u["pending_wallet"]      = None
#         save_all()
#         await message.answer(
#             f"✅ Approved `{target_id}`\n"
#             f"💸 {spins} spins = {usd(spins)} = {amount} TON\n"
#             f"[👉 Open Tonkeeper]({link})",
#             parse_mode="Markdown"
#         )
#         try:
#             await bot.send_message(
#                 int(target_id),
#                 f"✅ *Your withdrawal has been approved!*\n\n"
#                 f"💸 {spins} spins = {usd(spins)} = {amount} TON\n"
#                 f"Your money is on the way! 🎉\n\n"
#                 f"Thanks for playing Fortuno Aviator ✈️",
#                 parse_mode="Markdown",
#                 reply_markup=main_kb(int(target_id))
#             )
#         except Exception:
#             pass
#     except (IndexError, ValueError):
#         await message.answer("❌ Usage: /pay [user_id]")

# # ── Admin: /reject ────────────────────────────────────────
# @dp.message(Command("reject"))
# async def admin_reject(message: Message):
#     if message.from_user.id != ADMIN_ID:
#         return
#     try:
#         target_id = str(int(message.text.split()[1]))
#         u         = user_data.get(target_id)
#         if not u or not u.get("pending_withdrawal"):
#             await message.answer("❌ No pending withdrawal.")
#             return
#         spins                   = u["pending_spins"]
#         u["spins"]             += spins
#         u["pending_withdrawal"] = False
#         u["pending_spins"]      = 0
#         u["pending_wallet"]     = None
#         save_all()
#         await message.answer(
#             f"✅ Rejected · returned {spins} spins to `{target_id}`.",
#             parse_mode="Markdown"
#         )
#         try:
#             await bot.send_message(
#                 int(target_id),
#                 f"❌ *Your withdrawal was rejected.*\n\n"
#                 f"💰 {spins} spins have been returned to your balance.\n"
#                 f"Please contact support if you have questions.",
#                 parse_mode="Markdown",
#                 reply_markup=main_kb(int(target_id))
#             )
#         except Exception:
#             pass
#     except (IndexError, ValueError):
#         await message.answer("❌ Usage: /reject [user_id]")

# # ── Admin: /gift ──────────────────────────────────────────
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
#         await message.answer(
#             f"🎁 Gifted *{amount}* spins to `{target_id}`.",
#             parse_mode="Markdown"
#         )
#         try:
#             await bot.send_message(
#                 int(target_id),
#                 f"🎁 *You received {amount} free spins!*\n\n"
#                 f"💰 Your balance: *{u['spins']}* spins\n"
#                 f"Good luck! ✈️",
#                 parse_mode="Markdown",
#                 reply_markup=main_kb(int(target_id))
#             )
#         except Exception:
#             pass
#     except (IndexError, ValueError):
#         await message.answer("❌ Usage: /gift [user_id] [amount]")

# # ── Admin: /userinfo ──────────────────────────────────────
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
#             f"✈️ Rounds played: *{u.get('total_rounds_played',0)}*\n"
#             f"🏆 Best win: *{u.get('biggest_win',0)}* spins\n"
#             f"📈 Highest mult: *{u.get('highest_multiplier',0.0):.2f}x*\n"
#             f"💎 Purchases: *{u.get('purchases',0)}* · Deposited: *{u.get('ever_deposited',False)}*\n"
#             f"👥 Friends invited: *{u.get('referrals',0)}*\n"
#             f"📅 Joined: {u.get('joined_date','N/A')} · 🚫 Banned: *{u.get('banned',False)}*\n"
#             f"⏳ Pending withdrawal: *{u.get('pending_withdrawal',False)}*\n"
#             f"💵 Held spins: *{u.get('pending_spins',0)}*\n"
#             f"👛 `{u.get('pending_wallet','None')}`",
#             parse_mode="Markdown",
#             reply_markup=InlineKeyboardMarkup(inline_keyboard=[
#                 [InlineKeyboardButton(text="🎁 Gift spins", callback_data=f"gift_menu_{target_id}")],
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

# # ── Admin: /ban /unban ────────────────────────────────────
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

# # ── Admin: /broadcast ─────────────────────────────────────
# @dp.message(Command("broadcast"))
# async def admin_broadcast(message: Message):
#     if message.from_user.id != ADMIN_ID:
#         return
#     try:
#         text = message.text.split(" ", 1)[1]
#     except IndexError:
#         await message.answer("❌ Usage: /broadcast [message]")
#         return
#     await message.answer("📢 Sending to all users...")
#     sent = failed = 0
#     for k in user_data:
#         if user_data[k].get("banned"):
#             continue
#         try:
#             await bot.send_message(
#                 int(k),
#                 f"📢 *Fortuno Aviator:*\n\n{text}",
#                 parse_mode="Markdown"
#             )
#             sent += 1
#             await asyncio.sleep(0.05)
#         except Exception:
#             failed += 1
#     await message.answer(
#         f"✅ Done!\nSent: *{sent}* · Failed: *{failed}*",
#         parse_mode="Markdown"
#     )

# # ── Buy Spins ─────────────────────────────────────────────
# @dp.callback_query(F.data == "buy")
# async def process_buy(callback: types.CallbackQuery):
#     await callback.message.answer(
#         f"💎 *Buy Spins*\n\n"
#         f"Minimum: *10 Stars* = 100 spins\n"
#         f"1 spin = $0.01 · 97% RTP\n\n"
#         f"👇 Pick your package:",
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
#             parse_mode="Markdown",
#             reply_markup=main_kb(uid)
#         )
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
#         f"✅ *+{spins} Spins added to your account!*\n\n"
#         f"💰 Your balance: *{u['spins']}* spins\n\n"
#         f"✈️ Go fly and win big! Good luck! 🔥",
#         parse_mode="Markdown",
#         reply_markup=main_kb(uid)
#     )

# # ── Main ──────────────────────────────────────────────────
# async def main():
#     logging.basicConfig(
#         level=logging.INFO,
#         format="%(asctime)s [%(levelname)s] %(message)s"
#     )
#     logging.info("Fortuno Aviator ✈️ is online!")
#     await dp.start_polling(bot)

# if __name__ == "__main__":
#     asyncio.run(main())

"""
Fortuno Aviator ✈️ — PRODUCTION VERSION
Install: pip install aiogram
Run:     python3 main.py
"""

import logging, asyncio, json, os, random, datetime
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

TOKEN             = "8605162590:AAGg7lk-K8fqedcpQP9w8JdHrbdVO2X39wQ"
ADMIN_ID          = 8612272966
ADMIN_WALLET      = "UQDlWJTEIwwGt7vai3T6s5MXgULmXk4ojhseU_UxxL7SY2DK"
SPIN_USD          = 0.01
SPIN_TO_TON       = 0.002
MIN_WITHDRAW      = 200
HOUSE_EDGE        = 0.03
BET_OPTIONS       = [1, 5, 10, 25, 50]
STAR_PACKAGES     = [(10,100,"Starter"),(25,250,"Popular ⭐"),(50,500,"Big Win"),(100,1000,"Whale 🐋")]
DATA_FILE         = "aviator_user_data.json"
STATS_FILE        = "aviator_stats.json"
BOT_NAME          = "FortunoAviatorBot"
DAILY_EARLY_BIRD_LIMIT = 5
DAILY_EARLY_BIRD_SPINS = 5
TICK_INTERVAL     = 1.0
MIN_STARS_TO_UNLOCK = 50
MIN_REFS_TO_UNLOCK  = 5

bot = Bot(token=TOKEN)
dp  = Dispatcher(storage=MemoryStorage())
active_games: dict = {}

class WithdrawStates(StatesGroup):
    waiting_amount = State()
    waiting_wallet = State()

def _load(fp):
    if os.path.exists(fp):
        try:
            with open(fp,"r",encoding="utf-8") as f: return json.load(f)
        except: pass
    return {}

def _save(data,fp):
    tmp=fp+".tmp"
    with open(tmp,"w",encoding="utf-8") as f: json.dump(data,f,ensure_ascii=False,indent=2)
    os.replace(tmp,fp)

user_data=_load(DATA_FILE); stats=_load(STATS_FILE)

if not stats:
    stats={"total_players":0,"total_spins_bought":0,"total_referrals":0,"total_rounds_played":0,
           "total_cashouts":0,"total_crashes":0,"total_spins_won":0,"total_spins_lost":0,
           "total_ton_paid":0.0,"total_depositors":0,"daily_active":{},"daily_first_five":{},
           "daily_new_players":{},"daily_purchases":{},"daily_depositors":{},"daily_stars_spent":{},
           "daily_rounds_played":{},"daily_revenue_spins":{},"biggest_win_ever":0,"highest_multiplier":0.0}

for k,v in {"total_depositors":0,"daily_first_five":{},"daily_new_players":{},"daily_purchases":{},
            "daily_depositors":{},"daily_stars_spent":{},"daily_rounds_played":{},"daily_revenue_spins":{},
            "biggest_win_ever":0,"highest_multiplier":0.0}.items():
    if k not in stats: stats[k]=v

def save_all(): _save(user_data,DATA_FILE); _save(stats,STATS_FILE)

def get_user(uid):
    k=str(uid)
    if k not in user_data:
        user_data[k]={"spins":0,"ever_started":False,"pending_withdrawal":False,"pending_spins":0,
                      "pending_wallet":None,"referrals":0,"referred_by":None,"joined_date":str(date.today()),
                      "total_rounds_played":0,"total_won":0,"total_lost":0,"purchases":0,
                      "total_stars_spent":0,"ever_deposited":False,"banned":False,"bet_size":1,
                      "biggest_win":0,"highest_multiplier":0.0}
        stats["total_players"]+=1
        today=str(date.today())
        stats["daily_new_players"][today]=stats["daily_new_players"].get(today,0)+1
        save_all()
    u=user_data[k]
    if "ever_deposited" not in u: u["ever_deposited"]=u.get("purchases",0)>0
    if "total_stars_spent" not in u: u["total_stars_spent"]=0
    return u

def track_daily(uid):
    today=str(date.today())
    if today not in stats["daily_active"]: stats["daily_active"][today]=[]
    k=str(uid)
    if k not in stats["daily_active"][today]: stats["daily_active"][today].append(k)

def check_early_bird(uid):
    today=str(date.today()); winners=stats["daily_first_five"].setdefault(today,[]); k=str(uid)
    if k in winners or len(winners)>=DAILY_EARLY_BIRD_LIMIT: return False
    winners.append(k); get_user(uid)["spins"]+=DAILY_EARLY_BIRD_SPINS; save_all(); return True

def is_withdraw_unlocked(u):
    return u.get("total_stars_spent",0)>=MIN_STARS_TO_UNLOCK or u.get("referrals",0)>=MIN_REFS_TO_UNLOCK

def usd(s): return f"${s*SPIN_USD:.2f}"
def ton(s): return round(s*SPIN_TO_TON,4)
def pay_link(addr,amt,comment):
    nano=int(amt*1_000_000_000)
    return f"https://app.tonkeeper.com/transfer/{addr}?amount={nano}&text={quote(comment)}"

def generate_crash_point():
    r=random.random()
    if r<HOUSE_EDGE: return 1.00
    r2=random.random(); crash=1.0/(1.0-r2*(1.0-HOUSE_EDGE))
    return round(max(1.01,min(crash,200.0)),2)

def get_plane(m):
    if m<2.0: return "✈️"
    elif m<5.0: return "🛫"
    elif m<10.0: return "🚀"
    else: return "🛸"

def get_mood(m):
    if m<1.5: return "Just took off... 👀"
    elif m<2.0: return "Flying steady... 😏"
    elif m<3.0: return "Going higher! 😮"
    elif m<5.0: return "Getting risky... 😬"
    elif m<10.0: return "Very high now! 😱"
    else: return "INSANE height!! 🤑"

def danger_bar(mult,crash):
    BAR=10
    pct=max(0.0,min((mult-1.0)/(crash-1.0),1.0)) if crash>1.0 else 1.0
    red=int(round(pct*BAR)); green=BAR-red
    bar="🟩"*green+"🟥"*red
    if pct<0.3: lbl="SAFE ZONE ✅"
    elif pct<0.6: lbl="BE CAREFUL ⚠️"
    elif pct<0.85: lbl="DANGER! 🔴"
    else: lbl="CRASH COMING!! 💥"
    return f"{bar}\n{lbl}"

def flying_text(bet,mult,crash):
    return (f"{get_plane(mult)}  *{mult:.2f}x*  —  {get_mood(mult)}\n\n"
            f"{danger_bar(mult,crash)}\n\n"
            f"🎯 Bet: *{bet}* spins\n"
            f"💵 Cashout now = *{round(bet*mult)}* spins\n\n"
            f"⬇️ Press the button before it crashes!")

def main_kb(uid):
    u=get_user(uid)
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"✈️ PLAY  |  💰 {u['spins']} spins",callback_data="play")],
        [InlineKeyboardButton(text="💎 Buy Spins",callback_data="buy"),
         InlineKeyboardButton(text="💸 Withdraw",callback_data="withdraw")],
        [InlineKeyboardButton(text="📊 My Stats",callback_data="mystats"),
         InlineKeyboardButton(text="👥 Referral",callback_data="referral")],
        [InlineKeyboardButton(text="ℹ️ How to Play",callback_data="howtoplay")]])

def bet_kb(uid):
    u=get_user(uid); current=u.get("bet_size",1); rows=[]; row=[]
    for b in BET_OPTIONS:
        lbl=f"✅ {b}" if b==current else str(b)
        row.append(InlineKeyboardButton(text=f"{lbl} spin{'s' if b>1 else ''}",callback_data=f"setbet_{b}"))
        if len(row)==3: rows.append(row); row=[]
    if row: rows.append(row)
    rows.append([InlineKeyboardButton(text="🚀 FLY NOW!",callback_data="startgame")])
    rows.append([InlineKeyboardButton(text="🔙 Back",callback_data="back_main")])
    return InlineKeyboardMarkup(inline_keyboard=rows)

def cashout_kb():
    return InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="💰  CASH OUT NOW!  💰",callback_data="cashout")]])

def buy_kb():
    rows=[[InlineKeyboardButton(text=f"{l} — {sp} spins ({st} ⭐)",callback_data=f"buypack_{st}_{sp}")] for st,sp,l in STAR_PACKAGES]
    rows.append([InlineKeyboardButton(text="🔙 Back",callback_data="back_main")])
    return InlineKeyboardMarkup(inline_keyboard=rows)

@dp.message(Command("start"))
async def cmd_start(message: Message):
    uid=message.from_user.id; u=get_user(uid); args=message.text.split()
    if u.get("banned"): await message.answer("🚫 You are banned."); return
    track_daily(uid)
    if len(args)>1 and not u["ever_started"]:
        try:
            ref_id=int(args[1])
            if ref_id!=uid and not u.get("referred_by"):
                ru=get_user(ref_id); ru["spins"]+=5; ru["referrals"]+=1; u["referred_by"]=ref_id
                stats["total_referrals"]+=1; save_all()
                try: await bot.send_message(ref_id,f"🎉 *+5 spins!* Your friend joined!\n💰 Balance: *{ru['spins']}* spins\n👥 Referrals: *{ru['referrals']}*/{MIN_REFS_TO_UNLOCK}",parse_mode="Markdown")
                except: pass
        except: pass
    early=check_early_bird(uid); u["ever_started"]=True; save_all()
    em="\n🎁 *Early bird bonus: +5 free spins!*" if early else ""
    await message.answer(f"✈️ *Welcome to Fortuno Aviator!*\n━━━━━━━━━━━━━━━━━━━━━\n🎮 Watch the plane fly — cash out before it crashes!\n💰 Your balance: *{u['spins']}* spins{em}\n\nWhat do you want to do? 👇",parse_mode="Markdown",reply_markup=main_kb(uid))

@dp.callback_query(F.data=="howtoplay")
async def howtoplay(cb: types.CallbackQuery):
    await cb.message.answer("✈️ *How To Play — Very Simple!*\n━━━━━━━━━━━━━━━━━━━━━\n\n1️⃣ Press *PLAY* and choose your bet\n2️⃣ Press *🚀 FLY NOW!* — plane takes off!\n3️⃣ Watch multiplier go up: 1.20x → 2x → 5x...\n4️⃣ Watch safety bar:\n   🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩 = Safe\n   🟩🟩🟩🟩🟩🟥🟥🟥🟥🟥 = Risky!\n   🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥 = CRASH SOON!\n5️⃣ Press *💰 CASH OUT NOW* before all red!\n\n✅ Bet 10 spins → cashout at 3x → WIN 30 spins!\n💥 Bar goes full red = plane crashes = you lose!\n\n📈 97% RTP\n💸 Min withdraw: 200 spins = $2.00\n🔓 Unlock withdraw: spend 50 Stars OR invite 5 friends",parse_mode="Markdown",reply_markup=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="✈️ Play Now!",callback_data="play")],[InlineKeyboardButton(text="🔙 Back",callback_data="back_main")]]))
    await cb.answer()

@dp.callback_query(F.data=="back_main")
async def back_main(cb: types.CallbackQuery):
    u=get_user(cb.from_user.id)
    await cb.message.answer(f"✈️ *Fortuno Aviator*\n💰 Your balance: *{u['spins']}* spins",parse_mode="Markdown",reply_markup=main_kb(cb.from_user.id))
    await cb.answer()

@dp.callback_query(F.data=="play")
async def process_play(cb: types.CallbackQuery):
    uid=cb.from_user.id; u=get_user(uid)
    if u.get("banned"): await cb.answer("🚫 You are banned.",show_alert=True); return
    if uid in active_games: await cb.answer("⚠️ Game already running!",show_alert=True); return
    track_daily(uid)
    await cb.message.answer(f"✈️ *Choose Your Bet*\n━━━━━━━━━━━━━━━━\n💰 Balance: *{u['spins']}* spins\nCurrent bet: *{u.get('bet_size',1)}* spins\n\n👇 Pick bet then press 🚀 FLY NOW!",parse_mode="Markdown",reply_markup=bet_kb(uid))
    await cb.answer()

@dp.callback_query(F.data.startswith("setbet_"))
async def set_bet(cb: types.CallbackQuery):
    uid=cb.from_user.id; u=get_user(uid); bet=int(cb.data.split("_")[1])
    u["bet_size"]=bet; save_all()
    await cb.message.edit_reply_markup(reply_markup=bet_kb(uid))
    await cb.answer(f"✅ Bet set to {bet} spins!")

@dp.callback_query(F.data=="startgame")
async def start_game(cb: types.CallbackQuery):
    uid=cb.from_user.id; u=get_user(uid)
    if u.get("banned"): await cb.answer("🚫 You are banned.",show_alert=True); return
    if uid in active_games: await cb.answer("⚠️ Game already running!",show_alert=True); return
    bet=u.get("bet_size",1)
    if u["spins"]<bet: await cb.answer(f"❌ Need {bet} spins, have {u['spins']}.",show_alert=True); return
    u["spins"]-=bet; save_all()
    crash_point=generate_crash_point()
    cm=await cb.message.answer(f"✈️ *Plane is taking off!*\n\n🎯 Bet: *{bet}* spins\n⏳ *3...*\n\nReady your finger! 👇",parse_mode="Markdown")
    for i in [2,1]:
        await asyncio.sleep(1)
        try: await bot.edit_message_text(chat_id=cm.chat.id,message_id=cm.message_id,text=f"✈️ *Plane is taking off!*\n\n🎯 Bet: *{bet}* spins\n⏳ *{i}...*\n\nReady your finger! 👇",parse_mode="Markdown")
        except: pass
    await asyncio.sleep(1)
    msg=await bot.send_message(chat_id=cb.message.chat.id,text=flying_text(bet,1.00,crash_point),parse_mode="Markdown",reply_markup=cashout_kb())
    active_games[uid]={"bet":bet,"crash":crash_point,"multiplier":1.00,"msg_id":msg.message_id,"chat_id":cb.message.chat.id,"cashed_out":False,"task":None}
    active_games[uid]["task"]=asyncio.create_task(run_game(uid))
    await cb.answer()

async def run_game(uid):
    try:
        game=active_games[uid]; u=get_user(uid); mult=1.00; crash=game["crash"]; bet=game["bet"]
        while mult<crash:
            await asyncio.sleep(TICK_INTERVAL)
            if game["cashed_out"]: return
            if mult<2.0: mult+=random.uniform(0.08,0.18)
            elif mult<5.0: mult+=random.uniform(0.15,0.35)
            elif mult<10.0: mult+=random.uniform(0.30,0.70)
            else: mult+=random.uniform(0.80,2.50)
            mult=round(min(mult,crash),2); game["multiplier"]=mult
            try: await bot.edit_message_text(chat_id=game["chat_id"],message_id=game["msg_id"],text=flying_text(bet,mult,crash),parse_mode="Markdown",reply_markup=cashout_kb())
            except: pass
        if not game["cashed_out"]:
            game["cashed_out"]=True; today=str(date.today())
            u["total_rounds_played"]=u.get("total_rounds_played",0)+1; u["total_lost"]=u.get("total_lost",0)+bet
            stats["total_rounds_played"]=stats.get("total_rounds_played",0)+1
            stats["total_crashes"]=stats.get("total_crashes",0)+1
            stats["total_spins_lost"]=stats.get("total_spins_lost",0)+bet
            stats["daily_rounds_played"][today]=stats["daily_rounds_played"].get(today,0)+1; save_all()
            try: await bot.edit_message_text(chat_id=game["chat_id"],message_id=game["msg_id"],text=f"💥 *CRASHED at {crash:.2f}x!*\n\n🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥\nTOO LATE! 😭\n\n🎯 Bet: *{bet}* spins\n❌ Lost: *{bet}* spins\n💰 Balance: *{u['spins']}* spins\n\nCash out faster next time! 💪",parse_mode="Markdown",reply_markup=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="✈️ Play Again",callback_data="play")],[InlineKeyboardButton(text="💎 Buy Spins",callback_data="buy")]]))
            except: pass
            active_games.pop(uid,None)
    except asyncio.CancelledError: pass
    except Exception as e: logging.error(f"Game error {uid}: {e}"); active_games.pop(uid,None)

@dp.callback_query(F.data=="cashout")
async def process_cashout(cb: types.CallbackQuery):
    uid=cb.from_user.id; game=active_games.get(uid)
    if not game: await cb.answer("⚠️ No active game!",show_alert=True); return
    if game["cashed_out"]: await cb.answer("💥 Too late! Already crashed!",show_alert=True); return
    game["cashed_out"]=True
    if game["task"] and not game["task"].done(): game["task"].cancel()
    mult=game["multiplier"]; bet=game["bet"]; winnings=round(bet*mult); profit=winnings-bet
    u=get_user(uid); u["spins"]+=winnings; u["total_rounds_played"]=u.get("total_rounds_played",0)+1; u["total_won"]=u.get("total_won",0)+winnings
    if winnings>u.get("biggest_win",0): u["biggest_win"]=winnings
    if winnings>stats.get("biggest_win_ever",0): stats["biggest_win_ever"]=winnings
    if mult>u.get("highest_multiplier",0.0): u["highest_multiplier"]=mult
    if mult>stats.get("highest_multiplier",0.0): stats["highest_multiplier"]=mult
    today=str(date.today())
    stats["total_rounds_played"]=stats.get("total_rounds_played",0)+1
    stats["total_cashouts"]=stats.get("total_cashouts",0)+1
    stats["total_spins_won"]=stats.get("total_spins_won",0)+winnings
    stats["daily_rounds_played"][today]=stats["daily_rounds_played"].get(today,0)+1; save_all()
    try: await bot.edit_message_text(chat_id=game["chat_id"],message_id=game["msg_id"],text=f"{get_plane(mult)} *YOU CASHED OUT!* 🎉\n\n🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩\nPERFECT TIMING! ✅\n\n📈 Multiplier: *{mult:.2f}x*\n🎯 Bet: *{bet}* spins\n🏆 Won: *{winnings}* spins\n📊 Profit: *+{profit}* spins\n\n💰 Balance: *{u['spins']}* spins\n\n🔥 Well done!",parse_mode="Markdown",reply_markup=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="✈️ Play Again",callback_data="play")],[InlineKeyboardButton(text="💸 Withdraw",callback_data="withdraw")]]))
    except: await bot.send_message(game["chat_id"],f"✅ Cashed out at {mult:.2f}x! Won {winnings} spins!\n💰 Balance: {u['spins']} spins",reply_markup=main_kb(uid))
    active_games.pop(uid,None); await cb.answer(f"✅ Cashed out at {mult:.2f}x!")

@dp.callback_query(F.data=="mystats")
async def my_stats(cb: types.CallbackQuery):
    uid=cb.from_user.id; u=get_user(uid)
    stars=u.get("total_stars_spent",0); refs=u.get("referrals",0); unlocked=is_withdraw_unlocked(u)
    if unlocked: lock="✅ Withdrawal UNLOCKED!"
    else: lock=f"🔒 Locked — need {MIN_STARS_TO_UNLOCK-stars} more Stars OR {MIN_REFS_TO_UNLOCK-refs} more friends"
    await cb.message.answer(f"📊 *Your Stats*\n━━━━━━━━━━━━━━━━━━━━━\n✈️ Rounds: *{u.get('total_rounds_played',0)}*\n💰 Balance: *{u['spins']}* spins\n🏆 Best win: *{u.get('biggest_win',0)}* spins\n📈 Highest mult: *{u.get('highest_multiplier',0.0):.2f}x*\n⭐ Stars spent: *{stars}*/{MIN_STARS_TO_UNLOCK}\n👥 Friends invited: *{refs}*/{MIN_REFS_TO_UNLOCK}\n📅 Since: {u.get('joined_date','N/A')}\n\n{lock}",parse_mode="Markdown",reply_markup=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="🔙 Back",callback_data="back_main")]]))
    await cb.answer()

@dp.callback_query(F.data=="referral")
async def referral_menu(cb: types.CallbackQuery):
    uid=cb.from_user.id; u=get_user(uid); refs=u.get("referrals",0)
    link=f"https://t.me/{BOT_NAME}?start={uid}"; need=max(0,MIN_REFS_TO_UNLOCK-refs)
    status="✅ Withdrawal unlocked via referrals!" if refs>=MIN_REFS_TO_UNLOCK else f"⚠️ Invite *{need}* more friends to unlock withdrawal!"
    await cb.message.answer(f"👥 *Invite Friends — Earn Free Spins!*\n━━━━━━━━━━━━━━━━━━━━━\nFor every friend → *+5 free spins!*\n\n🔗 Your link:\n`{link}`\n\n👫 Friends invited: *{refs}*/{MIN_REFS_TO_UNLOCK}\n🎁 Spins earned: *{refs*5}*\n\n{status}",parse_mode="Markdown",reply_markup=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="🔙 Back",callback_data="back_main")]]))
    await cb.answer()

@dp.callback_query(F.data=="withdraw")
async def withdraw_menu(cb: types.CallbackQuery):
    uid=cb.from_user.id; u=get_user(uid)
    if not is_withdraw_unlocked(u):
        stars=u.get("total_stars_spent",0); refs=u.get("referrals",0)
        await cb.message.answer(
            f"🔒 *Withdrawal Locked*\n━━━━━━━━━━━━━━━━━━━━━\n\nTo unlock choose ONE:\n\n"
            f"💎 *Option 1 — Deposit:*\n   Spend *{MIN_STARS_TO_UNLOCK} Stars* ($0.50)\n   You spent: *{stars}*/{MIN_STARS_TO_UNLOCK} Stars\n   Need *{MIN_STARS_TO_UNLOCK-stars}* more Stars\n\n"
            f"👥 *Option 2 — Invite Friends:*\n   Invite *{MIN_REFS_TO_UNLOCK} friends*\n   You invited: *{refs}*/{MIN_REFS_TO_UNLOCK} friends\n   Need *{max(0,MIN_REFS_TO_UNLOCK-refs)}* more friends\n\n"
            f"Complete one to unlock! 🔓",
            parse_mode="Markdown",reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="💎 Deposit to Unlock!",callback_data="buy")],
                [InlineKeyboardButton(text="👥 Invite to Unlock!",callback_data="referral")],
                [InlineKeyboardButton(text="🔙 Back",callback_data="back_main")]]))
        await cb.answer(); return
    if u["spins"]<MIN_WITHDRAW:
        await cb.message.answer(f"💸 *Withdraw*\n\n❌ Need *{MIN_WITHDRAW} spins* minimum.\n💰 Balance: *{u['spins']}* spins\nNeed *{MIN_WITHDRAW-u['spins']}* more.",parse_mode="Markdown",reply_markup=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="✈️ Play Now",callback_data="play")],[InlineKeyboardButton(text="💎 Buy Spins",callback_data="buy")],[InlineKeyboardButton(text="🔙 Back",callback_data="back_main")]]))
        await cb.answer(); return
    if u["pending_withdrawal"]:
        await cb.message.answer(f"⏳ *Withdrawal Pending*\n\nYou requested *{u['pending_spins']}* spins.\nAdmin will pay within 24h.",parse_mode="Markdown",reply_markup=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="🔙 Back",callback_data="back_main")]]))
        await cb.answer(); return
    await cb.message.answer(f"💸 *Withdraw Your Winnings*\n\n💰 Balance: *{u['spins']}* spins = {usd(u['spins'])} = {ton(u['spins'])} TON\n📌 Minimum: *{MIN_WITHDRAW} spins*\n\nPress below:",parse_mode="Markdown",reply_markup=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="💸 Request Withdrawal",callback_data="withdraw_start")],[InlineKeyboardButton(text="🔙 Back",callback_data="back_main")]]))
    await cb.answer()

@dp.callback_query(F.data=="withdraw_start")
async def withdraw_start(cb: types.CallbackQuery,state: FSMContext):
    u=get_user(cb.from_user.id); await state.set_state(WithdrawStates.waiting_amount)
    await cb.message.answer(f"💸 How many spins?\nMin: *{MIN_WITHDRAW}* · Max: *{u['spins']}*\n\n👇 Type the number:",parse_mode="Markdown"); await cb.answer()

@dp.message(WithdrawStates.waiting_amount)
async def withdraw_amount(message: Message,state: FSMContext):
    uid=message.from_user.id; u=get_user(uid)
    try: amount=int(message.text.strip())
    except: await message.answer("❌ Type a number. Example: 200"); return
    if amount<MIN_WITHDRAW: await message.answer(f"❌ Minimum is {MIN_WITHDRAW} spins."); return
    if amount>u["spins"]: await message.answer(f"❌ You only have {u['spins']} spins."); return
    await state.update_data(amount=amount); await state.set_state(WithdrawStates.waiting_wallet)
    await message.answer("💳 Enter your TON wallet address:\n\nExample: `UQD...`\n\n👇 Paste it:",parse_mode="Markdown")

@dp.message(WithdrawStates.waiting_wallet)
async def withdraw_wallet(message: Message,state: FSMContext):
    uid=message.from_user.id; u=get_user(uid); wallet=message.text.strip(); data=await state.get_data(); amount=data["amount"]
    if len(wallet)<10: await message.answer("❌ Wrong wallet. Try again."); return
    u["spins"]-=amount; u["pending_withdrawal"]=True; u["pending_spins"]=amount; u["pending_wallet"]=wallet; save_all(); await state.clear()
    await message.answer(f"✅ *Withdrawal Sent!*\n\n💰 {amount} spins = {usd(amount)} = {ton(amount)} TON\n👛 `{wallet}`\n\n⏳ Admin pays within 24h. Thank you! ✈️",parse_mode="Markdown",reply_markup=main_kb(uid))
    try: await bot.send_message(ADMIN_ID,f"💸 *NEW WITHDRAWAL*\n👤 `{uid}` · @{message.from_user.username or 'no username'}\n💰 {amount} spins = {usd(amount)} = {ton(amount)} TON\n👛 `{wallet}`\n\n/pay {uid} to approve\n/reject {uid} to reject",parse_mode="Markdown")
    except: pass

@dp.message(Command("admin"))
async def admin_dashboard(message: Message):
    if message.from_user.id!=ADMIN_ID: return
    today=str(date.today())
    dau=len(stats["daily_active"].get(today,[])); new_p=stats["daily_new_players"].get(today,0)
    rt=stats["daily_rounds_played"].get(today,0); st=stats["daily_stars_spent"].get(today,0)
    pending=[(uid,ud) for uid,ud in user_data.items() if ud.get("pending_withdrawal")]
    ptxt="".join(f"  • `{uid}` — {ud['pending_spins']} spins → `{ud['pending_wallet'][:12]}...`\n" for uid,ud in pending[:5]) or "  None ✅\n"
    await message.answer(f"🛠 *Fortuno Aviator — Admin*\n━━━━━━━━━━━━━━━━━━━━━\n📅 Today: 👥{dau} active · 🆕{new_p} new · ✈️{rt} rounds · ⭐{st} stars\n\n📊 All Time\n  👥 {stats['total_players']} players · ✈️ {stats.get('total_rounds_played',0)} rounds\n  💰 {stats.get('total_cashouts',0)} cashouts · 💥 {stats.get('total_crashes',0)} crashes\n  🏆 Biggest win: {stats.get('biggest_win_ever',0)} spins\n  📈 Highest mult: {stats.get('highest_multiplier',0.0):.2f}x\n  💸 TON paid: {stats['total_ton_paid']}\n\n⏳ Pending:\n{ptxt}",parse_mode="Markdown")

@dp.message(Command("stats7"))
async def stats7(message: Message):
    if message.from_user.id!=ADMIN_ID: return
    today=date.today(); lines=["📈 *Last 7 Days*\n━━━━━━━━━━━━━━━━━━━━━"]
    for i in range(7):
        d=str(today-datetime.timedelta(days=i))
        lines.append(f"  `{d}` — 👥{len(stats['daily_active'].get(d,[]))} · 🆕{stats['daily_new_players'].get(d,0)} · ✈️{stats['daily_rounds_played'].get(d,0)} · ⭐{stats['daily_stars_spent'].get(d,0)}")
    await message.answer("\n".join(lines),parse_mode="Markdown")

@dp.message(Command("pay"))
async def admin_pay(message: Message):
    if message.from_user.id!=ADMIN_ID: return
    try:
        tid=str(int(message.text.split()[1])); u=user_data.get(tid)
        if not u or not u.get("pending_withdrawal"): await message.answer("❌ No pending withdrawal."); return
        spins=u["pending_spins"]; wallet=u["pending_wallet"]; amt=ton(spins); link=pay_link(wallet,amt,f"FortunoAviator {tid}")
        stats["total_ton_paid"]=round(stats.get("total_ton_paid",0)+amt,4)
        u["pending_withdrawal"]=False; u["pending_spins"]=0; u["pending_wallet"]=None; save_all()
        await message.answer(f"✅ Approved `{tid}`\n💸 {spins} spins = {usd(spins)} = {amt} TON\n[👉 Open Tonkeeper]({link})",parse_mode="Markdown")
        try: await bot.send_message(int(tid),f"✅ *Withdrawal Approved!*\n💸 {spins} spins = {usd(spins)} = {amt} TON sent!\nThanks for playing! ✈️",parse_mode="Markdown",reply_markup=main_kb(int(tid)))
        except: pass
    except: await message.answer("❌ Usage: /pay [user_id]")

@dp.message(Command("reject"))
async def admin_reject(message: Message):
    if message.from_user.id!=ADMIN_ID: return
    try:
        tid=str(int(message.text.split()[1])); u=user_data.get(tid)
        if not u or not u.get("pending_withdrawal"): await message.answer("❌ No pending withdrawal."); return
        spins=u["pending_spins"]; u["spins"]+=spins; u["pending_withdrawal"]=False; u["pending_spins"]=0; u["pending_wallet"]=None; save_all()
        await message.answer(f"✅ Rejected · returned {spins} spins to `{tid}`.",parse_mode="Markdown")
        try: await bot.send_message(int(tid),f"❌ *Withdrawal Rejected*\n💰 {spins} spins returned.",parse_mode="Markdown",reply_markup=main_kb(int(tid)))
        except: pass
    except: await message.answer("❌ Usage: /reject [user_id]")

@dp.message(Command("gift"))
async def admin_gift(message: Message):
    if message.from_user.id!=ADMIN_ID: return
    try:
        p=message.text.split(); tid=str(int(p[1])); amt=int(p[2]); u=get_user(int(tid)); u["spins"]+=amt; save_all()
        await message.answer(f"🎁 Gifted *{amt}* spins to `{tid}`.",parse_mode="Markdown")
        try: await bot.send_message(int(tid),f"🎁 *You received {amt} free spins!*\n💰 Balance: *{u['spins']}* spins",parse_mode="Markdown",reply_markup=main_kb(int(tid)))
        except: pass
    except: await message.answer("❌ Usage: /gift [user_id] [amount]")

@dp.message(Command("userinfo"))
async def admin_userinfo(message: Message):
    if message.from_user.id!=ADMIN_ID: return
    try:
        tid=str(int(message.text.split()[1])); u=user_data.get(tid)
        if not u: await message.answer("❌ User not found."); return
        unlocked=is_withdraw_unlocked(u)
        await message.answer(f"👤 *USER INFO* · `{tid}`\n━━━━━━━━━━━━━━━━━━━━\n💰 *{u.get('spins',0)}* spins · {usd(u.get('spins',0))} · {ton(u.get('spins',0))} TON\n✈️ Rounds: *{u.get('total_rounds_played',0)}*\n🏆 Best win: *{u.get('biggest_win',0)}* spins\n📈 Highest mult: *{u.get('highest_multiplier',0.0):.2f}x*\n⭐ Stars spent: *{u.get('total_stars_spent',0)}*/{MIN_STARS_TO_UNLOCK}\n👥 Referrals: *{u.get('referrals',0)}*/{MIN_REFS_TO_UNLOCK}\n🔓 Withdraw: *{'YES ✅' if unlocked else 'LOCKED 🔒'}*\n💎 Purchases: *{u.get('purchases',0)}*\n📅 Joined: {u.get('joined_date','N/A')} · 🚫 Banned: *{u.get('banned',False)}*\n⏳ Pending: *{u.get('pending_withdrawal',False)}* · Held: *{u.get('pending_spins',0)}*\n👛 `{u.get('pending_wallet','None')}`",parse_mode="Markdown",reply_markup=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="🎁 Gift spins",callback_data=f"gift_menu_{tid}")],[InlineKeyboardButton(text=f"{'✅ Unban' if u.get('banned') else '🚫 Ban'} user",callback_data=f"toggle_ban_{tid}")]]))
    except: await message.answer("❌ Usage: /userinfo [user_id]")

@dp.callback_query(F.data.startswith("toggle_ban_"))
async def toggle_ban(cb: types.CallbackQuery):
    if cb.from_user.id!=ADMIN_ID: await cb.answer("❌ Not authorized.",show_alert=True); return
    tid=cb.data.replace("toggle_ban_",""); u=user_data.get(tid)
    if not u: await cb.answer("❌ Not found.",show_alert=True); return
    u["banned"]=not u.get("banned",False); save_all()
    await cb.answer(f"{"🚫 Banned" if u["banned"] else "✅ Unbanned"} {tid}",show_alert=True)

@dp.message(Command("ban"))
async def admin_ban(message: Message):
    if message.from_user.id!=ADMIN_ID: return
    try: tid=str(int(message.text.split()[1])); get_user(int(tid))["banned"]=True; save_all(); await message.answer(f"🚫 Banned `{tid}`.",parse_mode="Markdown")
    except: await message.answer("❌ Usage: /ban [user_id]")

@dp.message(Command("unban"))
async def admin_unban(message: Message):
    if message.from_user.id!=ADMIN_ID: return
    try: tid=str(int(message.text.split()[1])); get_user(int(tid))["banned"]=False; save_all(); await message.answer(f"✅ Unbanned `{tid}`.",parse_mode="Markdown")
    except: await message.answer("❌ Usage: /unban [user_id]")

@dp.message(Command("broadcast"))
async def admin_broadcast(message: Message):
    if message.from_user.id!=ADMIN_ID: return
    try: text=message.text.split(" ",1)[1]
    except: await message.answer("❌ Usage: /broadcast [message]"); return
    await message.answer("📢 Sending..."); sent=failed=0
    for k in user_data:
        if user_data[k].get("banned"): continue
        try: await bot.send_message(int(k),f"📢 *Fortuno Aviator:*\n\n{text}",parse_mode="Markdown"); sent+=1; await asyncio.sleep(0.05)
        except: failed+=1
    await message.answer(f"✅ Sent: *{sent}* · Failed: *{failed}*",parse_mode="Markdown")

@dp.callback_query(F.data=="buy")
async def process_buy(cb: types.CallbackQuery):
    await cb.message.answer(f"💎 *Buy Spins*\n\nMin: *10 Stars* = 100 spins\n💡 Spend *{MIN_STARS_TO_UNLOCK} Stars* to unlock withdrawal!\n\n👇 Pick package:",parse_mode="Markdown",reply_markup=buy_kb()); await cb.answer()

@dp.callback_query(F.data.startswith("buypack_"))
async def process_buypack(cb: types.CallbackQuery):
    try: p=cb.data.split("_"); stars=int(p[1]); spins=int(p[2])
    except: await cb.answer("❌ Invalid.",show_alert=True); return
    lbl=next((l for s,sp,l in STAR_PACKAGES if s==stars and sp==spins),"Spins")
    await bot.send_invoice(cb.message.chat.id,title=f"{lbl} — {spins} Spins",description=f"{spins} spins · 97% RTP · TON payouts",payload=f"buy_{stars}_{spins}",provider_token="",currency="XTR",prices=[LabeledPrice(label=f"{spins} Spins",amount=stars)])
    await cb.answer()

@dp.pre_checkout_query()
async def pre_check(q: PreCheckoutQuery):
    try:
        p=q.invoice_payload.split("_")
        if p[0]!="buy": raise ValueError
        valid=any(s==int(p[1]) and sp==int(p[2]) for s,sp,_ in STAR_PACKAGES)
        if not valid: raise ValueError
    except: await q.answer(ok=False,error_message="Unknown product."); return
    await q.answer(ok=True)

@dp.message(F.successful_payment)
async def success_pay(m: Message):
    uid=m.from_user.id; u=get_user(uid); today=str(date.today())
    try: p=m.successful_payment.invoice_payload.split("_"); stars=int(p[1]); spins=int(p[2])
    except: spins=100; stars=10
    cid=m.successful_payment.telegram_payment_charge_id; seen=u.setdefault("processed_charge_ids",[])
    if cid in seen: await m.answer(f"✅ Already credited!\n💰 Balance: *{u['spins']}* spins",parse_mode="Markdown",reply_markup=main_kb(uid)); return
    seen.append(cid)
    if len(seen)>20: u["processed_charge_ids"]=seen[-20:]
    u["spins"]+=spins; u["purchases"]=u.get("purchases",0)+1; u["total_stars_spent"]=u.get("total_stars_spent",0)+stars
    if not u.get("ever_deposited"): u["ever_deposited"]=True; stats["total_depositors"]=stats.get("total_depositors",0)+1
    dep=stats["daily_depositors"].setdefault(today,[])
    if str(uid) not in dep: dep.append(str(uid))
    stats["total_spins_bought"]=stats.get("total_spins_bought",0)+spins
    stats["daily_purchases"][today]=stats["daily_purchases"].get(today,0)+1
    stats["daily_stars_spent"][today]=stats["daily_stars_spent"].get(today,0)+stars
    stats["daily_revenue_spins"][today]=stats["daily_revenue_spins"].get(today,0)+spins; save_all()
    just_unlocked=u["total_stars_spent"]>=MIN_STARS_TO_UNLOCK and (u["total_stars_spent"]-stars)<MIN_STARS_TO_UNLOCK
    um="\n\n🔓 *Withdrawal UNLOCKED!* You can now withdraw!" if just_unlocked else ""
    await m.answer(f"✅ *+{spins} Spins added!*\n\n💰 Balance: *{u['spins']}* spins\n⭐ Stars spent: *{u['total_stars_spent']}*/{MIN_STARS_TO_UNLOCK}{um}\n\n✈️ Fly high and win big! 🔥",parse_mode="Markdown",reply_markup=main_kb(uid))

async def main():
    logging.basicConfig(level=logging.INFO,format="%(asctime)s [%(levelname)s] %(message)s")
    logging.info("Fortuno Aviator ✈️ is online!")
    await dp.start_polling(bot)

if __name__=="__main__":
    asyncio.run(main())