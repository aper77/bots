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
{"date":"2026-01-10","time":"21:07","content":"💥 Turn $3 into $5 Instantly! 💸\nDeposit just $3 and get $5 FREE instantly 🎁 — credited immediately!\n\n⭐ Why this offer is 🔥\n✅ $5 bonus added instantly\n✅ Super low entry\n✅ Perfect for top slots like Sweet Bonanza 🎰\n\n💡 Tip: Use $5 on popular slots — big multipliers possible!\n\n🚀 Claim your $5 now: https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration\n\n⚡ Don’t wait — small deposit, huge fun!","images":["102.png"]},

{"date":"2026-01-11","time":"10:30","content":"🎰 SWEET BONANZA XMAS – CHASE THE MULTIPLIER MONSTER 💰\nSweet Bonanza Xmas is famous for sudden multiplier explosions and massive Free Spins payouts!\n\n💡 Why it’s special:\n✅ Free Spins Feature – Big wins happen here\n✅ 100X Multiplier Potential – Small bets can turn huge\n✅ Buy Bonus Option – Jump straight into action\n\n🎯 Play Smart:\n• Use steady bets or Buy Bonus if bankroll allows\n• Multipliers stack fast during Free Spins\n• High volatility = bigger payouts\n\n🚀 Play Sweet Bonanza Xmas now: https://fortunobet.com/com\n🌐 Explore more high-multiplier slots in the Casino Lobby!","images":["111.png"]},
{"date":"2026-01-11","time":"21:00","content":"👑 100% WELCOME BONUS UP TO $130! 💰\nStart strong on FortunoBet — get your first deposit matched 100% up to $130 and enjoy more spins, more play, and more winning chances instantly!\n\n⭐ Why players love this bonus:\n✅ Up to $130 extra balance\n✅ Double your bankroll instantly\n✅ Perfect for top slots & Buy Bonus features\n\n💡 Pro Tip: Use your bonus on popular slots like Gates of Olympus to maximize value\n\n🚀 Claim your bonus now:\nhttps://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration\n⚡ Bigger bankroll = bigger fun!","images":["112.png"]},

{"date":"2026-01-12","time":"10:30","content":"⚽️ 100% SPORTS BONUS UP TO $157 – BET BIGGER & SMARTER 🏆\nTake your sports betting to the next level with FortunoBet! Deposit once and get a 100% match up to $157.\n\n⭐ Why this bonus wins:\n✅ Deposit $157 → Play with $314\n✅ More freedom on top leagues & events\n✅ Ideal for accumulators & high-odds bets\n\n💡 Pro Tip: Spread bets across multiple matches to reduce risk\n\n🚀 Claim your Sports Bonus now:\nhttps://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=registration","images":["122.png"]},
{"date":"2026-01-12","time":"21:00","content":"🎉 1XBET $100,000 NEW YEAR GIVEAWAY 💰\nBet as usual and enter the $100,000 New Year Giveaway automatically — no extra cost, no extra steps!\n\n💡 Why join:\n✅ $100,000 prize pool\n✅ Free tickets with real bets\n✅ The more you bet, the more chances you get\n\n🎯 How it works:\n• Place normal bets\n• Receive tickets automatically\n• Winners announced soon\n\n🚀 Join now:\nhttps://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=promotions/santas-gift\n⏰ Limited-time event!","images":["121.png"]},

{"date":"2026-01-13","time":"10:30","content":"🎰 ULTIMATE CASINO BONUS: 50% CASH + 30 FREE SPINS UP TO $375 💰\nUnlock a powerful casino package on FortunoBet — extra cash plus Free Spins on top-performing slots.\n\n⭐ What you get:\n✅ Up to $375 bonus cash\n✅ 30 Free Spins on a high-payout slot\n✅ Play slots, tables & live casino\n\n💡 Pro Tip: Use cash bonus on Live Blackjack and Free Spins for jackpot hunting\n\n🚀 Claim your casino package:\nhttps://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=registration","images":["131.png"]},
{"date":"2026-01-13","time":"21:00","content":"🚨 STOP SCROLLING – FREE MONEY & FAST PAYOUTS 💰\nJoin FortunoBet in 2026 and access instant bonuses, fast withdrawals, and massive win potential.\n\n👑 Why players join daily:\n✅ Choose $5 low-risk start or $130 match bonus\n✅ Instant payouts with zero fees\n✅ Exclusive slots with up to 10,000X potential\n✅ 24/7 live support\n\n🔥 Registration takes under 30 seconds — don’t miss out!\n\n🚀 Start winning now:\nhttps://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=registration","images":["141.png"]},





{"date":"2026-01-16","time":"09:00","content":"🚨 URGENT: YOUR BALANCE IS ABOUT TO DOUBLE! 🚨\n\nStop betting with half a bankroll!\nFortunoBet (powered by 1xBet) has unlocked the Friday Reload. Deposit now and get the official 1xBet 100% bonus up to €300 💰\n\n🔥 THE POWER DEAL:\n✅ Deposit €300 ➡️ Play with €600\n✅ Valid for EVERY FortunoBet user today\n✅ Low x3 wagering – faster withdrawals\n\n⚠️ Offer expires at midnight. Miss it and lose free money.\n\n🌐 FortunoBet Official Website:\nfortunobet.com\n\n🚀 Activate Bonus Now:\nhttps://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=registration","images":["lucky_friday_extreme.png"]}

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




