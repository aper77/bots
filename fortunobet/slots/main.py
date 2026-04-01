# """
# FortunoBet — FULL VERSION
# ─────────────────────────
# Install:
#     pip install aiogram aiohttp

# TON auto-payment uses the TON Center HTTP API (no extra libraries needed).
# Put your mnemonic in MNEMONIC list below after creating a NEW wallet.
# """

# import logging
# import asyncio
# import json
# import os
# import aiohttp
# from datetime import date
# from aiogram import Bot, Dispatcher, F, types
# from aiogram.filters import Command, CommandObject
# from aiogram.fsm.context import FSMContext
# from aiogram.fsm.state import State, StatesGroup
# from aiogram.fsm.storage.memory import MemoryStorage
# from aiogram.types import (
#     LabeledPrice, PreCheckoutQuery, Message,
#     InlineKeyboardButton, InlineKeyboardMarkup
# )

# # ═══════════════════════════════════════════════════════════════════
# #   CONFIGURATION  — edit only this section
# # ═══════════════════════════════════════════════════════════════════

# TOKEN    = "8767986301:AAHpaeLqV0RG-2I5rYn3T18o9LFSOJoGqfI"
# ADMIN_ID = 7627990095

# # ── Exchange rate ──────────────────────────────────────────────────
# # 1 TON ≈ $5 USD  |  10 Stars = $0.13 = 100 spins
# # So 1 spin ≈ $0.0013
# # 500 spins ≈ $0.65 → we give 1 TON (~$5) per 500 spins
# # This is generous for players and keeps your game attractive.
# # Change SPINS_PER_TON to adjust:
# #   500  → generous (good for marketing)
# #   1000 → balanced
# #   2000 → more profit for you
# SPINS_PER_TON   = 500       # how many spins = 1 TON
# SPIN_USD_VALUE  = 0.0013    # 1 spin ≈ $0.0013 (used for display only)
# MIN_WITHDRAW    = 500       # minimum spins to request withdrawal

# # ── TON wallet for auto-payments ───────────────────────────────────
# # Replace these 24 words with YOUR NEW wallet mnemonic
# # Create a fresh wallet in Tonkeeper → Settings → Backup
# MNEMONIC = [
#     "lawsuit",  "paddle",  "skull",  "autumn",  "embrace",  "urge",
#     "wrist",  "spell",  "easily",  "vast", "poet", "clarify",
#     "behind", "style", "icon", "oak", "recipe", "method",
#     "coast", "gun", "family", "crop", "wrestle", "budget",
# ]

# # TON Center API key — get free at https://toncenter.com
# # Without key: 1 request/second (enough for small bot)
# # With free key: 10 requests/second
# TONCENTER_API_KEY = "bb283e94ecd9f2b1be3c3ebb4d88971f89b1768fe50544b818f8a7f6e9cef6b5"   # leave empty or paste your key

# # ── Slot machine values ────────────────────────────────────────────
# JACKPOT_VALUE  = 43        # dice value that shows 777
# BAR_VALUE      = 1         # dice value that shows BAR
# FRUIT_VALUES   = {22, 64}  # dice values that show fruit

# # Base payouts (multiplied by bet size)
# JACKPOT_PAYOUT = 150
# BAR_PAYOUT     = 40
# FRUIT_PAYOUT   = 5

# # Available bet multipliers
# BET_OPTIONS = [1, 5, 10, 25, 50]

# # ═══════════════════════════════════════════════════════════════════

# bot = Bot(token=TOKEN)
# dp  = Dispatcher(storage=MemoryStorage())

# # ── FSM states ─────────────────────────────────────────────────────
# class WithdrawStates(StatesGroup):
#     waiting_amount = State()   # user entered amount, waiting for wallet
#     waiting_wallet = State()   # waiting for wallet address

# # ── Persistence ────────────────────────────────────────────────────
# DATA_FILE  = "user_data.json"
# STATS_FILE = "stats.json"

# def _load(fp) -> dict:
#     if os.path.exists(fp):
#         try:
#             with open(fp, "r", encoding="utf-8") as f:
#                 return json.load(f)
#         except Exception:
#             pass
#     return {}

# def _save(data: dict, fp: str):
#     tmp = fp + ".tmp"
#     with open(tmp, "w", encoding="utf-8") as f:
#         json.dump(data, f, ensure_ascii=False, indent=2)
#     os.replace(tmp, fp)

# user_data: dict = _load(DATA_FILE)
# stats: dict     = _load(STATS_FILE)

# if not stats:
#     stats = {
#         "total_players": 0, "total_spins_bought": 0,
#         "total_referrals": 0, "total_spins_played": 0,
#         "total_jackpots": 0, "total_bar_wins": 0,
#         "total_fruit_wins": 0, "total_ton_paid": 0.0,
#         "daily_active": {}, "purchases": [],
#     }

# def save_all():
#     _save(user_data, DATA_FILE)
#     _save(stats,     STATS_FILE)

# def get_user(user_id: int) -> dict:
#     uid = str(user_id)
#     if uid not in user_data:
#         user_data[uid] = {
#             "spins": 0, "ever_started": False,
#             "pending_withdrawal": False, "pending_spins": 0,
#             "pending_wallet": None, "referrals": 0,
#             "referred_by": None, "joined_date": str(date.today()),
#             "total_spins_played": 0, "total_won": 0,
#             "purchases": 0, "banned": False, "bet_size": 1,
#         }
#         stats["total_players"] += 1
#         save_all()
#     return user_data[uid]

