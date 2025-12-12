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
{"date": "2025-12-13", "time": "12:30", "content": "🎁 STOP SCROLLING! Your $1750 Casino Package + 290 Free Spins Awaits! 🎰\n\nReady for a huge weekend boost? Our licensed partner is rolling out the ultimate welcome offer to kickstart your play! This is a massive 5-tiered package, but the best part is the Free Spins!\n\nHere's what you get:\n\n✅ Up to $1750 in Welcome Bonuses!\n🔥 A whopping 290 Free Spins included!\n🔑 Simple requirements across your first 5 deposits.\n\nDon't miss out on one of the biggest casino welcome packages available from a licensed, trusted provider.\n\n👇 CLAIM YOUR 290 SPINS NOW: https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration\n\n🌐 Browse the Casino: https://fortunobet.com\n\nWhat game will you use your first free spins on? 🏆", "images": ["131.jpg"]},
{"date": "2025-12-13", "time": "20:00", "content": "🏈 GET A 20% BONUS JUST FOR BETTING NFL! 💰\n\nReady for some huge weekend football action? Don't leave money on the field! With our licensed partner, every NFL bet you place gets you closer to a sweet reward.\n\nClaim the Touchdown Wins Weekly Bonus:\n✅ Bet on any NFL game this weekend (Chiefs vs Chargers, Ravens vs Bengals, etc.).\n✅ Get 20% of your total weekly wagers back as a bonus!\n✅ Maximize your football profits every Sunday!\n\nIt's the easiest way to add value to your sports betting strategy. Licensed and ready for action!\n\n👇 CLAIM YOUR 20% NFL BONUS NOW: https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration\n\n🌐 Browse the Sportsbook: https://fortunobet.com\n\nWho are you betting on to win this weekend?", "images": ["132.jpg"]},

{"date": "2025-12-14", "time": "12:00", "content": "🚀 FINISH STRONG! CLAIM YOUR FINAL $100 DEPOSIT BONUS! 🏅\n\nYou've made it to the last step of the Welcome Series! Why stop now when an easy bonus is waiting?\n\nThis Sunday, complete your bonus climb with the 4th Deposit Match:\n✅ 25% Match on your 4th deposit.\n✅ Max bonus up to $100.\n✅ The final bonus in your initial series!\n\nDon't leave free money on the table. Hit that deposit button and secure your full welcome package today!\n\n👇 CLAIM YOUR 4TH DEPOSIT BONUS NOW: https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration\n\n🌐 Access Your Account: https://fortunobet.com\n\nHow much are you banking for the week ahead?", "images": ["141.png"]},
{"date": "2025-12-14", "time": "17:00", "content": "🔥 NEW USER ALERT: CLAIM YOUR FREE $5 CASH NOW! 🔥\n\nStop planning and start playing! Exclusively for our Telegram members, FortunoBet is giving you FREE MONEY just for trying the platform.\n\nThis is the easiest bankroll boost you will ever get:\n✅ Deposit just $3.\n✅ Get an instant $5 FREE CASH from FortunoBet!\n\nThat's an exclusive 166% boost to get you started!\n\nOnce you are in, you immediately unlock our partner's full suite of massive bonuses: the $1,750 Welcome Package, 290 Free Spins, NFL Bonuses, and more!\n\nDon't wait—this exclusive offer is only for new depositors today!\n\n👇 DEPOSIT $3, GET $5 FREE & UNLOCK ALL BONUSES: https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration\n\n🌐 Visit FortunoBet: https://fortunobet.com\n\nWhat's your plan for turning $5 into $50?", "images": ["142.png"]},
{"date": "2025-12-14", "time": "21:00", "content": "⚽️ STOP BETTING ON LOW ODDS! YOU'RE LEAVING MONEY BEHIND! 📈\n\nYou deserve bigger wins for your knowledge. While other sites limit your choices, FortunoBet delivers the best odds and the widest range of events, making every bet count!\n\nWhy Bet with Us?\n✅ Massive Coverage: From major Soccer and NBA to niche Esports leagues—if a game is on, we've got the line.\n✅ Ideal Payouts: Our odds are constantly sharpened to offer the highest possible value on every match.\n✅ Trusted Action: Get fast payouts from a fully licensed, secure platform.\n\nStop settling for less! The best value for your weekend bets is right here.\n\n👇 GET HIGHER ODDS ON THOUSANDS OF SPORTS & ESPORTS: https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=line/esports\n\n🌐 Visit FortunoBet: https://fortunobet.com\n\nWho is your lock of the week? Let us know!", "images": ["143.png"]},

