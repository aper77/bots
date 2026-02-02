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

{"date":"2026-02-03","time":"15:00","content":"✨ STARBURST: SLOTS STRATEGY 🎰\n💎 Secret: I only play for the Rainbow Star Re-spin. 🚀 Strategy: I start with small stakes to grow the balance slow. No chasing big losses — stay disciplined. 🎯\n\n🎁 Bonus: 300% Bonus + Free Spins on first deposit. 📘 How: Deposit $5+ via OPay (NG) or M-Pesa (KE). 💰 Withdrawal: Instant payouts on original licensed slots.\n\n⏰ Active: 24/7 Today ⚠️ 18+ | Bet Responsibly\n\n👉 The link I use: https://www.fortunobet.com/com","images":["031.png"]},
{"date":"2026-02-03","time":"21:30","content":"🎮 MELBET: SMART START STRATEGY ⚽\n🔥 Strategy: Target odds 1.50–2.20 only. 🚀 Plan: I focus on single matches to grow the bankroll slow. No chasing big losses today. 🎯\n\n🎁 Bonus: 100% up to 15,000 KES / 150,000 NGN 📘 How: Deposit $5+ via M-Pesa (KE) or Instant Bank (NG). 💰 Withdrawal: Instant payouts—the same link I use. \n\n⏰ Active: Bonus expires tonight ⚠️ 18+ | Play Responsibly\n\n👉 The link I use: https://fortunobet.com/melbet","images":["032.png"]},

{"date":"2026-02-04","time":"15:00","content":"🏆 BARCELONA IN DANGER? 🇪🇸\n🔥 Match: Albacete vs Barcelona! 🚀 Strategy: I’m skipping the 1.20 odds. The real value is 'Both Teams to Score'—I play smart to grow the bankroll. 🎯\n\n🎁 Bonus: 100% up to 15,000 KES / 150,000 NGN 📘 How: Deposit $5+ via M-Pesa (KE) or Instant Bank (NG). 💰 Withdrawal: Fast payouts—this is the link I use.\n\n⏰ Active: Claim before kickoff tonight ⚠️ 18+ | Play Responsibly\n\n👉 The link I use: https://fortunobet.com/melbet","images":["041.jpg"]},
{"date":"2026-02-04","time":"15:00","content":"🏆 BARCELONA IN DANGER? 🇪🇸\n🔥 Match: Albacete vs Barcelona! 🛡️ Strategy: I use 'Correct Score Insurance'—if the score is wrong, I get a FREE BET refund. No chasing losses. 🎯\n\n🎁 Bonus: 100% up to ₦150,000 / 20,000 KES 📘 How: Deposit $5+ via OPay (NG) or M-Pesa (KE). 💰 Withdrawal: Fast payouts—this is the same link I use.\n\n⏰ Active: Protect your bet before kickoff! ⚠️ 18+ | Bet Responsibly\n\n👉 The link I use: https://fortunobet.com/1xbet","images":["042.png"]},

{"date":"2026-02-05","time":"15:00","content":"🔥 MAN CITY vs NEWCASTLE: SEMI-FINAL 🏴󠁧󠁢󠁥󠁮󠁧󠁿\n🚀 Haaland vs The Magpies! 🛡️ Strategy: I’m using 'Correct Score Insurance' for this—if we miss the score, we get a FREE BET refund. No risk today. 🎯\n\n🎁 Bonus: 100% up to ₦150,000 / 20,000 KES 📘 How: Deposit $5+ via OPay (NG) or M-Pesa (KE). 💰 Withdrawal: Instant payouts—the same link I use.\n\n⏰ Active: Protect your bet before kickoff! ⚠️ 18+ | Play Responsibly\n\n👉 The link I use: https://fortunobet.com/1xbet","images":["051.png"]},
{"date":"2026-02-05","time":"21:00","content":"🚀 MELBET MEGA BONUS: SMART GROWTH 💰\n💎 Strategy: I use this 100% bonus to double my bankroll and protect my capital. Play small, win steady, and stay disciplined. 🎯\n\n🎁 Bonus: 100% up to 150,000 NGN / 20,000 KES 📘 How: Deposit $5+ via OPay (NG) or M-Pesa (KE). 💰 Withdrawal: Instant cashouts—the same link I use.\n\n⏰ Active: Claim your gift before it expires tonight! ⚠️ 18+ | Play Responsibly\n\n👉 The link I use: https://fortunobet.com/melbet","images":["052.png"]},

