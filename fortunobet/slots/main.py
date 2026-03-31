import logging
import asyncio
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import Command, CommandObject
from aiogram.types import LabeledPrice, PreCheckoutQuery, Message, InlineKeyboardButton, InlineKeyboardMarkup

# --- CONFIGURATION ---
TOKEN = "8767986301:AAHpaeLqV0RG-2I5rYn3T18o9LFSOJoGqfI"
ADMIN_ID = 1002853287489 

# Win logic values
CHANCE_777 = 64        
CHANCE_BAR = 1         
CHANCE_FRUIT = [16, 22, 43, 48] 

bot = Bot(token=TOKEN)
dp = Dispatcher()
user_data = {} 

# --- KEYBOARD BUILDER ---
def get_main_kb(user_id):
    ref_link = f"https://t.me/FortunoSlotsbot?start={user_id}"
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🎰 SPIN (1 Credit)", callback_data="spin")],
        [InlineKeyboardButton(text="💎 BUY 100 SPINS (10 Stars)", callback_data="buy")],
        [InlineKeyboardButton(text="💸 WITHDRAW WINNINGS", callback_data="withdraw_req")],
        [InlineKeyboardButton(text="📢 INVITE FOR 5 SPINS", url=f"https://t.me/share/url?url={ref_link}")]
    ])

# --- START & MARKETING (10 FREE SPINS) ---
@dp.message(Command("start"))
async def cmd_start(message: Message, command: CommandObject):
    user_id = message.from_user.id
    if user_id not in user_data:
        user_data[user_id] = {"spins": 10} # 10 Free spins for trust building
        if command.args:
            try:
                ref_id = int(command.args)
                if ref_id in user_data and ref_id != user_id:
                    user_data[ref_id]["spins"] += 5
                    await bot.send_message(ref_id, "🎊 **Bonus!** Referral joined. +5 FREE SPINS!")
            except: pass

    await message.answer(
        "🎰 **WELCOME TO FORTUNOBET** 🎰\n\n"
        "High RTP Slots | Instant TON Payouts\n\n"
        f"💰 **Your Balance:** {user_data[user_id]['spins']} Spins",
        reply_markup=get_main_kb(user_id),
        parse_mode="Markdown"
    )

# --- GAME ENGINE (PROFITABLE RATIOS) ---
@dp.callback_query(F.data == "spin")
async def play_slots(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    if user_data.get(user_id, {}).get("spins", 0) < 1:
        await callback.answer("❌ Out of spins! Buy more or invite friends.", show_alert=True)
        return

    user_data[user_id]["spins"] -= 1
    msg = await callback.message.answer_dice(emoji="🎰")
    value = msg.dice.value
    await asyncio.sleep(2.5) 

    win_amount = 0
    win_text = "❌ No win. Try again!"
    
    if value == CHANCE_777:
        win_amount = 150 # Large win but safe for you
        win_text = "🔥 **JACKPOT!** +150 SPINS!"
    elif value == CHANCE_BAR:
        win_amount = 40 
        win_text = "💎 **BAR WIN!** +40 SPINS!"
    elif value in CHANCE_FRUIT:
        win_amount = 5   
        win_text = "✨ **FRUIT WIN!** +5 SPINS!"

    user_data[user_id]["spins"] += win_amount
    
    repeat_kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🎰 SPIN AGAIN", callback_data="spin")],
        [InlineKeyboardButton(text="💎 BUY SPINS", callback_data="buy")]
    ])

    await callback.message.answer(
        f"{win_text}\n💰 **Balance:** {user_data[user_id]['spins']} Spins",
        reply_markup=repeat_kb,
        parse_mode="Markdown"
    )

# --- WITHDRAWAL SYSTEM (500 MINIMUM) ---
@dp.callback_query(F.data == "withdraw_req")
async def withdraw_info(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    balance = user_data.get(user_id, {}).get("spins", 0)
    
    if balance < 500:
        await callback.answer(f"❌ Min. Withdraw is 500 Spins. (You have {balance})", show_alert=True)
    else:
        await callback.message.answer(
            "💸 **WITHDRAWAL REQUEST**\n\n"
            "Congratulations! Please send your **TON Wallet Address** below.\n"
            "The Admin will pay you in TON within 24 hours!"
        )

# Handling Wallet Input (Starts with UQ or EQ)
@dp.message(F.text.regexp(r"^(UQ|EQ|0Q)"))
async def handle_wallet(message: Message):
    user_id = message.from_user.id
    balance = user_data.get(user_id, {}).get("spins", 0)
    
    if balance < 500: return # Extra security

    # Notify YOU (The Admin)
    await bot.send_message(
        ADMIN_ID,
        f"🚨 **PAYOUT NEEDED!**\nUser: `{user_id}`\nBalance: {balance}\nWallet: `{message.text}`"
    )
    await message.answer("✅ **Request Received!** Admin is checking your balance. Wait for payout.")

# --- ADMIN TOOL: /gift [id] [amount] ---
@dp.message(Command("gift"))
async def admin_gift(message: Message):
    if message.from_user.id != ADMIN_ID: return
    try:
        args = message.text.split()
        target_id, amount = int(args[1]), int(args[2])
        if target_id not in user_data: user_data[target_id] = {"spins": 0}
        user_data[target_id]["spins"] += amount
        await message.answer(f"✅ Adjusted balance for {target_id} by {amount}")
    except: await message.answer("Use: `/gift [id] [amount]`")

# --- STARS PAYMENTS ---
@dp.callback_query(F.data == "buy")
async def process_buy(callback: types.CallbackQuery):
    await bot.send_invoice(
        callback.message.chat.id, title="100 Spins", description="Credits for FortunoBet",
        payload="buy_100", provider_token="", currency="XTR", prices=[LabeledPrice(label="100 Spins", amount=10)]
    )

@dp.pre_checkout_query()
async def pre_check(q: PreCheckoutQuery): await q.answer(ok=True)

@dp.message(F.successful_payment)
async def success_pay(m: Message):
    user_id = m.from_user.id
    if user_id not in user_data: user_data[user_id] = {"spins": 0}
    user_data[user_id]["spins"] += 100
    await m.answer("✅ **Success!** 100 Spins added.")

async def main():
    logging.basicConfig(level=logging.INFO)
    print("FortunoBet FINAL is Online...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())