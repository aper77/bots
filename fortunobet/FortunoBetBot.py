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
  "date": "2025-11-24",
  "time": "20:00",
  "content": "✨ ROLL THE DICE, WIN BIG! ✨\n\nReady for some fast-paced action and instant wins? Dive into **Lucky Dice** by Pragmatic Play at FortunoBet! 🎲\n\nThis thrilling game is all about predicting the outcome and hitting those lucky numbers for massive payouts. Simple to play, exciting to win!\n\n💡 **Pro Tip:** Maximize your gameplay by checking out our current bonuses! A deposit bonus or free spins could give you the edge you need to land those epic wins on Lucky Dice. The more you play, the more chances you have!\n\n⬇️ Play Lucky Dice NOW! ⬇️\nhttps://fortunobet.com",
  "images": ["241.png"]
},
{
  "date": "2025-11-25",
  "time": "12:00",
  "content": "💰 **MID-WEEK POWER PLAY: EPIC DEPOSIT SERIES!** 💰\n\nDon't wait for the weekend to win big! Boost your bankroll today with the incredible **Epic Deposit Series** and claim up to **$38,180** in bonus funds!\n\nThis massive offer covers your:\n* **2nd Deposit:** Up to $100 Match!\n* **3rd Deposit:** Up to $100 Match!\n* **4th Deposit:** Up to $100 Match!\n\n💡 **Pro Tip:** Keep the action going all week long. Every deposit gets you closer to that maximum payout!\n\n👉 **Claim Your Next Deposit Bonus Now:**\nhttps://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration\n\nDeposit now and chase those epic wins! 🚀",
  "images": ["251.png"]
},
  {
    "date": "2025-11-25",
    "time": "20:00",
    "content": "⚽🏈🏀 **THE ULTIMATE SPORTS ARENA IS HERE!** 🏒🎾🥊\n\nNo matter your game, FortunoBet has the odds and action you're looking for.\n\nFrom **Soccer** and **Basketball** to **Esports** and niche markets, we offer thousands of live and pre-match betting opportunities every day.\n\n🔥 **Why Choose FortunoBet Sports?**\n* **Massive Selection:** Bet on all major leagues and international events.\n* **Best Odds:** Competitive prices across the board.\n* **Live Betting:** Non-stop in-play excitement.\n\n👉 **SEE ALL SPORTS & BET NOW!** 👈\nhttps://fortunobet.com/com/sports",
    "images": ["252.png"]
  },
  {
    "date": "2025-11-26",
    "time": "12:00",
    "content": "✨ **WEDNESDAY BOOST: 75% SECOND DEPOSIT BONUS!** ✨\n\nReady for a mid-week reload? Your 2nd Deposit gets a massive match!\n\n🥈 **75% Match Bonus**\n💰 **Claim Up to $100**\n\nDon't miss out on the Deposit Series rewards—power up your account today!\n\n👉 **RELOAD NOW!**\nhttps://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration",
    "images": ["261.png"]
  },
    {
    "date": "2025-11-26",
    "time": "20:00",
    "content": "🤯 **OVER 1000 GAMES & COUNTING!** 🤯\n\n**Warning: Your game library is about to explode!** 💥\n\nAt FortunoBet, we don't just have slots—we have an *entire universe* of casino action. With **1000+** games and **NEW** titles added *every single day* (from top providers like Pragmatic Play and Evolution), you'll always find your next favorite slot, crash game, or Live Roulette table.\n\n🎲 **What's waiting for you?**\n* **MEGAWAYS** Slots with 117,649 ways to win!\n* **Live Casino** for real-dealer thrills.\n* **Jackpots** that could change your life!\n\nStop scrolling and start spinning! Your perfect game is waiting to be discovered.\n\n👉 **FIND YOUR FAVORITE GAME NOW!**\nhttps://fortunobet.com",
    "images": ["262.png"]
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




