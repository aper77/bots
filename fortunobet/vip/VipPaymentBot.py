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


VIP_TOKEN       = "8643569826:AAE6i7qJABI6OwexCLn7ohTOWwi2tU88-dg"
VIP_CHANNEL_ID  = -1003729457344
VIP_INVITE_LINK = "https://t.me/+zK2J-5fd9QEwNmRi"
ODDS_API_KEY    = "bd55794e7bf843f14ab61e3521a8023a"
REF_CODE        = "z4m5"
PROMO_CODE      = "fortunobet"
ADMIN_ID        = 7627990095
BOT_USERNAME    = "FortunoVIPbot"

WEEKLY_STARS  = 50    # $1
MONTHLY_STARS = 150   # $3

REFERRAL_NEEDED      = 5   # friends needed for reward
REFERRAL_REWARD_DAYS = 30  # days given as reward

DB_FILE           = os.path.join(os.path.dirname(os.path.abspath(__file__)), "vip_members.json")
REFS_FILE         = os.path.join(os.path.dirname(os.path.abspath(__file__)), "referrals.json")
SCRIPT_DIR        = os.path.dirname(os.path.abspath(__file__))
MORNING_PICK_FILE = os.path.join(SCRIPT_DIR, "morning_pick.json")

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

MIN_HOURS_UNTIL_MATCH = 0.5   # matches starting in 30+ minutes qualify
MAX_HOURS_UNTIL_MATCH = 48.0  # look up to 48 hours ahead so morning post always finds something
MIN_ODDS = 1.15
MAX_ODDS = 2.20

# ============================================================
# ADMIN COMMANDS  (only work for ADMIN_ID)
# ============================================================
#
#  /stats
#       Shows full VIP statistics:
#       - Total members ever, active now, expired
#       - Breakdown by plan: weekly / monthly / free
#       - Referral summary: referrers, total referrals, rewards given
#       - List of every currently active member with days remaining
#
#  /members
#       Full list of ALL members (active + expired) with:
#       - Status ✅/❌, username or ID, plan, days left, Telegram ID
#
#  /referrals
#       Per-user referral stats sorted by most referrals:
#       - Total referrals made, rewards earned, how many until next reward
#
#  /adddays <user_id> <days>
#       Add extra days to an EXISTING member's expiry.
#       Example: /adddays 123456789 7
#       - Extends from current expiry (not from today)
#       - Sends the user a notification with new expiry date + invite link
#       - If user not found → suggests /giveaccess instead
#
#  /giveaccess <user_id> <days>
#       Give FREE VIP access to a NEW user (not yet in database).
#       Example: /giveaccess 123456789 30
#       - Adds them to the database with plan = "free"
#       - Sends them the VIP invite link automatically
#       - If bot cannot message them → they must /start the bot first
#
#  /resetdb
#       ⚠️  DANGER: Clears the entire members database (vip_members.json).
#       Does NOT affect referrals.json or morning_pick.json.
#
#  /help
#       Shows all admin commands inside Telegram.
#
# ------------------------------------------------------------
# USEFUL LINKS
# ------------------------------------------------------------
#  Stars balance:
#  https://api.telegram.org/bot8643569826:AAE6i7qJABI6OwexCLn7ohTOWwi2tU88-dg/getMyStarBalance
#
#  Bot info:
#  https://api.telegram.org/bot8643569826:AAE6i7qJABI6OwexCLn7ohTOWwi2tU88-dg/getMe
#
# ------------------------------------------------------------
# FILES CREATED BY THE BOT
# ------------------------------------------------------------
#  vip_members.json   — active/expired VIP members database
#  referrals.json     — referral tracking per user
#  morning_pick.json  — today's morning match (auto-deleted after evening post)
#  vip_bot.log        — full runtime log
#
# ------------------------------------------------------------
# SCHEDULER  (timezone: Asia/Yerevan)
# ------------------------------------------------------------
#  10:00  — reminder_job  → warns members expiring within 24h
#  10:05  — kick_job      → removes expired members from channel
#  12:00  — morning_job   → posts morning pick to VIP channel
#  00:00  — evening_job   → posts evening pick (never same match as morning)
#
# ============================================================

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.FileHandler("vip_bot.log"), logging.StreamHandler()]
)
log = logging.getLogger(__name__)

