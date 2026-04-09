# import asyncio
# from telegram import Update, LabeledPrice, InlineKeyboardButton, InlineKeyboardMarkup
# from telegram.ext import Application, CommandHandler, PreCheckoutQueryHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler

# # ====== CONFIG ======
# VIP_TOKEN = "8643569826:AAE6i7qJABI6OwexCLn7ohTOWwi2tU88-dg"
# VIP_CHANNEL_ID = -1003729457344

# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     keyboard = [
#         [InlineKeyboardButton("⚡ 7 Days - 150 Stars ($3)", callback_data='pay_weekly')],
#         [InlineKeyboardButton("💎 30 Days - 500 Stars ($10)", callback_data='pay_monthly')]
#     ]
#     reply_markup = InlineKeyboardMarkup(keyboard)
    
#     await update.message.reply_text(
#         "💎 <b>FORTUNOBET VIP ACCESS</b>\n\n"
#         "🎯 <b>What You Get:</b>\n"
#         "• Premium betting tips daily\n"
#         "• Higher odds selections\n"
#         "• Early access to best games\n"
#         "• Telegram support\n\n"
#         "📊 <b>How It Works:</b>\n"
#         "• Free channel: Basic tips\n"
#         "• VIP channel: Premium selections\n"
#         "• Posted when quality games available\n"
#         "• 1-5 tips per day depending on matches\n\n"
#         "⚡ <b>Choose your access:</b>",
#         reply_markup=reply_markup,
#         parse_mode="HTML"
#     )

# async def handle_payment(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     query = update.callback_query
#     await query.answer()
    
#     if query.data == 'pay_weekly':
#         title = "VIP Weekly Access"
#         desc = "7 days of premium betting tips"
#         price = 150
#         payload = "weekly"
#         duration = "7 days"
#     else:
#         title = "VIP Monthly Access"
#         desc = "30 days of premium betting tips"
#         price = 500
#         payload = "monthly"
#         duration = "30 days"

#     await query.edit_message_text(
#         f"💎 <b>{title}</b>\n\n"
#         f"✅ {duration} of VIP access\n"
#         f"✅ Premium betting tips\n"
#         f"✅ Higher odds selections\n"
#         f"✅ Early access to best games\n"
#         f"✅ Telegram support\n\n"
#         f"💰 <b>Price: {price} Stars (${price/50:.0f})</b>\n\n"
#         f"👇 Tap button below to pay:",
#         parse_mode="HTML"
#     )
    
#     await context.bot.send_invoice(
#         chat_id=query.message.chat_id,
#         title=title,
#         description=desc,
#         payload=payload,
#         provider_token="", 
#         currency="XTR", 
#         prices=[LabeledPrice(title, price)]
#     )

# async def precheckout_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.pre_checkout_query.answer(ok=True)

# async def successful_payment_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     # Create single-use invite link
#     invite_link = await context.bot.create_chat_invite_link(
#         chat_id=VIP_CHANNEL_ID, 
#         member_limit=1
#     )
    
#     # Determine duration from payload
#     payload = update.message.successful_payment.invoice_payload
#     duration = "7 days" if payload == "weekly" else "30 days"
    
#     await update.message.reply_text(
#         f"✅ <b>PAYMENT CONFIRMED!</b>\n\n"
#         f"🎯 Your {duration} VIP access is ready!\n\n"
#         f"👇 <b>JOIN NOW:</b>\n"
#         f"{invite_link.invite_link}\n\n"
#         f"💚 Welcome to VIP channel!",
#         parse_mode="HTML"
#     )
    
#     # Send welcome message to VIP channel
#     try:
#         await context.bot.send_message(
#             chat_id=VIP_CHANNEL_ID,
#             text=f"💎 <b>NEW VIP MEMBER!</b>\n\n"
#                  f"Welcome @{update.message.from_user.username or 'Member'}!\n"
#                  f"Access: {duration}\n\n"
#                  f"Enjoy premium tips! 🔥",
#             parse_mode="HTML"
#         )
#     except:
#         pass

