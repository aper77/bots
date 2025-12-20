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
{"date": "2025-12-18", "time": "12:30", "content": "🤯 NEVER LOSE AN ACCUMULATOR AGAIN! 🛡️\n\nStop letting one bad pick cost you everything. FortunoBet has removed the risk with our 100% REFUND insurance!\n\nPlace an accumulator with 7+ selections and if only ONE pick misses, you get a FULL REFUND on your stake. It’s the ultimate way to bet big with maximum protection.\n\n* 🛡️ Ultimate Safety: Bet on big odds without the fear of a near-miss.\n* 💰 Zero Loss: If you only miss one, your stake comes right back.\n* ✅ Simple Rule: Needs 7+ selections to qualify.\n\nClick below and start building your insured accumulator today!\n\nClaim Your 100% Refund Insurance Now: https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=r…\n\n---\n\n### 👇 JUMP STRAIGHT TO THE ACTION 👇\n\n* HOTTEST GAMES: https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=r…\n* Explore the Casino Lobby: https://fortunobet.com\n\nWhat's the biggest payout you've ever missed by one game? Tell us below! 👇", "images": ["181.png"]},
{"date": "2025-12-18", "time": "23:55", "content": "⚡️ DEMI GODS V: BIG WIN STRATEGY ⚡️\n\n🎯 Goal: HUGE mythical jackpots.\n\nSMART MOVE: Use Buy Feature (if available) for instant Free Spins & massive multipliers! 🚀\n\nPLAY NOW: https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration", "images": ["182.png"]},

{"date": "2025-12-19", "time": "12:00", "content": "🚀 WEEKEND POWER UP: YOUR NEXT BONUS IS HERE! 🚀\n\nReady to maximize your weekend gaming funds? As a loyal FortunoBet player, you qualify for the final bonus in our Deposit Series!\n\nGet a massive 25% MATCH UP TO $100 on your 4th deposit right now!\n\n* 🏆 Top-Tier Reward: Claim up to $100 extra cash instantly.\n* 🔥 Instant Boost: Add serious value to your weekend play sessions.\n* 💰 Final Step: Complete the deposit series and unlock ongoing loyalty perks!\n\nDon't miss this chance to grab your extra $100 before you hit the weekend slots and tables!\n\nClaim Your $100 Bonus Now: https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration\n\n🌐 Explore the Casino Lobby: https://fortunobet.com\n\nWhat's the first game you'll play with your bonus cash? Tell us! 👇", "images": ["191.png"]},
{"date": "2025-12-19", "time": "20:00", "content": "🦌 MASTER THE GOLDHORN WILD HERD FOR MASSIVE WINS! 💰\n\nReady to join the herd and chase legendary jackpots? Goldhorn Wild Herd is built for players hunting HUGE rewards! Here is your quick strategy guide for max cash-out potential:\n\n### 🎯 Pro Strategy for Big Wins:\n\n* ⚡️ Stack Wilds: The Goldhorn Wilds are your key. Land multiple early to signal a high-win session.\n* 🔄 Chase the Bonus: The biggest money is in Free Spins. Bet strategically until you hit the bonus round where guaranteed features pay off.\n* ⚖️ Manage Risk: This is high-volatility. Manage your bets to last until the bonus triggers—patience leads to profit!\n\nStop spinning blind and start spinning like a pro. The Wild Herd awaits!\n\nPLAY GOLDHORN WILD HERD NOW: https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration\n\n🌐 Explore the Casino Lobby: https://fortunobet.com\n\nShare your biggest slot multiplier below! 👇", "images": ["192.png"]},