# def track_daily(user_id: int):
#     today = str(date.today())
#     if today not in stats["daily_active"]:
#         stats["daily_active"][today] = []
#     uid = str(user_id)
#     if uid not in stats["daily_active"][today]:
#         stats["daily_active"][today].append(uid)

# # ── Dollar / TON helpers ───────────────────────────────────────────
# def spins_to_usd(spins: int) -> str:
#     return f"${spins * SPIN_USD_VALUE:.2f}"

# def spins_to_ton(spins: int) -> float:
#     return round(spins / SPINS_PER_TON, 4)

# # ── TON auto-payment via TonCenter API ────────────────────────────
# async def send_ton_payment(to_address: str, amount_ton: float) -> tuple[bool, str]:
#     """
#     Send TON using TonCenter API.
#     Returns (success: bool, message: str)
#     """
#     try:
#         from tonsdk.contract.wallet import Wallets, WalletVersionEnum
#         from tonsdk.utils import to_nano
#         import base64

#         # Build wallet from mnemonic
#         _mnemonics, _pub_k, _priv_k, wallet = Wallets.from_mnemonics(
#             MNEMONIC, WalletVersionEnum.v4r2, workchain=0
#         )
#         wallet_address = wallet.address.to_string(True, True, True)
#         headers = {"Content-Type": "application/json"}
#         if TONCENTER_API_KEY:
#             headers["X-API-Key"] = TONCENTER_API_KEY

#         base_url = "https://toncenter.com/api/v2"

#         async with aiohttp.ClientSession() as session:
#             # Get seqno
#             async with session.get(
#                 f"{base_url}/runGetMethod",
#                 params={"address": wallet_address, "method": "seqno", "stack": "[]"},
#                 headers=headers
#             ) as r:
#                 data = await r.json()
#                 seqno = int(data["result"]["stack"][0][1], 16)

#             # Build transfer
#             query = wallet.create_transfer_message(
#                 to_addr=to_address,
#                 amount=to_nano(amount_ton, "ton"),
#                 seqno=seqno,
#                 payload="FortunoBet Payout",
#             )
#             boc = base64.b64encode(query["message"].to_boc(False)).decode()

#             # Send
#             async with session.post(
#                 f"{base_url}/sendBoc",
#                 json={"boc": boc},
#                 headers=headers
#             ) as r:
#                 result = await r.json()
#                 if result.get("ok"):
#                     return True, "✅ Payment sent successfully!"
#                 else:
#                     return False, f"API error: {result.get('error', 'unknown')}"

#     except ImportError:
#         return False, "tonsdk not installed. Run: pip install tonsdk"
#     except Exception as e:
#         return False, f"Error: {str(e)}"

# # ── Keyboards ──────────────────────────────────────────────────────
# def main_kb(user_id: int) -> InlineKeyboardMarkup:
#     user     = get_user(user_id)
#     bet      = user.get("bet_size", 1)
#     usd      = spins_to_usd(bet)
#     ref_link = f"https://t.me/FortunoSlotsbot?start={user_id}"
#     return InlineKeyboardMarkup(inline_keyboard=[
#         [InlineKeyboardButton(
#             text=f"🎰 SPIN  [{bet} spin{'s' if bet>1 else ''} = {usd}]",
#             callback_data="spin"
#         )],
#         [InlineKeyboardButton(text="🎲 CHANGE BET SIZE", callback_data="change_bet")],
#         [InlineKeyboardButton(text="💎 BUY 100 SPINS — 10 Stars", callback_data="buy")],
#         [InlineKeyboardButton(text="💸 WITHDRAW WINNINGS", callback_data="withdraw_req")],
#         [InlineKeyboardButton(text="📊 MY STATS", callback_data="my_stats")],
#         [InlineKeyboardButton(
#             text="📢 INVITE FRIEND (+5 SPINS)",
#             url=f"https://t.me/share/url?url={ref_link}"
#         )],
#     ])

# def bet_kb(user_id: int) -> InlineKeyboardMarkup:
#     user    = get_user(user_id)
#     balance = user.get("spins", 0)
#     buttons = []
#     for bet in BET_OPTIONS:
#         usd         = spins_to_usd(bet)
#         jackpot_win = spins_to_usd(JACKPOT_PAYOUT * bet)
#         # grey out if not enough spins
#         can_afford  = "✅" if balance >= bet else "❌"
#         buttons.append([InlineKeyboardButton(
#             text=f"{can_afford} {bet}x — costs {bet} spin{'s' if bet>1 else ''} ({usd}) | 🔥 jackpot = {jackpot_win}",
#             callback_data=f"bet_{bet}"
#         )])
#     buttons.append([InlineKeyboardButton(text="🔙 BACK", callback_data="back_main")])
#     return InlineKeyboardMarkup(inline_keyboard=buttons)

# def no_spins_kb(user_id: int) -> InlineKeyboardMarkup:
#     ref_link = f"https://t.me/FortunoSlotsbot?start={user_id}"
#     return InlineKeyboardMarkup(inline_keyboard=[
#         [InlineKeyboardButton(text="💎 BUY 100 SPINS — 10 Stars", callback_data="buy")],
#         [InlineKeyboardButton(text="📢 INVITE FRIEND (+5 FREE SPINS)", url=f"https://t.me/share/url?url={ref_link}")],
#         [InlineKeyboardButton(text="📊 MY STATS", callback_data="my_stats")],
#     ])