SPORT_PRIORITY = [
    # Updated June 2026 — only currently active sports.
    # Bot stops at first sport with a good match (1-3 API calls max).
    "soccer_fifa_world_cup",        # FIFA World Cup 2026 — biggest event right now
    "soccer_epl",                   # EPL — always has matches
    "soccer_brazil_campeonato",     # Brazil Serie A — active June/July
    "soccer_conmebol_copa_libertadores",  # Copa Libertadores — active
    "tennis_atp_wimbledon",         # Wimbledon starts late June
    "tennis_wta_wimbledon",         # Wimbledon WTA
    "baseball_mlb",                 # MLB — daily games all summer
    "basketball_wnba",              # WNBA — active June/July
]
SPORT_CATEGORY_PRIORITY = ["soccer", "tennis", "basketball"]

DEPOSIT_OFFERS = [
    ("₦500", "₦3,000"), ("₦10,000", "₦60,000"),
    ("₦20,000", "₦120,000"), ("₦5,000", "₦30,000"),
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
CTA_LABELS = ["Follow my bet NOW:", "Place your bet:", "Bet NOW:", "Join me:", "Follow NOW:"]
SPORT_EMOJIS = {"soccer": "⚽", "tennis": "🎾", "basketball": "🏀", "default": "🏆"}

# ============================================================
# MEMBERS DATABASE
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

def db_add_member(user_id: int, username: str, plan: str, days: int):
    data       = db_load()
    now        = datetime.now(timezone.utc)
    expires_dt = now + timedelta(days=days)
    expires    = expires_dt.strftime("%Y-%m-%d %H:%M:%S")
    data[str(user_id)] = {
        "username": username or str(user_id),
        "plan":     plan,
        "expires":  expires,
        "joined":   now.strftime("%Y-%m-%d %H:%M:%S"),
    }
    db_save(data)
    log.info(f"Member: {user_id} ({plan}, {days}d) expires {expires}")
    return expires, expires_dt

def db_add_free_days(user_id: int, days: int):
    data = db_load()
    key  = str(user_id)
    if key not in data:
        return None, None
    now     = datetime.now(timezone.utc)
    current = datetime.strptime(data[key]["expires"], "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc)
    base    = current if current > now else now
    new_dt  = base + timedelta(days=days)
    new_exp = new_dt.strftime("%Y-%m-%d %H:%M:%S")
    data[key]["expires"] = new_exp
    db_save(data)
    return new_exp, new_dt

def db_get_expiring_soon() -> list:
    data, now = db_load(), datetime.now(timezone.utc)
    soon, result = now + timedelta(hours=24), []
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
    active = expired = weekly = monthly = free = 0
    for info in data.values():
        try:
            exp = datetime.strptime(info["expires"], "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc)
            if exp > now:
                active += 1
                p = info.get("plan", "")
                if p == "weekly": weekly += 1
                elif p == "monthly": monthly += 1
                else: free += 1
            else:
                expired += 1
        except Exception:
            continue
    return {"total": len(data), "active": active, "expired": expired,
            "weekly": weekly, "monthly": monthly, "free": free}

# ============================================================
# REFERRAL DATABASE
# ============================================================

def refs_load() -> dict:
    if not os.path.exists(REFS_FILE):
        return {}
    try:
        with open(REFS_FILE, "r") as f:
            return json.load(f)
    except Exception:
        return {}

def refs_save(data: dict):
    try:
        with open(REFS_FILE, "w") as f:
            json.dump(data, f, indent=2)
    except Exception as e:
        log.error(f"Refs save error: {e}")

def refs_get_link(user_id: int) -> str:
    return f"https://t.me/{BOT_USERNAME}?start=ref_{user_id}"

def refs_register(referrer_id: int, referrer_username: str, new_user_id: int) -> bool:
    """Register referral. Returns True if reward earned."""
    data = refs_load()
    key  = str(referrer_id)
    if key not in data:
        data[key] = {
            "username":       referrer_username or str(referrer_id),
            "referral_count": 0,
            "rewards_given":  0,
            "referred_users": []
        }
    if new_user_id in data[key]["referred_users"]:
        return False
    data[key]["referred_users"].append(new_user_id)
    data[key]["referral_count"] += 1
    total       = data[key]["referral_count"]
    rewards_due = total // REFERRAL_NEEDED
    earned      = rewards_due > data[key]["rewards_given"]
    if earned:
        data[key]["rewards_given"] += 1
    refs_save(data)
    log.info(f"Referral: {new_user_id} → {referrer_id} (total: {total}, reward: {earned})")
    return earned

def refs_stats() -> dict:
    data = refs_load()
    return {
        "total_referrers": len(data),
        "total_referrals": sum(v["referral_count"] for v in data.values()),
        "total_rewards":   sum(v["rewards_given"] for v in data.values()),
    }

# ============================================================
# MORNING PICK PERSISTENCE
# ============================================================

# Armenia is UTC+4. Both morning (12:00) and evening (00:00) jobs
# run on the same Armenian calendar day. Using UTC here caused the
# bug: at 00:00 Armenia = 20:00 UTC previous day, so the date check
# failed and the morning pick was ignored — allowing the same match.
ARMENIA_TZ = timezone(timedelta(hours=4))

def morning_pick_save(pick: dict):
    """Save morning pick to disk so it survives bot restarts."""
    try:
        data = {
            "match_id":    pick["match_id"],
            "pick":        pick["pick"],
            "pick_odds":   pick["pick_odds"],
            "home_team":   pick["home_team"],
            "away_team":   pick["away_team"],
            "sport_cat":   pick["sport_cat"],
            "sport_title": pick["sport_title"],
            "saved_date":  datetime.now(ARMENIA_TZ).strftime("%Y-%m-%d"),
        }
        with open(MORNING_PICK_FILE, "w") as f:
            json.dump(data, f, indent=2)
        log.info(f"Morning pick saved to disk: {pick['match_id']}")
    except Exception as e:
        log.error(f"Failed to save morning pick: {e}")

def morning_pick_load() -> dict | None:
    """Load today's morning pick from disk. Returns None if not today's or missing."""
    try:
        if not os.path.exists(MORNING_PICK_FILE):
            return None
        with open(MORNING_PICK_FILE, "r") as f:
            data = json.load(f)
        today = datetime.now(ARMENIA_TZ).strftime("%Y-%m-%d")
        if data.get("saved_date") != today:
            log.info("Morning pick on disk is from a previous day — ignoring.")
            return None
        log.info(f"Loaded today's morning pick from disk: {data['match_id']}")
        return data
    except Exception as e:
        log.error(f"Failed to load morning pick: {e}")
        return None

def morning_pick_clear():
    """Delete the morning pick file after the evening post is sent."""
    try:
        if os.path.exists(MORNING_PICK_FILE):
            os.remove(MORNING_PICK_FILE)
            log.info("Morning pick file cleared.")
    except Exception as e:
        log.error(f"Failed to clear morning pick: {e}")

# ============================================================
# ADMIN COMMANDS
# ============================================================

def is_admin(uid: int) -> bool:
    return uid == ADMIN_ID

async def cmd_stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_admin(update.effective_user.id): return
    s, rs, data, now = db_stats(), refs_stats(), db_load(), datetime.now(timezone.utc)
    lines = []
    for uid, info in data.items():
        try:
            exp = datetime.strptime(info["expires"], "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc)
            if exp > now:
                name = f"@{info['username']}" if info.get("username") and not info["username"].isdigit() else f"ID:{uid}"
                lines.append(f"  • {name} — {info.get('plan','?')} — {(exp-now).days}d left")
        except Exception:
            continue
    await update.message.reply_text(
        f"📊 <b>VIP STATISTICS</b>\n\n"
        f"👥 Total ever: {s['total']}\n"
        f"✅ Active now: {s['active']}\n"
        f"❌ Expired: {s['expired']}\n\n"
        f"⚡ Weekly: {s['weekly']}\n"
        f"💎 Monthly: {s['monthly']}\n"
        f"🎁 Free: {s['free']}\n\n"
        f"🔗 <b>REFERRAL STATS</b>\n"
        f"👤 Active referrers: {rs['total_referrers']}\n"
        f"📥 Total referrals made: {rs['total_referrals']}\n"
        f"🏆 Total rewards given: {rs['total_rewards']}\n\n"
        f"<b>Active Members:</b>\n" + ("\n".join(lines) if lines else "  No active members"),
        parse_mode="HTML"
    )

async def cmd_referrals(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_admin(update.effective_user.id): return
    data = refs_load()
    if not data:
        await update.message.reply_text("No referrals yet.")
        return
    lines = ["<b>REFERRAL STATS PER USER:</b>\n"]
    for uid, info in sorted(data.items(), key=lambda x: x[1]["referral_count"], reverse=True):
        name       = f"@{info['username']}" if info.get("username") and not info["username"].isdigit() else f"ID:{uid}"
        refs       = info["referral_count"]
        rewards    = info["rewards_given"]
        next_r     = REFERRAL_NEEDED - (refs % REFERRAL_NEEDED) if refs % REFERRAL_NEEDED != 0 else REFERRAL_NEEDED
        lines.append(f"👤 {name}\n   Referrals: {refs} | Rewards: {rewards} | Next reward in: {next_r} more")
    text = "\n\n".join(lines)
    for i in range(0, len(text), 3500):
        await update.message.reply_text(text[i:i+3500], parse_mode="HTML")

async def cmd_members(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_admin(update.effective_user.id): return
    data, now = db_load(), datetime.now(timezone.utc)
    if not data:
        await update.message.reply_text("No members in database.")
        return
    lines = ["<b>ALL VIP MEMBERS:</b>\n"]
    for uid, info in data.items():
        try:
            exp       = datetime.strptime(info["expires"], "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc)
            status    = "✅" if exp > now else "❌"
            days_left = max(0, (exp - now).days)
            name      = f"@{info['username']}" if info.get("username") and not info["username"].isdigit() else f"ID:{uid}"
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
    new_exp, _ = db_add_free_days(user_id, days)
    if new_exp:
        try:
            await context.bot.send_message(
                chat_id=user_id,
                text=f"🎁 <b>You received {days} free VIP days!</b>\n\n"
                     f"Access expires: <b>{new_exp} UTC</b>\n\n"
                     f"👇 <b>Join VIP channel:</b>\n{VIP_INVITE_LINK}\n\nEnjoy! 🔥",
                parse_mode="HTML"
            )
        except Exception as e:
            log.warning(f"Could not notify {user_id}: {e}")
        await update.message.reply_text(f"✅ Added {days} days to {user_id}\nNew expiry: {new_exp}")
    else:
        await update.message.reply_text(f"⚠️ User {user_id} not found.\nUse /giveaccess {user_id} {days}")

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
    expires, _ = db_add_member(user_id, str(user_id), "free", days=days)
    try:
        await context.bot.send_message(
            chat_id=user_id,
            text=f"🎁 <b>You got {days} days FREE VIP access!</b>\n\n"
                 f"Access expires: <b>{expires} UTC</b>\n\n"
                 f"👇 <b>Join VIP channel now:</b>\n{VIP_INVITE_LINK}\n\nEnjoy! 🔥",
            parse_mode="HTML"
        )
        notified = True
    except Exception as e:
        log.warning(f"Could not notify {user_id}: {e}")
        notified = False
    reply = f"✅ Gave {days} free days to {user_id}\nExpires: {expires}\nInvite: {VIP_INVITE_LINK}"
    if not notified:
        reply += f"\n⚠️ Could not message user — they must start the bot first."
    await update.message.reply_text(reply)

async def cmd_resetdb(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_admin(update.effective_user.id): return
    db_save({})
    await update.message.reply_text("✅ Members database cleared.")

async def cmd_help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_admin(update.effective_user.id): return
    await update.message.reply_text(
        "<b>ADMIN COMMANDS:</b>\n\n"
        "/stats — Members + referral summary\n"
        "/members — Full members list\n"
        "/referrals — Referral stats per user\n"
        "/adddays &lt;id&gt; &lt;days&gt; — Add days to member\n"
        "/giveaccess &lt;id&gt; &lt;days&gt; — Give free access\n"
        "/resetdb — Clear members database\n"
        "/help — Show this list\n\n"
        f"Referral reward: {REFERRAL_NEEDED} friends = {REFERRAL_REWARD_DAYS} days free",
        parse_mode="HTML"
    )

# ============================================================
# VIP PAYMENT BOT HANDLERS
# ============================================================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user

    # Handle referral: /start ref_123456789
    if context.args and context.args[0].startswith("ref_"):
        try:
            referrer_id = int(context.args[0].replace("ref_", ""))
            if referrer_id != user.id:
                earned = refs_register(referrer_id, None, user.id)
                refs_data = refs_load()
                ref_info  = refs_data.get(str(referrer_id), {})
                total     = ref_info.get("referral_count", 0)
                if earned:
                    new_exp, _ = db_add_free_days(referrer_id, REFERRAL_REWARD_DAYS)
                    if not new_exp:
                        new_exp, _ = db_add_member(referrer_id, str(referrer_id), "referral", days=REFERRAL_REWARD_DAYS)
                    try:
                        await context.bot.send_message(
                            chat_id=referrer_id,
                            text=f"🎉 <b>Referral reward earned!</b>\n\n"
                                 f"You now have <b>{total}</b> referrals!\n\n"
                                 f"<b>Reward: {REFERRAL_REWARD_DAYS} days FREE VIP!</b>\n"
                                 f"New expiry: <b>{new_exp} UTC</b>\n\n"
                                 f"👇 Join VIP channel:\n{VIP_INVITE_LINK}\n\n"
                                 f"Keep sharing to earn more! 🔥",
                            parse_mode="HTML"
                        )
                    except Exception as e:
                        log.warning(f"Could not notify referrer {referrer_id}: {e}")
                else:
                    next_r = REFERRAL_NEEDED - (total % REFERRAL_NEEDED)
                    try:
                        await context.bot.send_message(
                            chat_id=referrer_id,
                            text=f"👥 <b>New referral!</b>\n\n"
                                 f"Someone joined through your link!\n"
                                 f"Total referrals: <b>{total}</b>\n\n"
                                 f"<b>{next_r} more</b> friends = {REFERRAL_REWARD_DAYS} free days! 🔥",
                            parse_mode="HTML"
                        )
                    except Exception as e:
                        log.warning(f"Could not notify referrer {referrer_id}: {e}")
        except Exception as e:
            log.warning(f"Referral error: {e}")

    keyboard = [
        [InlineKeyboardButton(f"⚡ 7 Days — {WEEKLY_STARS} Stars ($1)", callback_data='pay_weekly')],
        [InlineKeyboardButton(f"💎 30 Days — {MONTHLY_STARS} Stars ($3)", callback_data='pay_monthly')],
        [InlineKeyboardButton("🔗 My Referral Link", callback_data='my_referral')],
    ]
    await update.message.reply_text(
        "💎 <b>FORTUNOBET VIP ACCESS</b>\n\n"
        "🎯 <b>What You Get:</b>\n"
        "• Premium betting picks daily\n"
        "• Higher odds selections\n"
        "• Real match analysis\n"
        "• Telegram support\n\n"
        f"🔗 <b>Invite {REFERRAL_NEEDED} friends = {REFERRAL_REWARD_DAYS} days FREE!</b>\n\n"
        "⚡ <b>Choose your access:</b>",
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="HTML"
    )

async def handle_payment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == 'my_referral':
        user      = query.from_user
        ref_link  = refs_get_link(user.id)
        refs_data = refs_load()
        ref_info  = refs_data.get(str(user.id), {})
        total     = ref_info.get("referral_count", 0)
        rewards   = ref_info.get("rewards_given", 0)
        next_r    = REFERRAL_NEEDED - (total % REFERRAL_NEEDED) if total % REFERRAL_NEEDED != 0 else REFERRAL_NEEDED
        await query.edit_message_text(
            f"🔗 <b>YOUR REFERRAL LINK</b>\n\n"
            f"<code>{ref_link}</code>\n\n"
            f"Share this link with friends.\n"
            f"Every <b>{REFERRAL_NEEDED} friends</b> who start the bot = <b>{REFERRAL_REWARD_DAYS} days FREE</b> for you!\n\n"
            f"📊 <b>Your stats:</b>\n"
            f"👥 Total referrals: {total}\n"
            f"🏆 Rewards earned: {rewards}\n"
            f"⏳ Next reward in: {next_r} more friends\n\n"
            f"Tap the link above to copy it! 📋",
            parse_mode="HTML"
        )
        return

    if query.data == 'pay_weekly':
        title, desc, price, payload, days, duration = "VIP Weekly Access", "7 days of premium picks", WEEKLY_STARS, "weekly", 7, "7 days"
    else:
        title, desc, price, payload, days, duration = "VIP Monthly Access", "30 days of premium picks", MONTHLY_STARS, "monthly", 30, "30 days"

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
    days     = 7 if plan == "weekly" else 30
    duration = f"{days} days"
    username = user.username or user.first_name or str(user.id)
    expires, _ = db_add_member(user.id, username, plan, days=days)
    await update.message.reply_text(
        f"✅ <b>PAYMENT CONFIRMED!</b>\n\n"
        f"🎯 Your {duration} VIP access is ready!\n"
        f"Expires: <b>{expires} UTC</b>\n\n"
        f"👇 <b>JOIN NOW:</b>\n{VIP_INVITE_LINK}\n\n"
        f"💚 Welcome to Fortunobet VIP!\n\n"
        f"🔗 Earn free days by referring friends!\nTap /start → My Referral Link",
        parse_mode="HTML"
    )
    try:
        await context.bot.send_message(
            chat_id=VIP_CHANNEL_ID,
            text=f"💎 <b>NEW VIP MEMBER!</b>\n\nWelcome @{username}!\nPlan: {duration}\n\nEnjoy! 🔥",
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
                    text=f"⏰ <b>Your VIP access has expired.</b>\n\n"
                         f"You have been removed from the VIP channel.\n\n"
                         f"Tap /start to renew and rejoin. 🔥",
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
            params={"apiKey": ODDS_API_KEY, "regions": "eu", "markets": "h2h",
                    "oddsFormat": "decimal", "dateFormat": "iso"},
            timeout=10
        )
        remaining = r.headers.get("x-requests-remaining", "?")
        used      = r.headers.get("x-requests-used", "?")
        log.info(f"Odds API [{sport_key}] status={r.status_code} | used={used} | remaining={remaining}")
        if r.status_code == 422:
            log.error("❌ ODDS API QUOTA EXCEEDED — no credits left! Renew at the-odds-api.com")
            return []
        if r.status_code == 401:
            log.error("❌ ODDS API: Invalid API key!")
            return []
        return r.json() if r.status_code == 200 else []
    except Exception as e:
        log.error(f"Fetch error {sport_key}: {e}")
        return []

def fetch_active_sports() -> list:
    try:
        r = requests.get("https://api.the-odds-api.com/v4/sports",
                         params={"apiKey": ODDS_API_KEY}, timeout=10)
        return [s["key"] for s in r.json() if s.get("active")] if r.status_code == 200 else []
    except Exception as e:
        log.error(f"Sports error: {e}")
        return []

# ============================================================
# MATCH SELECTOR
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
        outcome_prices: dict = {}
        for bm in match["bookmakers"]:
            for market in bm.get("markets", []):
                if market["key"] != "h2h": continue
                for outcome in market["outcomes"]:
                    p = outcome["price"]
                    d = float(p) if (isinstance(p, (int, float)) and p > 10) else (american_to_decimal(int(p)) if isinstance(p, int) else float(p))
                    outcome_prices.setdefault(outcome["name"], []).append(d)
        if not outcome_prices: continue
        avg  = {t: round(sum(v)/len(v), 2) for t, v in outcome_prices.items()}
        fav  = min(avg, key=avg.get)
        odds = avg[fav]
        if not (MIN_ODDS <= odds <= MAX_ODDS): continue
        candidates.append({
            "match_id": match["id"], "sport_key": match["sport_key"],
            "sport_cat": get_sport_category(match["sport_key"]),
            "sport_title": match["sport_title"],
            "home_team": match["home_team"], "away_team": match["away_team"],
            "commence": commence, "pick": fav, "pick_odds": odds,
            "all_odds": avg, "hours_until": hours_until,
        })
    if not candidates: return None
    candidates.sort(key=lambda c: abs(c["pick_odds"] - 1.55))
    return candidates[0]

def find_best_match(exclude_id: str = None) -> dict | None:
    log.info("Finding best future match...")

    # STEP 1: Try priority list first (saves API quota)
    for sport_key in SPORT_PRIORITY:
        matches = fetch_odds(sport_key)
        if not matches:
            continue
        pick = get_best_pick(matches, exclude_id=exclude_id)
        if pick:
            log.info(f"Priority pick: {pick['pick']} @ {pick['pick_odds']} | {pick['hours_until']:.1f}h | {sport_key}")
            return pick

    # STEP 2: Fallback — fetch ALL active sports from API and try every one.
    # This guarantees a post even when priority sports have no matches.
    log.warning("Priority sports empty — trying ALL active sports as fallback...")
    try:
        r = requests.get("https://api.the-odds-api.com/v4/sports",
                         params={"apiKey": ODDS_API_KEY}, timeout=10)
        if r.status_code != 200:
            log.error(f"Could not fetch active sports: {r.status_code}")
            return None
        # Filter: active, not outrights (outrights have no h2h odds), not already tried
        all_keys = [
            s["key"] for s in r.json()
            if s.get("active") and not s.get("has_outrights", False) == True
            and not s.get("has_outrights") and s["key"] not in SPORT_PRIORITY
        ]
        # Prefer soccer, then tennis, then everything else
        def sport_order(key):
            if "soccer" in key: return 0
            if "tennis" in key: return 1
            if "basketball" in key: return 2
            if "baseball" in key: return 3
            return 9
        all_keys.sort(key=sport_order)
        log.info(f"Fallback: trying {len(all_keys)} additional sports...")
        for sport_key in all_keys:
            matches = fetch_odds(sport_key)
            if not matches:
                continue
            pick = get_best_pick(matches, exclude_id=exclude_id)
            if pick:
                log.info(f"Fallback pick: {pick['pick']} @ {pick['pick_odds']} | {pick['hours_until']:.1f}h | {sport_key}")
                return pick
    except Exception as e:
        log.error(f"Fallback search error: {e}")

    log.warning("No future match found in ANY sport.")
    return None

# ============================================================
# POST GENERATOR
# ============================================================

def format_match_datetime(dt: datetime) -> str:
    return dt.strftime("%A, %b %d — %H:%M UTC")

def build_odds_block(pick: dict) -> str:
    return "\n".join(
        f"✅ {t} — {o}" if t == pick["pick"] else f"     {t} — {o}"
        for t, o in sorted(pick["all_odds"].items(), key=lambda x: x[1])
    )

def generate_morning_post(pick: dict) -> str:
    emoji, link, dep = SPORT_EMOJIS.get(pick["sport_cat"], "🏆"), SPORT_LINKS.get(pick["sport_cat"], SPORT_LINKS["default"]), random.choice(DEPOSIT_OFFERS)
    return (
        f"{emoji} <b>{random.choice(BET_OPENERS_MORNING).format(pick=pick['pick'])}</b>\n\n"
        f"<b>{pick['away_team']} vs {pick['home_team']}</b>\n"
        f"{pick['sport_title']}\n📅 {format_match_datetime(pick['commence'])}\n\n"
        f"{build_odds_block(pick)}\n\n"
        f"{random.choice(ANALYSIS_LINES).format(pick=pick['pick'])}\n"
        f"{random.choice(BET_AMOUNTS)} placed on <b>{pick['pick']}</b> @ {pick['pick_odds']}. 💸\n\n"
        f"{random.choice(CHALLENGE_LINES)}\n\n"
        f"Deposit {dep[0]} → play with {dep[1]}\n"
        f"🔑 Code: <code>{PROMO_CODE}</code>\n\n"
        f"👉 <b>{random.choice(CTA_LABELS)}</b>\n{link}"
    )

def generate_evening_post(pick: dict, morning_pick: dict = None) -> str:
    emoji, link, dep = SPORT_EMOJIS.get(pick["sport_cat"], "🏆"), SPORT_LINKS.get(pick["sport_cat"], SPORT_LINKS["default"]), random.choice(DEPOSIT_OFFERS)
    ref = f"📌 Morning pick: <b>{morning_pick['pick']}</b> @ {morning_pick['pick_odds']} — check result! ✅\n\n" if morning_pick else ""
    return (
        f"{emoji} <b>{random.choice(BET_OPENERS_EVENING)}</b>\n\n{ref}"
        f"<b>{pick['away_team']} vs {pick['home_team']}</b>\n"
        f"{pick['sport_title']}\n📅 {format_match_datetime(pick['commence'])}\n\n"
        f"{build_odds_block(pick)}\n\n"
        f"{random.choice(ANALYSIS_LINES).format(pick=pick['pick'])}\n"
        f"{random.choice(BET_AMOUNTS)} on <b>{pick['pick']}</b> @ {pick['pick_odds']}. 🔥\n\n"
        f"{random.choice(CHALLENGE_LINES)}\n\n"
        f"Deposit {dep[0]} → play with {dep[1]}\n"
        f"🔑 Code: <code>{PROMO_CODE}</code>\n\n"
        f"👉 <b>{random.choice(CTA_LABELS)}</b>\n{link}"
    )

# ============================================================
# SEND WITH IMAGE
# ============================================================

async def send_to_vip(text: str, sport_cat: str):
    bot        = Bot(token=VIP_TOKEN)
    image_path = SPORT_IMAGES.get(sport_cat, SPORT_IMAGES["default"])
    try:
        if os.path.exists(image_path):
            with open(image_path, "rb") as photo:
                await bot.send_photo(chat_id=VIP_CHANNEL_ID, photo=photo,
                                     caption=text[:1024], parse_mode=ParseMode.HTML)
        else:
            await bot.send_message(chat_id=VIP_CHANNEL_ID, text=text,
                                   parse_mode=ParseMode.HTML, disable_web_page_preview=True)
        log.info("✅ Post sent.")
    except Exception as e:
        log.error(f"Send error: {e}")

# ============================================================
# SCHEDULER JOBS
# ============================================================

async def morning_job():
    log.info("=== MORNING JOB (12:00 Armenia) ===")
    pick = find_best_match()
    if not pick:
        log.warning("No future match. Skipping.")
        return
    morning_pick_save(pick)
    await send_to_vip(generate_morning_post(pick), pick["sport_cat"])

async def evening_job():
    log.info("=== EVENING JOB (00:00 Armenia) ===")
    saved_morning = morning_pick_load()
    exclude_id    = saved_morning["match_id"] if saved_morning else None
    if exclude_id:
        log.info(f"Excluding morning match: {exclude_id}")
    pick = find_best_match(exclude_id=exclude_id)
    if not pick:
        log.warning("No future match. Skipping.")
        return
    await send_to_vip(generate_evening_post(pick, morning_pick=saved_morning), pick["sport_cat"])
    morning_pick_clear()

# ============================================================
# MAIN
# ============================================================

async def main():
    log.info("🚀 Fortunobet VIP Bot + Auto-Poster starting...")
    for sport, path in SPORT_IMAGES.items():
        log.info(f"{'✅' if os.path.exists(path) else '❌ MISSING'} {sport}: {path}")
    log.info(f"📋 Members: {len(db_load())} | Referrers: {len(refs_load())}")

    saved = morning_pick_load()
    if saved:
        log.info(f"📌 Today's morning pick already on disk: {saved['match_id']} — {saved['pick']}")

    scheduler = AsyncIOScheduler(timezone="Asia/Yerevan")
    scheduler.add_job(morning_job,  "cron", hour=12, minute=0, id="morning")
    scheduler.add_job(evening_job,  "cron", hour=0,  minute=0, id="evening")
    scheduler.add_job(reminder_job, "cron", hour=10, minute=0, id="reminder")
    scheduler.add_job(kick_job,     "cron", hour=10, minute=5, id="kick")
    scheduler.start()
    log.info("Scheduler: 12:00 morning | 00:00 evening | 10:00 reminder | 10:05 kick")

    app = Application.builder().token(VIP_TOKEN).build()
    app.add_handler(CommandHandler("start",      start))
    app.add_handler(CommandHandler("stats",      cmd_stats))
    app.add_handler(CommandHandler("members",    cmd_members))
    app.add_handler(CommandHandler("referrals",  cmd_referrals))
    app.add_handler(CommandHandler("adddays",    cmd_adddays))
    app.add_handler(CommandHandler("giveaccess", cmd_giveaccess))
    app.add_handler(CommandHandler("resetdb",    cmd_resetdb))
    app.add_handler(CommandHandler("help",       cmd_help))
    app.add_handler(CallbackQueryHandler(handle_payment))
    app.add_handler(PreCheckoutQueryHandler(precheckout_callback))
    app.add_handler(MessageHandler(filters.SUCCESSFUL_PAYMENT, successful_payment_callback))

    log.info("💎 VIP Bot starting...")
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