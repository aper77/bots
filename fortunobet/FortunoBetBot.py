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
  "date": "2025-11-27",
  "time": "20:00",
  "content": "💀 QUEEN HALLOWEEN DELUXE - THIS SLOT PAYS! 💀\n\nStop playing for fun. Start playing for PROFIT.\n\n🎯 BEST BETTING STRATEGY:\n* GO MAX BET! 🚀 Unlock the highest potential in the Bonus Round.\n* Land 3+ Scatter Symbols to trigger the 10 FREE SPINS!\n* WILD SUBSTITUTIONS create massive winning lines.\n\n🔥 This game is a JACKPOT machine! The expanding wilds and free spins can wipe out your balance... in your favor!\n\n⚡ Stop waiting. Start WINNING. Play NOW!\n➡️ https://fortunobet.com",
  "images": ["271.jpg"]
},
{
  "date": "2025-11-28",
  "time": "12:00",
  "content": "🚀 TODAY'S MONEY MAKER! 🚀\n\n💥 DOUBLE YOUR DEPOSIT - UP TO $130! 💥\n\n🔥 START WITH DOUBLE POWER!\n• 100% BONUS on your first deposit\n• MAXIMUM $130 extra playing money\n• INSTANT CREDIT - no waiting!\n\n🎯 HOW TO CLAIM:\n1. Register at FortunoBet\n2. Make your first deposit\n3. Get DOUBLE THE MONEY instantly!\n\n⚡ Stop starting from zero! Start with DOUBLE FIREPOWER!\n\n💸 READY TO 2X YOUR MONEY?\n⬇️ CLICK & CLAIM YOUR $130 NOW! ⬇️\nhttps://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration",
  "images": ["281.jpg"]
},
  {
    "date": "2025-11-28",
    "time": "20:00",
    "content": "⚽ TODAY'S AFRICAN FAVORITES! ⚽\n\n🔥 TOP 3 MATCHES FOR KENYA & NIGERIA:\n\n🎯 NOTTINGHAM FOREST vs MALMO\n⏰ 18:00 WAT/EAT\n💰 ODDS: 1.23 (Home) | 6.05 (Draw) | 13.00 (Away)\n⭐ African stars in both teams!\n\n🎯 RANGERS vs BRAGA  \n⏰ 21:00 WAT/EAT\n💰 ODDS: 3.26 (Home) | 3.44 (Draw) | 2.19 (Away)\n⚡ High-scoring potential!\n\n🎯 REAL BETIS vs UTRECHT\n⏰ 21:00 WAT/EAT\n💰 ODDS: 1.34 (Home) | 5.05 (Draw) | 8.90 (Away)\n🌟 Spanish football favorite!\n\n💸 READY TO BET?\n⬇️ CLICK & WIN BIG! ⬇️\nhttps://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=line/football\n\nPerfect timing for evening betting action!",
    "images": ["282.jpg"]
  },
  {
    "date": "2025-11-29",
    "time": "12:00",
    "content": "🔥 MID-WEEK BOOSTER! 🔥\n\n💰 50% BONUS + 30 FREE SPINS - UP TO $375! 💰\n\n⚡ DOUBLE VALUE DEAL:\n• 50% EXTRA on your deposit\n• PLUS 30 FREE SPINS\n• MAXIMUM $375 bonus money!\n\n🎯 PERFECT FOR:\n• Slot lovers wanting free spins\n• Players looking to extend their bankroll\n• Mid-week gaming sessions\n\n💸 HOW TO CLAIM:\n1. Make a deposit\n2. Get 50% bonus instantly\n3. Receive 30 free spins automatically\n\n🚀 BOOST YOUR MID-WEEK GAMING!\n⬇️ CLICK & CLAIM YOUR $375 + 30 SPINS! ⬇️\nhttps://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration\n\n🌐 Official Website: https://fortunobet.com\n\nPerfect timing to refresh your gaming balance!",
    "images": ["291.jpg"]
  },
    {
    "date": "2025-11-29",
    "time": "20:00",
    "content": "🎯 DOMINATE LOCO LUCK THUNDERSPIN! 🎯\n\n⚡ WINNING STRATEGY:\n• BET MAX LINES - Cover all wins\n• TRIGGER BONUS - 3+ scatters = free spins\n• EXPANDING WILDS - Cover entire reels\n• LIGHTNING MULTIPLIERS - Up to 10x!\n\n💡 PRO MOVE: Medium bets + bonus hunting = MAX WINS!\n\n⚡ READY TO WIN BIG?\n⬇️ PLAY SMART NOW! ⬇️\nhttps://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration\n\n🌐 https://fortunobet.com\n\nRide the thunder to victory! ⚡",
    "images": ["292.webp"]
  },
  ]

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