# spin_again_kb = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text="🎰 SPIN AGAIN", callback_data="spin")],
#     [InlineKeyboardButton(text="🎲 CHANGE BET",  callback_data="change_bet")],
#     [InlineKeyboardButton(text="💎 BUY SPINS",   callback_data="buy")],
# ])

# # ── /start ─────────────────────────────────────────────────────────
# @dp.message(Command("start"))
# async def cmd_start(message: Message, command: CommandObject):
#     user_id = message.from_user.id
#     user    = get_user(user_id)
#     is_new  = not user.get("ever_started", False)

#     if is_new:
#         user["spins"]        = 10
#         user["ever_started"] = True

#     if command.args and is_new:
#         try:
#             ref_id = int(command.args)
#             if ref_id != user_id:
#                 ref = get_user(ref_id)
#                 ref["spins"]        += 5
#                 ref["referrals"]    += 1
#                 user["referred_by"]  = ref_id
#                 stats["total_referrals"] += 1
#                 save_all()
#                 await bot.send_message(
#                     ref_id,
#                     f"🎊 *Friend joined using your link!*\n"
#                     f"*+5 FREE SPINS* added!\n"
#                     f"💰 Balance: *{ref['spins']}* spins\n"
#                     f"👥 Total friends invited: *{ref['referrals']}*",
#                     parse_mode="Markdown"
#                 )
#         except (ValueError, TypeError):
#             pass

#     track_daily(user_id)
#     save_all()

#     usd_val = spins_to_usd(user["spins"])
#     await message.answer(
#         "🎰 *WELCOME TO FORTUNOBET* 🎰\n\n"
#         "High RTP Slots | Instant TON Payouts\n\n"
#         f"💰 *Balance:* {user['spins']} spins (~{usd_val})\n"
#         f"{'🆕 *You got 10 FREE spins to start!* 🎁' if is_new else ''}\n\n"
#         f"📌 *How to win:*\n"
#         f"🎰 Spin to win spins\n"
#         f"🎲 Pick a bigger bet for bigger wins\n"
#         f"🏆 Reach {MIN_WITHDRAW} spins → Withdraw as TON\n"
#         f"📢 Invite friends → +5 spins each",
#         reply_markup=main_kb(user_id),
#         parse_mode="Markdown",
#     )

# # ── Change bet ──────────────────────────────────────────────────────
# @dp.callback_query(F.data == "change_bet")
# async def change_bet_menu(callback: types.CallbackQuery):
#     user = get_user(callback.from_user.id)
#     await callback.message.answer(
#         "🎲 *SELECT YOUR BET SIZE*\n\n"
#         "Higher bet = more spins risked BUT wins are multiplied!\n\n"
#         f"💰 Your balance: *{user['spins']}* spins "
#         f"(~{spins_to_usd(user['spins'])})\n\n"
#         f"Win table at each bet size:\n"
#         f"{'Bet':<6} {'Fruit':>8} {'Bar':>8} {'Jackpot':>10}\n"
#         + "\n".join([
#             f"{b}x{'':<4} "
#             f"+{FRUIT_PAYOUT*b:>5} spins  "
#             f"+{BAR_PAYOUT*b:>5} spins  "
#             f"+{JACKPOT_PAYOUT*b:>6} spins"
#             for b in BET_OPTIONS
#         ]),
#         reply_markup=bet_kb(callback.from_user.id),
#         parse_mode="Markdown",
#     )
#     await callback.answer()

# @dp.callback_query(F.data.startswith("bet_"))
# async def set_bet(callback: types.CallbackQuery):
#     user     = get_user(callback.from_user.id)
#     bet_size = int(callback.data.split("_")[1])

#     if user["spins"] < bet_size:
#         await callback.answer(
#             f"❌ Not enough spins! You need {bet_size} spins for this bet.",
#             show_alert=True
#         )
#         return

#     user["bet_size"] = bet_size
#     save_all()

#     await callback.message.answer(
#         f"✅ *Bet set to {bet_size}x!*\n\n"
#         f"💰 Balance: *{user['spins']}* spins (~{spins_to_usd(user['spins'])})\n"
#         f"Each spin costs *{bet_size}* spin{'s' if bet_size>1 else ''} "
#         f"(~{spins_to_usd(bet_size)})\n\n"
#         f"🔥 Jackpot = *+{JACKPOT_PAYOUT * bet_size}* spins "
#         f"(~{spins_to_usd(JACKPOT_PAYOUT * bet_size)})\n"
#         f"💎 Bar win = *+{BAR_PAYOUT * bet_size}* spins "
#         f"(~{spins_to_usd(BAR_PAYOUT * bet_size)})\n"
#         f"✨ Fruit win = *+{FRUIT_PAYOUT * bet_size}* spins "
#         f"(~{spins_to_usd(FRUIT_PAYOUT * bet_size)})",
#         reply_markup=main_kb(callback.from_user.id),
#         parse_mode="Markdown",
#     )
#     await callback.answer(f"Bet set to {bet_size}x!")

# # ── Spin ────────────────────────────────────────────────────────────
# @dp.callback_query(F.data == "spin")
# async def play_slots(callback: types.CallbackQuery):
#     user_id  = callback.from_user.id
#     user     = get_user(user_id)
#     bet_size = user.get("bet_size", 1)

