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
# Saturday	13:00 (1:00 PM)	  (5:30 PM) — MOST IMPORTANT TIME
# Sunday	14:00 (2:00 PM)	19:00 (7:00 PM)

posts =[
# Monday
{"date":"2026-01-19","time":"15:00","content":"💰 FortunoBet 2nd deposit boost\n🔥 I’m using this to increase stake size on today’s bets\n🎁 75% extra bonus on your second deposit\n💰 Deposit $100 → play with $175 real balance\n⏰ Limited-time offer, may close anytime\n⚠️ Real money betting | 18+\n👉 Activate your 2nd deposit bonus: https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration","images":["191.jpg"]},
{"date":"2026-01-19","time":"21:00","content":"⚽ Elche vs Sevilla – Spain La Liga\n🔥 I’m backing Sevilla for a solid win tonight, but expecting Elche to push for a goal\n🎁 1XBET 100% deposit bonus up to €300 (x3 wagering)\n💰 Deposit & play real money from $10+\n⏰ Match kicks off today — act before kickoff!\n⚠️ Real money betting | 18+\n👉 Register & bet now: https://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=registration","images":["192.jpg"]},

{"date":"2026-01-20","time":"15:00","content":"🎁 FortunoBet x 1xBet Santa’s Gift\n🔥 I’m joining this while placing my regular bets anyway\n🎁 Real bets earn tickets for MacBooks, iPhone prizes & $100,000 pool\n💰 Deposit & place real money bets to collect tickets\n⏰ Promotion ending soon, entries close shortly\n⚠️ Real money betting | 18+\n👉 Join the Santa’s Gift draw here: https://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=promotions/santas-gift","images":["201.png"]},
{"date":"2026-01-20","time":"21:30","content":"⚽ Brighton & Hove Albion vs Bournemouth – EPL\n🔥 Brighton looks strong at home, expecting a solid win tonight\n🎁 1XBET 100% deposit bonus up to €300 (x3 wagering)\n💰 Deposit & play real money from $10+\n⏰ Match kicks off tomorrow — act before kickoff!\n⚠️ Real money betting | 18+\n👉 Register & bet now: https://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=registration","images":["202.jpg"]},

{"date":"2026-01-21","time":"15:00","content":"⚡ FortunoBet x 1xBet 'No Risk Bet' ⚡\n🔥 I’m using this to try bigger stakes safely on today’s matches\n🎁 Bet correct score – lose? Get 100% refund as Free Bet\n💰 Deposit & play real money to unlock this offer\n⏰ Limited-time, offer ends soon\n⚠️ Real money betting | 18+\n👉 Place your risk-free bet here: https://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=promotions/no-risk-bet","images":["211.png"]},
{"date":"2026-01-21","time":"21:30","content":"⚽ Internazionale Milano vs Arsenal – UEFA Champions League\n🔥 Arsenal looks solid on the road, but Inter can surprise at home\n🎁 1XBET 100% deposit bonus up to €300 (x3 wagering)\n💰 Deposit & play real money from $10+\n⏰ Match kicks off tomorrow — act before kickoff!\n⚠️ Real money betting | 18+\n👉 Register & bet now: https://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=registration","images":["212.jpg"]},

{"date":"2026-01-22","time":"15:00","content":"🎁 1XBET 100% First Deposit Bonus – Up to $157!\n🔥 I just doubled my first deposit and it’s giving me more betting power — you can too!\n💰 Deposit & play real money from $10+\n⏰ Bonus only available today — claim it before it’s gone!\n⚠️ Real money betting | 18+\n👉 Grab your bonus now: https://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=bonus/rules/1st","images":["221.jpg"]},
{"date":"2026-01-22","time":"21:00","content":"⚽ Olympique de Marseille vs Liverpool – UEFA Champions League\n🔥 Backing Liverpool with Salah to make an impact tonight, Marseille will push too\n🎁 1XBET 100% deposit bonus up to €300 (x3 wagering)\n💰 Deposit & play real money from $10+\n⏰ Post-match urgency — act before kickoff!\n⚠️ Real money betting | 18+\n👉 Register & bet now: https://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=registration","images":["222.png"]},

{"date":"2026-01-23","time":"16:00","content":"🎁 Lucky Friday: 100% Deposit Reload Bonus – Up to 300 EUR\n🔥 Boost your betting balance instantly — perfect for this weekend!\n💰 Deposit & play real money from $10+\n⏰ Bonus valid today only — claim it within 24 hours!\n⚠️ Real money betting | 18+\n👉 Grab your bonus now: https://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=promotions/lucky-friday","images":["231.png"]},
{"date":"2026-01-23","time":"22:00","content":"⚽ Braga vs Nottingham Forest – UEFA Europa League\n🔥 Betting on Nottingham Forest for an away push, Braga will fight hard too\n🎁 1XBET 100% deposit bonus up to €300 (x3 wagering)\n💰 Deposit & play real money from $10+\n⏰ Kickoff tonight — act before 00:00 GMT!\n⚠️ Real money betting | 18+\n👉 Register & bet now: https://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=registration","images":["232.png"]},

{"date":"2026-01-24","time":"13:00","content":"🎁 1XBET New Year’s Lucky Ticket Wheel & Draw – Win up to 5000 EUR!\n🔥 Spin the wheel daily after your deposit — extra prizes & bonuses up for grabs\n💰 Deposit & play real money from $10+\n⏰ Bonus clawback today — register and spin before midnight!\n⚠️ Real money betting | 18+\n👉 Join the Wheel & Draw now: https://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=promotions/new-years-wheel-2026","images":["241.png"]},
{"date":"2026-01-24","time":"17:30","content":"⚽ Derby County vs West Bromwich Albion – England Championship\n🔥 Backing West Brom to push for an away win, Derby will fight hard too\n🎁 1XBET 100% deposit bonus up to €300 (x3 wagering)\n💰 Deposit & play real money from $10+\n⏰ Kickoff tonight — act before 00:00 GMT!\n⚠️ Real money betting | 18+\n👉 Register & bet now: https://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=registration","images":["242.png"]},

{"date":"2026-01-25","time":"14:00","content":"🎁 1XBET Santa's Gift – Win up to $100,000 Cash + Tech Prizes!\n🔥 Place bets today and enter the final Superprize draw — real prizes, real excitement!\n💰 Deposit & play real money from $10+\n⏰ Only today — draw closes at midnight!\n⚠️ Real money betting | 18+\n👉 Claim your Santa's Gift entry now: https://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=promotions/santas-gift","images":["251.png"]},
{"date":"2026-01-25","time":"19:00","content":"⚽ River Plate vs Barracas Central – Argentina Primera Division\n🔥 River Plate should dominate, strong at home vs struggling Barracas\n🎁 1XBET 100% deposit bonus up to €300 (x3 wagering)\n💰 Deposit & play real money from $10+\n⏰ Match kicks off today — don’t miss your chance!\n⚠️ Real money betting | 18+\n👉 Register & bet now: https://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=registration","images":["252.png"]},

{"date":"2026-01-26","time":"15:00","content":"🎁 1XBET Daily 1xGames Tournament – Win an Apple iPad Air!\n🔥 Compete today in the tournament with real bets and climb the leaderboard!\n💰 Deposit & play real money from $10+\n⏰ Tournament ends tonight — act fast!\n⚠️ Real money betting | 18+\n👉 Join & play now: https://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=promotions/daily-tournament","images":["261.png"]},
{"date":"2026-01-26","time":"21:00","content":"⚽ Villarreal vs Real Madrid – Spain La Liga\n🔥 Real Madrid strong away, likely to take control — good for a confident bet\n🎁 1XBET 100% deposit bonus up to €300 (x3 wagering)\n💰 Deposit & play real money from $10+\n⏰ Match kicks off tonight — lock in your stake!\n⚠️ Real money betting | 18+\n👉 Register & bet now: https://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=registration","images":["262.png"]},
]

