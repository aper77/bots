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
{"date":"2026-01-10","time":"21:00","content":"💥 Turn $3 into $5 Instantly! 💸 Deposit just $3 and get $5 FREE instantly 🎁 — credited immediately! ⭐ Why this offer is 🔥 ✅ $5 bonus added instantly ✅ Super low entry ✅ Perfect for top slots like Sweet Bonanza 🎰 💡 Tip: Use $5 on popular slots — big multipliers possible! 🚀 Claim your $5 now: https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration ⚡ Don’t wait — small deposit, huge fun!","images":["102.png"]},

{"date":"2026-01-11","time":"10:30","content":"🎰 SWEET BONANZA XMAS – CHASE THE MULTIPLIER MONSTER 💰 Sweet Bonanza Xmas is famous for sudden multiplier explosions and massive Free Spins payouts! 💡 Why it’s special ✅ Free Spins Feature – Big wins happen here ✅ 100X Multiplier Potential – Small bets can turn huge ✅ Buy Bonus Option – Jump straight into action 🎯 Play Smart: Use steady bets or Buy Bonus if bankroll allows, Multipliers stack fast during Free Spins, High volatility = bigger payouts 🚀 Play Sweet Bonanza Xmas now: https://fortunobet.com/com 🌐 Explore more high-multiplier slots in the Casino Lobby!","images":["111.png"]},
{"date":"2026-01-11","time":"21:00","content":"👑 100% WELCOME BONUS UP TO $130! 💰 Start your FortunoBet journey with confidence — we’ll match your first deposit dollar-for-dollar up to $130, giving you extra spins and more fun instantly! ⭐ Why this bonus is amazing ✅ Up to $130 FREE on your first deposit ✅ Double your starting balance instantly ✅ Try top slots with extra bankroll 💡 Pro Tip: Use your bonus on exciting slots like Gates of Olympus and explore 'Buy Bonus' features safely 🚀 Claim your bonus now: https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration ⚡ Don’t wait — bigger bankroll, bigger fun!","images":["112.png"]},

{"date":"2026-01-12","time":"10:30","content":"⚽️ LEVEL UP YOUR BETTING: 100% SPORTS BONUS UP TO $157! 🏆\n\nBoost your weekend betting with FortunoBet! We match your first deposit 100% up to $157, giving you extra funds to enjoy more bets and more excitement.\n\n⭐ WHY THIS BONUS IS GREAT:\n✅ Deposit $157 and play with $314 instantly\n✅ Place higher-value bets on major leagues\n✅ Perfect for players looking to get more from their bets\n\n💡 PRO TIP: Try using the bonus to explore high-odds selections or accumulators safely for bigger wins.\n\n👇 CLAIM YOUR 100% SPORTS MATCH BONUS NOW:\nhttps://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=registration","images":["122.png"]},
{"date":"2026-01-12","time":"21:00","content":"🎉 1XBET $100,000 NEW YEAR GIVEAWAY 💰\n\n1xBet is giving away $100,000 this New Year 🎁 Join just by placing your normal bets — free tickets are added automatically.\n\n💡 WHY JOIN?\n✅ $100,000 prize pool\n✅ Free tickets with real bets\n✅ No extra purchase needed\n\n🎯 HOW IT WORKS\n• Bet as usual\n• Earn tickets automatically\n• More bets = more chances\n\n👇 ENTER NOW\nhttps://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=promotions/santas-gift\n\n⏰ Ends soon!","images":["121.png"]},

{"date":"2026-01-13","time":"10:30","content":"🎰 ULTIMATE CASINO PACKAGE: 50% BONUS + 30 FREE SPINS UP TO $375! 💰\n\nGet the best of both worlds! FortunoBet gives you a 50% cash bonus plus 30 Free Spins on top slots — perfect for more fun and bigger wins.\n\n⭐ WHAT YOU GET:\n✅ Up to $375 bonus cash\n✅ 30 Free Spins on a high-payout slot\n✅ Cash bonus for table games/live casino, Free Spins for slots\n\n💡 PRO TIP: Try your bonus on Live Blackjack and use Free Spins to chase slot jackpots.\n\n👇 CLAIM YOUR BONUS PACKAGE NOW:\nhttps://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=registration","images":["131.png"]},
{"date":"2026-01-13","time":"21:00","content":"🥳 IT'S LUCKY FRIDAY! DOUBLE YOUR MONEY WITH 100% RELOAD BONUS UP TO 300 EUR! 💰\n\nEvery Friday, FortunoBet matches your deposit 100% up to 300 EUR — perfect for Friday night matches and weekend slots.\n\n⭐ WHY THIS BONUS IS GREAT:\n✅ Deposit 300 EUR, play with 600 EUR\n✅ Extra funds for weekend betting fun\n✅ Low x3 wagering on accumulator bets within 24 hours\n\n💡 PRO TIP: Deposit early on Friday to make the most of the 24-hour betting window!\n\n👇 CLAIM YOUR LUCKY FRIDAY BONUS NOW:\nhttps://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=registration","images":["132.png"]},

{"date":"2026-01-14","time":"10:30","content":"STOP SCROLLING! 🚨 FREE MONEY & INSTANT WINS START HERE 💰\n\nJoin FortunoBet — the fastest, easiest path to payouts in 2026! Over 100,000 players join us every month.\n\n👑 WHY REGISTER NOW:\n✅ Pick your bonus: $5 Low-Risk Start or $130 Match\n✅ Instant payouts with ZERO fees\n✅ Access exclusive slots & 10,000X jackpot potential\n✅ 24/7 friendly support\n\n🔥 DON’T MISS OUT: Registration is FAST, FREE, and takes less than 30 seconds!\n\n👇 YOUR FREE WINNINGS ARE WAITING:\nhttps://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=registration","images":["141.png"]},
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




