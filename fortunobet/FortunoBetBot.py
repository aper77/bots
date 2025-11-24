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
  "content": "🎲 Feeling lucky today? Try your hand at Lucky Dice!\n\nPredict the dice, hit the right numbers, and win instantly with Pragmatic Play’s exciting game at FortunoBet. It’s simple, fast, and fun!\n\n💡 Why play now?\n\n- Boost your chances with current deposit bonuses or free spins\n- Instant wins every round\n- Easy to pick up and start playing immediately\n\nReady to roll and see if luck is on your side? ⬇️\nhttps://fortunobet.com\n\nWhat’s your favorite winning strategy—high numbers or low? Let us know!",
  "images": ["241.png"]
},
{
  "date": "2025-11-25",
  "time": "12:00",
  "content": "💰 Boost Your Wins Mid-Week with the Epic Deposit Series! 💰\n\nTake advantage of our Epic Deposit Series and claim up to **$38,180** in bonus funds to grow your bankroll faster.\n\n📌 How it works:\n- 2nd Deposit: Up to $100 Match\n- 3rd Deposit: Up to $100 Match\n- 4th Deposit: Up to $100 Match\n\n💡 Pro Tip: Keep depositing throughout the week to get closer to the maximum bonus and enjoy more chances to win.\n\n👉 Claim Your Bonus Now: https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration\n\nWhich deposit level will you hit next? Let us know and start winning!",
  "images": ["251.png"]
},
  {
    "date": "2025-11-25",
    "time": "20:00",
    "content": "⚽🏈🏀 THE ULTIMATE SPORTS ARENA IS HERE! 🏒🎾🥊\n\nNo matter your game, FortunoBet has the odds and action you're looking for.\n\nFrom Soccer and Basketball to Esports and niche markets, we offer thousands of live and pre-match betting opportunities every day.\n\n🔥 Why Choose FortunoBet Sports?\n- Massive Selection: Bet on all major leagues and international events.\n- Best Odds: Competitive prices across the board.\n- Live Betting: Non-stop in-play excitement.\n\n👉 SEE ALL SPORTS & BET NOW! 👈\nhttps://fortunobet.com/com/sports",
    "images": ["252.png"]
  },
  {
    "date": "2025-11-26",
    "time": "12:00",
    "content": "✨ Mid-Week Boost: 75% Bonus on Your 2nd Deposit! ✨\n\nReload your account and enjoy a 75% match bonus, claiming up to $100 on your 2nd deposit. Keep your mid-week momentum going and maximize your playing power!\n\n💡 Why reload now?\n- Instantly boost your bankroll\n- More chances to win in the Deposit Series\n- Quick and easy to claim\n\n👉 Claim Your Bonus Here: https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration\n\nWill you go for the full $100 bonus this week? Let us know!",
    "images": ["261.png"]
  },
    {
    "date": "2025-11-26",
    "time": "20:00",
    "content": "🤯 OVER 1000 GAMES & COUNTING! 🤯\n\nYour game library is about to explode! 💥\n\nAt FortunoBet, we offer an entire universe of casino action. With over 1000 games and new titles added every day from top providers like Pragmatic Play and Evolution, you'll always find your next favorite slot, crash game, or Live Roulette table.\n\n🎲 What's waiting for you?\n- MEGAWAYS Slots with 117,649 ways to win\n- Live Casino for real-dealer thrills\n- Jackpots that could change your life\n\nStop scrolling and start spinning! Your perfect game is ready to be discovered.\n\n👉 FIND YOUR FAVORITE GAME NOW! https://fortunobet.com",
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




