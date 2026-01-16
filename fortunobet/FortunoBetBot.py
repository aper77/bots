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

# Monday	15:00 (3:00 PM)	21:00 (9:00 PM)
# Tuesday	15:00 (3:00 PM)	21:30 (9:30 PM) — Champions League Night
# Wednesday	15:00 (3:00 PM)	21:30 (9:30 PM) — Champions League Night
# Thursday	15:00 (3:00 PM)	21:00 (9:00 PM)
# Friday	16:00 (4:00 PM)	22:00 (10:00 PM) — Weekend kickoff
# Saturday	13:00 (1:00 PM)	17:30 (5:30 PM) — MOST IMPORTANT TIME
# Sunday	14:00 (2:00 PM)	19:00 (7:00 PM)

posts =[
{"date":"2026-01-14","time":"10:30","content":"💥 URGENT: DOUBLE YOUR BALANCE TODAY! 💰\nTop up now with FortunoBet & get 100% bonus up to €300 at 1xBet\n✅ Deposit €300 → Play with €600 instantly\n✅ Low x3 wagering – fast withdrawals\n🔥 Only today – don’t miss out!\n👉 Activate your bonus: https://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=registration","images":["141.jpg"]},
{"date":"2026-01-14","time":"21:00","content":"🎲 BET SMART & WIN FAST 💸\nFortunoBet + 1xBet are giving new players $130 match bonus or start low with $5\n✅ Instant credit – start playing immediately\n✅ Slots, live games & sports bets\n⏰ Limited spots – don’t wait!\n👉 Claim your bonus now: https://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=registration","images":["142.jpg"]},

{"date":"2026-01-15","time":"10:30","content":"🔥 DOUBLE YOUR MONEY TODAY! 💰\nFortunoBet + MelBet offer 100% match bonus for all new players\n✅ Deposit $130 → Play with $260 instantly\n✅ Best odds for today’s matches\n⏳ First 100 players only – hurry!\n👉 Grab your $130 bonus: https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration","images":["151.png"]},
{"date":"2026-01-15","time":"21:00","content":"✨ STARBURST JACKPOTS EXPLODING! ✨\nPlay the legendary 1xBet STARBURST slot on FortunoBet\n✅ Wild Respins & Both Ways Pay for huge wins\n✅ High RTP – frequent payouts\n💰 Use your welcome bonus for extra spins\n⏰ Don’t wait – spin now!\n👉 Play STARBURST: https://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=slots/game/123199/1xbet-starburst","images":["152.jpg"]},

{"date":"2026-01-16","time":"10:30","content":"⚽ Copa del Rey: Racing Santander vs Barcelona\n🔥 Barcelona rarely slips in cup games\n💰 Pick: Barcelona to WIN\n🎁 100% bonus up to €300 (x3 wagering)\n⏰ Odds active before kickoff\n👉 Bet now: https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=line/football","images":["161foot.png"]},
{"date":"2026-01-16","time":"21:00","content":"🍭 SWEET BONANZA 1000 JACKPOTS! 🍭\nFortunoBet players hitting up to 25,000x wins on Sweet Bonanza 1000\n✅ Huge Multipliers – 1,000x bombs in bonus round\n✅ Max Win – up to 25,000x your stake\n✅ Buy Bonus – jump straight into Free Spins\n💰 Small bet → massive payout\n👉 Play SWEET BONANZA 1000: https://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=slots/game/95425/sweet-bonanza-1000","images":["162.png"]},

{"date":"2026-01-17","time":"13:00","content":"💎 UNLOCK THE $38,180 EPIC DEPOSIT SERIES! 💎\nFortunoBet + MelBet are giving huge match bonuses across your 1st-4th deposits\n✅ Maximum rewards for weekend high-rollers\n✅ Instant VIP status for all participants\n🔥 Start your $38K journey now!\n👉 Start the EPIC series: https://refpa3365.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration","images":["172.png"]},
{"date":"2026-01-17","time":"17:30","content":"⚽️ PREMIER LEAGUE: FOREST vs ARSENAL 🔥 The Gunners are hunting for the title! Our experts are backing Arsenal to WIN today. 💰 🇳🇬 NIGERIA: ₦800,000 Bonus! 🇰🇪 KENYA: KSh 26,000 Bonus! ✅ USE PROMO CODE: 1x_4023125 ⏰ Kickoff: 6:30 PM (NG) | 8:30 PM (KE) 👉 CLAIM TRIPLE BONUS: https://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=line/football","images":["171foot.png"]},

{"date":"2026-01-18","time":"14:00","content":"🥂 SUNDAY VIP TREAT: 50% BONUS + 100 FREE SPINS! 🥂\nFortunoBet + MelBet VIP reload – deposit today\n✅ 50% EXTRA CASH on Sunday deposit\n✅ 100 FREE SPINS on top-paying slots\n✅ Faster weekend withdrawals for VIPs\n⏰ Valid 24 hours only\n👉 Claim your Sunday VIP Treat: https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration","images":["181.png"]},
{"date":"2026-01-18","time":"19:00","content":"⚽️ PREMIER LEAGUE: VILLA vs EVERTON 🔥 Villa are unstoppable at home this season! Our expert pick: Aston Villa to WIN 💰 🇳🇬 NIGERIA: ₦800,000 Bonus! 🇰🇪 KENYA: KSh 26,000 Bonus! ✅ USE PROMO CODE: 1x_4023125 ⏰ Kickoff: 5:30 PM (NG) | 7:30 PM (KE) 👉 BET NOW: https://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=line/football","images":["182foot.png"]},

# Monday
{"date":"2026-01-19","time":"15:00","content":"💰 75% EXTRA ON 2ND DEPOSIT! 💥\nFortunoBet keeps the cash flowing – deposit now\n✅ Deposit $100 → Play with $175 instantly\n✅ Use extra funds for bigger bets on sports & events\n🔥 Limited-time – don’t miss out!\n👉 Activate your 2nd bonus: https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration","images":["161.jpg"]},
{"date":"2026-01-19","time":"21:00","content":"🎁 LAST CHANCE: WIN A MACBOOK OR SHARE OF $100,000! 🎁\nFortunoBet + 1xBet Santa’s Gift – Apple MacBooks, iPhone 17 & cash prizes\n✅ Every bet earns tickets to the SUPERPRIZE draw\n✅ Collect candies & lollipops for guaranteed bonuses\n⏰ Clock is ticking – join before prizes end!\n👉 Enter the $100,000 draw: https://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=promotions/santas-gift","images":["171.png"]},

{"date":"2026-01-20","time":"15:00","content":"⚡ RISK-FREE BET ON BIG MATCHES! ⚡\nFortunoBet + 1xBet 'No Risk Bet' guarantee – play smart!\n✅ Bet Correct Score – if you lose, get 100% refund as Free Bet\n✅ Zero risk, pure profit potential\n💰 Perfect for sports bettors today\n⏰ Limited offer – don’t miss out!\n👉 Place your risk-free bet: https://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=promotions/no-risk-bet","images":["182.png"]},

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




