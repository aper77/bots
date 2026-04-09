import asyncio
import requests
import random
import logging
import os
import json
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
ADMIN_ID       = 7627990095

# Prices in Telegram Stars (50 Stars = $1)
WEEKLY_STARS  = 100   # $2
MONTHLY_STARS = 400   # $8

DB_FILE    = os.path.join(os.path.dirname(os.path.abspath(__file__)), "vip_members.json")
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

# Only pick matches starting between 1h and 24h from now
MIN_HOURS_UNTIL_MATCH = 1.0
MAX_HOURS_UNTIL_MATCH = 24.0

MIN_ODDS = 1.15
MAX_ODDS = 2.20

# ============================================================
# ADMIN COMMANDS REFERENCE
# ============================================================
# /stats          — Total members, active, expired, weekly vs monthly
# /members        — Full list with names, plan, days remaining
# /adddays  <user_id> <days>  — Add free days to existing member
# /giveaccess <user_id> <days> — Give free access to new user + invite link
# /help           — Show all commands
#
# Check Stars balance:
# https://api.telegram.org/bot8643569826:AAE6i7qJABI6OwexCLn7ohTOWwi2tU88-dg/getMyStarBalance
# ============================================================

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
# DATABASE
# ============================================================

def db_load() -> dict:
    if not os.path.exists(DB_FILE):
        return {}
    try:
        with open(DB_FILE, "r") as f:
            return json.load(f)
    except Exception:
        return {}


def db_save(data: dict):
    try:
        with open(DB_FILE, "w") as f:
            json.dump(data, f, indent=2)
    except Exception as e:
        log.error(f"DB save error: {e}")


def db_add_member(user_id: int, username: str, plan: str, extra_days: int = 0):
    data    = db_load()
    now     = datetime.now(timezone.utc)
    days    = (7 if plan == "weekly" else 30) + extra_days
    expires = (now + timedelta(days=days)).strftime("%Y-%m-%d %H:%M:%S")
    data[str(user_id)] = {
        "username": username or "Member",
        "plan":     plan,
        "expires":  expires,
        "joined":   now.strftime("%Y-%m-%d %H:%M:%S"),
    }
    db_save(data)
    log.info(f"Member added: {user_id} ({plan}+{extra_days}d) expires {expires}")
    return expires


