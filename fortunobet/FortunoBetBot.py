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

# ====== TEXT & IMAGE POSTS SCHEDULE ======
posts = [
{
  "date": "2025-11-20",
  "time": "15:45",
  "content": "🔥 READY TO WIN THIS WEDNESDAY? LET’S GO, KENYA! 🔥\n\nYour chance to boost your bankroll is LIVE right now.\nMake a deposit this morning and GET 100% BONUS up to $130 instantly! 💰💥\n\nNo limits. No delays. Just DOUBLE the money and start playing.\nPerfect for Sportsbook, Casino, Live Games — everything you love.\n\n👉 Visit FortunoBet (Main Site):\nhttps://fortunobet.com\n\n👉 Full Registration (Bonus + ACCA Insurance):\nhttps://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration\n\nThis is your mid-week power boost.\n🔥 Take the bonus.\n🔥 Place your bets.\n🔥 Start winning today! 🚀",
  "images": ["bonus.png"]
},
{
  "date": "2025-11-21",
  "time": "21:00",
  "content": "🔥 WEDNESDAY NIGHT FOOTBALL ACTION — LET’S CASH IN! 🔥\n\nTwo massive games TONIGHT — perfect time to smash big bets and boost your winnings!\n\n⚽ Palmeiras vs Vitória\n⚽ Fluminense vs Flamengo (Huge Derby!)\n\nThese matches are LOADED with value. Don’t wait. Jump straight into Football Section and place your winning combo now!\n\n👉 Football Section:\nhttps://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=line/football\n\n👉 FortunoBet:\nhttps://fortunobet.com\n\n💥 Don’t miss your chance — odds are FIRE tonight! Place your bets and LET’S WIN BIG! 💰🔥",
  "images": ["second.png"]
}   ]

# ====== FUNCTION TO SEND POSTS ======
def send_post(post):
    try:
        if "images" in post and post["images"]:
            # If multiple images, send as album
            if len(post["images"]) > 1:
                media_group = []
                for idx, img_file in enumerate(post["images"]):
                    if os.path.exists(img_file):
                        if idx == 0:
                            media_group.append(InputMediaPhoto(open(img_file, "rb"), caption=post["content"]))
                        else:
                            media_group.append(InputMediaPhoto(open(img_file, "rb")))
                if media_group:
                    bot.send_media_group(chat_id=CHANNEL_ID, media=media_group)
            else:
                # Single image
                img_file = post["images"][0]
                if os.path.exists(img_file):
                    with open(img_file, "rb") as photo:
                        bot.send_photo(chat_id=CHANNEL_ID, photo=photo, caption=post["content"])
                else:
                    bot.send_message(chat_id=CHANNEL_ID, text=post["content"])
        else:
            # Text only
            bot.send_message(chat_id=CHANNEL_ID, text=post["content"])

        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Posted: {post['content']}")
    except Exception as e:
        print(f"Failed to post {post['content']}: {e}")

# ====== IMMEDIATE POSTS IF BOT STARTS LATE ======
now = datetime.now(TIMEZONE)
for post in posts:
    hour, minute = map(int, post["time"].split(":"))
    post_time = TIMEZONE.localize(datetime(now.year, now.month, now.day, hour, minute))
    if now >= post_time and now <= post_time + timedelta(minutes=5):
        send_post(post)  # post immediately if missed within last 5 minutes

# ====== SCHEDULE JOBS ======
for post in posts:
    hour, minute = map(int, post["time"].split(":"))
    scheduler.add_job(send_post, 'cron', hour=hour, minute=minute, args=[post], timezone=TIMEZONE,
                      misfire_grace_time=300)  # 5 minutes grace time

# ====== START BOT ======
print("Bot is running and will post messages automatically...")
scheduler.start()
