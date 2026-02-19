from telegram import Bot, InputMediaPhoto
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime, timedelta
import pytz
import os

# ====== CONFIG ======
BOT_TOKEN = "7924334103:AAHkeWr7KvmWpu9gFk7Eknd9_6NJn3S1WjA"
CHANNEL_ID = "@fortuno_bet"  # Your channel username
TIMEZONE = pytz.timezone('Asia/Yerevan')  # Armenia timezone

bot = Bot(token=BOT_TOKEN)
scheduler = BlockingScheduler()

# MONDAY
# 14:00 — Register & Deposit Guide (VALUE)
# 23:00 — Welcome Bonus (HYPE)

# TUESDAY  
# 14:00 — Withdrawal Guide (VALUE)
# 23:00 — Deposit Bonus (HYPE)

# WEDNESDAY
# 14:00 — How to Bet Example (VALUE)
# 23:00 — Sports Bonus (HYPE)

# THURSDAY
# 14:00 — Safe Betting Tips (VALUE)  
# 23:00 — Reload Bonus (HYPE)

# FRIDAY
# 15:00 — Weekend Betting Guide (VALUE)
# 23:30 — Weekend Bonus (HYPE)

# SATURDAY
# 13:00 — Live Bet Example (VALUE)
# 22:00 — Hot Bonus (HYPE)

# SUNDAY
# 14:00 — Withdraw + Tips (VALUE)
# 22:00 — Final Bonus (HYPE)