#     if user.get("banned"):
#         await callback.answer("🚫 You are banned.", show_alert=True)
#         return

#     if user["spins"] < bet_size:
#         await callback.message.answer(
#             f"😢 *Not enough spins!*\n\n"
#             f"Your balance: *{user['spins']}* spins\n"
#             f"Your bet: *{bet_size}x* (costs {bet_size} spins)\n\n"
#             f"👇 *Get more spins:*\n"
#             f"💎 Buy 100 spins — *10 Telegram Stars*\n"
#             f"📢 Invite a friend — *+5 FREE spins*\n"
#             f"🎲 Or lower your bet size!",
#             reply_markup=no_spins_kb(user_id),
#             parse_mode="Markdown",
#         )
#         await callback.answer("❌ Not enough spins!", show_alert=False)
#         return

#     user["spins"]             -= bet_size
#     user["total_spins_played"] = user.get("total_spins_played", 0) + bet_size
#     stats["total_spins_played"] = stats.get("total_spins_played", 0) + bet_size
#     track_daily(user_id)
#     save_all()

#     msg   = await callback.message.answer_dice(emoji="🎰")
#     value = msg.dice.value
#     await asyncio.sleep(2.5)

#     if value == JACKPOT_VALUE:
#         win_amount = JACKPOT_PAYOUT * bet_size
#         win_text   = f"🔥 *JACKPOT! 7️⃣7️⃣7️⃣*\n+{win_amount} SPINS! (~{spins_to_usd(win_amount)})"
#         stats["total_jackpots"] = stats.get("total_jackpots", 0) + 1
#     elif value == BAR_VALUE:
#         win_amount = BAR_PAYOUT * bet_size
#         win_text   = f"💎 *BAR WIN!*\n+{win_amount} SPINS! (~{spins_to_usd(win_amount)})"
#         stats["total_bar_wins"] = stats.get("total_bar_wins", 0) + 1
#     elif value in FRUIT_VALUES:
#         win_amount = FRUIT_PAYOUT * bet_size
#         win_text   = f"✨ *FRUIT WIN!*\n+{win_amount} SPINS! (~{spins_to_usd(win_amount)})"
#         stats["total_fruit_wins"] = stats.get("total_fruit_wins", 0) + 1
#     else:
#         win_amount = 0
#         win_text   = "❌ *No win.* Try again!"

#     user["spins"]    += win_amount
#     user["total_won"] = user.get("total_won", 0) + win_amount
#     save_all()

#     # Withdraw hint
#     hint = ""
#     if 0 < MIN_WITHDRAW - user["spins"] <= 100:
#         hint = f"\n\n🔥 *Almost there!* Only {MIN_WITHDRAW - user['spins']} more spins to withdraw!"
#     elif user["spins"] >= MIN_WITHDRAW:
#         hint = f"\n\n💸 *You can withdraw now!* Press WITHDRAW WINNINGS!"

#     await callback.message.answer(
#         f"{win_text}\n\n"
#         f"💰 *Balance:* {user['spins']} spins (~{spins_to_usd(user['spins'])})"
#         f"{hint}",
#         reply_markup=spin_again_kb,
#         parse_mode="Markdown",
#     )
#     await callback.answer()

# # ── My stats ────────────────────────────────────────────────────────
# @dp.callback_query(F.data == "my_stats")
# async def my_stats(callback: types.CallbackQuery):
#     user_id  = callback.from_user.id
#     user     = get_user(user_id)
#     ref_link = f"https://t.me/FortunoSlotsbot?start={user_id}"

#     await callback.message.answer(
#         f"📊 *YOUR STATS*\n\n"
#         f"💰 Balance: *{user['spins']}* spins\n"
#         f"     ≈ *{spins_to_usd(user['spins'])}* USD\n"
#         f"     ≈ *{spins_to_ton(user['spins'])} TON*\n\n"
#         f"🎰 Spins played: *{user.get('total_spins_played', 0)}*\n"
#         f"🏆 Spins won: *{user.get('total_won', 0)}*\n"
#         f"🎲 Current bet: *{user.get('bet_size', 1)}x*\n"
#         f"👥 Friends invited: *{user.get('referrals', 0)}*\n"
#         f"💎 Purchases: *{user.get('purchases', 0)}*\n"
#         f"📅 Joined: *{user.get('joined_date', 'N/A')}*\n\n"
#         f"📌 Withdraw minimum: *{MIN_WITHDRAW} spins*\n"
#         f"     = *{spins_to_ton(MIN_WITHDRAW)} TON* "
#         f"(~{spins_to_usd(MIN_WITHDRAW)} USD)\n\n"
#         f"🔗 *Your invite link:*\n`{ref_link}`",
#         parse_mode="Markdown",
#         reply_markup=InlineKeyboardMarkup(inline_keyboard=[
#             [InlineKeyboardButton(text="📢 SHARE MY LINK", url=f"https://t.me/share/url?url={ref_link}")],
#             [InlineKeyboardButton(text="🔙 BACK", callback_data="back_main")],
#         ])
#     )
#     await callback.answer()

# @dp.callback_query(F.data == "back_main")
# async def back_main(callback: types.CallbackQuery):
#     user = get_user(callback.from_user.id)
#     await callback.message.answer(
#         f"🎰 *FORTUNOBET*\n\n"
#         f"💰 *Balance:* {user['spins']} spins (~{spins_to_usd(user['spins'])})",
#         reply_markup=main_kb(callback.from_user.id),
#         parse_mode="Markdown",
#     )
#     await callback.answer()

