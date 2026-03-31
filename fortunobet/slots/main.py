import logging
import asyncio
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import Command, CommandObject
from aiogram.types import LabeledPrice, PreCheckoutQuery, Message, InlineKeyboardButton, InlineKeyboardMarkup

# --- CONFIGURATION ---
TOKEN = "8767986301:AAHpaeLqV0RG-2I5rYn3T18o9LFSOJoGqfI"
ADMIN_ID = 1002853287489 

# Win logic
CHANCE_777 = 64        
CHANCE_BAR = 1         
CHANCE_FRUIT = [16, 22, 43, 48] 

bot = Bot(token=TOKEN)
dp = Dispatcher()
user_data = {} 

# --- START MESSAGE ---
@dp.message(Command("start"))
async def cmd_start(message: Message, command: CommandObject):
    user_id = message.from_user.id
    if user_id not in user_data:
        user_data[user_id] = {"spins": 5} # Increased to 5 free spins so they can test!
        if command.args:
            try:
                ref_id = int(command.args)
                if ref_id in user_data and ref_id != user_id:
                    user_data[ref_id]["spins"] += 5
                    await bot.send_message(ref_id, "🎊 **New Referral!** You earned +5 FREE SPINS!")
            except ValueError: pass

    ref_link = f"https://t.me/{(await bot.get_me()).username}?start={user_id}"
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🎰 SPIN (1 Credit)", callback_data="spin")],
        [InlineKeyboardButton(text="💎 BUY 100 SPINS (10 Stars)", callback_data="buy")],
        [InlineKeyboardButton(text="📢 INVITE FRIENDS", url=f"https://t.me/share/url?url={ref_link}")]
    ])
    
    await message.answer("🎰 **WELCOME TO FORTUNOBET SLOTS** 🎰\n\nHigh RTP. Big Wins. Fast Action.\n\n💰 **Balance:** " + str(user_data[user_id]['spins']) + " Spins", reply_markup=kb, parse_mode="Markdown")

# --- ADMIN GIFT ---
@dp.message(Command("gift"))
async def admin_gift(message: Message):
    if message.from_user.id != ADMIN_ID: return 
    try:
        args = message.text.split()
        target_id, amount = int(args[1]), int(args[2])
        if target_id not in user_data: user_data[target_id] = {"spins": 0}
        user_data[target_id]["spins"] += amount
        await message.answer(f"✅ Gifted {amount} to {target_id}")
    except Exception: await message.answer("Use: `/gift [id] [amount]`")

# --- PAYMENTS ---
@dp.callback_query(F.data == "buy")
async def process_buy(callback: types.CallbackQuery):
    await bot.send_invoice(callback.message.chat.id, title="100 Credits", description="FortunoBet Slots", payload="buy_100", provider_token="", currency="XTR", prices=[LabeledPrice(label="100 Spins", amount=10)])

@dp.pre_checkout_query()
async def process_pre_checkout(q: PreCheckoutQuery): await q.answer(ok=True)

@dp.message(F.successful_payment)
async def on_success_pay(m: Message):
    user_data[m.from_user.id]["spins"] += 100
    await m.answer("✅ 100 Spins added!")

# --- GAME ENGINE (FIXED FOR CONTINUOUS PLAY) ---
@dp.callback_query(F.data == "spin")
async def play_slots(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    if user_data.get(user_id, {}).get("spins", 0) < 1:
        await callback.answer("❌ Out of spins!", show_alert=True)
        return

    user_data[user_id]["spins"] -= 1
    msg = await callback.message.answer_dice(emoji="🎰")
    await asyncio.sleep(2.5) 

    value = msg.dice.value
    win_text = "❌ No win."
    if value == CHANCE_777:
        user_data[user_id]["spins"] += 500
        win_text = "🔥 **JACKPOT 7-7-7!** +500 SPINS!"
    elif value == CHANCE_BAR:
        user_data[user_id]["spins"] += 100
        win_text = "💎 **BAR WIN!** +100 SPINS!"
    elif value in CHANCE_FRUIT:
        user_data[user_id]["spins"] += 10
        win_text = "✨ **FRUIT WIN!** +10 SPINS!"

    # --- THE FIX: ADD KEYBOARD HERE ---
    repeat_kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🎰 SPIN AGAIN", callback_data="spin")],
        [InlineKeyboardButton(text="💎 BUY SPINS", callback_data="buy")]
    ])

    await callback.message.answer(
        f"{win_text}\n💰 **Spins left:** {user_data[user_id]['spins']}",
        reply_markup=repeat_kb,
        parse_mode="Markdown"
    )

async def main():
    print("FortunoBet is Online...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())