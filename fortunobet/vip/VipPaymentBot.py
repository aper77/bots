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



    """
FORTUNOBET AUTO-POSTER BOT v3.0
================================
- Fetches odds → picks best match → sends post WITH IMAGE to VIP channel
- Images: football.jpeg / tennis.jpeg / basketball.png (same folder as script)
- Schedule (Armenia UTC+4):
    12:00 Armenia = 09:00 Nigeria  → Morning post
    00:00 Armenia = 21:00 Nigeria  → Evening post (PEAK)

SETUP:
    pip install requests python-telegram-bot apscheduler

PUT THESE FILES IN SAME FOLDER AS THIS SCRIPT:
    football.jpeg
    tennis.jpeg
    basketball.png
"""

import requests
import asyncio
import random
import logging
import os
from datetime import datetime, timezone, timedelta
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from telegram import Bot, InputMediaPhoto
from telegram.constants import ParseMode

# ============================================================
# CONFIG
# ============================================================

ODDS_API_KEY   = "bd55794e7bf843f14ab61e3521a8023a"
BOT_TOKEN      = "8643569826:AAE6i7qJABI6OwexCLn7ohTOWwi2tU88-dg"
VIP_CHANNEL_ID = -1003729457344
REF_CODE       = "z4m5"
PROMO_CODE     = "fortunobet"

# Image files — must be in same folder as this script
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

SPORT_IMAGES = {
    "soccer":     os.path.join(SCRIPT_DIR, "football.jpeg"),
    "tennis":     os.path.join(SCRIPT_DIR, "tennis.jpeg"),
    "basketball": os.path.join(SCRIPT_DIR, "basketball.png"),
    "default":    os.path.join(SCRIPT_DIR, "football.jpeg"),
}

# Sport betting links
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
# SPORT PRIORITY — Football first for Nigeria/Ghana
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
# ODDS API
# ============================================================

def american_to_decimal(american: int) -> float:
    if american > 0:
        return round((american / 100) + 1, 3)
    else:
        return round((100 / abs(american)) + 1, 3)


def fetch_odds(sport_key: str) -> list:
    url = f"https://api.the-odds-api.com/v4/sports/{sport_key}/odds"
    params = {
        "apiKey": ODDS_API_KEY,
        "regions": "eu",
        "markets": "h2h",
        "oddsFormat": "decimal",
        "dateFormat": "iso",
    }
    try:
        r = requests.get(url, params=params, timeout=10)
        if r.status_code == 200:
            return r.json()
        log.warning(f"API {r.status_code} for {sport_key}")
        return []
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
        if r.status_code == 200:
            return [s["key"] for s in r.json() if s.get("active")]
        return []
    except Exception as e:
        log.error(f"Sports list error: {e}")
        return []

# ============================================================
# MATCH SELECTOR
# ============================================================

def get_sport_category(sport_key: str) -> str:
    if "soccer" in sport_key:
        return "soccer"
    elif "tennis" in sport_key:
        return "tennis"
    elif "basketball" in sport_key:
        return "basketball"
    return "default"


def get_best_pick(matches: list, exclude_id: str = None) -> dict | None:
    now = datetime.now(timezone.utc)
    candidates = []

    for match in matches:
        if exclude_id and match.get("id") == exclude_id:
            continue

        bookmakers = match.get("bookmakers", [])
        if not bookmakers:
            continue

        try:
            commence = datetime.fromisoformat(
                match["commence_time"].replace("Z", "+00:00")
            )
        except Exception:
            continue

        if commence <= now:
            continue

        outcome_prices: dict[str, list[float]] = {}
        for bm in bookmakers:
            for market in bm.get("markets", []):
                if market["key"] != "h2h":
                    continue
                for outcome in market["outcomes"]:
                    name  = outcome["name"]
                    price = outcome["price"]
                    if isinstance(price, (int, float)) and price > 10:
                        decimal = float(price)
                    elif isinstance(price, int):
                        decimal = american_to_decimal(price)
                    else:
                        decimal = float(price)
                    outcome_prices.setdefault(name, []).append(decimal)

        if not outcome_prices:
            continue

        avg_odds = {
            team: round(sum(p) / len(p), 2)
            for team, p in outcome_prices.items()
        }

        favorite    = min(avg_odds, key=avg_odds.get)
        fav_odds    = avg_odds[favorite]
        hours_until = (commence - now).total_seconds() / 3600

        if not (MIN_ODDS <= fav_odds <= MAX_ODDS):
            continue
        if hours_until < 0.5:
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

    good = [c for c in candidates if 2 <= c["hours_until"] <= 20]
    pool = good if good else candidates
    pool.sort(key=lambda c: abs(c["pick_odds"] - 1.55))
    return pool[0]