# # ── Withdraw — STEP 1: ask how much ────────────────────────────────
# @dp.callback_query(F.data == "withdraw_req")
# async def withdraw_start(callback: types.CallbackQuery, state: FSMContext):
#     user = get_user(callback.from_user.id)

#     if user["spins"] < MIN_WITHDRAW:
#         needed = MIN_WITHDRAW - user["spins"]
#         await callback.message.answer(
#             f"💸 *WITHDRAWAL*\n\n"
#             f"❌ Minimum is *{MIN_WITHDRAW} spins* to withdraw.\n\n"
#             f"Your balance: *{user['spins']}* spins\n"
#             f"You need *{needed}* more spins!\n\n"
#             f"*{MIN_WITHDRAW} spins = {spins_to_ton(MIN_WITHDRAW)} TON "
#             f"(~{spins_to_usd(MIN_WITHDRAW)} USD)*",
#             parse_mode="Markdown",
#             reply_markup=InlineKeyboardMarkup(inline_keyboard=[
#                 [InlineKeyboardButton(text="🎰 KEEP SPINNING", callback_data="spin")],
#                 [InlineKeyboardButton(text="💎 BUY SPINS", callback_data="buy")],
#             ])
#         )
#         await callback.answer()
#         return

#     if user.get("pending_withdrawal"):
#         await callback.answer("⏳ You have a pending withdrawal already!", show_alert=True)
#         return

#     await state.set_state(WithdrawStates.waiting_amount)
#     await callback.message.answer(
#         f"💸 *WITHDRAWAL*\n\n"
#         f"Your balance: *{user['spins']}* spins\n"
#         f"     ≈ *{spins_to_ton(user['spins'])} TON* "
#         f"(~{spins_to_usd(user['spins'])} USD)\n\n"
#         f"📝 *How many spins do you want to withdraw?*\n"
#         f"Minimum: *{MIN_WITHDRAW} spins*\n"
#         f"Maximum: *{user['spins']} spins* (your full balance)\n\n"
#         f"Just type a number below 👇",
#         parse_mode="Markdown",
#         reply_markup=InlineKeyboardMarkup(inline_keyboard=[
#             [InlineKeyboardButton(
#                 text=f"💰 WITHDRAW ALL ({user['spins']} spins)",
#                 callback_data=f"withdraw_all"
#             )],
#             [InlineKeyboardButton(text="❌ CANCEL", callback_data="cancel_withdraw")],
#         ])
#     )
#     await callback.answer()

# # ── Withdraw — user types amount ────────────────────────────────────
# @dp.message(WithdrawStates.waiting_amount)
# async def withdraw_amount_entered(message: Message, state: FSMContext):
#     user = get_user(message.from_user.id)

#     try:
#         amount = int(message.text.strip())
#     except ValueError:
#         await message.answer("❌ Please enter a valid number. Example: `500`", parse_mode="Markdown")
#         return

#     if amount < MIN_WITHDRAW:
#         await message.answer(
#             f"❌ Minimum withdrawal is *{MIN_WITHDRAW} spins*.\n"
#             f"You entered: *{amount}*. Please enter a bigger number.",
#             parse_mode="Markdown"
#         )
#         return

#     if amount > user["spins"]:
#         await message.answer(
#             f"❌ You only have *{user['spins']}* spins.\n"
#             f"Please enter *{user['spins']}* or less.",
#             parse_mode="Markdown"
#         )
#         return

#     # Save chosen amount to FSM
#     await state.update_data(withdraw_amount=amount)
#     await state.set_state(WithdrawStates.waiting_wallet)

#     ton_amount = spins_to_ton(amount)
#     await message.answer(
#         f"✅ *{amount} spins selected*\n"
#         f"You will receive: *{ton_amount} TON* "
#         f"(~{spins_to_usd(amount)} USD)\n\n"
#         f"📝 Now send your *TON wallet address*:\n"
#         f"_(Starts with UQ, EQ, or 0Q)_",
#         parse_mode="Markdown",
#         reply_markup=InlineKeyboardMarkup(inline_keyboard=[
#             [InlineKeyboardButton(text="❌ CANCEL", callback_data="cancel_withdraw")]
#         ])
#     )

# # ── Withdraw — withdraw ALL button ──────────────────────────────────
# @dp.callback_query(F.data == "withdraw_all")
# async def withdraw_all(callback: types.CallbackQuery, state: FSMContext):
#     user   = get_user(callback.from_user.id)
#     amount = user["spins"]
#     await state.update_data(withdraw_amount=amount)
#     await state.set_state(WithdrawStates.waiting_wallet)
#     ton_amount = spins_to_ton(amount)
#     await callback.message.answer(
#         f"✅ *Withdrawing all {amount} spins*\n"
#         f"You will receive: *{ton_amount} TON* "
#         f"(~{spins_to_usd(amount)} USD)\n\n"
#         f"📝 Now send your *TON wallet address*:\n"
#         f"_(Starts with UQ, EQ, or 0Q)_",
#         parse_mode="Markdown",
#         reply_markup=InlineKeyboardMarkup(inline_keyboard=[
#             [InlineKeyboardButton(text="❌ CANCEL", callback_data="cancel_withdraw")]
#         ])
#     )
#     await callback.answer()