# def main():
#     app = Application.builder().token(VIP_TOKEN).build()
    
#     app.add_handler(CommandHandler("start", start))
#     app.add_handler(CallbackQueryHandler(handle_payment))
#     app.add_handler(PreCheckoutQueryHandler(precheckout_callback))
#     app.add_handler(MessageHandler(filters.SUCCESSFUL_PAYMENT, successful_payment_callback))
    
#     print("💎 FortunoBet VIP Payment Bot is LIVE!")
#     print("Bot: @FortunoVIPbot")
#     print("VIP Channel ID:", VIP_CHANNEL_ID)
#     app.run_polling()

# if __name__ == "__main__":
#     main()


    # https://api.telegram.org/bot8643569826:AAE6i7qJABI6OwexCLn7ohTOWwi2tU88-dg/getMyStarBalance



import asyncio
import requests
import random
import logging
import os
from datetime import datetime, timezone, timedelta
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from telegram import Bot, Update, LabeledPrice, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, PreCheckoutQueryHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler
from telegram.constants import ParseMode

# ============================================================
# CONFIG
# ============================================================

VIP_TOKEN      = "8643569826:AAE6i7qJABI6OwexCLn7ohTOWwi2tU88-dg"
VIP_CHANNEL_ID = -1003729457344
ODDS_API_KEY   = "bd55794e7bf843f14ab61e3521a8023a"
REF_CODE       = "z4m5"
PROMO_CODE     = "fortunobet"

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

SPORT_IMAGES = {
    "soccer":     os.path.join(SCRIPT_DIR, "football.jpeg"),
    "tennis":     os.path.join(SCRIPT_DIR, "tennis.jpeg"),
    "basketball": os.path.join(SCRIPT_DIR, "basketball.png"),
    "default":    os.path.join(SCRIPT_DIR, "football.jpeg"),
}

SPORT_LINKS = {
    "soccer":     f"https://one-vv858.com/betting/prematch/soccer-18?p={REF_CODE}",
    "tennis":     f"https://one-vv858.com/betting/live/tennis-33?p={REF_CODE}",
    "basketball": f"https://one-vv858.com/betting/prematch/basketball-23?p={REF_CODE}",
    "default":    f"https://one-vv858.com/?p={REF_CODE}",
}

MIN_ODDS = 1.15
MAX_ODDS = 2.20

# ============================================================
# LOGGING
# ============================================================

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("autoposter.log"),
        logging.StreamHandler()
    ]
)
log = logging.getLogger(__name__)

# ============================================================
# SPORT PRIORITY
# ============================================================

SPORT_PRIORITY = [
    "soccer_epl",
    "soccer_uefa_champs_league",
    "soccer_uefa_europa_league",
    "soccer_spain_la_liga",
    "soccer_italy_serie_a",
    "soccer_germany_bundesliga",
    "soccer_france_ligue_one",
    "soccer_efl_champ",
    "soccer_turkey_super_league",
    "tennis_atp_monte_carlo_masters",
    "tennis_atp_french_open",
    "tennis_wta_french_open",
    "tennis_atp_us_open",
    "basketball_nba",
    "basketball_euroleague",
]

SPORT_CATEGORY_PRIORITY = ["soccer", "tennis", "basketball"]

# ============================================================
# CONTENT BLOCKS
# ============================================================

DEPOSIT_OFFERS = [
    ("₦500",    "₦3,000"),
    ("₦10,000", "₦60,000"),
    ("₦20,000", "₦120,000"),
    ("₦5,000",  "₦30,000"),
]

BET_AMOUNTS = ["$100", "$50", "$200", "$150"]

BET_OPENERS_MORNING = [
    "I just placed my bet. {pick} is my pick today.",
    "Bet locked in. Going with {pick} this morning.",
    "Just placed {pick}. Match starting later today.",
    "My bet is in — {pick} to win this one.",
    "I studied this match. Placing {pick} now.",
]

