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
{"date": "2025-12-20", "time": "20:00", "content": "🤯 THE ULTIMATE WEEKEND HACK IS HERE: RISK-FREE ACCUMULATORS! 🛡️💰 Stop letting a single late goal or bad call destroy your payout! FortunoBet offers the best safety net for this weekend's football slate. HOW IT WORKS: Build an Acca with 7 or more picks. If only ONE selection loses, you get 100% OF YOUR STAKE REFUNDED! This is full 100% REFUND INSURANCE. Aim for a massive win with a safety net. LOCK IN YOUR 100% REFUND INSURANCE HERE: 👇 https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration 🌐 Visit the Platform: https://fortunobet.com 💸 Time to build that winning slip with zero fear!", "images": ["202.png"]},

{"date": "2025-12-21", "time": "12:00", "content": "💥 DEPOSIT NOW! Your $500,000 Jackpot is Waiting! You're one click away from the biggest wins! Your potential fortune in Coinspin Fever is LOCKED until you deposit. COINSPIN FEVER: High volatility, massive payouts. 👑 INSTANT BONUS: Deposit now and get your MATCH BONUS immediately! ⏱️ DON'T MISS IT! Winners are spinning now. Get in the game and grab the win! 👇 ACTIVATE YOUR ACCOUNT & SPIN NOW: https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration 🌐 LOGIN & DEPOSIT: https://fortunobet.com", "images": ["222.png"]},
{"date": "2025-12-21", "time": "20:00", "content": "⭐ UNLOCK THE NEXT LEVEL! Your 3rd Deposit Comes with a HUGE 75% Bonus! You're on a roll! The journey gets even better. We're fueling your play with a substantial boost on your third deposit. Don't miss out on this incredible value: 🎉 Get a massive 75% Match Bonus on your 3rd deposit! 💰 Claim up to $500 FREE to explore more games. 📈 Elevate your bankroll and chase those bigger wins. This is the perfect opportunity to maximize your gameplay. 👇 JUMP STRAIGHT TO THE ACTION 👇 HOTTEST GAMES: https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration 🌐 Explore the Casino Lobby: https://fortunobet.com", "images": ["212.png"]},

{"date": "2025-12-22", "time": "12:00", "content": "🔥 YOU ARE MISSING OUT ON FREE MONEY RIGHT NOW! 🔥 The only thing stopping you from winning is the registration button! MelBet's bonus structure is one of the best, but you need to act fast to claim it. Here’s Why You Need To Join TODAY: 🔥 ONE-CLICK ENTRY: Registration takes LESS THAN 60 SECONDS via \"One-Click.\" 🛡️ 100% SECURE: MelBet is a fully licensed, secure partner. Your funds are protected. 👑 INSTANT UNLOCK: Signing up now instantly unlocks the massive Welcome Package and every exclusive bonus we drop in this channel. Stop watching everyone else cash out. Your win starts and ends with this click. Don't delay your payout! 👇 GET REGISTERED NOW https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration 🌐 Official Partner Site: https://fortunobet.com Can you register in under 30 seconds? Reply with DONE!", "images": ["221.png"]},
{"date": "2025-12-22", "time": "20:00", "content": "🚀 DON'T SLOW DOWN! Your Second Big Casino Boost is Here! You crushed your first deposit—now it's time for the massive follow-up! Keep your bankroll growing with the next step in our Welcome Package. We're making sure your momentum never stops: ✨ Get a huge 50% Match Bonus on your 2nd deposit! 💸 Claim up to $300 FREE in bonus money. ✅ Double your playtime and explore hundreds of new slots and tables. This is your chance to turn a great start into a major win streak. 👇 JUMP STRAIGHT TO THE ACTION 👇 HOTTEST GAMES: https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration 🌐 Explore the Casino Lobby: https://fortunobet.com", "images": ["211.png"]},

{"date": "2025-12-23", "time": "12:00", "content": "🎰 STOP SEARCHING! FIND YOUR NEXT JACKPOT INSTANTLY! 💡 Tired of endless scrolling to find a quality game? At FortunoBet, we make winning easy! Our Casino section is engineered for speed, discovery, and high payouts. Why Our Casino is Built to Win: ✅ New & Trending Filters: See the highest rating and newest games that are hot right now! ✅ Instant Search: Find your favorite slots and tables in seconds. ✅ Massive Selection: Thousands of games, including the newest releases from top providers. Don't waste time on cold games. Jump straight to the top-rated hits where the big money is dropping! 👇 JUMP STRAIGHT TO THE HOTTEST GAMES: https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration 🌐 Explore the Casino Lobby: https://fortunobet.com What's the highest-rated slot you'll try first?", "images": ["162.png"]},

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




