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
{"date":"2026-01-26","time":"15:00","content":"⚽ FortunoBet Registration & Bonus Guide\n🔥 Start safe with low-risk bets — perfect for beginners\n📘 Register and deposit via Mpesa (KE) or Instant Bank (NG)\n🎁 Use your welcome bonus carefully — small bets to meet x3 wagering\n💰 Minimum deposit $5+ real money (not for free hunters)\n⏰ Bonus valid today — claim before it expires\n⚠️ Real money | 18+ | Bet responsibly\n👉 Register & claim your bonus: https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration","images":["261.png"]},
{"date":"2026-01-26","time":"21:00","content":"🎮 1XBET Daily 1xGames Tournament\n🔥 Low-risk leaderboard bets — small combos increase winning odds\n📘 Play smart: manage bankroll, focus on one game at a time\n🎁 Use your 1xBet bonus safely (x3 wagering) to boost chances\n💰 Deposit via Mpesa (KE) or Instant Bank (NG) — min $5+ real money\n⏰ Tournament ends tonight — join before it closes\n⚠️ Real money | 18+ | Bet responsibly\n👉 Register & play smart: https://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=promotions/daily-tournament","images":["262.png"]},

{"date":"2026-01-27","time":"15:00","content":"🏦 MelBet Withdrawal Tips\n🔥 Safe, fast withdrawals — low-risk, reliable methods\n📘 Withdraw via Mpesa (KE) or Instant Bank (NG) and track bonus wagering\n🎁 Ensure any bonus conditions are cleared before cashing out\n💰 Minimum withdrawal $5+ real money (not for free hunters)\n⏰ Withdraw today for instant access to funds\n⚠️ Real money | 18+ | Bet responsibly\n👉 Withdraw safely: https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration","images":["271.png"]},
{"date":"2026-01-27","time":"21:30","content":"🎮 MelBet Beginner-Friendly Bet\n🔥 Odds 1.50–2.20 — high chance for safe play\n📘 Focus on one match or small combo, track your units, avoid chasing losses\n🎁 Use your Double First Deposit Bonus via Mpesa (KE) or Instant Bank (NG) safely — up to $100\n💰 Minimum deposit $5+ real money (not for free hunters)\n⏰ Bonus expires today — claim it before it runs out\n⚠️ Real money | 18+ | Bet responsibly\n👉 Register & start smart betting: https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration","images":["272.png"]},

{"date":"2026-01-28","time":"15:00","content":"🎯 MelBet Low-Risk Betting Tip\n🔥 Odds 1.50–2.20 — safer bets for beginners\n📘 Focus on one match and track your bankroll carefully to stay in control\n🎁 Claim your 1st Deposit Welcome Bonus via Mpesa (KE) or Instant Bank (NG) safely — 100% match up to $130\n💰 Min deposit $5+ real money (not for free hunters)\n⏰ Use your bonus today to maximize winnings\n⚠️ Real money | 18+ | Bet responsibly\n👉 Register & start betting: https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration","images":["281.png"]},
{"date":"2026-01-28","time":"21:30","content":"⚡ FortunoBet Tip – 1XBet\n⚽ Safe Betting Tips for Beginners\n🔥 Focus on low-risk bets (1.50–2.20) — higher chance to win steadily\n📘 Bet **one small unit per match** and track results carefully for long-term growth\n🎁 **100% deposit bonus up to €300** (x3 wagering) – use it to double your first stake smartly\n💰 Minimum deposit: ₦500 / KSh 100\n⏰ Bonus expires in **2h** — don’t miss it!\n⚠️ Real money betting | 18+\n👉 Register & start safe betting: https://fortunobet.com/1xbet","images":["282.png"]},

{"date":"2026-01-29","time":"15:00","content":"I’m avoiding risky combos today — one match only, slow and controlled ⚽\nOdds around 1.50–2.20 are enough if you respect bankroll discipline.\nIf you use the MelBet bonus, start with small stakes until wagering is cleared 📘\n🎁 MelBet welcome bonus available via Mpesa (KE) or Instant Bank (NG).\n💰 Real money required — minimum deposit ₦500 / KSh 100.\n⏰ Bonus window is short today, don’t delay decisions.\n⚠️ Real money betting | 18+\n👉 Start small here: https://fortunobet.com/melbet","images":["291.png"]},
{"date":"2026-01-29","time":"21:00","content":"💎 1XBet – How I Use the Deposit Bonus\n\nI don’t rush big deposits. I go step by step so I don’t lose control.\n\n📘 I deposit small amounts, track every step, and only move forward when I’m comfortable.\n\n🎁 1XBet gives 100% bonus up to €300 — I use it smart, not greedy.\n💰 Minimum deposit $5+ real money (not for free hunters)\n\n⏰ If you want to use the bonus properly, better start early.\n\n⚠️ Real money betting | 18+\n👉 Same 1XBet link I use: https://fortunobet.com/1xbet","images":["292.png"]},