def find_best_match(exclude_id: str = None) -> dict | None:
    log.info("Finding best match...")

    for sport_key in SPORT_PRIORITY:
        matches = fetch_odds(sport_key)
        if not matches:
            continue
        pick = get_best_pick(matches, exclude_id=exclude_id)
        if pick:
            log.info(f"Pick: {pick['pick']} @ {pick['pick_odds']} ({sport_key})")
            return pick

    log.info("Trying fallback sports...")
    active = fetch_active_sports()
    for cat in SPORT_CATEGORY_PRIORITY:
        for sport_key in active:
            if sport_key in SPORT_PRIORITY or cat not in sport_key:
                continue
            matches = fetch_odds(sport_key)
            if not matches:
                continue
            pick = get_best_pick(matches, exclude_id=exclude_id)
            if pick:
                log.info(f"Fallback: {pick['pick']} ({sport_key})")
                return pick

    log.warning("No match found.")
    return None

# ============================================================
# POST GENERATOR
# ============================================================

def format_match_time(dt: datetime) -> str:
    nigeria_time = dt + timedelta(hours=1)
    return nigeria_time.strftime("%I:%M %p Nigeria time")


def build_odds_block(pick: dict) -> str:
    lines = []
    for team, odds in sorted(pick["all_odds"].items(), key=lambda x: x[1]):
        if team == pick["pick"]:
            lines.append(f"✅ {team} — {odds}")
        else:
            lines.append(f"     {team} — {odds}")
    return "\n".join(lines)


def generate_morning_post(pick: dict) -> str:
    emoji      = SPORT_EMOJIS.get(pick["sport_cat"], "🏆")
    link       = SPORT_LINKS.get(pick["sport_cat"], SPORT_LINKS["default"])
    deposit    = random.choice(DEPOSIT_OFFERS)
    bet_amount = random.choice(BET_AMOUNTS)
    match_time = format_match_time(pick["commence"])
    opener     = random.choice(BET_OPENERS_MORNING).format(pick=pick["pick"])
    analysis   = random.choice(ANALYSIS_LINES).format(pick=pick["pick"])
    challenge  = random.choice(CHALLENGE_LINES)
    cta        = random.choice(CTA_LABELS)
    odds_block = build_odds_block(pick)

    return (
        f"{emoji} <b>{opener}</b>\n"
        f"\n"
        f"<b>{pick['away_team']} vs {pick['home_team']}</b>\n"
        f"{pick['sport_title']} | {match_time}\n"
        f"\n"
        f"{odds_block}\n"
        f"\n"
        f"{analysis}\n"
        f"{bet_amount} placed on <b>{pick['pick']}</b> @ {pick['pick_odds']}. 💸\n"
        f"\n"
        f"{challenge}\n"
        f"\n"
        f"Deposit {deposit[0]} → play with {deposit[1]}\n"
        f"🔑 Code: <code>{PROMO_CODE}</code>\n"
        f"\n"
        f"👉 <b>{cta}</b>\n"
        f"{link}"
    )


def generate_evening_post(pick: dict, morning_pick: dict = None) -> str:
    emoji      = SPORT_EMOJIS.get(pick["sport_cat"], "🏆")
    link       = SPORT_LINKS.get(pick["sport_cat"], SPORT_LINKS["default"])
    deposit    = random.choice(DEPOSIT_OFFERS)
    bet_amount = random.choice(BET_AMOUNTS)
    match_time = format_match_time(pick["commence"])
    opener     = random.choice(BET_OPENERS_EVENING)
    analysis   = random.choice(ANALYSIS_LINES).format(pick=pick["pick"])
    challenge  = random.choice(CHALLENGE_LINES)
    cta        = random.choice(CTA_LABELS)
    odds_block = build_odds_block(pick)

    morning_ref = ""
    if morning_pick:
        morning_ref = (
            f"📌 Morning pick: <b>{morning_pick['pick']}</b> "
            f"@ {morning_pick['pick_odds']} — check the result! ✅\n\n"
        )

    return (
        f"{emoji} <b>{opener}</b>\n"
        f"\n"
        f"{morning_ref}"
        f"<b>{pick['away_team']} vs {pick['home_team']}</b>\n"
        f"{pick['sport_title']} | {match_time}\n"
        f"\n"
        f"{odds_block}\n"
        f"\n"
        f"{analysis}\n"
        f"{bet_amount} on <b>{pick['pick']}</b> @ {pick['pick_odds']}. 🔥\n"
        f"\n"
        f"{challenge}\n"
        f"\n"
        f"Deposit {deposit[0]} → play with {deposit[1]}\n"
        f"🔑 Code: <code>{PROMO_CODE}</code>\n"
        f"\n"
        f"👉 <b>{cta}</b>\n"
        f"{link}"
    )

