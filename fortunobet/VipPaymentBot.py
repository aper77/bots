import asyncio
from telegram import Update, LabeledPrice, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, PreCheckoutQueryHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler

# ====== CONFIG ======
VIP_TOKEN = "8643569826:AAE6i7qJABI6OwexCLn7ohTOWwi2tU88-dg"
VIP_CHANNEL_ID = -1003729457344  # <--- Use this exact number

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🎫 1 Week - 150 Stars ($3)", callback_data='pay_weekly')],
        [InlineKeyboardButton("💎 1 Month - 500 Stars ($10)", callback_data='pay_monthly')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "🏆 <b>Welcome to FortunoBet VIP!</b>\n\nSelect your access plan below to get tonight's high-odds tips instantly:",
        reply_markup=reply_markup,
        parse_mode="HTML"
    )

async def handle_payment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == 'pay_weekly':
        title, desc, price, payload = "VIP Weekly Pass", "7 days of premium tips", 150, "weekly"
    else:
        title, desc, price, payload = "VIP Monthly Pass", "30 days of premium tips", 500, "monthly"

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
    invite_link = await context.bot.create_chat_invite_link(chat_id=VIP_CHANNEL_ID, member_limit=1)
    await update.message.reply_text(
        f"✅ <b>Payment Received!</b>\n\nJoin the VIP channel here:\n{invite_link.invite_link}",
        parse_mode="HTML"
    )

def main():
    app = Application.builder().token(VIP_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handle_payment))
    app.add_handler(PreCheckoutQueryHandler(precheckout_callback))
    app.add_handler(MessageHandler(filters.SUCCESSFUL_PAYMENT, successful_payment_callback))
    print("VIP Payment Bot is live...")
    app.run_polling()

if __name__ == "__main__":
    main()