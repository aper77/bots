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
  "date": "2025-12-03",
  "time": "12:00",
  "content": "🚀 🤩 Your cash just got a whole lot bigger at FortunoBet.\n\nWe're kicking off your winning week by **DOUBLING** your very first deposit! Get a **100% Match Bonus** up to **$130** just for signing up and making a deposit.\n\n* 💰 **100% Match:** Double your funds instantly.\n* 💵 **Up to $130 FREE** to play with.\n* 🎰 Use it on slots, live casino, or sports!\n\nIt's the ultimate welcome package to start your journey!\n\nReady to claim your $130 bonus and start playing? 👇\n\n**Claim Your 100% Bonus Now!**\n\nRegister Here: https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration\nVisit Fortunobet: 🌐 https://fortunobet.com",
  "images": ["031.jpg"]
},
{
  "date": "2025-12-03",
  "time": "20:00",
  "content": "💰 STOP! Guaranteed Wednesday Profit Alert! \n\nWe've locked in the two safest bets for tomorrow's Cup matches to **DOUBLE** your money with a high-probability Accumulator! Get incredible value with a total combined odds of **2.30X**!\n\n* ⚽ **Freiburg & Napoli** are strong home favorites.\n* ✅ **2.30X Odds:** Turn ₦5,000 into **₦11,500+** instantly.\n* ⏰ **Kick-off:** Don't miss the 6:00 PM Nigerian time games!\n\nOur experts did the work—all you have to do is bet.\n\nReady to place this winning slip? Click below to load the matches! 👇\n\n**PLACE THE 2.30X ACCA NOW!**\n\nPlace Bet Here:https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=line/football\nVisit Fortunobet:🌐 https://fortunobet.com",
  "images": [
    "032.jpg"
  ]
},
{
  "date": "2025-12-04",
  "time": "12:00",
  "content": "🤩 DID YOU CLAIM YOUR FIRST BONUS? Don't Stop Now!\n\nWe're rewarding our loyal players with the next step in the Epic Deposit Series: A massive **75% Match Bonus** on your second deposit! This is your chance to keep the winning streak alive!\n\n* 🥈 **75% Bonus Match** - HUGE value you won't find anywhere else.\n* 💵 **Up to $100 FREE** added instantly to your balance.\n* 🚀 **Fuel Your Play** and explore all our top casino games.\n\nKeep that momentum going and take your Thursday play to the next level!\n\n**Claim Your 75% Bonus & Level Up!** 👇\n\n https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration \n\n🌐 Official Website: https://fortunobet.com\n\n#FortunoBet #SecondDeposit #DepositBonus #CasinoBonus\n\nHow high will you climb with this extra boost? 🚀",
  "images": [
    "041.jpg"
  ]
},
{
  "date": "2025-12-04",
  "time": "20:00",
  "content": "🚨 ALERT: You're Leaving Money on the Table! 🚨\n\nStop hunting for single offers! FortunoBet has loaded our **entire bonus section** with **massive rewards**—from Welcome Matches to Weekly Cashbacks.\n\nClick below to unlock a universe of opportunities and let Fortuno bring you fortune!\n\n### 💰 Your Benefits Today:\n\n* **ALL Offers in ONE Place:** Find the perfect bonus for *your* game (Casino, Sports, VIP).\n* 🔥 **ML_1577703:** Use this exclusive code for potential extra rewards!\n* 💎 **Play with Confidence:** Trust FortunoBet for transparent bonuses and secure play.\n\nDon't settle for less. We have a bonus waiting for every kind of player!\n\n**See All Bonuses & Claim Your Fortune!** 👇\n\nhttps://fortunobet.com/com/bonuses\n\n🌐 Official Website: https://fortunobet.com\n\nWhat's the best bonus you've ever claimed? Share below! 🏆",
  "images": [
    "042.png"
  ]
},
{
  "date": "2025-12-05",
  "time": "12:00",
  "content": "🎉 IT'S FRIDAY! Get 100 FREE SPINS to start the weekend! 🎉\n\nKick off your weekend like a VIP! FortunoBet is giving you a powerful deposit match **AND** a massive stack of Free Spins to hit the slots!\n\nDeposit today and automatically unlock the best Friday treat:\n\n* 🥂 **50% Match Bonus** up to **$100**!\n* 🎰 **100 Free Spins** on a top slot! (That's 100 extra chances to win big!)\n* 🚀 **Weekend Boost:** Double the fun, double the chances to win big!\n\nYour luxury weekend starts now. Claim your free spins before they're gone!\n\n**Claim Your 50% Match + 100 FS!** 👇\n\nhttps://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration\n\n🌐 Official Website: https://fortunobet.com\n\nWhich slot are you spinning your 100 Free Spins on? Let us know! 🥳",
  "images": [
    "051.png"
  ]
},
{
  "date": "2025-12-02",
  "time": "20:00",
  "content": "🤯 STOP LOSING! WIN MORE on Velvet Games Today! 💡\n\nKnowledge is power! Master the strategies pros use to maximize profits and minimize losses on **Velvet Games by Evoplay**—it's time to play smarter.\n\nHere are 3 expert tips to help you secure a win:\n\n* ✅ **Money Management:** **Never chase losses!** Set a strict limit and stick to it; consistency beats impulsive betting every time.\n* 📈 **Smart Scaling:** Start small to find the game's rhythm. Only increase your stake when you are confidently **ahead**.\n* 🎯 **Target Multipliers:** Dedicate a specific, safe bankroll to chase those huge X-wins or bonus features—that's where the **BIG money** is!\n\nStart using these techniques now to build your winning bankroll!\n\n**Play Velvet Games & Start Winning!** 👇\n\nPlay Velvet Games Here:https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration\n🌐 Official Website: https://fortunobet.com\n\nReady to try these tips? Let us know when you hit that first big win! 🏆",
  "images": [
    "052.webp"
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