{"date":"2026-01-30","time":"16:00","content":"🎯 My MelBet Live Betting Style\n\nLive betting is dangerous if you rush. I wait, watch, then place ONE small bet.\n\n📘 No multiple live combos. One move, then I stop.\n\n🎁 MelBet bonuses work fine for live bets if you stay disciplined.\n💰 Minimum stake $5+ real money\n📲 Mpesa (KE) & Instant Bank (NG)\n\n⏰ First half is usually enough — no need to overplay.\n\n⚠️ Real money | 18+ | Bet responsibly\n👉 MelBet link I’m using: https://fortunobet.com/melbet","images":["301.jpg"]},
{"date":"2026-01-30","time":"22:00","content":"💸 1XBet Cashback Tip (Very Important)\n\nLosses happen. I don’t chase them — I let cashback do its job.\n\n📘 I just bet normally and the system counts losses automatically.\n\n🎁 3% weekly loss cashback helps protect part of my deposits.\n💰 Minimum deposit $5+ real money\n\n⏰ Check your account before midnight so you don’t miss it.\n\n⚠️ Real money betting | 18+\n👉 Cashback works on this link: https://fortunobet.com/1xbet","images":["302.png"]},

{"date":"2026-01-31","time":"13:00","content":"🏦 How I Withdraw from MelBet (Important)\n\nI never rush withdrawals. I always clear bonus rules first, then test with a small amount.\n\n📘 Many failed withdrawals happen because this step is skipped.\n\n🎁 MelBet withdrawals are fast when details are correct.\n💰 Minimum withdrawal: $5+ real money\n\n⏰ Most times I get paid the same day.\n\n⚠️ Real money | 18+ | Bet responsibly\n👉 Withdraw from MelBet here: https://fortunobet.com/melbet","images":["311.jpg"]},
{"date":"2026-01-31","time":"17:30","content":"🥈 1XBet Second Deposit Tip (Read First)\n\nSecond deposits cause problems when people rush. I keep it controlled.\n\n📘 Small deposit, calm betting, and tracking everything matters.\n\n🎁 75% second deposit bonus up to $100\n📲 Mpesa (KE) & Instant Bank (NG)\n💰 Minimum deposit: $5+ real money\n\n⏰ This bonus does not wait forever.\n\n⚠️ Real money betting | 18+\n👉 1XBet link I personally use: https://fortunobet.com/1xbet","images":["312.png"]},

{"date":"2026-02-01","time":"14:00","content":"Don't let your winnings sit there! 🏦\n\nOne thing I’ve learned: Withdraw in small parts. It keeps your account clean and the processing is much faster.\n\n⚡️ Fastest payouts (usually same day)\n💰 Min Withdrawal: $5+\n🚀 No delays on this portal\n\nMove your money safely here:\n👇👇👇\nhttps://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration","images":["011.png"]},
{"date":"2026-02-01","time":"19:00","content":"The 2nd Deposit Secret 🥈\n\nMost people fail their second bonus because they rush. I keep it controlled: deposit small, play calm, and win.\n\n✅ 75% Bonus active (up to $100)\n📲 Instant Sync: Mpesa & Bank\n💰 Start with: $5+ minimum\n\nLock in your 2nd bonus before it expires:\n👇👇👇\nhttps://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=registration","images":["012.png"]},

{"date":"2026-02-02","time":"15:00","content":"New to the game? Read this. ⚽\n\nIf you’re just starting on MelBet, don't go big yet. Register, deposit a small amount ($5), and learn the system first.\n\n🎁 Easier wagering when you start small\n💰 Min Deposit: $5 only\n⏰ Best time to start is today\n\nOpen your account correctly here:\n👇👇👇\nhttps://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration","images":["021.png"]},
{"date":"2026-02-02","time":"21:00","content":"How I tested 1XBet... 🧐\n\nI didn't trust it until I saw the money in my bank. I started with a small $5 test—withdrawals were instant, so now I'm all in.\n\n🎁 100% Match Bonus (Double your money)\n⚡️ Reliable: Mpesa & Instant Bank\n💰 Entry: Only $5+\n\nUse the link I personally trust:\n👇👇👇\nhttps://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=registration","images":["022.jpg"]},
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




