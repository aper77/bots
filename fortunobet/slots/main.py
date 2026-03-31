import logging
import asyncio
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import Command, CommandObject
from aiogram.types import LabeledPrice, PreCheckoutQuery, Message, InlineKeyboardButton, InlineKeyboardMarkup

# --- CONFIGURATION ---
# Your provided Token and ID
TOKEN = "8767986301:AAHpaeLqV0RG-2I5rYn3T18o9LFSOJoGqfI"
ADMIN_ID = 1002853287489 

# Win logic based on Telegram's 1-64 dice values
CHANCE_777 = 64        # Jackpot
CHANCE_BAR = 1         # Medium Win
CHANCE_FRUIT = [16, 22, 43, 48] # Small Wins

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Simple Database (In production, use SQLite)
user_data = {} 

# --- BRANDED TEXTS ---
START_TEXT = (
    "🎰 **WELCOME TO FORTUNOBET SLOTS** 🎰\n\n"
    "The most **aggressive** high-RTP slots on Telegram. "
    "Designed for 600+ pro gamblers.\n\n"
    "💰 **Provably Fair:** Telegram RNG engine.\n"
    "🚀 **Instant Play:** No slow deposit wait times.\n"
    "🎁 **Bonus:** New players get 1 free spin!"
)

# --- START & REFERRAL SYSTEM ---
@dp.message(Command("start"))
async def cmd_start(message: Message, command: CommandObject):
    user_id = message.from_user.id
    
    if user_id not in user_data:
        user_data[user_id] = {"spins": 1} # 1 Free welcome spin
        
        # Handle Referrals
        if command.args:
            try:
                ref_id = int(command.args)
                if ref_id in user_data and ref_id != user_id:
                    user_data[ref_id]["spins"] += 5
                    await bot.send_message(ref_id, "🎊 **New Referral!** You earned +5 FREE SPINS!")
            except ValueError:
                pass

    ref_link = f"https://t.me/{(await bot.get_me()).username}?start={user_id}"
    
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🎰 SPIN (1 Credit)", callback_data="spin")],
        [InlineKeyboardButton(text="💎 BUY 100 SPINS (10 Stars)", callback_data="buy")],
        [InlineKeyboardButton(text="📢 INVITE FRIENDS", url=f"https://t.me/share/url?url={ref_link}")]
    ])
    
    await message.answer(START_TEXT, reply_markup=kb, parse_mode="Markdown")

# --- THE HIDDEN ROUTE (ADMIN ONLY) ---
@dp.message(Command("gift"))
async def admin_gift(message: Message):
    if message.from_user.id != ADMIN_ID:
        return 

    try:
        # Command format: /gift [user_id] [amount]
        args = message.text.split()
        target_id = int(args[1])
        amount = int(args[2])
        
        if target_id not in user_data:
            user_data[target_id] = {"spins": 0}
            
        user_data[target_id]["spins"] += amount
        await message.answer(f"✅ Gifted {amount} spins to {target_id}")
        await bot.send_message(target_id, f"🎁 **FORTUNOBET ADMIN GIFT:** You received {amount} FREE SPINS!")
    except Exception:
        await message.answer("Error! Use: `/gift [user_id] [amount]`")

# --- STARS PAYMENT ---
@dp.callback_query(F.data == "buy")
async def process_buy(callback: types.CallbackQuery):
    await bot.send_invoice(
        callback.message.chat.id,
        title="100 Fortuno Credits",
        description="High RTP Credits for FortunoBet Slots.",
        payload="buy_100",
        provider_token="", # Stars needs no token
        currency="XTR",
        prices=[LabeledPrice(label="100 Spins", amount=10)]
    )

@dp.pre_checkout_query()
async def process_pre_checkout(query: PreCheckoutQuery):
    await query.answer(ok=True)

@dp.message(F.successful_payment)
async def on_success_pay(message: Message):
    user_id = message.from_user.id
    user_data[user_id]["spins"] = user_data.get(user_id, {}).get("spins", 0) + 100
    await message.answer("✅ **Success!** 100 Spins added. Go hit the Jackpot!")

# --- GAME ENGINE ---
@dp.callback_query(F.data == "spin")
async def play_slots(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    
    if user_data.get(user_id, {}).get("spins", 0) < 1:
        await callback.answer("❌ Out of spins! Buy more or invite friends.", show_alert=True)
        return

    user_data[user_id]["spins"] -= 1
    msg = await callback.message.answer_dice(emoji="🎰")
    value = msg.dice.value
    
    await asyncio.sleep(2.5) # Wait for reels

    if value == CHANCE_777:
        user_data[user_id]["spins"] += 500
        await callback.message.answer("🔥 **JACKPOT 7-7-7!** You won 500 SPINS! 🔥")
    elif value == CHANCE_BAR:
        user_data[user_id]["spins"] += 100
        await callback.message.answer("💎 **BAR WIN!** You won 100 SPINS!")
    elif value in CHANCE_FRUIT:
        user_data[user_id]["spins"] += 10
        await callback.message.answer("✨ **FRUIT WIN!** +10 Spins added!")
    else:
        await callback.message.answer(f"No win. Spins left: {user_data[user_id]['spins']}")

async def main():
    logging.basicConfig(level=logging.INFO)
    print("FortunoBet is Online...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())