# # ── Withdraw — cancel ───────────────────────────────────────────────
# @dp.callback_query(F.data == "cancel_withdraw")
# async def cancel_withdraw(callback: types.CallbackQuery, state: FSMContext):
#     await state.clear()
#     user = get_user(callback.from_user.id)
#     await callback.message.answer(
#         "❌ *Withdrawal cancelled.*",
#         parse_mode="Markdown",
#         reply_markup=main_kb(callback.from_user.id)
#     )
#     await callback.answer()

# # ── Withdraw — user sends wallet address ────────────────────────────
# @dp.message(WithdrawStates.waiting_wallet)
# async def withdraw_wallet_entered(message: Message, state: FSMContext):
#     wallet = message.text.strip()

#     # Validate wallet address
#     if not (wallet.startswith(("UQ", "EQ", "0Q")) and len(wallet) >= 48):
#         await message.answer(
#             "❌ *Invalid wallet address!*\n\n"
#             "It must start with *UQ*, *EQ*, or *0Q* and be 48+ characters.\n"
#             "Please check and try again.",
#             parse_mode="Markdown"
#         )
#         return

#     user_id = message.from_user.id
#     user    = get_user(user_id)
#     data    = await state.get_data()
#     amount  = data.get("withdraw_amount", 0)

#     if amount > user["spins"]:
#         await message.answer(
#             f"❌ You no longer have enough spins. "
#             f"Your balance: *{user['spins']}*.",
#             parse_mode="Markdown"
#         )
#         await state.clear()
#         return

#     ton_amount = spins_to_ton(amount)
#     user["pending_withdrawal"] = True
#     user["pending_spins"]      = amount
#     user["pending_wallet"]     = wallet
#     save_all()
#     await state.clear()

#     await bot.send_message(
#         ADMIN_ID,
#         f"🚨 *PAYOUT REQUEST*\n\n"
#         f"👤 {message.from_user.full_name}\n"
#         f"🆔 `{user_id}`\n"
#         f"🎰 Spins: *{amount}*\n"
#         f"💎 TON: *{ton_amount}*\n"
#         f"💵 USD: *{spins_to_usd(amount)}*\n"
#         f"👛 Wallet:\n`{wallet}`\n\n"
#         f"Type `/pay {user_id}` to send TON automatically!",
#         parse_mode="Markdown",
#     )
#     await message.answer(
#         f"✅ *Withdrawal request submitted!*\n\n"
#         f"Amount: *{amount} spins*\n"
#         f"You will receive: *{ton_amount} TON* "
#         f"(~{spins_to_usd(amount)} USD)\n\n"
#         f"Processing within 24 hours. 🙏",
#         parse_mode="Markdown",
#         reply_markup=main_kb(user_id)
#     )

# # ── Admin: /pay — AUTO TON SEND ─────────────────────────────────────
# @dp.message(Command("pay"))
# async def admin_pay(message: Message):
#     if message.from_user.id != ADMIN_ID:
#         return
#     try:
#         target_id = str(int(message.text.split()[1]))
#         user      = user_data.get(target_id)
#         if not user or not user.get("pending_withdrawal"):
#             await message.answer("❌ No pending withdrawal found for this user.")
#             return

#         wallet     = user.get("pending_wallet")
#         amount     = user.get("pending_spins", 0)
#         ton_amount = spins_to_ton(amount)

#         await message.answer(
#             f"⏳ Sending *{ton_amount} TON* to:\n`{wallet}`",
#             parse_mode="Markdown"
#         )

#         success, msg = await send_ton_payment(wallet, ton_amount)

#         if success:
#             user["spins"]             -= amount
#             user["pending_withdrawal"] = False
#             user["pending_spins"]      = 0
#             user["pending_wallet"]     = None
#             stats["total_ton_paid"]    = round(
#                 stats.get("total_ton_paid", 0) + ton_amount, 4
#             )
#             save_all()
#             await message.answer(
#                 f"✅ *{ton_amount} TON sent successfully!*\n"
#                 f"User: `{target_id}`\nWallet: `{wallet}`",
#                 parse_mode="Markdown"
#             )
#             await bot.send_message(
#                 int(target_id),
#                 f"💸 *Withdrawal complete!*\n\n"
#                 f"*{ton_amount} TON* has been sent to your wallet!\n"
#                 f"(~{spins_to_usd(amount)} USD)\n\n"
#                 f"Thank you for playing FortunoBet! 🎰",
#                 parse_mode="Markdown",
#                 reply_markup=main_kb(int(target_id))
#             )
#         else:
#             await message.answer(
#                 f"❌ *Auto payment failed!*\n{msg}\n\n"
#                 f"Send manually:\nAmount: *{ton_amount} TON*\n"
#                 f"Wallet: `{wallet}`\n\n"
#                 f"Then type `/paydone {target_id}` to confirm.",
#                 parse_mode="Markdown"
#             )
#     except (IndexError, ValueError):
#         await message.answer("Usage: `/pay [user_id]`", parse_mode="Markdown")