{"date":"2026-02-06","time":"16:00","content":"🥂 FRIDAY VIP TREAT: CASH + 100 SPINS! 🎁\n🔥 Winter Olympics: Opening Ceremony! 🚀 Strategy: I use the 50% Bonus for the games and the 100 Spins to hunt the jackpot. Play smart. 🎯\n\n🎁 Bonus: 50% Cash + 100 FREE SPINS 📘 How: Deposit $5+ via OPay (NG) or M-Pesa (KE). 💰 Withdrawal: Fast & reliable—the same link I use.\n\n⏰ Friday Only: Claim your VIP gift before midnight! ⚠️ 18+ | Bet Responsibly\n\n👉 The link I use: https://fortunobet.com/melbet","images":["061.png"]},
{"date":"2026-02-06","time":"22:00","content":"🔥 BETIS vs ATLETICO MADRID: COPA DEL REY 🇪🇸\n🚀 Huge Quarter-Final! 🛡️ Strategy: I’m playing with '3% Weekly Cashback'—win or lose, I get money back every week. No fear, just smart growth. 🎯\n\n🎁 Bonus: 100% up to ₦150,000 / 20,000 KES 📘 How: Deposit $5+ via OPay (NG) or M-Pesa (KE). 💰 Withdrawal: Instant payouts in 60 seconds—the link I use.\n\n⏰ Active: Secure your cashback before the deadline! ⚠️ 18+ | Bet Responsibly\n\n👉 The link I use: https://fortunobet.com/1xbet","images":[""]},

{"date":"2026-02-07","time":"13:00","content":"🚀 MAN UTD vs TOTTENHAM: OLD TRAFFORD 🔴⚪️\n🔥 Game of the Week! 🚀 Strategy: I’m skipping the straight win. 'Both Teams to Score' is where I grow the bankroll slow. Stay disciplined. 🎯\n\n🎁 Bonus: 100% up to 150,000 NGN / 20,000 KES 📘 How: Deposit $5+ via OPay (NG) or M-Pesa (KE). 💰 Withdrawal: Instant payouts—the same link I use.\n\n⏰ Active: Kickoff is early today! ⚠️ 18+ | Play Responsibly\n\n👉 The link I use: https://fortunobet.com/melbet","images":["071.png"]},
{"date":"2026-02-07","time":"17:30","content":"🎡 1XBET LUCKY WHEEL: €5,000 JACKPOT! 🎁\n🚀 Saturday Craziness: I’m spinning the wheel for that €5,000 cash. 🛡️ Strategy: I play the Barcelona vs Mallorca match to earn my tickets. Stay smart, win steady. 🎯\n\n🎁 Bonus: Spin & Win €5,000 + Tech Prizes 📘 How: Deposit $5+ via OPay (NG) or M-Pesa (KE). 💰 Withdrawal: Fast as a Ferrari—the same link I use.\n\n⏰ Active: The Wheel is spinning today! ⚠️ 18+ | Bet Responsibly\n\n👉 The link I use: https://fortunobet.com/1xbet","images":["072.png"]},

{"date":"2026-02-08","time":"14:00","content":"🔥 LIVERPOOL vs MAN CITY: THE TITLE WAR! 🏆\n🚀 Anfield Clash: Salah vs Haaland! 🛡️ Strategy: I use 'Correct Score Insurance' for this battle. If the score is wrong, I get a FREE BET refund. No risk, just smart play. 🎯\n\n🎁 Bonus: 100% up to ₦150,000 / 20,000 KES 📘 How: Deposit $5+ via OPay (NG) or M-Pesa (KE). 💰 Withdrawal: Instant payouts—the same link I use.\n\n⏰ Active: Protect your bet before kickoff! ⚠️ 18+ | Bet Responsibly\n\n👉 The link I use: https://fortunobet.com/1xbet","images":["081.png"]},
{"date":"2026-02-08","time":"19:00","content":"🏈 SUPER BOWL 60: THE ULTIMATE WAR! 🇺🇸\n🔥 Patriots vs Seahawks: The rematch! 🛡️ Strategy: I’m playing with '3% Weekly Cashback' tonight. Win or lose, I get money back automatically. Smart bankroll growth only. 🎯\n\n🎁 Bonus: 100% Match + 3% Weekly Cashback 📘 How: Deposit $5+ via OPay (NG) or M-Pesa (KE). 💰 Withdrawal: Fast processing for the Big Game—the link I use.\n\n⏰ Active: Cashback drops before kickoff! ⚠️ 18+ | Play Responsibly\n\n👉 The link I use: https://fortunobet.com/melbet","images":["082.png"]},

{"date":"2026-02-09","time":"09:00","content":"👑 ROYAL MONDAY: $8 BONUS + DERBY DAY! 🎁\n🔥 Porto vs Sporting CP! 🚀 Strategy: This is a 1st vs 2nd battle. I play it safe and use the bonus to grow the bankroll slow. Stay disciplined. 🎯\n\n🎁 Bonus: $8 FREE ($3 Melbet + $5 Partner Gift) 📘 How: Deposit $3+ via OPay (NG) or M-Pesa (KE). 💰 Payouts: Guaranteed safe & official—the link I use.\n\n⏰ Active: Claim before the Derby kickoff! ⚠️ 18+ | Play Responsibly\n\n👉 The link I use: https://www.fortunobet.com/com","images":["5bonus.jpeg"]},
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