# ============================================================
# TELEGRAM — Send photo + caption
# ============================================================

async def send_to_vip(text: str, sport_cat: str):
    bot        = Bot(token=BOT_TOKEN)
    image_path = SPORT_IMAGES.get(sport_cat, SPORT_IMAGES["default"])

    # Telegram caption limit is 1024 chars
    caption = text[:1024]

    try:
        if os.path.exists(image_path):
            with open(image_path, "rb") as photo:
                await bot.send_photo(
                    chat_id=VIP_CHANNEL_ID,
                    photo=photo,
                    caption=caption,
                    parse_mode=ParseMode.HTML,
                )
            log.info(f"✅ Photo post sent ({sport_cat} image).")
        else:
            # Fallback: send text only if image file missing
            log.warning(f"Image not found: {image_path}. Sending text only.")
            await bot.send_message(
                chat_id=VIP_CHANNEL_ID,
                text=text,
                parse_mode=ParseMode.HTML,
                disable_web_page_preview=True,
            )
            log.info("✅ Text post sent (no image).")
    except Exception as e:
        log.error(f"Telegram error: {e}")

# ============================================================
# STATE
# ============================================================

_morning_pick: dict | None = None

# ============================================================
# JOBS
# ============================================================

async def morning_job():
    global _morning_pick
    log.info("=== MORNING JOB (12:00 Armenia = 09:00 Nigeria) ===")
    pick = find_best_match()
    if not pick:
        log.warning("No pick found. Skipping.")
        return
    _morning_pick = pick
    post = generate_morning_post(pick)
    await send_to_vip(post, pick["sport_cat"])


async def evening_job():
    global _morning_pick
    log.info("=== EVENING JOB (00:00 Armenia = 21:00 Nigeria PEAK) ===")
    exclude = _morning_pick["match_id"] if _morning_pick else None
    pick    = find_best_match(exclude_id=exclude)
    if not pick:
        log.warning("No pick found. Skipping.")
        return
    post = generate_evening_post(pick, morning_pick=_morning_pick)
    await send_to_vip(post, pick["sport_cat"])


async def test_job():
    """One-time test post sent immediately — remove after testing"""
    log.info("=== TEST POST (one-time) ===")
    pick = find_best_match()
    if not pick:
        log.warning("No pick found for test.")
        return
    post = generate_morning_post(pick)
    log.info("--- POST PREVIEW ---\n" + post)
    await send_to_vip(post, pick["sport_cat"])
    log.info("✅ Test post sent to VIP channel!")

# ============================================================
# MAIN
# ============================================================

async def main():
    log.info("🚀 Fortunobet Auto-Poster v3.0 starting...")

    # Verify images exist on startup
    for sport, path in SPORT_IMAGES.items():
        if os.path.exists(path):
            log.info(f"✅ Image found: {sport} → {path}")
        else:
            log.warning(f"⚠️  Image MISSING: {sport} → {path}")

    scheduler = AsyncIOScheduler(timezone="Asia/Yerevan")

    # ── Regular schedule ──────────────────────────────────────
    # 12:00 Armenia = 09:00 Nigeria
    scheduler.add_job(morning_job, "cron", hour=12, minute=0, id="morning")

    # 00:00 Armenia = 21:00 Nigeria PEAK
    scheduler.add_job(evening_job, "cron", hour=0,  minute=0, id="evening")

    # ── ONE-TIME TEST POST at 14:59 Armenia today ─────────────
    # Remove or comment out this block after first test
    now_armenia = datetime.now(timezone(timedelta(hours=4)))
    test_time   = now_armenia.replace(hour=14, minute=59, second=0, microsecond=0)
    if now_armenia < test_time:
        scheduler.add_job(
            test_job,
            "date",
            run_date=test_time,
            id="test_post",
            timezone="Asia/Yerevan"
        )
        log.info(f"🧪 Test post scheduled for 14:59 Armenia time today.")
    else:
        log.info("⚠️  14:59 Armenia already passed today. Test post skipped.")
        log.info("    To test manually run: python test_post.py")

    scheduler.start()
    log.info("Scheduler running.")
    log.info("Regular schedule: 12:00 (morning) | 00:00 (peak night) Armenia time")

    try:
        while True:
            await asyncio.sleep(60)
    except (KeyboardInterrupt, SystemExit):
        log.info("Shutdown.")
        scheduler.shutdown()


if __name__ == "__main__":
    asyncio.run(main())