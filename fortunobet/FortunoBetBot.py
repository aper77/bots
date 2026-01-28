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

{"date":"2026-01-29","time":"15:00","content":"⚽ Low-Risk Betting Tips\n🔥 Odds 1.50–2.20 give beginners a higher success rate\n📘 Bet 1–2 units per match, track bankroll, avoid risky combos to stay disciplined\n🎁 Use your MelBet bonus safely via Mpesa (KE) or Instant Bank (NG)\n💰 Minimum deposit: ₦500 / KSh 100\n⏰ Bonus expires in 2h — claim and play responsibly\n⚠️ Real money | 18+ | Bet responsibly\n👉 Register & start safe betting: https://fortunobet.com/melbet","images":["291.png"]},
{"date":"2026-01-29","time":"21:00","content":"💎 FortunoBet Tip – 1XBet\n🔥 Beginner-friendly multi-deposit bonus — each step is low-risk\n📘 Deposit small amounts per step and track units to manage risk safely\n🎁 **100% deposit bonus up to €300** – use each step to double your first stake smartly\n💰 Minimum deposit $5+ real money per step (not for free hunters)\n⏰ Complete your deposits **today** to maximize rewards\n⚠️ Real money betting | 18+\n👉 Register & start your Epic Deposit Series: https://fortunobet.com/1xbet","images":["292.png"]},

{"date":"2026-01-30","time":"16:00","content":"🎯 MelBet Live Bet Example\n🔥 Low-risk live betting: 1.50–2.20 odds — beginner-friendly\n📘 Watch the match, place a single small live bet, avoid chasing multiple combos\n🎁 Use bonuses safely via Mpesa (KE) or Instant Bank (NG)\n💰 Minimum stake $5+ real money (not for free hunters)\n⏰ Place your live bet in the first half to stay in control\n⚠️ Real money | 18+ | Bet responsibly\n👉 Start live betting: https://fortunobet.com/melbet","images":["301.jpg"]},
{"date":"2026-01-30","time":"22:00","content":"💸 FortunoBet Tip – 1XBet\n🔥 Low-risk way to recover some losses safely\n📘 Play normally and avoid chasing losses; cashback applies automatically\n🎁 **3% weekly loss cashback** – protects your deposits smartly\n💰 Minimum deposit $5+ real money (not for free hunters)\n⏰ Cashback valid **today** — check your account before midnight\n⚠️ Real money betting | 18+\n👉 Claim your cashback: https://fortunobet.com/1xbet","images":["302.png"]},

{"date":"2026-01-31","time":"13:00","content":"🏦 MelBet Withdrawal Tips\n🔥 Safe and fast withdrawals — low-risk, reliable methods\n📘 Ensure bonus wagering is cleared and withdraw small amounts first to stay in control\n🎁 Track withdrawals to avoid mistakes and stay in control\n💰 Minimum withdrawal $5+ real money (not for free hunters)\n⏰ Withdraw today for instant access to funds\n⚠️ Real money | 18+ | Bet responsibly\n👉 Withdraw safely via MelBet: https://fortunobet.com/melbet","images":["311.jpg"]},
{"date":"2026-01-31","time":"17:30","content":"🥈 FortunoBet Tip – 1XBet\n🔥 Boost your bankroll safely — perfect for low-risk play\n📘 Deposit small, track units, and use the bonus progressively to avoid risk\n🎁 **75% 2nd deposit bonus up to $100** – claim smartly via Mpesa (KE) or Instant Bank (NG)\n💰 Minimum deposit $5+ real money (not for free hunters)\n⏰ Bonus valid **today** — deposit before it expires\n⚠️ Real money betting | 18+\n👉 Register & claim your 2nd Deposit Bonus: https://fortunobet.com/1xbet","images":["312.png"]},

{"date":"2026-02-01","time":"14:00","content":"🏦 MelBet Withdrawal Tips\n🔥 Safe, fast withdrawals — low-risk and reliable\n📘 Withdraw after clearing bonus requirements and track amounts carefully\n🎁 Track your withdrawals to avoid mistakes and stay in control\n💰 Minimum withdrawal $5+ real money (not for free hunters)\n⏰ Withdraw today for instant access to funds\n⚠️ Real money | 18+ | Bet responsibly\n👉 Withdraw safely here: https://fortunobet.com/melbet","images":["011.png"]},
{"date":"2026-02-01","time":"19:00","content":"🥈 FortunoBet Tip – 1XBet\n🔥 Boost your bankroll safely — perfect for low-risk play\n📘 Deposit small, track units carefully, and use bonus to maximize profit without chasing\n🎁 **75% 2nd deposit bonus up to $100** – claim safely via Mpesa (KE) or Instant Bank (NG)\n💰 Minimum deposit $5+ real money (not for free hunters)\n⏰ Bonus valid **today only** — deposit before it expires\n⚠️ Real money betting | 18+\n👉 Register & claim your 2nd Deposit Bonus: https://fortunobet.com/1xbet","images":["012.png"]},

{"date":"2026-02-02","time":"15:00","content":"⚽ FortunoBet Registration & Deposit Guide\n🔥 Start safe with low-risk bets — perfect for beginners\n📘 Deposit and track your first bets carefully to meet wagering requirements safely\n🎁 Use your account safely — small bets to meet x3 wagering\n💰 Minimum deposit $5+ real money (not for free hunters)\n⏰ Register and deposit today — don’t miss out\n⚠️ Real money | 18+ | Bet responsibly\n👉 Register & start here: https://fortunobet.com/melbet","images":["021.png"]},
{"date":"2026-02-02","time":"21:00","content":"🎉 FortunoBet Tip – 1XBet\n🔥 Beginner-friendly bonus — boost your bankroll safely\n📘 Deposit small and track your units carefully to use your bonus smartly\n🎁 **100% first deposit bonus up to $100** – claim safely via Mpesa (KE) or Instant Bank (NG)\n💰 Minimum deposit $5+ real money (not for free hunters)\n⏰ Bonus valid **today only** — deposit before it expires\n⚠️ Real money betting | 18+\n👉 Register & claim your bonus: https://fortunobet.com/1xbet","images":["022.jpg"]},
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




