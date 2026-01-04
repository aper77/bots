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
{"date":"2026-01-04","time":"15:00","content":"💰 $100,000 giveaway is URGENTLY live on 1XBET.\nBet and get free tickets for the biggest New Year prize draw.\n👇 Enter the 1XBET draw in the next 15 minutes: https://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=promotions/santas-gift","images":["041.png"]},
{"date":"2026-01-04","time":"23:00","content":"🔥 Get $5 free cash: Deposit $3 on 1XBET or MelBet.\nURGENT: Limited to the first 50 users who deposit now.\n👇 Claim your MelBet/1XBET gift $150 midnight: https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration","images":["042.png"]},

{"date":"2026-01-05","time":"15:00","content":"🔥 MelBet Multiplier: Win 2.11X live now.\nHigh-odds goal bet needs URGENT action.\n👉 Claim this fast payout: https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=line/football","images":["051.png"]},
{"date":"2026-01-05","time":"23:00","content":"🔥 1XBET: Man City wins at 1.67X.\nEasiest Premier League win guaranteed.\n👉 Claim in 10 minutes: https://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=line/football","images":["052.png"]},

{"date":"2026-01-06","time":"15:00","content":"💰 MelBet: Get 3% Cashback now.\nWeekly loss protection, credited instantly.\n👉 Claim your risk-free money today: https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration","images":["061.png"]},
{"date":"2026-01-06","time":"23:00","content":"💰 MelBet: Spinomenal's Demi Gods V is live.\nTrigger Free Spins for the huge MULTIPLIER win.\n👉 Play the slot right now: https://fortunobet.com/com","images":['062.png']},

{"date":"2026-01-07","time":"15:00","content":"🔥 1XBET: Double your money this Friday.\n100% Reload Bonus requires URGENT accumulator bets.\n👉 Deposit and claim your bonus now: https://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=line/football","images":["071.png"]},
{"date":"2026-01-07","time":"23:00","content":"💰 1XBET: Sweet Bonanza 1000 is upgraded.\nBuy the bonus for 100X multiplier chance.\n👉 Spin for huge payouts now: https://fortunobet.com/com","images":["072.png"]},

{"date":"2026-01-08","time":"15:00","content":"💰 1XBET: CRUSH the bookies with the best odds.\nMassive markets guaranteed for your instant, biggest payout.\n👉 Win your massive betting slip now: https://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=line/football","images":["081.png"]},
{"date":"2026-01-08","time":"23:00","content":"🔥 MelBet: STOP losing value on your bets.\n1,500+ markets daily secure your winning edge URGENTLY.\n👉 Register for the best football odds: https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration","images":["082.png"]},

{"date":"2026-01-09","time":"15:00","content":"🔥 1XBET: DOUBLE your deposit for the weekend.\n100% Reload Bonus is URGENTLY live right now.\n👉 Claim your FREE 300 EUR betting cash: https://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=line/football","images":["091.png"]},
{"date":"2026-01-09","time":"23:00","content":"🔥 MelBet: Get 100 FREE SPINS now.\nThis 50% Friday VIP Treat is URGENTLY activated.\n👉 Claim your free casino spins here: https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration","images":["092.png"]},

{"date":"2026-01-10","time":"15:00","content":"💰 MelBet: Play Coinspin Fever now.\nHit the Hold and Spin feature for the Grand Jackpot.\n👉 Claim your huge 5000X prize here: https://fortunobet.com/com","images":["101.png"]},
{"date":"2026-01-10","time":"23:00","content":"💰 1XBET: Sweet Bonanza Xmas is dropping cash.\nHit the Free Spins for a 100X Multiplier Bomb payout.\n👉 Buy your bonus round URGENTLY now: https://fortunobet.com/com","images":["102.png"]},
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