# # ── Admin: /paydone — manual confirm ───────────────────────────────
# @dp.message(Command("paydone"))
# async def admin_paydone(message: Message):
#     if message.from_user.id != ADMIN_ID:
#         return
#     try:
#         target_id  = str(int(message.text.split()[1]))
#         user       = user_data.get(target_id)
#         if not user:
#             await message.answer("❌ User not found.")
#             return
#         amount     = user.get("pending_spins", 0)
#         ton_amount = spins_to_ton(amount)
#         user["spins"]             -= amount
#         user["pending_withdrawal"] = False
#         user["pending_spins"]      = 0
#         user["pending_wallet"]     = None
#         stats["total_ton_paid"]    = round(stats.get("total_ton_paid", 0) + ton_amount, 4)
#         save_all()
#         await message.answer(f"✅ Manually confirmed. {ton_amount} TON for user {target_id}.")
#         await bot.send_message(
#             int(target_id),
#             f"💸 *Withdrawal complete!*\n"
#             f"*{ton_amount} TON* sent!\n"
#             f"Thank you for playing! 🎰",
#             parse_mode="Markdown",
#             reply_markup=main_kb(int(target_id))
#         )
#     except (IndexError, ValueError):
#         await message.answer("Usage: `/paydone [user_id]`", parse_mode="Markdown")

# # ── Admin: /admin dashboard ─────────────────────────────────────────
# @dp.message(Command("admin"))
# async def admin_dashboard(message: Message):
#     if message.from_user.id != ADMIN_ID:
#         return
#     today        = str(date.today())
#     active_today = len(stats["daily_active"].get(today, []))
#     pending      = [(uid, u) for uid, u in user_data.items() if u.get("pending_withdrawal")]
#     top_players  = sorted(user_data.items(), key=lambda x: x[1].get("spins", 0), reverse=True)[:5]
#     top_refs     = sorted(user_data.items(), key=lambda x: x[1].get("referrals", 0), reverse=True)[:5]

#     top_text  = "\n".join([f"  {i+1}. `{uid}` — {u.get('spins',0)} spins ({spins_to_usd(u.get('spins',0))})" for i,(uid,u) in enumerate(top_players)])
#     ref_text  = "\n".join([f"  {i+1}. `{uid}` — {u.get('referrals',0)} referrals" for i,(uid,u) in enumerate(top_refs)])
#     pend_text = "\n".join([f"  • `{uid}` — {spins_to_ton(u.get('pending_spins',0))} TON" for uid,u in pending]) or "  None ✅"

#     await message.answer(
#         f"🔐 *ADMIN DASHBOARD*\n"
#         f"━━━━━━━━━━━━━━━━━━━━\n\n"
#         f"👥 *PLAYERS*\n"
#         f"  Total: *{stats['total_players']}*\n"
#         f"  Active today: *{active_today}*\n"
#         f"  Referrals: *{stats['total_referrals']}*\n\n"
#         f"🎰 *GAME*\n"
#         f"  Spins played: *{stats.get('total_spins_played',0)}*\n"
#         f"  Jackpots: *{stats.get('total_jackpots',0)}*\n"
#         f"  Bar wins: *{stats.get('total_bar_wins',0)}*\n"
#         f"  Fruit wins: *{stats.get('total_fruit_wins',0)}*\n\n"
#         f"💎 *MONEY*\n"
#         f"  Spins sold: *{stats.get('total_spins_bought',0)}*\n"
#         f"  TON paid out: *{stats.get('total_ton_paid',0)} TON*\n\n"
#         f"💸 *PENDING PAYOUTS*\n{pend_text}\n\n"
#         f"🏆 *TOP 5 PLAYERS*\n{top_text}\n\n"
#         f"📢 *TOP 5 REFERRERS*\n{ref_text}\n\n"
#         f"━━━━━━━━━━━━━━━━━━━━\n"
#         f"🛠 *COMMANDS*\n"
#         f"`/pay [id]` — auto send TON\n"
#         f"`/paydone [id]` — manual confirm\n"
#         f"`/gift [id] [spins]` — give spins\n"
#         f"`/ban [id]` / `/unban [id]`\n"
#         f"`/broadcast [msg]` — message all users",
#         parse_mode="Markdown",
#     )

# # ── Admin: /gift ────────────────────────────────────────────────────
# @dp.message(Command("gift"))
# async def admin_gift(message: Message):
#     if message.from_user.id != ADMIN_ID:
#         return
#     try:
#         parts     = message.text.split()
#         target_id = str(int(parts[1]))
#         amount    = int(parts[2])
#         user      = get_user(int(target_id))
#         user["spins"] += amount
#         save_all()
#         await message.answer(
#             f"✅ Added *{amount}* spins to `{target_id}`.\nNew balance: *{user['spins']}*.",
#             parse_mode="Markdown"
#         )
#         await bot.send_message(
#             int(target_id),
#             f"🎁 *You received {amount} free spins!*\n"
#             f"💰 Balance: {user['spins']} spins "
#             f"(~{spins_to_usd(user['spins'])})\nGood luck! 🎰",
#             parse_mode="Markdown"
#         )
#     except (IndexError, ValueError):
#         await message.answer("Usage: `/gift [user_id] [amount]`", parse_mode="Markdown")

# # ── Admin: /ban /unban ──────────────────────────────────────────────
# @dp.message(Command("ban"))
# async def admin_ban(message: Message):
#     if message.from_user.id != ADMIN_ID:
#         return
#     try:
#         target_id = str(int(message.text.split()[1]))
#         get_user(int(target_id))["banned"] = True
#         save_all()
#         await message.answer(f"🚫 User `{target_id}` banned.", parse_mode="Markdown")
#     except (IndexError, ValueError):
#         await message.answer("Usage: `/ban [user_id]`", parse_mode="Markdown")