{"date": "2025-12-15", "time": "12:00", "content": "🎉 MONDAY MONEY MOVES: CONGRATS ON YOUR WEEKEND WINS! 💰\n\nAlright, legends! I saw those winning slips, and what a weekend it was! Whether you cashed out big on the NFL or smashed the slots, you proved this platform pays.\n\nBut the game doesn't stop. We're just getting started on another week of domination.\n\n✅ New week, new opportunities: Fresh lines, hot tables, and massive jackpots waiting.\n📈 Keep the momentum: Those winning streaks don't build themselves.\n🏆 Your biggest win is next: Every bet is a step closer to that life-changing payout.\n\nForget the Monday blues. This is about making green! Let's carry that winning energy straight into a new week of crushing it.\n\n👇 YOUR NEXT WIN STARTS HERE: https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration\n\n🌐 Check Your Balance & New Bets: https://fortunobet.com\n\nWho's ready to turn Monday into a payday? Let's go!", "images": ["151.png"]},
{"date": "2025-12-15", "time": "20:00", "content": "GO BIG OR GO HOME—RISK FREE! 🛡️💰\n\nI’m looking at the board for this weekend’s massive football slate, and FortunoBet is literally GIVING us a safety net. If you aren't building an Acca tonight, you’re missing the easiest win of the month.\n\n🔥 THE WEEKEND HACK:\nBuild a parlay with 7+ picks. If ONE team lets you down, you get **100% OF YOUR MONEY BACK.** One bad apple won't spoil your payout! 🍎❌\n\nREAL TALK: I’ve checked the payouts this week—they are fast and legit. Don't be the guy watching everyone else post their winning slips on Sunday. Get your risk-free slip in right now.\n\n👇 **LOCK IN YOUR INSURANCE HERE:** https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration\n\n🌐 **Visit the Platform:** https://fortunobet.com\n\n💸 Let’s get this bread risk-free. See you at the top! 🤜🤛", "images": ["152.png"]},

{"date": "2025-12-16", "time": "12:00", "content": "🔥 MID-WEEK CASH BACK! GET 20% OF YOUR WAGERS FREE! 🏈\n\nYour betting week starts NOW! Why wait for Sunday when you can earn bonuses all week long? Our licensed partner is rewarding every NFL bet you place with massive cash back.\n\nThis is the easiest bonus money you'll earn this week:\n✅ Bet on any NFL market.\n✅ Receive 20% of your total weekly wagers back as a bonus!\n✅ Fuel your bankroll for the next round of games!\n\nDon't let your NFL knowledge go unrewarded. Every Monday, cash drops straight into your account. Start earning today!\n\n👇 CLAIM YOUR 20% WEEKLY BONUS NOW: https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration\n\n🌐 Browse the Sportsbook: https://fortunobet.com\n\nWhat's your first mid-week NFL bet?", "images": ["161.png"]},
{"date": "2025-12-16", "time": "20:00", "content": "🎰 STOP SEARCHING! FIND YOUR NEXT JACKPOT INSTANTLY! 💡\n\nTired of endless scrolling to find a quality game? At FortunoBet, we make winning easy! Our Casino section is engineered for speed, discovery, and high payouts.\n\nWhy Our Casino is Built to Win:\n✅ New & Trending Filters: See the highest rating and newest games that are hot right now!\n✅ Instant Search: Find your favorite slots and tables in seconds.\n✅ Massive Selection: Thousands of games, including the newest releases from top providers.\n\nDon't waste time on cold games. Jump straight to the top-rated hits where the big money is dropping!\n\n👇 JUMP STRAIGHT TO THE HOTTEST GAMES: https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration\n\n🌐 Explore the Casino Lobby: https://fortunobet.com\n\nWhat's the highest-rated slot you'll try first?", "images": ["162.png"]},

{"date": "2025-12-17", "time": "12:00", "content": "👑 WARNING: YOU ARE MISSING OUT ON FREE MONEY RIGHT NOW! 💸\n\nListen up. If you haven't registered on MelBet yet, you are *leaving your winning bet* on the table. We only partner with the best, and **MelBet's bonus structure is insane**—but you can't claim it until you're in the game.\n\nThe ONLY Way To Win Today:\n🔥 Stop The Excuses: Registration takes **LESS THAN 60 SECONDS** via \"One-Click.\"\n🛡️ 100% TRUSTED: MelBet is a fully licensed, secure partner. Your money is safer here than in your wallet.\n👑 Unlock EVERYTHING: By signing up now, you instantly unlock the massive Welcome Package and every exclusive bonus we drop in this channel.\n\n**Stop watching everyone else cash out. Your win starts and ends with this click.**\n\n👇 GET REGISTERED NOW—DON'T DELAY YOUR PAYOUT! https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration\n\n🌐 Official Partner Site: https://fortunobet.com\n\nIf you can register in under 30 seconds, reply with \"DONE\"!", "images": ["171.png"]},
{"date": "2025-12-17", "time": "14:00", "content": "💸 THE ONLY THING BETWEEN YOU AND YOUR PAYOUT IS A DEPOSIT BUTTON! 🛑\n\nStop acting like a tourist! You registered. Now act like a winner. Your account is empty, and your potential bonuses are **LITERALLY LOCKED** until you fund your account. The winners are depositing now. Where are you?\n\nTHIS IS NOT A GAME, THIS IS A WEALTH TRANSFER:\n🔥 STOP THE HESITATION: Deposit is instant. We accept everything from cards to crypto. You have no excuse.\n👑 IMMEDIATE REWARD: The moment your money hits, we hit you back with a **MATCH BONUS** and instantly unlock the exclusive, high-value bonuses the casuals never see.\n🛡️ TRUST IS BUILT ON SPEED: Our platform is secure, and our payouts are fast. Prove you're serious, and we prove we pay.\n\n**Every minute you wait, you are watching someone else take your jackpot. Get off the bench.**\n\n👇 DEPOSIT NOW AND ACTIVATE YOUR WINNING ACCOUNT: https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration\n\n🌐 LOGIN & DEPOSIT: https://fortunobet.com\n\nIs today the day you stop losing money and start making it?", "images": ["172.png"]},
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