{"date": "2025-12-20", "time": "12:00", "content": "🔥 STOP BETTING ALONE. JOIN THE WINNING HERD! 🤝 Tired of losing? FortunoBet is the fastest-growing, most trusted betting community on Telegram, focused on long-term, sustainable profit. ✅ Verified Results & Elite Picks from top experts. 🫂 Join 1000+ members who share strategies and celebrate real wins. The time for solo struggling is over. We guarantee trust and profit. JOIN THE 1000+ WINNERS NOW! ➡️ https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration 🌐 Explore FortunoBet: https://fortunobet.com", "images": ["201.png"]},
{"date": "2025-12-20", "time": "20:00", "content": "🤯 RISK-FREE WEEKEND ACCUMULATOR HACK! 🛡️💰\n\n🎯 HOW IT WORKS (100% REFUND INSURANCE):\n* Build 7+ picks.\n* If you miss by just ONE, you get 100% STAKE REFUNDED!\n\nLOCK IN YOUR ZERO-FEAR BET! 👇\nhttps://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration\n\n🌐 Platform: https://fortunobet.com", "images": ["202.png"]},

{"date": "2025-12-21", "time": "12:00", "content": "💥 DEPOSIT NOW! Your $500,000 Jackpot is Waiting!\n\nYou're one click away from the biggest wins! Your potential fortune in Coinspin Fever is LOCKED until you deposit.\n\n👑 INSTANT BONUS: Deposit now and get your MATCH BONUS immediately!\n⏱️ DON'T MISS IT! Winners are spinning now.\n\n👇 ACTIVATE YOUR ACCOUNT & SPIN NOW:\nhttps://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration\n\n🌐 LOGIN & DEPOSIT: https://fortunobet.com", "images": ["222.png"]},
{"date": "2025-12-21", "time": "20:00", "content": "⭐ UNLOCK THE NEXT LEVEL! Your 3rd Deposit Comes with a HUGE 75% Bonus!\n\nWe're fueling your play with a substantial boost on your third deposit. Don't miss out on this incredible value:\n\n🎉 Get a massive 75% Match Bonus on your 3rd deposit!\n💰 Claim up to $500 FREE!\n📈 Elevate your bankroll and chase those bigger wins.\n\n👇 JUMP STRAIGHT TO THE ACTION 👇\nHOTTEST GAMES: https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration\n\n🌐 Explore the Casino Lobby: https://fortunobet.com", "images": ["212.png"]},

{"date": "2025-12-22", "time": "12:00", "content": "🔥 YOU ARE MISSING OUT ON FREE MONEY RIGHT NOW! 🔥\n\nThe only thing stopping you from winning is the registration button! Act fast to claim your bonus.\n\nHere’s Why You Need To Join TODAY:\n🔥 ONE-CLICK ENTRY: Registration takes LESS THAN 60 SECONDS.\n🛡️ 100% SECURE: Your funds are protected.\n👑 INSTANT UNLOCK: Get the massive Welcome Package immediately!\n\nStop watching everyone else cash out. Don't delay your payout!\n\n👇 GET REGISTERED NOW:\nhttps://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration\n\n🌐 Official Partner Site: https://fortunobet.com", "images": ["221.png"]},
{"date": "2025-12-22", "time": "20:00", "content": "🚀 DON'T SLOW DOWN! Your Second Big Casino Boost is Here!\n\nKeep your bankroll growing with the next step in our Welcome Package. We're making sure your momentum never stops:\n\n✨ Get a huge 50% Match Bonus on your 2nd deposit!\n💸 Claim up to $300 FREE in bonus money.\n✅ Double your playtime and explore new games.\n\n👇 JUMP STRAIGHT TO THE ACTION 👇\nHOTTEST GAMES: https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration\n\n🌐 Explore the Casino Lobby: https://fortunobet.com", "images": ["211.png"]},

{"date": "2025-12-23", "time": "12:00", "content": "🎰 STOP SEARCHING! FIND YOUR NEXT JACKPOT INSTANTLY! 💡\n\nTired of endless scrolling? Our Casino is engineered for speed, discovery, and high payouts.\n\nWhy Our Casino is Built to Win:\n✅ New & Trending Filters: See the hottest games right now!\n✅ Instant Search: Find your favorite slots in seconds.\n✅ Massive Selection: Thousands of games from top providers.\n\nDon't waste time. Jump straight to the top-rated hits!\n\n👇 JUMP STRAIGHT TO THE HOTTEST GAMES:\nhttps://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration\n\n🌐 Explore the Casino Lobby: https://fortunobet.com", "images": ["162.png"]},
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




