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
{"date":"2025-12-31","time":"15:00","content":"🎁 HAPPY HOLIDAYS, GLOBAL WINNERS! 🎉\n\nThe entire FortunoBet family wishes you peace, joy, and GREAT FORTUNE today and throughout the New Year! 🥂\n\nThank you for placing your trust with us this year. We look forward to celebrating even bigger wins with you in the future!\n\n👇 YOUR TRUSTED HOME FOR WINNINGS 👇\nVISIT US NOW: https://fortunobet.com/com","images":["311.png"]},
{"date":"2025-12-31","time":"23:00","content":"💥 FINAL HOUR: NEW YEAR'S $5 FREE CASH! 🎁\n\n⏰ ENDS AT MIDNIGHT! ⏰\n\nIf you've registered but haven't made a deposit, FortunoBet has a gift to start your 2026!\n\nGET $5 FREE CASH IN 1 MINUTE:\n• Deposit just $3 or more right now.\n• We instantly gift you $5 EXTRA! 💰\n\nIt's the easiest $5 you will make today. Don't let this New Year's cash bonus expire!\n\n👇 CLAIM YOUR $5 BONUS NOW! 👇\n\nMELBET REGISTRATION: https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration\n\n1XBET REGISTRATION: https://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=registration\n\n🌐 Official Partner Site: https://fortunobet.com","images":["312.png"]},

{"date":"2026-01-01","time":"15:00","content":"🇳🇬 NIGERIA PLAYERS: SIGN UP IN 60 SECONDS! 🚀\n\nStop wasting time! The fastest way to get your $157 bonus is the 'One-Click' method. It takes less than a minute.\n\n⚡️ ONE-CLICK REGISTRATION GUIDE:\n\n1. CLICK HERE: Tap the link below.\n2. CODE! Enter Promo Code: 1x_4023125 (REQUIRED for max bonus).\n3. CONFIRM: Ensure NGN is selected. Hit 'REGISTER'.\n4. DEPOSIT: Fund your account and claim your $157 Welcome Bonus!\n\nDO IT NOW! YOUR ACCOUNT IS WAITING. 👇\n\nhttps://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=bonus/rules/1st\n\n(Powered by Fortunobet: https://www.fortunobet.com/com)","images":["011.png"]},
{"date":"2026-01-01","time":"23:00","content":"🔥 LATE NIGHT DEPOSIT: FREE CASH + FREE SPINS! 🔥\n\nIt's still New Year's Day! If you grabbed the first bonus, Melbet's Second Gift is waiting to double your fun before midnight!\n\nGET YOUR 2ND GIFT:\n• 50% BONUS: More funds for tonight's games!\n• 40 FREE SPINS: Hit a quick New Year's jackpot!\n\nEnd Day 1 as a winner! Claim your extra cash and spins instantly.\n\n👇 CLAIM YOUR MELBET REWARD! 👇\n\nGET BONUS HERE: https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration\n\n🌐 FortunoBet Promotions: https://fortunobet.com","images":["012.png"]},

{"date":"2026-01-02","time":"15:00","content":"💰 FORGET NEW YEAR'S RESOLUTIONS—START WITH NEW YEAR'S PROFITS!\n\nStop guessing and start winning! We've done the work to bring you 3 GUARANTEED WINNERS for January 2nd. Turn a small stake into a major payday!\n\n🔥 YOUR JANUARY 2ND WINNING TREBLE:\n\n⚽️ AFCON (11:00 AM)\n🇲🇦 Morocco vs. Mali 🇲🇱 -> Morocco Win!\n\n⚽️ Premier League (3:30 PM)\n🌳 Nott'm Forest vs. Man City 🏙️ -> OVER 2.5 Goals!\n\n⚽️ Premier League (7:00 PM)\n🔴 Man United vs. Newcastle ⚫️ -> Both Teams To Score!\n\nReady to cash out today? Click below to lock in your bets: 👇\n\nhttps://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=line/football\n\n(Powered by Fortunobet: https://www.fortunobet.com/com)","images":["021.png"]},
{"date":"2026-01-02","time":"23:00","content":"🚨 FREE CASH ALERT: 1XBET DOUBLES YOUR MONEY! 🚨\n\nIt's Friday! Deposit anything today and 1XBET instantly DOUBLES IT up to €300! Fuel your weekend bets with the house's money.\n\n💰 MAX REWARD, MINIMUM WAGERING (x3).\n⏱️ 24 HOURS ONLY!\n\nDOUBLE YOUR BANKROLL NOW! 👇\n\nhttps://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=promotions/lucky-friday\n\n(Powered by Fortunobet: https://www.fortunobet.com/com)","images":["022.png"]},

{"date":"2026-01-03","time":"15:00","content":"🔥 Double Your Start: 1XBET gives $157 free cash.\n$100\%$ deposit match. Fast payout guaranteed.\n👇 Claim your bonus in the next 10 minutes: https://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=bonus/rules/1st","images":["031.png"]},
{"date":"2026-01-03","time":"23:00","content":"🔥 $300$ for $100$: MelBet triples your first deposit now.\n$200\%$ welcome match. Free cash credited instantly.\n👇 Claim your MelBet bonus in the next 7 minutes: https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration","images":["032.png"]},

{"date":"2026-01-04","time":"15:00","content":"💰 $100,000$ giveaway is URGENTLY live on 1XBET.\nBet and get free tickets for the biggest New Year prize draw.\n👇 Enter the 1XBET draw in the next 15 minutes: https://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=promotions/santas-gift","images":["041.png"]},
{"date":"2026-01-04","time":"23:00","content":"🔥 Get $5$ free cash: Deposit $3$ on 1XBET or MelBet.\nURGENT: Limited to the first 50 users who deposit now.\n👇 Claim your MelBet/1XBET gift $\mathbf{before}$ midnight: https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration","images":["042.png"]},
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