# {"date":"2026-01-14","time":"10:30","content":"💥 URGENT: DOUBLE YOUR BALANCE TODAY! 💰\nTop up now with FortunoBet & get 100% bonus up to €300 at 1xBet\n✅ Deposit €300 → Play with €600 instantly\n✅ Low x3 wagering – fast withdrawals\n🔥 Only today – don’t miss out!\n👉 Activate your bonus: https://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=registration","images":["141.jpg"]},
# {"date":"2026-01-14","time":"21:00","content":"🎲 BET SMART & WIN FAST 💸\nFortunoBet + 1xBet are giving new players $130 match bonus or start low with $5\n✅ Instant credit – start playing immediately\n✅ Slots, live games & sports bets\n⏰ Limited spots – don’t wait!\n👉 Claim your bonus now: https://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=registration","images":["142.jpg"]},

# {"date":"2026-01-15","time":"10:30","content":"🔥 DOUBLE YOUR MONEY TODAY! 💰\nFortunoBet + MelBet offer 100% match bonus for all new players\n✅ Deposit $130 → Play with $260 instantly\n✅ Best odds for today’s matches\n⏳ First 100 players only – hurry!\n👉 Grab your $130 bonus: https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration","images":["151.png"]},
# {"date":"2026-01-15","time":"21:00","content":"✨ STARBURST JACKPOTS EXPLODING! ✨\nPlay the legendary 1xBet STARBURST slot on FortunoBet\n✅ Wild Respins & Both Ways Pay for huge wins\n✅ High RTP – frequent payouts\n💰 Use your welcome bonus for extra spins\n⏰ Don’t wait – spin now!\n👉 Play STARBURST: https://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=slots/game/123199/1xbet-starburst","images":["152.jpg"]},