posts = [

{"date":"2026-02-16","time":"14:00","content":"💰 <b>You deposited once — now get 75% extra on your 2nd!</b>\n\nMost people sleep on this bonus. Don't be one of them.\n\nDeposit ₦5,000 → play with ₦8,750\nDeposit ₦20,000 → play with ₦35,000\n\n⚡ Min deposit: ₦1,000 only\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Claim it now:</b> https://1wyuds.com/casino/list?open=register&p=cguo","images":["161.png"]},
{"date":"2026-02-16","time":"23:00","content":"🏆 <b>Back Barcelona tonight — and enter to win $4,700 cash + iPhone 16 Pro</b>\n\nOne bet = one draw ticket. That simple.\nTickets start from just $1.18 — anyone can enter.\n\nYou're already watching the match. Might as well get paid for it. 👀\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Get your ticket:</b> https://1wyuds.com/casino/list?open=register&p=cguo","images":["162.png"]},

{"date":"2026-02-17","time":"14:00","content":"⚽ <b>Girona vs Barcelona — and the odds are JUICY</b>\n\nBarca wants top spot. Girona wants blood at home. 😤\nThis is not a walk in the park.\n\n📊 Today's odds:\n🏠 Girona win → 6.00\n🤝 Draw → 5.50\n🚀 Barcelona win → 1.40\n\nWhatever side you back — do it with MORE money:\n\nDeposit ₦10,000 → play with ₦60,000\nDeposit ₦50,000 → play with ₦300,000\n\n⚡ Instant cashout to Opay, Palmpay & Kuda. Zero wahala.\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Bet now:</b> https://1wkrii.life/v3/landing-page/football?p=5pe0","images":["171.png"]},

{"date":"2026-02-18","time":"14:00","content":"🎰 <b>Sweet Bonanza Xmas is eating people alive right now</b>\n\nHigh volatility. Tumble wins. One spin can change your whole day.\n\nThis slot doesn't play — it PAYS. 💥\n\nDeposit ₦2,000 → play with ₦12,000\nMore spins. More chances. More wins.\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Spin now:</b> https://1wkrii.life/casino/list?open=register&p=cguo","images":["181.png"]},
{"date":"2026-02-18","time":"23:00","content":"🇳🇬 <b>Nigerians — this platform was built for you</b>\n\nDeposit with what you use every day:\nOpay ✅  Palmpay ✅  Bank Transfer ✅  USDT ✅\n\nDeposit in under 2 minutes.\nWithdraw same day — no stories, no delays.\n\nDeposit ₦2,000 → play with ₦12,000\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Start today:</b> https://1wkrii.life/casino/list?open=register&p=cguo","images":["182.png"]},

{"date":"2026-02-19","time":"14:00","content":"🎁 <b>Double bonuses — one registration</b>\n\n💥 1WIN: 500% deposit boost\n💥 + $3 cash instantly\n\nDeposit $5 → play bigger from first spin. 💰\nWithdraw same day — no stories.\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>Register & claim now:</b> https://1wffxn.life/v3/aggressive-casino?p=xomk","images":["191.png"]},
{"date":"2026-02-19","time":"23:00","content":"💸 <b>Quick win report</b>\n\n₦2,000 → ₦27,600 last night. ✅\nWithdrawal processed same day.\n\nNo glitch — just bonus + smart play.\n\n👀 If you’ve been waiting, now is your chance.\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>Start now:</b> https://1wffxn.life/v3/aggressive-casino?p=xomk","images":["192.png"]},

{"date":"2026-02-20","time":"15:00","content":"⚡ <b>₦256,000,000 prize pool — week closing soon</b>\n\nEvery deposit = automatic entry. 🔥\nOne move could change your month.\n\nDeposit → bonus hits instantly. ✅\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>Enter now:</b> https://1wffxn.life/v3/aggressive-casino?p=xomk","images":["201.png"]},
{"date":"2026-02-20","time":"23:00","content":"💰 <b>First time on 1WIN? Multiply instantly</b>\n\n₦2,000 → ₦12,000\n₦10,000 → ₦60,000 ⚡\nInstant 500% match. Withdraw same day.\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>Register here:</b> https://1wkrii.life/casino/list?open=register&p=cguo","images":["202.png"]},

{"date":"2026-02-21","time":"13:00","content":"💸 <b>Lose today? 30% cashback</b>\n\nEvery losing bet is protected. ✅\nWin → collect. Lose → recover.\nSmart players protect bankroll. 💰\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>Start protected:</b> https://1wffxn.life/v3/aggressive-casino?p=xomk","images":["211.png"]},
{"date":"2026-02-21","time":"22:00","content":"🎁 <b>Bonuses grow with every deposit</b>\n\n1st → 100% + 70 spins\n2nd → 120% + 100 spins\n3rd → 130% + 150 spins\n4th → 150% + 180 spins 💥\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>Unlock now:</b> https://1wffxn.life/v3/aggressive-casino?p=xomk","images":["212.png"]},

{"date":"2026-02-22","time":"14:00","content":"🎰 <b>500 free spins built into first 4 deposits</b>\n\nDeposit anyway → get 500 extra chances. 💎\nSmart players always take value.\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>Claim spins:</b> https://1wffxn.life/v3/aggressive-casino?p=xomk","images":["221.png"]},
{"date":"2026-02-22","time":"22:00","content":"💰 <b>Start with ₦1,000 — double instantly</b>\n\n100% bonus added automatically + 70 spins 🎁\nSmall start. Big upside.\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>Begin now:</b> https://1wffxn.life/v3/aggressive-casino?p=xomk","images":["222.png"]},

{"date":"2026-02-23","time":"14:00","content":"🇳🇬🇰🇪 <b>Low entry. High potential</b>\n\n₦1,000 → ₦2,000\n₦5,000 → ₦10,000 💰\nBonus hits instantly. Withdraw anytime — no wahala.\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>Register today:</b> https://1wffxn.life/v3/aggressive-casino?p=xomk","images":["231.png"]},
{"date":"2026-02-23","time":"23:00","content":"⏰ <b>Welcome bonus won’t stay forever</b>\n\n100% + 70 spins first deposit → up to 500% across 4 deposits 🔥\nThose inside are already playing bigger.\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>Join before it ends:</b> https://1wffxn.life/v3/aggressive-casino?p=xomk","images":["232.png"]},

{"date":"2026-02-24","time":"14:00","content":"🏆 <b>Why players choose 1WIN daily</b>\n\n✅ 500% welcome boost\n✅ 30% cashback daily\n✅ 50 free bets daily\n✅ Same-day withdrawal 💰\n\nIf your platform gives less — switch now.\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>Move now:</b> https://1wffxn.life/v3/aggressive-casino?p=xomk","images":["241.png"]},
{"date":"2026-02-24","time":"23:00","content":"🌙 <b>Live matches, live odds, live money</b>\n\nFirst deposit = 500% instantly ⚡\n₦2,000 → ₦12,000 tonight. Don’t wait.\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>Jump in:</b> https://1wkrii.life/v3/landing-page/football?p=5pe0","images":["172.png"]}
]
# ====== FUNCTION TO SEND POSTS ======
def send_post(post):
    try:
        # We use HTML mode to support <b>bold</b> and <code>tap-to-copy</code>
        P_MODE = "HTML"

        if "images" in post and post["images"]:
            # If multiple images, send as album
            if len(post["images"]) > 1:
                media_group = []
                for idx, img_file in enumerate(post["images"]):
                    if os.path.exists(img_file):
                        if idx == 0:
                            # Apply HTML formatting to the caption
                            media_group.append(InputMediaPhoto(open(img_file, "rb"), caption=post["content"], parse_mode=P_MODE))
                        else:
                            media_group.append(InputMediaPhoto(open(img_file, "rb")))
                if media_group:
                    bot.send_media_group(chat_id=CHANNEL_ID, media=media_group)
            else:
                # Single image
                img_file = post["images"][0]
                if os.path.exists(img_file):
                    with open(img_file, "rb") as photo:
                        # Apply HTML formatting to the photo caption
                        bot.send_photo(chat_id=CHANNEL_ID, photo=photo, caption=post["content"], parse_mode=P_MODE)
                else:
                    # Fallback to text if image missing
                    bot.send_message(chat_id=CHANNEL_ID, text=post["content"], parse_mode=P_MODE)
        else:
            # Text only
            bot.send_message(chat_id=CHANNEL_ID, text=post["content"], parse_mode=P_MODE)

        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Posted Successfully")
    except Exception as e:
        print(f"Failed to post: {e}")

# ====== SCHEDULE JOBS ======
for post in posts:
    # Convert string date to real datetime
    post_date = datetime.strptime(post["date"], "%Y-%m-%d")
    hour, minute = map(int, post["time"].split(":"))

    # Schedule EXACT date + time
    scheduler.add_job(
        send_post,
        'cron',
        year=post_date.year,
        month=post_date.month,
        day=post_date.day,
        hour=hour,
        minute=minute,
        args=[post],
        timezone=TIMEZONE,
        misfire_grace_time=300
    )


# ====== START BOT ======
print("Bot is running and will post messages automatically...")
scheduler.start()