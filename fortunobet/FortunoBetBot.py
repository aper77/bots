from telegram import Bot, InputMediaPhoto
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime, timedelta
import pytz
import os

# ====== CONFIG ======
BOT_TOKEN = "8758294585:AAGKPOwbpKN1jb8B7KIvUGcM2voJDPz5DPc"
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

{"date":"2026-03-23","time":"14:00","content":"💚 <b>$150 → $181.50. Elena Rybakina ✅</b>\n\nWTA Miami. USA. Hard. 🎾\nOdds 1.21 — ultra safe tennis.\n\n$31.50 profit. One match.\nNew week. First bet. GREEN. 💸\n\nLast week: 6 wins, 1 loss, withdrew ₦158k.\nThis week: Already started winning.\n\nYou watched all last week.\nStill watching this week? 🔥\n\nDeposit ₦10,000 → play with ₦60,000\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Start NOW:</b>\nhttps://1wfafs.life/casino/list?open=register&p=z4m5","images":["win1.png"]},
{"date":"2026-03-23","time":"23:30","content":"🎰 <b>₦5,200,000 won on Gates of Olympus yesterday</b>\n\nNigerian player.\n₦50,000 bet.\n₦5,200,000 won. 💰\n\nOne spin. Life changed.\n\nSlots pay MORE than sports.\nCasino = bigger wins. 🔥\n\nSame platform you're watching.\n\nDeposit ₦20,000 → play with ₦120,000\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Play slots:</b>\nhttps://1wfafs.life/casino/list?open=register&p=z4m5","images":["232.png"]},

{"date":"2026-03-24","time":"14:00","content":"💸 <b>Withdrew GH₵187.20 yesterday — Instant</b>\n\nMar 23, 01:13 PM ✅\nTelecel Cash 💚\n\nRequested afternoon.\nArrived afternoon.\nSame minute.\n\nGhana mobile money works.\nTelecel works.\nZero wahala. 🔥\n\nYou can't withdraw what you don't deposit.\n\nDeposit ₦10,000 → play with ₦60,000\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Start:</b>\nhttps://1wfafs.life/casino/list?open=register&p=z4m5","images":["withdrow1.png"]},
{"date":"2026-03-24","time":"23:30","content":"💚 <b>Start with ₦500. Not ₦10,000.</b>\n\n₦500 minimum via Opay.\n₦500 → ₦3,000 instant. ⚡\n\nTest today:\n✅ Deposit ₦500\n✅ Play one bet\n✅ Withdraw ₦2,000\n✅ Money arrives 15 minutes\n\nProof first. Big deposit after.\n\nSmart players test.\nScared players watch. 🔥\n\nDeposit ₦500 → play with ₦3,000\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Test now:</b>\nhttps://1wfafs.life/casino/list?open=register&p=z4m5","images":["242.png"]},

{"date":"2026-03-25","time":"14:00","content":"💚 <b>$100 → $137. Tommy Paul ✅</b>\n\nATP Miami. USA. Hard. 🎾\nOdds 1.37 — safe tennis.\n\n$37 profit. One match.\nSmall bet. Clean win. 💸\n\nMonday: $31.50 ✅\nWednesday: $37 ✅\nTwo days. Two wins.\n\nThey deposited Monday.\nAlready in profit.\n\nYou're still watching? 🔥\n\nDeposit ₦20,000 → play with ₦120,000\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Join NOW:</b>\nhttps://1wfafs.life/casino/list?open=register&p=z4m5","images":["win2.png"]},
{"date":"2026-03-25","time":"23:30","content":"⚠️ <b>Bonus expires 48 hours after registration</b>\n\nRegistered Monday? Expires Wednesday 11:59 PM.\nRegistered Tuesday? Expires Thursday 11:59 PM.\n\n500% isn't lifetime.\nYou have 48 hours. ⏰\n\nAfter 48 hours:\n❌ No 500% bonus\n❌ Regular deposit only\n❌ You missed it\n\nRegistered already?\nDeposit before deadline. 🔥\n\nDeposit ₦5,000 → play with ₦30,000\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Deposit NOW:</b>\nhttps://1wfafs.life/casino/list?open=register&p=z4m5","images":["252.png"]},