# {"date":"2026-01-16","time":"10:30","content":"⚽ Copa del Rey: Racing Santander vs Barcelona\n🔥 Barcelona rarely slips in cup games\n💰 Pick: Barcelona to WIN\n🎁 100% bonus up to €300 (x3 wagering)\n⏰ Odds active before kickoff\n👉 Bet now: https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=line/football","images":["161foot.png"]},
# {"date":"2026-01-16","time":"21:00","content":"🍭 SWEET BONANZA 1000 JACKPOTS! 🍭\nFortunoBet players hitting up to 25,000x wins on Sweet Bonanza 1000\n✅ Huge Multipliers – 1,000x bombs in bonus round\n✅ Max Win – up to 25,000x your stake\n✅ Buy Bonus – jump straight into Free Spins\n💰 Small bet → massive payout\n👉 Play SWEET BONANZA 1000: https://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=slots/game/95425/sweet-bonanza-1000","images":["162.png"]},

# {"date":"2026-01-17","time":"13:00","content":"💎 UNLOCK THE $38,180 EPIC DEPOSIT SERIES! 💎\nFortunoBet + MelBet are giving huge match bonuses across your 1st-4th deposits\n✅ Maximum rewards for weekend high-rollers\n✅ Instant VIP status for all participants\n🔥 Start your $38K journey now!\n👉 Start the EPIC series: https://refpa3365.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration","images":["172.png"]},
# {"date":"2026-01-17","time":"17:30","content":"⚽️ PREMIER LEAGUE: FOREST vs ARSENAL 🔥 The Gunners are hunting for the title! Our experts are backing Arsenal to WIN today. 💰 🇳🇬 NIGERIA: ₦800,000 Bonus! 🇰🇪 KENYA: KSh 26,000 Bonus! ✅ USE PROMO CODE: 1x_4023125 ⏰ Kickoff: 6:30 PM (NG) | 8:30 PM (KE) 👉 CLAIM TRIPLE BONUS: https://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=line/football","images":["171foot.png"]},

# {"date":"2026-01-18","time":"14:00","content":"🥂 SUNDAY VIP TREAT: 50% BONUS + 100 FREE SPINS! 🥂\nFortunoBet + MelBet VIP reload – deposit today\n✅ 50% EXTRA CASH on Sunday deposit\n✅ 100 FREE SPINS on top-paying slots\n✅ Faster weekend withdrawals for VIPs\n⏰ Valid 24 hours only\n👉 Claim your Sunday VIP Treat: https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration","images":["181.png"]},
# {"date":"2026-01-18","time":"19:00","content":"⚽ Aston Villa vs Everton – Triple Bonus\n🔥 Strong home form — this is a good spot for Villa\n💰 ₦800,000 (Nigeria) | KSh 26,000 (Kenya)\n⏰ Bonus active before kickoff\n👉 Activate & bet now:\nhttps://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=line/football","images":["182foot.png"]},





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




