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

# Monday

# 15:00 (3:00 PM) — Register & Deposit Guide

# 21:00 (9:00 PM) —  Welcome Bonus

# Tuesday

# 15:00 (3:00 PM) — Withdrawal Guide 

# 21:30 (9:30 PM) —  Deposit Bonus

# Wednesday

# 15:00 (3:00 PM) — How to Bet (Example)

# 21:30 (9:30 PM) — Sports Bonus

# Thursday

# 15:00 (3:00 PM) — Safe Betting Tips

# 21:00 (9:00 PM) — Reload Bonus

# Friday

# 16:00 (4:00 PM) — Weekend Betting Guide

# 22:00 (10:00 PM) — Weekend Bonus

# Saturday

# 13:00 (1:00 PM) — Live Bet Example

# 17:30 (5:30 PM) — Hot Bonus

# Sunday

# 14:00 (2:00 PM) — Withdraw + Tips

# 19:00 (7:00 PM) — Final Bonus

posts =[
{"date":"2026-02-02","time":"15:00","content":"🇳🇬🇰🇪 UDINESE vs ROMA: The Battle of Italy! ⚽\n🔥 Kickoff: 20:45 (NG) / 22:45 (KE). Don't miss the action!\n🦅 Maduka Okoye vs the Roma Giants — Who wins tonight?\n🎁 1XBET EXCLUSIVE: Get your 300% Bonus before kickoff!\n📘 Easy Registration & Instant M-Pesa / OPay Deposits.\n💰 Huge Odds: Roma (2.01) | Draw (3.39) | Udinese (4.47)\n⏰ Time is running out — claim your welcome gift now!\n⚠️ 18+ | Bet Responsibly\n👉 Register & Claim: https://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=registration","images":["021.png"]},
{"date":"2026-02-02","time":"20:00","content":"👑 ROYAL MONDAY MADNESS: 100% RELOAD BONUS! 💰\n🔥 Match Tonight: Udinese vs Roma (Serie A) 🇮🇹\n🚀 Monday special: Deposit now and MelBet will DOUBLE your money!\n🎁 Bonus: 100% up to $100 / 15,000 KES / 150,000 NGN\n📘 How to claim: Deposit via M-Pesa or Instant Bank before midnight!\n💰 Use your extra cash to back Roma at 2.01 odds today!\n⏰ Hurry — this offer disappears at 23:59 tonight! \n⚠️ 18+ | Play Responsibly\n👉 Claim Royal Monday Bonus: https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration","images":["022.png"]},

{"date":"2026-02-03","time":"15:00","content":"✨ STARBURST: THE WINNER'S GUIDE! 🎰\n💎 SECRET: Hit the Rainbow Star for a FREE Mega Re-spin and big payouts!\n🎁 1XBET EXCLUSIVE: 300% Bonus + Free Spins on your first deposit.\n💰 Instant M-Pesa (KE) & OPay (NG) cashouts for all players!\n🚀 Start your winning streak on an original licensed platform today.\n⚠️ 18+ | Bet Responsibly\n👉 PLAY NOW: https://www.fortunobet.com/com","images":["031.png"]},
{"date":"2026-02-03","time":"21:30","content":"🎮 MelBet: START SMART, WIN BIG! ⚽\n🔥 SAFE STRATEGY: Target odds 1.50–2.20 for the best win-rate today!\n🎁 BONUS: Double your first deposit up to $100 / 15,000 KES / 150,000 NGN!\n📘 HOW: Register and deposit via M-Pesa (KE) or Instant Bank (NG) to activate.\n💰 TIP: Focus on a single match or small combo to grow your bankroll safely.\n⏰ LAST CALL: This welcome gift expires today — don't leave money on the table!\n⚠️ 18+ | Play Responsibly\n👉 START WINNING: https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration","images":["032.png"]},

{"date":"2026-02-04","time":"15:00","content":"🏆 BARCELONA IN DANGER? 🇪🇸\n🔥 Copa del Rey: Albacete vs Barcelona! After knocking out Real Madrid, can the underdogs shock Barca too?\n💎 TIP: Barcelona are favorites (1.20), but 'Both Teams to Score' offers huge value!\n🎁 MELBET BONUS: Get a 100% Match up to $130 / 15,000 KES / 150,000 NGN!\n📘 Easy Deposits: Use M-Pesa (KE) or Instant Bank (NG) to fund your account now.\n💰 Start with a safe 1.50+ combo to clear your bonus wagering easily.\n⏰ Don't wait — claim your Royal Bonus before kickoff tonight!\n⚠️ 18+ | Bet Responsibly\n👉 Register & Win: https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration","images":["041.jpg"]},
{"date":"2026-02-04","time":"15:00","content":"🏆 BARCELONA IN DANGER? 🇪🇸\n🔥 Copa del Rey: Albacete vs Barcelona! Can the underdogs pull off a massive shock tonight?\n🛡️ 1XBET SPECIAL: Correct Score Insurance! Bet on the score & get a FREE BET refund if you lose!\n🎁 BONUS: 100% Match up to ₦150,000 / 20,000 KES!\n💰 Instant M-Pesa (KE) & OPay (NG) Deposits.\n⏰ Limited Offer: Protect your bet before kickoff!\n⚠️ 18+ | Bet Responsibly\n👉 PLAY NOW: https://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=promotions/lucky-friday","images":["042.png"]},

{"date":"2026-02-05","time":"15:00","content":"🔥 MAN CITY vs NEWCASTLE: SEMI-FINAL WAR! 🏴󠁧󠁢󠁥󠁮󠁧󠁿\n🚀 Haaland vs The Magpies — who wins tonight?\n🛡️ 1XBET EXCLUSIVE: Correct Score Insurance! Bet now & get a FREE BET if you lose! No risk!\n🎁 BONUS: 100% Match up to ₦150,000 / 20,000 KES!\n💰 Instant OPay & M-Pesa deposits.\n⚠️ 18+ | Play Responsibly\n👉 PLAY NOW: https://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=registration","images":["051.png"]},
{"date":"2026-02-05","time":"21:00","content":"🚀 MELBET MEGA BONUS: DOUBLE YOUR CASH! 💰\n🎁 100% Welcome Bonus up to $130 / 150,000 NGN / 20,000 KES!\n⚡️ FAST: Instant OPay (NG) & M-Pesa (KE) deposits.\n💎 TIP: Double your bankroll & win bigger tonight!\n⏰ HURRY: Claim your $130 gift before it expires!\n⚠️ 18+ | Play Responsibly\n👉 CLAIM BONUS: https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration","images":["052.png"]},

{"date":"2026-02-06","time":"16:00","content":"🥂 FRIDAY VIP TREAT: CASH + 100 FREE SPINS! 🎁\n🔥 WINTER OLYMPICS START: Get a 50% Bonus + 100 SPINS for the Opening Ceremony! 🇮🇹\n💰 Instant Payouts: OPay (NG) & M-Pesa (KE) — fast & reliable.\n⚡️ PRO TIP: Use your 100 Free Spins to hit the jackpot before the games begin!\n⏰ FRIDAY ONLY: Claim your VIP gift before midnight!\n⚠️ 18+ | Bet Responsibly\n👉 CLAIM BONUS: https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration","images":["061.png"]},
{"date":"2026-02-06","time":"22:00","content":"🔥 BETIS vs ATLETICO MADRID: COPA DEL REY WAR! 🇪🇸\n🚀 Huge Quarter-Final! Can Griezmann lead Atletico to the Semis tonight?\n💸 1XBET CASHBACK: Don't fear the loss! Get 3% Weekly Cashback automatically on every bet!\n🎁 BONUS: 100% Match up to ₦150,000 / 20,000 KES!\n💰 Instant Payouts: OPay (NG) & M-Pesa (KE) — ready in 60 seconds!\n⏰ CHECK NOW: Secure your cashback before the midnight deadline!\n⚠️ 18+ | Bet Responsibly\n👉 GET CASHBACK: https://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=registration","images":[""]},

{"date":"2026-02-07","time":"13:00","content":"🚀 MAN UTD vs TOTTENHAM: OLD TRAFFORD CLASH! 🔴⚪️\n🔥 Massive Saturday! Can United stop Spurs in the game of the week?\n🎁 MELBET MEGA BONUS: 100% First Deposit Match up to $130 / 150,000 NGN / 20,000 KES!\n🏦 SAFE PAYOUTS: Win big and withdraw fast via M-Pesa (KE) & OPay (NG)!\n💎 PRO TIP: Double your cash & bet 'Both Teams to Score' for an easy weekend win!\n⏰ HURRY: Kickoff is near! Claim your $130 gift and win today!\n⚠️ 18+ | Bet Responsibly\n👉 CLAIM BONUS & WIN: https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration","images":["071.png"]},
{"date":"2026-02-07","time":"17:30","content":"🎡 1XBET LUCKY WHEEL: WIN €5,000 TODAY! 🎁\n🚀 SATURDAY CRAZINESS: Spin the wheel and win up to €5,000 CASH + massive tech prizes! 📱\n🔥 GAME ON: Barcelona vs Mallorca! Bet on the stars and earn your lucky tickets now!\n💰 Instant Payouts: OPay (NG) & M-Pesa (KE) — fast as a Ferrari! ⚡️\n⏰ HURRY: The Wheel is spinning! Don't let your €5,000 jackpot slip away!\n⚠️ 18+ | Bet Responsibly\n👉 SPIN & WIN NOW: https://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=registration","images":["072.png"]},

{"date":"2026-02-08","time":"14:00","content":"🔥 LIVERPOOL vs MAN CITY: THE TITLE WAR! 🏆\n🚀 ANFIELD CLASH: Salah vs Haaland! Who wins today?\n🛡️ 1XBET RISK-FREE: Bet Correct Score & get a FREE BET refund if you lose!\n🎁 NEW USER: 100% Match up to ₦150,000 / 20,000 KES!\n💰 Instant Payouts: OPay (NG) & M-Pesa (KE) — fast & safe.\n⚠️ 18+ | Bet Responsibly\n👉 CLAIM FREE BET: https://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=registration","images":["081.png"]},
{"date":"2026-02-08","time":"19:00","content":"🏈 SUPER BOWL 60: THE ULTIMATE WAR! 🇺🇸\n🔥 PATRIOTS vs SEAHAWKS: The biggest betting night of the year is HERE!\n💸 WEEKLY CASHBACK: Sunday night special! Get 3% back on your weekly losses automatically! 🔄\n💎 PRO TIP: Withdraw in small parts tonight for the fastest processing!\n⏰ DON'T MISS: The cashback drops before the Super Bowl kickoff! 🏆\n⚠️ 18+ | Play Responsibly\n👉 CLAIM CASHBACK: https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration","images":["082.png"]},

{"date":"2026-02-09","time":"09:00","content":"👑 ROYAL MONDAY MADNESS: GET $8 FREE! 🎁\n🔥 DERBY DAY: Porto vs Sporting CP! Who rules Portugal tonight?\n💎 PARTNER SPECIAL: Deposit $3+ and get an $8 BONUS instantly ($3 from Melbet + $5 from us!) 🚀\n✅ LICENSED ONLY: Official partner link for safe, guaranteed payouts.\n💰 FAST CASH: Withdraw your derby winnings via M-Pesa & OPay same day!\n⚠️ 18+ | Play Responsibly\n👉 CLAIM YOUR $8 NOW: https://www.fortunobet.com/com","images":["5bonus.jpeg"]},
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




