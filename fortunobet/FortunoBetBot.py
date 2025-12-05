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
  "date": "2025-12-05",
  "time": "20:00",
  "content": "🤯 STOP LOSING! WIN MORE on Velvet Games Today! 💡\n\nKnowledge is power! Master the strategies pros use to maximize profits and minimize losses on **Velvet Games by Evoplay**—it's time to play smarter.\n\nHere are 3 expert tips to help you secure a win:\n\n* ✅ **Money Management:** **Never chase losses!** Set a strict limit and stick to it; consistency beats impulsive betting every time.\n* 📈 **Smart Scaling:** Start small to find the game's rhythm. Only increase your stake when you are confidently **ahead**.\n* 🎯 **Target Multipliers:** Dedicate a specific, safe bankroll to chase those huge X-wins or bonus features—that's where the **BIG money** is!\n\nStart using these techniques now to build your winning bankroll!\n\n**Play Velvet Games & Start Winning!** 👇\n\nPlay Velvet Games Here:https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration\n🌐 Official Website: https://fortunobet.com\n\nReady to try these tips? Let us know when you hit that first big win! 🏆",
  "images": [
    "052.webp"
  ]
},
{
  "date": "2025-12-06",
  "time": "12:00",
  "content": "🚀 Deposit Now & Double Your Rewards! 💰\n\n🚨 SPECIAL ALERT: FIRST DEPOSIT DAY! 🚨\n\nToday is the day to make your first deposit at FortunoBet and unlock exclusive, limited-time benefits! We've partnered with our top casino and sportsbook providers to offer an unprecedented bonus boost just for you.\n\nEnjoy an immediate Extra Bonus with significantly MORE matched funds and free spins/bets from our partners! Plus, FortunoBet is adding an extra $5 directly to your account with a FREE $5 Deposit, so you can access premier Casino Games and Sports Betting with a bigger starting bankroll!\n\nThis exclusive offer is valid TODAY ONLY for the FIRST users to make their initial deposit. Don't miss out on the easiest way to multiply your play!\n\n👉 Click Here to Claim Your $5 + Mega Bonus Now:\nRegister Here: https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration\n\n🌐 Visit Fortunobet: https://fortunobet.com\n\nReady to turn $5 into a big win? Let us know in the comments! 👇",
  "images": ["061.jpg"]
},
{
  "date": "2025-12-06",
  "time": "20:00",
  "content": "🏆 STOP! GUARANTEED PROFIT ALERT! 💰\n\nTomorrow's cup matches offer an incredible chance to DOUBLE YOUR MONEY with our expert-picked accumulator! We've identified two high-probability wins, giving you a total combined odds of 2.30X.\n\n* ✅ Double Your Cash: Turn your stake into 2.30X profit instantly.\n* ⚽ Safest Picks: Betting on strong home favorites: Freiburg & Napoli.\n* Time Sensitive: Lock in this winning slip before the 6:00 PM kick-off (Nigerian Time)!\n\nOur experts have locked the value—all you need to do is bet. Don't let this sure-fire opportunity pass!\n\n👉 Click Here to Load the 2.30X Winning Slip:\nPlace Bet Here: https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=line/football\n\n🌐 Visit Fortunobet: https://fortunobet.com\n\nAre you placing this bet with us? Let us know! 👇",
  "images": [
    "062.jpg"
  ]
},
{
  "date": "2025-12-07",
  "time": "12:00",
  "content": "🤩 DID YOU CLAIM YOUR FIRST BONUS? Don't Stop Now! 🚀\n\nWe're rewarding our active players with the next step in our Epic Deposit Series: A massive 75% Match Bonus on your second deposit! This is your chance to keep the winning streak alive!\n\n* 🥈 75% Bonus Match: HUGE value you won't find anywhere else.\n* 💵 Up to $100 FREE: Added instantly to your balance to fuel your play.\n* Keep the Momentum: Perfect for exploring all our top casino games and slots.\n\nKeep that momentum going and take your play to the next level today!\n\nClaim Your 75% Bonus & Level Up! 👇\n\n https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration \n\n🌐 Official Website: https://fortunobet.com\n\nHow high will you climb with this extra boost? 🚀",
  "images": [
    "071.jpg"
  ]
},
{
  "date": "2025-12-07",
  "time": "20:00",
  "content": "🚨 ALERT: You're Leaving Money on the Table! 💰\n\nStop hunting for single offers! FortunoBet has loaded our entire bonus section with massive rewards—from Welcome Matches to Weekly Cashbacks.\n\n* ✅ ALL Offers in ONE Place: Find the perfect bonus for *your* game (Casino, Sports, VIP).\n* 🔥 Exclusive Code: Use ML_1577703 for potential extra rewards!\n* Play with Confidence: Trust FortunoBet for transparent bonuses and secure play.\n\nClick below to unlock a universe of opportunities and let Fortuno bring you fortune! Don't settle for less—we have a bonus waiting for every kind of player!\n\n👉 See All Bonuses & Claim Your Fortune! 👇\n\nhttps://fortunobet.com/com/bonuses\n\n🌐 Official Website: https://fortunobet.com\n\nWhat's the best bonus you've ever claimed? Share below! 🏆",
  "images": [
    "072.jpg"
  ]
},
{
  "date": "2025-12-08",
  "time": "12:00",
  "content": "👑 MONDAY MADNESS IS HERE! Double Your Cash Today! 🚀\n\nBeat the Monday blues and kickstart your week with a guaranteed win! Make any deposit today and FortunoBet will reward you with a full 100% Match Bonus instantly.\n\n* ✅ 100% Match: Whatever you deposit, we double it for free.\n* 💰 Maximum Playtime: Get the biggest possible bankroll boost for your Casino and Sports bets.\n* Weekly Power: This offer renews every Monday to maximize your winning potential!\n\nDon't wait—this massive bonus is only valid today!\n\n👉 Click Here to Claim Your 100% Monday Match Now!\nRegister Here: https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration\n\n🌐 Visit Fortunobet: https://fortunobet.com\n\nWhat are you betting on this week with your double money? Tell us! 👇",
  "images": [
    "081.png"
  ]
},
{
  "date": "2025-12-08",
  "time": "20:00",
  "content": "🤯 STOP LOSING! WIN MORE on Velvet Games Today! 💡\n\nKnowledge is power! Master the strategies pros use to maximize profits and minimize losses on Velvet Games by Evoplay—it's time to play smarter.\n\nEnter our promo code: ML_1577703 for potential extra rewards!\n\nHere are 3 expert tips to help you secure a win:\n\n* ✅ Money Management: Never chase losses! Set a strict limit and stick to it; consistency beats impulsive betting every time.\n* 📈 Smart Scaling: Start small to find the game's rhythm. Only increase your stake when you are confidently ahead.\n* 🎯 Target Multipliers: Dedicate a specific, safe bankroll to chase those huge X-wins or bonus features—that's where the BIG money is!\n\nStart using these techniques now to build your winning bankroll!\n\n👉 Play Velvet Games & Start Winning! 👇\n\nPlay Velvet Games Here: https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration\n🌐 Official Website: https://fortunobet.com\n\nReady to try these tips? Let us know when you hit that first big win! 🏆",
  "images": [
    "082.png"
  ]
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