# {"date":"2026-03-26","time":"14:00","content":"💔 <b>Lost $70 — sharing honestly</b>\n\nATP Miami. Felix Auger-Aliassime. 🎾\nOdds: 1.26\n\nLost. ❌\n$70 gone. 😤\n\nReal betting.\nNot every bet wins.\n\nThis week so far:\n3 wins = $105.50 ✅\n1 loss = -$70 ❌\nStill in plus. +$35.50 💚\n\nMore wins than losses = profit. 🔥\n\nDeposit ₦20,000 → play with ₦120,000\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Join:</b>\nhttps://1wfafs.life/casino/list?open=register&p=z4m5","images":["lose1.png"]},
{"date":"2026-03-26","time":"22:00","content":"💰 <b>30% cashback on every losing day</b>\n\nAutomatic. No claim needed. ✅\n\nLose ₦10,000 → ₦3,000 back tomorrow\nLose ₦50,000 → ₦15,000 back tomorrow\n\nEvery bet protected.\nZero risk.\n\nOther platforms?\nYou lose = gone forever. ❌\n\nHere?\nYou lose = 30% back tomorrow. 💚\n\nSmart players choose protection. 🔥\n\nDeposit ₦20,000 → play with ₦120,000\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Join protected:</b>\nhttps://1wfafs.life/casino/list?open=register&p=z4m5","images":["262.jpeg"]},

{"date":"2026-03-27","time":"14:00","content":"💚 <b>$150 → $168. Alexander Zverev ✅</b>\n\nATP Miami. 🎾 Ultra safe win.\nThree wins this week. Still in plus. 🔥\n\nDeposit ₦30,000 → play with ₦180,000\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Join:</b>\nhttps://1wfafs.life/casino/list?open=register&p=z4m5","images":["win3.png"]},
{"date":"2026-03-27","time":"23:30","content":"🎰 <b>₦12.1 Billion Drops & Wins live</b>\n\n€7,350,000 prize pool. 🎲\nEvery spin = chance to win millions. 💰\n\n<b>Could be you. Enter now.</b> 🔥\n\nDeposit ₦20,000 → play with ₦120,000\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Enter now:</b>\nhttps://1wfafs.life/casino/list?open=register&p=z4m5","images":["272.jpeg"]},

{"date":"2026-03-28","time":"11:00","content":"💸 <b>Withdrew ₦114,646 — Instant ✅</b>\n\nPalmpay 💚 Arrived same minute.\nNigeria & Ghana both work. 🔥\n\n<b>You can't withdraw what you don't deposit.</b>\n\nDeposit ₦10,000 → play with ₦60,000\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Start:</b>\nhttps://1wfafs.life/casino/list?open=register&p=z4m5","images":["withdrow2.png"]},
{"date":"2026-03-28","time":"16:49","content":"💸 <b>Screenshot Contest — Win ₦5,000!</b>\n\nDeposited this week? Send screenshot. 💰\nBest screenshot = ₦5,000 bonus! 🔥\n\n(Already 3 entries received)\n\nDeposit ₦10,000 → play with ₦60,000\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Deposit & win:</b>\nhttps://1wfafs.life/casino/list?open=register&p=z4m5","images":["282.png"]},

{"date":"2026-03-29","time":"11:00","content":"💚 <b>4 wins, 1 loss. Net: +$57.50 profit 🔥</b>\n\n80% win rate. Showed everything. 💸\nThey withdrew profits. You just watched.\n\n<b>Your turn NOW. STOP WATCHING.</b> 💸\n\nDeposit ₦100,000 → play with ₦600,000\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>JOIN:</b>\nhttps://1wfafs.life/casino/list?open=register&p=z4m5","images":["win4.png","lose1.png"]},
{"date":"2026-03-29","time":"22:00","content":"⏰ <b>Monday midnight: Deposit or lose 500%</b>\n\n48-hour bonus closing. ⚠️\nAfter deadline: ❌ No 500% bonus. 🔥\n\n<b>Deposit before midnight or lose bonus forever.</b>\n\nDeposit ₦10,000 → play with ₦60,000\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Deposit NOW:</b>\nhttps://1wfafs.life/casino/list?open=register&p=z4m5","images":["292.png"]}
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