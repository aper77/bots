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

{"date":"2026-03-02","time":"14:00","content":"💸 <b>Withdrew ₦38,000 this morning — 35 minutes</b>\n\nRequested: 10:22 AM ✅\nArrived Opay: 10:57 AM ✅\n\nSame day. Zero wahala. Every time. 💚\n\nYou can't withdraw what you don't deposit.\nStart today. Withdraw this week.\n\nDeposit ₦5,000 → play with ₦30,000\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Start now:</b>\nhttps://1wfafs.life/casino/list?open=register&p=z4m5","images":["021.png"]},

{"date":"2026-03-03","time":"14:00","content":"💸 <b>Withdrew ₦38,000 yesterday — 41 minutes</b>\n\nRequested: 2:15 PM ✅\nArrived Opay: 2:56 PM ✅\n\nSame day. Zero wahala. Every time. 💚\n\nYou can't withdraw what you don't deposit.\nStart today. Withdraw this week.\n\nDeposit ₦5,000 → play with ₦30,000\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>Start now:</b> https://1wfafs.life/casino/list?open=register&p=z4m5","images":["031.png"]},
{"date":"2026-03-03","time":"21:00","content":"📊 <b>Last 48 hours on this channel:</b>\n\n✅ 14 deposits\n✅ ₦340,000 total volume\n✅ 5 withdrawals same day\n✅ Biggest win: ₦92,000\n\nThey joined Wednesday. Withdrew Friday.\nYou're still watching. 💸\n\nYou joining? 🔥\n\nDeposit ₦5,000 → play with ₦30,000\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>Join now:</b> https://1wfafs.life/casino/list?open=register&p=z4m5","images":["032.png"]},

{"date":"2026-03-04","time":"14:00","content":"💰 <b>Start ₦1,000. Withdraw ₦10,000 next week.</b>\n\nMinimum deposit. Maximum opportunity. 💚\n\n₦1,000 → ₦2,000 + 70 spins instantly\n\nSmall start. Big results.\nStart today. See results by weekend.\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>Begin now:</b> https://1wfafs.life/casino/list?open=register&p=z4m5","images":["041.png"]},
{"date":"2026-03-04","time":"21:00","content":"💚 <b>Member result: Started ₦5,000 two weeks ago</b>\n\n\"Balance today: ₦41,000\nWithdrew ₦18,000 to Palmpay\nStill playing with ₦23,000\nThis is real.\" — Emeka, Lagos\n\nHis screenshot proves it. ✅\n\nTwo weeks ago he was watching.\nToday he's winning. Your turn? 🔥\n\nDeposit ₦5,000 → play with ₦30,000\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>Start today:</b> https://1wfafs.life/casino/list?open=register&p=z4m5","images":["042.png"]},

{"date":"2026-03-05","time":"14:00","content":"🇳🇬 <b>Why Nigerians choose 1WIN:</b>\n\n✅ Opay/Palmpay instant deposit\n✅ Same-day withdrawal (proven)\n✅ 30% cashback protection\n✅ 500% welcome bonus\n\nYour platform gives less? Switch today. 💸\n\nDeposit ₦2,000 → play with ₦12,000\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>Join now:</b> https://1wfafs.life/casino/list?open=register&p=z4m5","images":["051.png"]},
{"date":"2026-03-05","time":"21:00","content":"⚽ <b>Weekend here — all big leagues live</b>\n\nPremier League, La Liga, Serie A 🔥\n\n27 people from this channel placed weekend bets.\nMatches start tomorrow morning.\n\nYou watching or playing?\n\nDeposit ₦10,000 → play with ₦60,000\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>Bet now:</b> https://1wfafs.life/casino/list?open=register&p=z4m5","images":["052.png"]},

{"date":"2026-03-06","time":"14:00","content":"💰 <b>Lost this week? 30% returns Monday</b>\n\nAutomatic cashback. No claim. ✅\n\nLose ₦20,000 → ₦6,000 back Monday.\n\nSmart players protect bankroll. 💚\nJoin before week ends.\n\nDeposit ₦2,000 → play with ₦12,000\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>Join protected:</b> https://1wfafs.life/casino/list?open=register&p=z4m5","images":["012.png"]},

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