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

{"date":"2026-02-27","time":"14:00","content":"💚 <b>$100 → $106. Real Madrid ✅</b>\n\nUEFA Champions League. Odds 1.06 — safe play, big volume. 🏆\n\n$6 profit? Do this 5 times = $30 daily.\nDo it 20 days = $600/month extra. 💸\n\nSmall players watch. Big players bet.\nWhich one are you? 🔥\n\nDeposit ₦50,000 → play with ₦300,000\n\n⏰ <b>Before midnight = EXTRA ₦1,000</b>\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>Join now:</b> https://1wfafs.life/casino/list?open=register&p=z4m5","images":["win2.jpeg"]},
{"date":"2026-02-27","time":"21:00","content":"📊 <b>Last 48 hours on this channel:</b>\n\n✅ 18 new deposits\n✅ ₦420,000 total deposited\n✅ 6 withdrawals processed same day\n✅ Biggest win: ₦87,000\n\nYou're watching. They're cashing out. 👀\n\nDeposit ₦2,000 → play with ₦12,000\n\n⏰ <b>Tonight only: EXTRA ₦500 bonus</b>\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>Your turn:</b> https://1wfafs.life/casino/list?open=register&p=z4m5","images":["272.png"]},

{"date":"2026-02-28","time":"14:00","content":"💸 <b>Withdrew ₦32,000 yesterday — same day</b>\n\nRequested: 2:45 PM ✅\nArrived Opay: 3:18 PM ✅\n\n33 minutes. Zero wahala.\n\nThis is why I trust 1WIN. 💚\n\nYou can't withdraw what you don't deposit.\nStart small. Build big.\n\nDeposit ₦2,000 → play with ₦12,000\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>Start now:</b> https://1wfafs.life/casino/list?open=register&p=z4m5","images":["281.png"]},
{"date":"2026-02-28","time":"21:00","content":"⚽ <b>Weekend coming — Premier League + La Liga live</b>\n\nMan City, Arsenal, Real Madrid, Barca all play. 🔥\n\n23 people from this channel already placed bets for weekend.\n\nYou watching or playing?\n\nDeposit ₦10,000 → play with ₦60,000\n\n⏰ <b>Deposit tonight = EXTRA ₦800</b>\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>Bet now:</b> https://1wfafs.life/casino/list?open=register&p=z4m5","images":["282.png"]},

{"date":"2026-03-01","time":"14:00","content":"⚽ <b>My pick: Inter Milan both halves at 2.1</b>\n\nBodo/Glimt weak defense. Inter needs statement win.\n\nI'm backing this with ₦15,000. 💰\n\nBoth halves = ₦31,500 profit if hits.\n\nDeposit ₦5,000 → play with ₦30,000\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>Bet with me:</b> https://1wfafs.life/casino/list?open=register&p=z4m5","images":["011.png"]},
{"date":"2026-03-01","time":"21:00","content":"💰 <b>Lost money this week? Get 30% back tonight</b>\n\nAutomatic cashback. No claim needed. ✅\n\nLose ₦20,000 → ₦6,000 returns Monday morning.\n\nSmart players protect bankroll. 💚\n\nDeposit ₦2,000 → play with ₦12,000\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>Join protected:</b> https://1wfafs.life/casino/list?open=register&p=z4m5","images":["012.png"]},

{"date":"2026-03-02","time":"14:00","content":"📊 <b>This week so far:</b>\n\nMonday: $12 profit ✅\nTuesday: $6 profit ✅\nWednesday: Waiting for Inter result\n\nSmall bets. Steady wins. This is the way. 💚\n\n38 people from this channel placed bets yesterday.\nYour turn? 🔥\n\nDeposit ₦2,000 → play with ₦12,000\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>Start winning:</b> https://1wfafs.life/casino/list?open=register&p=z4m5","images":["021.png"]},
{"date":"2026-03-02","time":"21:00","content":"🎁 <b>2nd deposit = 120% + 100 Free Spins</b>\n\n1WIN keeps rewarding. Not just first deposit. 💚\n\n487 Nigerians claimed this yesterday.\n\nDeposit ₦5,000 → play with ₦11,000 + 100 spins\n\n⏰ <b>Expires Monday midnight</b>\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>Claim yours:</b> https://1wfafs.life/casino/list?open=register&p=z4m5","images":["022.png"]},

{"date":"2026-03-03","time":"14:00","content":"💸 <b>How to turn ₦5,000 into ₦50,000 in 30 days:</b>\n\nWeek 1: Deposit ₦5,000 → get ₦30,000 with bonus\nWeek 2: Win ₦8,000 → reinvest half\nWeek 3: Withdraw ₦15,000 → play with rest\nWeek 4: Balance ₦50,000+ 💚\n\nSmall money makes big money. Proof in my wins.\n\nDeposit ₦5,000 → play with ₦30,000\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>Start today:</b> https://1wfafs.life/casino/list?open=register&p=z4m5","images":["031.png"]},
{"date":"2026-03-03","time":"21:00","content":"🏆 <b>4th deposit = 150% + 180 Free Spins</b>\n\nFinal bonus. Biggest reward. 🔥\n\nOnly 300 players claimed last week.\n\nDeposit ₦5,000 → play with ₦12,500 + 180 spins\n\n⏰ <b>Limited time offer</b>\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>Unlock now:</b> https://1wfafs.life/casino/list?open=register&p=z4m5","images":["032.png"]},

{"date":"2026-03-04","time":"14:00","content":"💰 <b>Start with ₦1,000 today. Withdraw ₦10,000 next week.</b>\n\nMinimum deposit. Maximum opportunity. 💚\n\n₦1,000 → ₦2,000 instantly + 70 spins\n\nSmall start. Big results.\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>Begin now:</b> https://1wfafs.life/casino/list?open=register&p=z4m5","images":["041.png"]},
{"date":"2026-03-04","time":"21:00","content":"⏰ <b>Welcome bonus expires Friday 11:59 PM</b>\n\n100% + 70 spins. Last 48 hours. 🔥\n\nThose who joined last week?\nAlready playing with 5x their money.\n\nThose waiting?\nStill waiting. ⌛\n\nDeposit ₦2,000 → play with ₦4,000 + 70 spins\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>Last chance:</b> https://1wfafs.life/casino/list?open=register&p=z4m5","images":["042.png"]},

{"date":"2026-03-05","time":"14:00","content":"🇳🇬 <b>Why Nigerians trust 1WIN:</b>\n\n✅ Opay/Palmpay instant deposit\n✅ Same-day withdrawal (no stories)\n✅ 30% cashback protection\n✅ 500% welcome bonus\n\nIf your platform gives less — you're losing money. 💸\n\nDeposit ₦2,000 → play with ₦12,000\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>Switch today:</b> https://1wfafs.life/casino/list?open=register&p=z4m5","images":["051.png"]},
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