# @dp.message(Command("unban"))
# async def admin_unban(message: Message):
#     if message.from_user.id != ADMIN_ID:
#         return
#     try:
#         target_id = str(int(message.text.split()[1]))
#         get_user(int(target_id))["banned"] = False
#         save_all()
#         await message.answer(f"✅ User `{target_id}` unbanned.", parse_mode="Markdown")
#     except (IndexError, ValueError):
#         await message.answer("Usage: `/unban [user_id]`", parse_mode="Markdown")

# # ── Admin: /broadcast ───────────────────────────────────────────────
# @dp.message(Command("broadcast"))
# async def admin_broadcast(message: Message):
#     if message.from_user.id != ADMIN_ID:
#         return
#     try:
#         text = message.text.split(" ", 1)[1]
#     except IndexError:
#         await message.answer("Usage: `/broadcast [message]`", parse_mode="Markdown")
#         return
#     sent = failed = 0
#     for uid in user_data:
#         if user_data[uid].get("banned"):
#             continue
#         try:
#             await bot.send_message(int(uid), f"📢 *FortunoBet:*\n\n{text}", parse_mode="Markdown")
#             sent += 1
#             await asyncio.sleep(0.05)
#         except Exception:
#             failed += 1
#     await message.answer(f"✅ Sent: *{sent}* | Failed: *{failed}*", parse_mode="Markdown")

# # ── Stars payment ────────────────────────────────────────────────────
# @dp.callback_query(F.data == "buy")
# async def process_buy(callback: types.CallbackQuery):
#     await bot.send_invoice(
#         callback.message.chat.id,
#         title="100 Spins",
#         description="100 credits for FortunoBet slots",
#         payload="buy_100",
#         provider_token="",
#         currency="XTR",
#         prices=[LabeledPrice(label="100 Spins", amount=10)],
#     )
#     await callback.answer()

# @dp.pre_checkout_query()
# async def pre_check(q: PreCheckoutQuery):
#     await q.answer(ok=True)

# @dp.message(F.successful_payment)
# async def success_pay(m: Message):
#     user = get_user(m.from_user.id)
#     user["spins"]    += 100
#     user["purchases"] = user.get("purchases", 0) + 1
#     stats["total_spins_bought"] = stats.get("total_spins_bought", 0) + 100
#     save_all()
#     await m.answer(
#         f"✅ *100 Spins added!*\n"
#         f"💰 Balance: *{user['spins']}* spins "
#         f"(~{spins_to_usd(user['spins'])})\n"
#         f"Good luck! 🎰",
#         parse_mode="Markdown",
#     )

# # ── Main ─────────────────────────────────────────────────────────────
# async def main():
#     logging.basicConfig(
#         level=logging.INFO,
#         format="%(asctime)s [%(levelname)s] %(message)s"
#     )
#     logging.info("FortunoBet FULL VERSION is online.")
#     await dp.start_polling(bot)

# if __name__ == "__main__":
#     asyncio.run(main())

    
# /gift 7627990095 50
# /admin — full dashboard
# /broadcast [message] — send a message to ALL users at once
# /ban [user_id] — ban a cheater
# /unban [user_id] — unban them
# /gift and /pay — same as before

# MNEMONIC = [
#     "lawsuit",  "paddle",  "skull",  "autumn",  "embrace",  "urge",
#     "wrist",  "spell",  "easily",  "vast", "poet", "clarify",
#     "behind", "style", "icon", "oak", "recipe", "method",
#     "coast", "gun", "family", "crop", "wrestle", "budget",
# ]



import asyncio
from tonutils.wallet import WalletV5R1
from tonutils.client import ToncenterClient

# ── CONFIGURATION ───────────────────────────
MNEMONIC = [
    "lawsuit",  "paddle",  "skull",  "autumn",  "embrace",  "urge",
    "wrist",  "spell",  "easily",  "vast", "poet", "clarify",
    "behind", "style", "icon", "oak", "recipe", "method",
    "coast", "gun", "family", "crop", "wrestle", "budget",
]

# Your UQDP address
MY_ADDRESS = "UQDPwPEdG-8d0Tr-lgZtLSlyvt-Mti1N3sBmMw90UaXL7-L1"
API_KEY = "bb283e94ecd9f2b1be3c3ebb4d88971f89b1768fe50544b818f8a7f6e9cef6b5"
DESTINATION = "UQD2nimQdNGpQGFnmNvYUhiXTS92RjPCtdRRcsFYHn-6auoM"
# ─────────────────────────────────────────────

async def main():
    client = ToncenterClient(api_key=API_KEY)
    
    # Create the W5 Wallet object
    wallet = WalletV5R1.from_mnemonic(client, MNEMONIC)
    
    print(f"Script Address: {wallet.address}")
    print(f"Target Address: {MY_ADDRESS}")
    
    if str(wallet.address) != MY_ADDRESS:
        print("❌ Warning: Address still does not match. Checking W5 Beta...")
        # Some early W5 wallets use a different ID, but V5R1 is the standard now.
    
    # Check Balance
    balance = await wallet.get_balance()
    print(f"Balance: {balance / 1e9} TON")
    
    if balance > 0.01 * 1e9:
        print("Sending 0.01 TON...")
        tx = await wallet.transfer(destination=DESTINATION, amount=0.01, comment="FortunoBet W5 Test")
        print(f"✅ Success! Transaction hash: {tx}")
    else:
        print("❌ Insufficient funds.")

if __name__ == "__main__":
    asyncio.run(main())