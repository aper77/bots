import asyncio
from telegram import Update, LabeledPrice, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, PreCheckoutQueryHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler

# ====== CONFIG ======
VIP_TOKEN = "8643569826:AAE6i7qJABI6OwexCLn7ohTOWwi2tU88-dg"
VIP_CHANNEL_ID = -1003729457344

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("⚡ 7 Days - 150 Stars ($3)", callback_data='pay_weekly')],
        [InlineKeyboardButton("💎 30 Days - 500 Stars ($10)", callback_data='pay_monthly')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "💎 <b>FORTUNOBET VIP ACCESS</b>\n\n"
        "🎯 <b>What You Get:</b>\n"
        "• 3-5 premium tickets daily\n"
        "• 85%+ accuracy rate\n"
        "• Early access (posted 6pm daily)\n"
        "• Higher odds (3.5-12.0)\n"
        "• Small stakes, big wins\n\n"
        "🔥 <b>Today's VIP Results:</b>\n"
        "Ticket 1: ✅ Won (odds 8.2)\n"
        "Ticket 2: ✅ Won (odds 5.6)\n"
        "Ticket 3: ✅ Won (odds 4.1)\n\n"
        "💰 Last 7 days: 18 wins, 4 losses (82%)\n\n"
        "⚡ <b>Choose your access:</b>",
        reply_markup=reply_markup,
        parse_mode="HTML"
    )

async def handle_payment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == 'pay_weekly':
        title = "VIP Weekly Access"
        desc = "7 days of premium betting tips (85%+ accuracy)"
        price = 150
        payload = "weekly"
        duration = "7 days"
    else:
        title = "VIP Monthly Access"
        desc = "30 days of premium betting tips (85%+ accuracy)"
        price = 500
        payload = "monthly"
        duration = "30 days"

    await query.edit_message_text(
        f"💎 <b>{title}</b>\n\n"
        f"✅ {duration} of VIP access\n"
        f"✅ 3-5 premium tickets daily\n"
        f"✅ 85%+ win rate\n"
        f"✅ Early access 6pm daily\n"
        f"✅ Telegram support\n\n"
        f"💰 <b>Price: {price} Stars (${price/50:.0f})</b>\n\n"
        f"👇 Tap button below to pay:",
        parse_mode="HTML"
    )
    
    await context.bot.send_invoice(
        chat_id=query.message.chat_id,
        title=title,
        description=desc,
        payload=payload,
        provider_token="", 
        currency="XTR", 
        prices=[LabeledPrice(title, price)]
    )

async def precheckout_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.pre_checkout_query.answer(ok=True)

async def successful_payment_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Create single-use invite link
    invite_link = await context.bot.create_chat_invite_link(
        chat_id=VIP_CHANNEL_ID, 
        member_limit=1
    )
    
    # Determine duration from payload
    payload = update.message.successful_payment.invoice_payload
    duration = "7 days" if payload == "weekly" else "30 days"
    
    await update.message.reply_text(
        f"✅ <b>PAYMENT CONFIRMED!</b>\n\n"
        f"🎯 Your {duration} VIP access is ready!\n\n"
        f"👇 <b>JOIN NOW:</b>\n"
        f"{invite_link.invite_link}\n\n"
        f"⚡ Tonight's tips posted at 6pm\n"
        f"💚 Welcome to the winners' circle!",
        parse_mode="HTML"
    )
    
    # Send welcome message to VIP channel
    try:
        await context.bot.send_message(
            chat_id=VIP_CHANNEL_ID,
            text=f"💎 <b>NEW VIP MEMBER!</b>\n\n"
                 f"Welcome @{update.message.from_user.username or 'Member'}!\n"
                 f"Access: {duration}\n\n"
                 f"Tonight's premium tickets posted at 6pm. 🔥",
            parse_mode="HTML"
        )
    except:
        pass

def main():
    app = Application.builder().token(VIP_TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handle_payment))
    app.add_handler(PreCheckoutQueryHandler(precheckout_callback))
    app.add_handler(MessageHandler(filters.SUCCESSFUL_PAYMENT, successful_payment_callback))
    
    print("💎 FortunoBet VIP Payment Bot is LIVE!")
    print("Bot: @FortunoVIPbot")
    print("VIP Channel ID:", VIP_CHANNEL_ID)
    app.run_polling()

if __name__ == "__main__":
    main()