def db_add_free_days(user_id: int, days: int):
    data = db_load()
    key  = str(user_id)
    if key not in data:
        return None
    now     = datetime.now(timezone.utc)
    current = datetime.strptime(data[key]["expires"], "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc)
    base    = current if current > now else now
    new_exp = (base + timedelta(days=days)).strftime("%Y-%m-%d %H:%M:%S")
    data[key]["expires"] = new_exp
    db_save(data)
    return new_exp


def db_get_expiring_soon() -> list:
    data, now, soon = db_load(), datetime.now(timezone.utc), datetime.now(timezone.utc) + timedelta(hours=24)
    result = []
    for uid, info in data.items():
        try:
            exp = datetime.strptime(info["expires"], "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc)
            if now < exp <= soon:
                result.append({"user_id": int(uid), **info, "expires_dt": exp})
        except Exception:
            continue
    return result


def db_get_expired() -> list:
    data, now = db_load(), datetime.now(timezone.utc)
    result = []
    for uid, info in data.items():
        try:
            exp = datetime.strptime(info["expires"], "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc)
            if exp < now:
                result.append({"user_id": int(uid), **info})
        except Exception:
            continue
    return result


def db_remove_member(user_id: int):
    data = db_load()
    data.pop(str(user_id), None)
    db_save(data)


def db_stats() -> dict:
    data, now = db_load(), datetime.now(timezone.utc)
    active = expired = weekly = monthly = 0
    for info in data.values():
        try:
            exp = datetime.strptime(info["expires"], "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc)
            if exp > now:
                active += 1
                if info.get("plan") == "weekly": weekly += 1
                else: monthly += 1
            else:
                expired += 1
        except Exception:
            continue
    return {"total": len(data), "active": active, "expired": expired, "weekly": weekly, "monthly": monthly}

# ============================================================
# ADMIN COMMANDS
# ============================================================

def is_admin(user_id: int) -> bool:
    return user_id == ADMIN_ID


async def cmd_stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_admin(update.effective_user.id): return
    s    = db_stats()
    data = db_load()
    now  = datetime.now(timezone.utc)
    lines = []
    for uid, info in data.items():
        try:
            exp = datetime.strptime(info["expires"], "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc)
            if exp > now:
                name = f"@{info['username']}" if info.get("username") else f"ID:{uid}"
                lines.append(f"  • {name} — {info.get('plan','?')} — {(exp-now).days}d left")
        except Exception:
            continue
    await update.message.reply_text(
        f"📊 <b>VIP STATISTICS</b>\n\n"
        f"👥 Total ever: {s['total']}\n"
        f"✅ Active now: {s['active']}\n"
        f"❌ Expired: {s['expired']}\n\n"
        f"⚡ Weekly: {s['weekly']}\n"
        f"💎 Monthly: {s['monthly']}\n\n"
        f"<b>Active Members:</b>\n" + ("\n".join(lines) if lines else "  No active members"),
        parse_mode="HTML"
    )


async def cmd_members(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_admin(update.effective_user.id): return
    data = db_load()
    now  = datetime.now(timezone.utc)
    if not data:
        await update.message.reply_text("No members in database.")
        return
    lines = ["<b>ALL VIP MEMBERS:</b>\n"]
    for uid, info in data.items():
        try:
            exp      = datetime.strptime(info["expires"], "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc)
            status   = "✅" if exp > now else "❌"
            days_left = max(0, (exp - now).days)
            name     = f"@{info['username']}" if info.get("username") else f"ID:{uid}"
            lines.append(f"{status} {name} | {info.get('plan','?')} | {days_left}d | ID:{uid}")
        except Exception:
            lines.append(f"❓ ID:{uid}")
    text = "\n".join(lines)
    for i in range(0, len(text), 3500):
        await update.message.reply_text(text[i:i+3500], parse_mode="HTML")


async def cmd_adddays(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_admin(update.effective_user.id): return
    args = context.args
    if not args or len(args) < 2:
        await update.message.reply_text("Usage: /adddays <user_id> <days>\nExample: /adddays 123456789 7")
        return
    try:
        user_id, days = int(args[0]), int(args[1])
    except ValueError:
        await update.message.reply_text("❌ Numbers only.")
        return
    new_exp = db_add_free_days(user_id, days)
    if new_exp:
        try:
            await context.bot.send_message(
                chat_id=user_id,
                text=f"🎁 <b>You received {days} free VIP days!</b>\n\nNew expiry: <b>{new_exp} UTC</b>\n\nEnjoy your picks! 🔥",
                parse_mode="HTML"
            )
        except Exception:
            pass
        await update.message.reply_text(f"✅ Added {days} days to {user_id}\nNew expiry: {new_exp}")
    else:
        await update.message.reply_text(f"⚠️ User {user_id} not found.\nUse /giveaccess {user_id} {days} to add as new member.")


async def cmd_giveaccess(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_admin(update.effective_user.id): return
    args = context.args
    if not args or len(args) < 2:
        await update.message.reply_text("Usage: /giveaccess <user_id> <days>\nExample: /giveaccess 123456789 7")
        return
    try:
        user_id, days = int(args[0]), int(args[1])
    except ValueError:
        await update.message.reply_text("❌ Numbers only.")
        return
    expires = db_add_member(user_id, None, "free", extra_days=days - 7)
    try:
        invite    = await context.bot.create_chat_invite_link(chat_id=VIP_CHANNEL_ID, member_limit=1)
        invite_url = invite.invite_link
    except Exception:
        invite_url = "Could not generate link"
    try:
        await context.bot.send_message(
            chat_id=user_id,
            text=f"🎁 <b>You got {days} days FREE VIP access!</b>\n\n👇 Join now:\n{invite_url}\n\nEnjoy! 🔥",
            parse_mode="HTML"
        )
    except Exception:
        pass
    await update.message.reply_text(f"✅ Gave {days} free days to {user_id}\nExpires: {expires}\nInvite: {invite_url}")


async def cmd_help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_admin(update.effective_user.id): return
    await update.message.reply_text(
        "<b>ADMIN COMMANDS:</b>\n\n"
        "/stats — Statistics summary\n"
        "/members — Full members list\n"
        "/adddays &lt;id&gt; &lt;days&gt; — Add days to existing member\n"
        "/giveaccess &lt;id&gt; &lt;days&gt; — Give free access to new user\n"
        "/help — Show this list\n\n"
        "<b>Examples:</b>\n"
        "/adddays 123456789 7\n"
        "/giveaccess 987654321 3",
        parse_mode="HTML"
    )

# ============================================================
# VIP PAYMENT BOT HANDLERS
# ============================================================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton(f"⚡ 7 Days — {WEEKLY_STARS} Stars ($2)", callback_data='pay_weekly')],
        [InlineKeyboardButton(f"💎 30 Days — {MONTHLY_STARS} Stars ($8)", callback_data='pay_monthly')]
    ]
    await update.message.reply_text(
        "💎 <b>FORTUNOBET VIP ACCESS</b>\n\n"
        "🎯 <b>What You Get:</b>\n"
        "• Premium betting picks daily\n"
        "• Higher odds selections\n"
        "• Real match analysis\n"
        "• Telegram support\n\n"
        "⚡ <b>Choose your access:</b>",
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="HTML"
    )


async def handle_payment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == 'pay_weekly':
        title, desc, price, payload, duration = "VIP Weekly Access", "7 days of premium picks", WEEKLY_STARS, "weekly", "7 days"
    else:
        title, desc, price, payload, duration = "VIP Monthly Access", "30 days of premium picks", MONTHLY_STARS, "monthly", "30 days"
    await query.edit_message_text(
        f"💎 <b>{title}</b>\n\n"
        f"✅ {duration} VIP access\n"
        f"✅ Daily premium picks\n"
        f"✅ Higher odds selections\n"
        f"✅ Telegram support\n\n"
        f"💰 <b>Price: {price} Stars</b>\n\n"
        f"👇 Tap below to pay:",
        parse_mode="HTML"
    )
    await context.bot.send_invoice(
        chat_id=query.message.chat_id,
        title=title, description=desc, payload=payload,
        provider_token="", currency="XTR",
        prices=[LabeledPrice(title, price)]
    )


async def precheckout_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.pre_checkout_query.answer(ok=True)


async def successful_payment_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user     = update.message.from_user
    payload  = update.message.successful_payment.invoice_payload
    plan     = "weekly" if payload == "weekly" else "monthly"
    duration = "7 days" if plan == "weekly" else "30 days"
    expires  = db_add_member(user.id, user.username, plan)
    invite   = await context.bot.create_chat_invite_link(chat_id=VIP_CHANNEL_ID, member_limit=1)
    await update.message.reply_text(
        f"✅ <b>PAYMENT CONFIRMED!</b>\n\n"
        f"🎯 Your {duration} VIP access is ready!\n"
        f"Expires: <b>{expires} UTC</b>\n\n"
        f"👇 <b>JOIN NOW:</b>\n{invite.invite_link}\n\n"
        f"💚 Welcome to Fortunobet VIP!",
        parse_mode="HTML"
    )
    try:
        await context.bot.send_message(
            chat_id=VIP_CHANNEL_ID,
            text=f"💎 <b>NEW VIP MEMBER!</b>\n\nWelcome @{user.username or 'Member'}!\nPlan: {duration}\n\nEnjoy! 🔥",
            parse_mode="HTML"
        )
    except Exception:
        pass

# ============================================================
# REMINDER + KICK JOBS
# ============================================================

async def reminder_job():
    log.info("=== REMINDER JOB ===")
    expiring = db_get_expiring_soon()
    if not expiring:
        log.info("No members expiring soon.")
        return
    bot = Bot(token=VIP_TOKEN)
    for m in expiring:
        try:
            await bot.send_message(
                chat_id=m["user_id"],
                text=f"⚠️ <b>VIP access expiring soon!</b>\n\n"
                     f"Expires: <b>{m['expires_dt'].strftime('%B %d at %H:%M UTC')}</b>\n\n"
                     f"Tap /start to renew now. 🔥",
                parse_mode="HTML"
            )
            log.info(f"Reminder sent: {m['user_id']}")
        except Exception as e:
            log.warning(f"Reminder failed {m['user_id']}: {e}")


async def kick_job():
    log.info("=== KICK JOB ===")
    expired = db_get_expired()
    if not expired:
        log.info("No expired members.")
        return
    bot = Bot(token=VIP_TOKEN)
    for m in expired:
        try:
            await bot.ban_chat_member(chat_id=VIP_CHANNEL_ID, user_id=m["user_id"])
            await bot.unban_chat_member(chat_id=VIP_CHANNEL_ID, user_id=m["user_id"])
            db_remove_member(m["user_id"])
            try:
                await bot.send_message(
                    chat_id=m["user_id"],
                    text=f"⏰ <b>Your VIP access has expired.</b>\n\nYou have been removed from the VIP channel.\n\nTap /start to renew. 🔥",
                    parse_mode="HTML"
                )
            except Exception:
                pass
            log.info(f"Kicked: {m['user_id']}")
        except Exception as e:
            log.warning(f"Kick failed {m['user_id']}: {e}")

# ============================================================
# ODDS API
# ============================================================

def american_to_decimal(american: int) -> float:
    return round((american / 100) + 1, 3) if american > 0 else round((100 / abs(american)) + 1, 3)


def fetch_odds(sport_key: str) -> list:
    try:
        r = requests.get(
            f"https://api.the-odds-api.com/v4/sports/{sport_key}/odds",
            params={"apiKey": ODDS_API_KEY, "regions": "eu", "markets": "h2h", "oddsFormat": "decimal", "dateFormat": "iso"},
            timeout=10
        )
        return r.json() if r.status_code == 200 else []
    except Exception as e:
        log.error(f"Fetch error {sport_key}: {e}")
        return []


def fetch_active_sports() -> list:
    try:
        r = requests.get("https://api.the-odds-api.com/v4/sports", params={"apiKey": ODDS_API_KEY}, timeout=10)
        return [s["key"] for s in r.json() if s.get("active")] if r.status_code == 200 else []
    except Exception as e:
        log.error(f"Sports list error: {e}")
        return []

# ============================================================
# MATCH SELECTOR — future matches only
# ============================================================

def get_sport_category(sport_key: str) -> str:
    if "soccer" in sport_key: return "soccer"
    if "tennis" in sport_key: return "tennis"
    if "basketball" in sport_key: return "basketball"
    return "default"


def get_best_pick(matches: list, exclude_id: str = None) -> dict | None:
    now, candidates = datetime.now(timezone.utc), []
    for match in matches:
        if exclude_id and match.get("id") == exclude_id: continue
        if not match.get("bookmakers"): continue
        try:
            commence = datetime.fromisoformat(match["commence_time"].replace("Z", "+00:00"))
        except Exception:
            continue
        hours_until = (commence - now).total_seconds() / 3600
        if not (MIN_HOURS_UNTIL_MATCH <= hours_until <= MAX_HOURS_UNTIL_MATCH): continue
        outcome_prices: dict[str, list[float]] = {}
        for bm in match["bookmakers"]:
            for market in bm.get("markets", []):
                if market["key"] != "h2h": continue
                for outcome in market["outcomes"]:
                    price = outcome["price"]
                    decimal = float(price) if (isinstance(price, (int, float)) and price > 10) else (american_to_decimal(int(price)) if isinstance(price, int) else float(price))
                    outcome_prices.setdefault(outcome["name"], []).append(decimal)
        if not outcome_prices: continue
        avg_odds = {t: round(sum(p)/len(p), 2) for t, p in outcome_prices.items()}
        favorite = min(avg_odds, key=avg_odds.get)
        fav_odds = avg_odds[favorite]
        if not (MIN_ODDS <= fav_odds <= MAX_ODDS): continue
        candidates.append({
            "match_id": match["id"], "sport_key": match["sport_key"],
            "sport_cat": get_sport_category(match["sport_key"]),
            "sport_title": match["sport_title"],
            "home_team": match["home_team"], "away_team": match["away_team"],
            "commence": commence, "pick": favorite, "pick_odds": fav_odds,
            "all_odds": avg_odds, "hours_until": hours_until,
        })
    if not candidates: return None
    candidates.sort(key=lambda c: abs(c["pick_odds"] - 1.55))
    return candidates[0]


def find_best_match(exclude_id: str = None) -> dict | None:
    log.info("Finding best FUTURE match...")
    for sport_key in SPORT_PRIORITY:
        pick = get_best_pick(fetch_odds(sport_key), exclude_id=exclude_id)
        if pick:
            log.info(f"✅ Pick: {pick['pick']} @ {pick['pick_odds']} | {pick['hours_until']:.1f}h away ({sport_key})")
            return pick
    for cat in SPORT_CATEGORY_PRIORITY:
        for sport_key in fetch_active_sports():
            if sport_key in SPORT_PRIORITY or cat not in sport_key: continue
            pick = get_best_pick(fetch_odds(sport_key), exclude_id=exclude_id)
            if pick:
                log.info(f"✅ Fallback: {pick['pick']} ({sport_key})")
                return pick
    log.warning("No future match found.")
    return None

# ============================================================
# POST GENERATOR — UTC time + full date
# ============================================================

def format_match_datetime(dt: datetime) -> str:
    # UTC — works for all Africa: Nigeria = UTC+1, Ghana = UTC+0
    return dt.strftime("%A, %b %d — %H:%M UTC")


def build_odds_block(pick: dict) -> str:
    return "\n".join(
        f"✅ {t} — {o}" if t == pick["pick"] else f"     {t} — {o}"
        for t, o in sorted(pick["all_odds"].items(), key=lambda x: x[1])
    )


def generate_morning_post(pick: dict) -> str:
    emoji, link, deposit = SPORT_EMOJIS.get(pick["sport_cat"], "🏆"), SPORT_LINKS.get(pick["sport_cat"], SPORT_LINKS["default"]), random.choice(DEPOSIT_OFFERS)
    return (
        f"{emoji} <b>{random.choice(BET_OPENERS_MORNING).format(pick=pick['pick'])}</b>\n\n"
        f"<b>{pick['away_team']} vs {pick['home_team']}</b>\n"
        f"{pick['sport_title']}\n"
        f"📅 {format_match_datetime(pick['commence'])}\n\n"
        f"{build_odds_block(pick)}\n\n"
        f"{random.choice(ANALYSIS_LINES).format(pick=pick['pick'])}\n"
        f"{random.choice(BET_AMOUNTS)} placed on <b>{pick['pick']}</b> @ {pick['pick_odds']}. 💸\n\n"
        f"{random.choice(CHALLENGE_LINES)}\n\n"
        f"Deposit {deposit[0]} → play with {deposit[1]}\n"
        f"🔑 Code: <code>{PROMO_CODE}</code>\n\n"
        f"👉 <b>{random.choice(CTA_LABELS)}</b>\n{link}"
    )


def generate_evening_post(pick: dict, morning_pick: dict = None) -> str:
    emoji, link, deposit = SPORT_EMOJIS.get(pick["sport_cat"], "🏆"), SPORT_LINKS.get(pick["sport_cat"], SPORT_LINKS["default"]), random.choice(DEPOSIT_OFFERS)
    morning_ref = f"📌 Morning pick: <b>{morning_pick['pick']}</b> @ {morning_pick['pick_odds']} — check result! ✅\n\n" if morning_pick else ""
    return (
        f"{emoji} <b>{random.choice(BET_OPENERS_EVENING)}</b>\n\n"
        f"{morning_ref}"
        f"<b>{pick['away_team']} vs {pick['home_team']}</b>\n"
        f"{pick['sport_title']}\n"
        f"📅 {format_match_datetime(pick['commence'])}\n\n"
        f"{build_odds_block(pick)}\n\n"
        f"{random.choice(ANALYSIS_LINES).format(pick=pick['pick'])}\n"
        f"{random.choice(BET_AMOUNTS)} on <b>{pick['pick']}</b> @ {pick['pick_odds']}. 🔥\n\n"
        f"{random.choice(CHALLENGE_LINES)}\n\n"
        f"Deposit {deposit[0]} → play with {deposit[1]}\n"
        f"🔑 Code: <code>{PROMO_CODE}</code>\n\n"
        f"👉 <b>{random.choice(CTA_LABELS)}</b>\n{link}"
    )

# ============================================================
# TELEGRAM SEND WITH IMAGE
# ============================================================

async def send_to_vip(text: str, sport_cat: str):
    bot        = Bot(token=VIP_TOKEN)
    image_path = SPORT_IMAGES.get(sport_cat, SPORT_IMAGES["default"])
    try:
        if os.path.exists(image_path):
            with open(image_path, "rb") as photo:
                await bot.send_photo(chat_id=VIP_CHANNEL_ID, photo=photo, caption=text[:1024], parse_mode=ParseMode.HTML)
        else:
            log.warning(f"Image missing: {image_path} — text only")
            await bot.send_message(chat_id=VIP_CHANNEL_ID, text=text, parse_mode=ParseMode.HTML, disable_web_page_preview=True)
        log.info("✅ Post sent.")
    except Exception as e:
        log.error(f"Send error: {e}")

# ============================================================
# SCHEDULER JOBS
# ============================================================

_morning_pick: dict | None = None


async def morning_job():
    global _morning_pick
    log.info("=== MORNING JOB (12:00 Armenia) ===")
    pick = find_best_match()
    if not pick: log.warning("No future match. Skipping."); return
    _morning_pick = pick
    await send_to_vip(generate_morning_post(pick), pick["sport_cat"])


async def evening_job():
    global _morning_pick
    log.info("=== EVENING JOB (00:00 Armenia PEAK) ===")
    pick = find_best_match(exclude_id=_morning_pick["match_id"] if _morning_pick else None)
    if not pick: log.warning("No future match. Skipping."); return
    await send_to_vip(generate_evening_post(pick, morning_pick=_morning_pick), pick["sport_cat"])


async def test_job():
    log.info("=== TEST POST (15:40 Armenia) ===")
    pick = find_best_match()
    if not pick: log.warning("No future match for test. Skipping."); return
    await send_to_vip(generate_morning_post(pick), pick["sport_cat"])
    log.info("✅ Test post sent!")

# ============================================================
# MAIN
# ============================================================

async def main():
    log.info("🚀 Fortunobet VIP Bot + Auto-Poster starting...")
    for sport, path in SPORT_IMAGES.items():
        log.info(f"{'✅' if os.path.exists(path) else '❌ MISSING'} {sport}: {path}")
    log.info(f"📋 VIP members in database: {len(db_load())}")

    scheduler = AsyncIOScheduler(timezone="Asia/Yerevan")
    scheduler.add_job(morning_job,  "cron", hour=12, minute=0,  id="morning")
    scheduler.add_job(evening_job,  "cron", hour=0,  minute=0,  id="evening")
    scheduler.add_job(reminder_job, "cron", hour=10, minute=0,  id="reminder")
    scheduler.add_job(kick_job,     "cron", hour=10, minute=5,  id="kick")

    now_armenia = datetime.now(timezone(timedelta(hours=4)))
    test_time   = now_armenia.replace(hour=15, minute=40, second=0, microsecond=0)
    if now_armenia < test_time:
        scheduler.add_job(test_job, "date", run_date=test_time, id="test_post", timezone="Asia/Yerevan")
        log.info("🧪 Test post scheduled: 15:40 Armenia today.")
    else:
        log.warning("⚠️  15:40 Armenia already passed. Test post skipped.")

    scheduler.start()
    log.info("Scheduler: 15:40 test | 12:00 morning | 00:00 evening | 10:00 reminder | 10:05 kick")

    app = Application.builder().token(VIP_TOKEN).build()
    app.add_handler(CommandHandler("start",      start))
    app.add_handler(CommandHandler("stats",      cmd_stats))
    app.add_handler(CommandHandler("members",    cmd_members))
    app.add_handler(CommandHandler("adddays",    cmd_adddays))
    app.add_handler(CommandHandler("giveaccess", cmd_giveaccess))
    app.add_handler(CommandHandler("help",       cmd_help))
    app.add_handler(CallbackQueryHandler(handle_payment))
    app.add_handler(PreCheckoutQueryHandler(precheckout_callback))
    app.add_handler(MessageHandler(filters.SUCCESSFUL_PAYMENT, successful_payment_callback))

    log.info("💎 VIP Payment Bot starting...")
    async with app:
        await app.initialize()
        await app.start()
        await app.updater.start_polling()
        log.info("✅ All systems running!")
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



        # https://api.telegram.org/bot8643569826:AAE6i7qJABI6OwexCLn7ohTOWwi2tU88-dg/getMyStarBalance

        # /stats   Total members, active, expired, weekly vs monthly
        # /members Full list with names, plan, days remaining
        # /adddays 123456789 7 Add 7 free days to existing member
        # /giveaccess 123456789 7 Give 7 free days to new user + sends them invite link
        # /helpShows all commands