BET_OPENERS_EVENING = [
    "Evening pick. My bet is placed. 💸",
    "Just locked my evening bet. Here it is.",
    "I am betting tonight. Here is my pick.",
    "Evening selection is in. Follow me on this one.",
    "My night pick is placed. Join me. 🔥",
]

ANALYSIS_LINES = [
    "{pick} has the better form right now. Clear pick for me.",
    "Looked at this carefully. {pick} is the right side.",
    "{pick} is strong here. Bookmakers agree. I am going in.",
    "My analysis is simple — {pick} wins this. Confident.",
    "Numbers are clear. {pick} is where the value is today.",
    "I watched the odds move. {pick} is my pick. No doubt.",
    "{pick} has been consistent. I am backing them tonight.",
]

CHALLENGE_LINES = [
    "STOP WATCHING. Start winning. 🔥",
    "You're still watching? Join me on this one.",
    "Smart people follow. Scared people watch. 🔥",
    "They followed Monday. Already in profit. You still watching?",
    "Stop doubting. Start winning with me.",
    "How many more wins before you join? 🔥",
    "Are you in or still watching from the side?",
    "My followers are winning. You can too. 🔥",
]

CTA_LABELS = [
    "Follow my bet NOW:",
    "Place your bet:",
    "Bet NOW:",
    "Join me:",
    "Follow NOW:",
]

SPORT_EMOJIS = {
    "soccer":     "⚽",
    "tennis":     "🎾",
    "basketball": "🏀",
    "default":    "🏆",
}

# ============================================================
# VIP PAYMENT BOT HANDLERS
# ============================================================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("⚡ 7 Days - 150 Stars ($3)", callback_data='pay_weekly')],
        [InlineKeyboardButton("💎 30 Days - 500 Stars ($10)", callback_data='pay_monthly')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "💎 <b>FORTUNOBET VIP ACCESS</b>\n\n"
        "🎯 <b>What You Get:</b>\n"
        "• Premium betting tips daily\n"
        "• Higher odds selections\n"
        "• Early access to best games\n"
        "• Telegram support\n\n"
        "📊 <b>How It Works:</b>\n"
        "• Free channel: Basic tips\n"
        "• VIP channel: Premium selections\n"
        "• Posted when quality games available\n"
        "• 1-5 tips per day depending on matches\n\n"
        "⚡ <b>Choose your access:</b>",
        reply_markup=reply_markup,
        parse_mode="HTML"
    )


async def handle_payment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == 'pay_weekly':
        title    = "VIP Weekly Access"
        desc     = "7 days of premium betting tips"
        price    = 150
        payload  = "weekly"
        duration = "7 days"
    else:
        title    = "VIP Monthly Access"
        desc     = "30 days of premium betting tips"
        price    = 500
        payload  = "monthly"
        duration = "30 days"

    await query.edit_message_text(
        f"💎 <b>{title}</b>\n\n"
        f"✅ {duration} of VIP access\n"
        f"✅ Premium betting tips\n"
        f"✅ Higher odds selections\n"
        f"✅ Early access to best games\n"
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
    invite_link = await context.bot.create_chat_invite_link(
        chat_id=VIP_CHANNEL_ID,
        member_limit=1
    )
    payload  = update.message.successful_payment.invoice_payload
    duration = "7 days" if payload == "weekly" else "30 days"

    await update.message.reply_text(
        f"✅ <b>PAYMENT CONFIRMED!</b>\n\n"
        f"🎯 Your {duration} VIP access is ready!\n\n"
        f"👇 <b>JOIN NOW:</b>\n"
        f"{invite_link.invite_link}\n\n"
        f"💚 Welcome to VIP channel!",
        parse_mode="HTML"
    )

    try:
        await context.bot.send_message(
            chat_id=VIP_CHANNEL_ID,
            text=f"💎 <b>NEW VIP MEMBER!</b>\n\n"
                 f"Welcome @{update.message.from_user.username or 'Member'}!\n"
                 f"Access: {duration}\n\n"
                 f"Enjoy premium tips! 🔥",
            parse_mode="HTML"
        )
    except Exception:
        pass

# ============================================================
# ODDS API
# ============================================================

def american_to_decimal(american: int) -> float:
    if american > 0:
        return round((american / 100) + 1, 3)
    else:
        return round((100 / abs(american)) + 1, 3)


def fetch_odds(sport_key: str) -> list:
    try:
        r = requests.get(
            f"https://api.the-odds-api.com/v4/sports/{sport_key}/odds",
            params={
                "apiKey": ODDS_API_KEY,
                "regions": "eu",
                "markets": "h2h",
                "oddsFormat": "decimal",
                "dateFormat": "iso",
            },
            timeout=10
        )
        return r.json() if r.status_code == 200 else []
    except Exception as e:
        log.error(f"Fetch error {sport_key}: {e}")
        return []


def fetch_active_sports() -> list:
    try:
        r = requests.get(
            "https://api.the-odds-api.com/v4/sports",
            params={"apiKey": ODDS_API_KEY},
            timeout=10
        )
        return [s["key"] for s in r.json() if s.get("active")] if r.status_code == 200 else []
    except Exception as e:
        log.error(f"Sports list error: {e}")
        return []

# ============================================================
# MATCH SELECTOR
# ============================================================

def get_sport_category(sport_key: str) -> str:
    if "soccer"     in sport_key: return "soccer"
    if "tennis"     in sport_key: return "tennis"
    if "basketball" in sport_key: return "basketball"
    return "default"


def get_best_pick(matches: list, exclude_id: str = None) -> dict | None:
    now = datetime.now(timezone.utc)
    candidates = []

    for match in matches:
        if exclude_id and match.get("id") == exclude_id:
            continue
        if not match.get("bookmakers"):
            continue
        try:
            commence = datetime.fromisoformat(match["commence_time"].replace("Z", "+00:00"))
        except Exception:
            continue
        if commence <= now:
            continue

        outcome_prices: dict[str, list[float]] = {}
        for bm in match["bookmakers"]:
            for market in bm.get("markets", []):
                if market["key"] != "h2h":
                    continue
                for outcome in market["outcomes"]:
                    price = outcome["price"]
                    if isinstance(price, (int, float)) and price > 10:
                        decimal = float(price)
                    elif isinstance(price, int):
                        decimal = american_to_decimal(price)
                    else:
                        decimal = float(price)
                    outcome_prices.setdefault(outcome["name"], []).append(decimal)

        if not outcome_prices:
            continue

        avg_odds    = {t: round(sum(p)/len(p), 2) for t, p in outcome_prices.items()}
        favorite    = min(avg_odds, key=avg_odds.get)
        fav_odds    = avg_odds[favorite]
        hours_until = (commence - now).total_seconds() / 3600

        if not (MIN_ODDS <= fav_odds <= MAX_ODDS) or hours_until < 0.5:
            continue

        candidates.append({
            "match_id":    match["id"],
            "sport_key":   match["sport_key"],
            "sport_cat":   get_sport_category(match["sport_key"]),
            "sport_title": match["sport_title"],
            "home_team":   match["home_team"],
            "away_team":   match["away_team"],
            "commence":    commence,
            "pick":        favorite,
            "pick_odds":   fav_odds,
            "all_odds":    avg_odds,
            "hours_until": hours_until,
        })

    if not candidates:
        return None

    pool = [c for c in candidates if 2 <= c["hours_until"] <= 20] or candidates
    pool.sort(key=lambda c: abs(c["pick_odds"] - 1.55))
    return pool[0]


def find_best_match(exclude_id: str = None) -> dict | None:
    log.info("Finding best match...")
    for sport_key in SPORT_PRIORITY:
        matches = fetch_odds(sport_key)
        pick    = get_best_pick(matches, exclude_id=exclude_id)
        if pick:
            log.info(f"Pick: {pick['pick']} @ {pick['pick_odds']} ({sport_key})")
            return pick

    for cat in SPORT_CATEGORY_PRIORITY:
        for sport_key in fetch_active_sports():
            if sport_key in SPORT_PRIORITY or cat not in sport_key:
                continue
            pick = get_best_pick(fetch_odds(sport_key), exclude_id=exclude_id)
            if pick:
                log.info(f"Fallback: {pick['pick']} ({sport_key})")
                return pick

    log.warning("No match found.")
    return None

# ============================================================
# POST GENERATOR
# ============================================================

def format_match_time(dt: datetime) -> str:
    return (dt + timedelta(hours=1)).strftime("%I:%M %p Nigeria time")


def build_odds_block(pick: dict) -> str:
    return "\n".join(
        f"✅ {t} — {o}" if t == pick["pick"] else f"     {t} — {o}"
        for t, o in sorted(pick["all_odds"].items(), key=lambda x: x[1])
    )


def generate_morning_post(pick: dict) -> str:
    emoji   = SPORT_EMOJIS.get(pick["sport_cat"], "🏆")
    link    = SPORT_LINKS.get(pick["sport_cat"], SPORT_LINKS["default"])
    deposit = random.choice(DEPOSIT_OFFERS)
    return (
        f"{emoji} <b>{random.choice(BET_OPENERS_MORNING).format(pick=pick['pick'])}</b>\n\n"
        f"<b>{pick['away_team']} vs {pick['home_team']}</b>\n"
        f"{pick['sport_title']} | {format_match_time(pick['commence'])}\n\n"
        f"{build_odds_block(pick)}\n\n"
        f"{random.choice(ANALYSIS_LINES).format(pick=pick['pick'])}\n"
        f"{random.choice(BET_AMOUNTS)} placed on <b>{pick['pick']}</b> @ {pick['pick_odds']}. 💸\n\n"
        f"{random.choice(CHALLENGE_LINES)}\n\n"
        f"Deposit {deposit[0]} → play with {deposit[1]}\n"
        f"🔑 Code: <code>{PROMO_CODE}</code>\n\n"
        f"👉 <b>{random.choice(CTA_LABELS)}</b>\n"
        f"{link}"
    )


def generate_evening_post(pick: dict, morning_pick: dict = None) -> str:
    emoji   = SPORT_EMOJIS.get(pick["sport_cat"], "🏆")
    link    = SPORT_LINKS.get(pick["sport_cat"], SPORT_LINKS["default"])
    deposit = random.choice(DEPOSIT_OFFERS)
    morning_ref = (
        f"📌 Morning pick: <b>{morning_pick['pick']}</b> @ {morning_pick['pick_odds']} — check the result! ✅\n\n"
        if morning_pick else ""
    )
    return (
        f"{emoji} <b>{random.choice(BET_OPENERS_EVENING)}</b>\n\n"
        f"{morning_ref}"
        f"<b>{pick['away_team']} vs {pick['home_team']}</b>\n"
        f"{pick['sport_title']} | {format_match_time(pick['commence'])}\n\n"
        f"{build_odds_block(pick)}\n\n"
        f"{random.choice(ANALYSIS_LINES).format(pick=pick['pick'])}\n"
        f"{random.choice(BET_AMOUNTS)} on <b>{pick['pick']}</b> @ {pick['pick_odds']}. 🔥\n\n"
        f"{random.choice(CHALLENGE_LINES)}\n\n"
        f"Deposit {deposit[0]} → play with {deposit[1]}\n"
        f"🔑 Code: <code>{PROMO_CODE}</code>\n\n"
        f"👉 <b>{random.choice(CTA_LABELS)}</b>\n"
        f"{link}"
    )

# ============================================================
# TELEGRAM SEND WITH IMAGE
# ============================================================

async def send_to_vip(text: str, sport_cat: str):
    bot        = Bot(token=VIP_TOKEN)
    image_path = SPORT_IMAGES.get(sport_cat, SPORT_IMAGES["default"])
    caption    = text[:1024]
    try:
        if os.path.exists(image_path):
            with open(image_path, "rb") as photo:
                await bot.send_photo(
                    chat_id=VIP_CHANNEL_ID,
                    photo=photo,
                    caption=caption,
                    parse_mode=ParseMode.HTML,
                )
        else:
            log.warning(f"Image missing: {image_path} — sending text only")
            await bot.send_message(
                chat_id=VIP_CHANNEL_ID,
                text=text,
                parse_mode=ParseMode.HTML,
                disable_web_page_preview=True,
            )
        log.info("✅ Post sent.")
    except Exception as e:
        log.error(f"Telegram send error: {e}")

# ============================================================
# SCHEDULER JOBS
# ============================================================

_morning_pick: dict | None = None


async def morning_job():
    global _morning_pick
    log.info("=== MORNING JOB (12:00 Armenia = 09:00 Nigeria) ===")
    pick = find_best_match()
    if not pick:
        log.warning("No pick. Skipping.")
        return
    _morning_pick = pick
    await send_to_vip(generate_morning_post(pick), pick["sport_cat"])


async def evening_job():
    global _morning_pick
    log.info("=== EVENING JOB (00:00 Armenia = 21:00 Nigeria PEAK) ===")
    pick = find_best_match(exclude_id=_morning_pick["match_id"] if _morning_pick else None)
    if not pick:
        log.warning("No pick. Skipping.")
        return
    await send_to_vip(generate_evening_post(pick, morning_pick=_morning_pick), pick["sport_cat"])


async def test_job():
    log.info("=== TEST POST (15:15 Armenia) ===")
    pick = find_best_match()
    if not pick:
        log.warning("No pick for test. Skipping.")
        return
    await send_to_vip(generate_morning_post(pick), pick["sport_cat"])
    log.info("✅ Test post sent!")

# ============================================================
# MAIN — runs VIP bot + scheduler together
# ============================================================

async def main():
    log.info("🚀 Fortunobet VIP Bot + Auto-Poster starting...")

    # Check images
    for sport, path in SPORT_IMAGES.items():
        log.info(f"{'✅' if os.path.exists(path) else '❌ MISSING'} {sport}: {path}")

    # --- Scheduler setup ---
    scheduler = AsyncIOScheduler(timezone="Asia/Yerevan")
    scheduler.add_job(morning_job, "cron", hour=12, minute=0, id="morning")
    scheduler.add_job(evening_job, "cron", hour=0,  minute=0, id="evening")

    # One-time test post at 14:59 Armenia today
    now_armenia = datetime.now(timezone(timedelta(hours=4)))
    test_time   = now_armenia.replace(hour=15, minute=15, second=0, microsecond=0)
    if now_armenia < test_time:
        scheduler.add_job(test_job, "date", run_date=test_time, id="test_post", timezone="Asia/Yerevan")
        log.info("🧪 Test post scheduled: 15:15 Armenia today.")
    else:
        log.warning("⚠️  15:15 Armenia already passed. Test post will not fire today.")

    scheduler.start()
    log.info("Scheduler running: 15:15 test | 12:00 morning | 00:00 peak")

    # --- VIP Payment Bot setup ---
    app = Application.builder().token(VIP_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handle_payment))
    app.add_handler(PreCheckoutQueryHandler(precheckout_callback))
    app.add_handler(MessageHandler(filters.SUCCESSFUL_PAYMENT, successful_payment_callback))

    log.info("💎 VIP Payment Bot starting...")
    log.info(f"VIP Channel ID: {VIP_CHANNEL_ID}")

    # Run both together
    async with app:
        await app.initialize()
        await app.start()
        await app.updater.start_polling()
        log.info("✅ Both systems running!")
        try:
            while True:
                await asyncio.sleep(60)
        except (KeyboardInterrupt, SystemExit):
            log.info("Shutting down...")
        finally:
            scheduler.shutdown()
            await app.updater.stop()
            await app.stop()


if __name__ == "__main__":
    asyncio.run(main())