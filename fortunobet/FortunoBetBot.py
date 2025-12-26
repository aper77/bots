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

{"date": "2025-12-27", "time": "15:00", "content": "TRIPLE YOUR MONEY! 🤯 Fortunobet has partnered with 1xBet to give you the BIGGEST welcome bonus in Nigeria!\n\nIt takes 60 seconds to register and get your huge deposit bonus.\n\n#️⃣ Your Exclusive Code: 1x_4023125 (MUST USE THIS CODE!)\n\nCLICK NOW to claim your bonus:\nhttps://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=registration", "images": ["foruno+1xbet.jpg"]},
{"date": "2025-12-27", "time": "23:00", "content": "🎁 WIN UP TO 5000 EUR TODAY! 🎁\n\nThe biggest giveaway of the year is LIVE! 1xBet is running the New Year's Lucky Wheel where you get daily spins and a chance to win the huge €5,000 grand prize!\n\nIt takes 5 seconds to claim your daily ticket. Don't let this huge cash prize pass you by!\n\n👇 CLAIM YOUR FREE TICKET NOW 👇\nGET STARTED: https://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=promotions/new-years-wheel-2026\n\nIs today your lucky day?", "images": ["1xbetbonus.jpg"]},

{"date": "2025-12-28", "time": "15:00", "content": "75% POWER-UP! DON'T WAIT. DOMINATE TENNIS.\n\nYour 3rd deposit gets a massive 75% BONUS (up to $500 FREE)!\n\nBet on the stars: Rublev, Rybakina, & Kyrgios are playing Dec 28th. Use our edge to win big!\n\nCLAIM YOUR 75% NOW ⬇️\nhttps://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=line/tennis\n\n🌐 Official Partner Site: https://fortunobet.com", "images": ["281.png"]},
{"date": "2025-12-28", "time": "23:00", "content": "🤑 $100,000 CASH GIVEAWAY IS LIVE! 🤑\n\nThis is not a drill! 1xBet's 'Santa's Gift' draw gives you a chance to win the final Superprize: **$100,000 in cash** plus amazing tech prizes!\n\nEvery bet you place earns you tickets for the huge draw. You must be registered to win the life-changing prize.\n\n👇 GET YOUR TICKETS NOW! 👇\nCLAIM YOUR TICKET: https://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=promotions/santas-gift\n\nWhat would you do with $100,000?", "images": ["1xbetsanta.png"]},

{"date": "2025-12-29", "time": "15:00", "content": "🛡️ MONDAY BETTING INSURANCE! 🛡️\n\nTake the risk out of your week! Place a Correct Score bet on any match with 1xBet. If your prediction loses, they give you a Free Bet Refund!\n\nThis is the best way to chase high odds without the worry. Your first bet of the week is protected!\n\n👇 GET YOUR FREE BET INSURANCE 👇\nBET NOW: https://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=promotions/no-risk-bet\n\nWhich match are you predicting tonight?", "images": ["1xbet29.png"]},
{"date": "2025-12-29", "time": "23:00", "content": "🎰 STOP SEARCHING! FIND YOUR NEXT JACKPOT INSTANTLY! 💡\n\nTired of endless scrolling? Our Casino is engineered for speed, discovery, and high payouts.\n\nWhy Our Casino is Built to Win:\n✅ New & Trending Filters: See the hottest games right now!\n✅ Instant Search: Find your favorite slots in seconds.\n✅ Massive Selection: Thousands of games from top providers.\n\nDon't waste time. Jump straight to the top-rated hits!\n\n👇 JUMP STRAIGHT TO THE HOTTEST GAMES:\nhttps://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration\n\n🌐 Explore the Casino Lobby: https://fortunobet.com", "images": ["162.png"]},

{"date": "2025-12-30", "time": "15:00", "content": "KNOCKOUT DAY! 🏆 YOUR CHANCE TO WIN BIG.\n\nThe London Derby is LIVE, and AFCON giants are in action. Double your money on the biggest games with the best odds on FortunoBet!\n\nTODAY'S TOP PICKS:\n* Arsenal vs Palace: London Cup Drama! Odds: 1.536\n* Algeria vs Sudan: Mahrez on the hunt! Algeria Win: 1.435\n\nGET YOUR SLIP READY. BET NOW! 👇\nhttps://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=line/football\n\n🌐 Official Site: https://fortunobet.com", "images": ["241.png"]},
{"date": "2025-12-30", "time": "23:00", "content": "🏆 UNLOCK ALL THE BONUSES! 🏆\n\nWhy choose one bonus when you can have BOTH? Fortunobet has gathered the BEST offers from Melbet and 1xBet in one place.\n\nFrom huge welcome matches to daily free bets and loyalty cashback, your rewards are waiting!\n\nJoin our winning team and claim every bonus:\n\n👇 YOUR BONUS HUB 👇\nhttps://fortunobet.com/com/bonuses", "images": ["30m=x.png"]},

{"date": "2025-12-31", "time": "15:00", "content": "🎁 HAPPY HOLIDAYS, GLOBAL WINNERS! 🎉\n\nOn this festive day, the whole FortunoBet family wishes you peace, joy, and **GREAT FORTUNE**! Thank you for placing your trust with us this year.\n\nYour Trusted Home for Winnings: 👇\nhttps://fortunobet.com/com", "images": ["251.png"]},
{"date": "2025-12-31", "time": "23:00", "content": "⏰ LAST CHANCE: FREE MONEY GIFT! 🎁\n\nYou're registered, but you haven't played! Don't miss out on your welcome reward.\n\nGet MORE Partner Bonuses on your 1st Deposit.\nDeposit $3 or more right now, and FortunoBet gifts you $5 EXTRA!\nStop waiting. Start winning with free cash! 👇\n\nGET REGISTERED NOW:\nhttps://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration\n\n🌐 Official Partner Site: https://fortunobet.com", "images": ["252.png"]},

{"date": "2026-01-01", "time": "15:00", "content": "STOP! YOUR 2ND GIFT IS WAITING! 💰\n\nYou've started strong—now claim your next reward! Your **Second Deposit** guarantees you a massive match bonus and **FREE SPINS** from FortunoBet.\n\nDon't break your winning streak!\n\nCLAIM GIFT #2 HERE: 👇\nhttps://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration", "images": ["261.png"]},
{"date": "2026-01-01", "time": "23:00", "content": "💣 THE BOMB! HIT 5.196 ODDS TODAY! 🏆\n\nDon't bet alone! We’ve cracked today’s best Football matches into one high-value Accumulator bet. This is your chance for a huge, fast win.\n\n* Overall Odds: 5.196 (Boosted!)\n* 4 Hand-Picked Selections\n* First Match Kicks Off at 3:00 PM (Nigerian Time)!\n\nStop studying. Start winning. This bet slip is guaranteed value.\n\nCLAIM THIS ACCUMULATOR NOW: 👇\nhttps://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=line/basketball", "images": ["262.png"]},

{"date": "2026-01-02", "time": "15:00", "content": "👑 BOXING DAY CHAOS CONTINUES! DEC 27 TOP PICKS! 🚀\n\nYour lucky day is here! Forget the rest, this is the action that matters. We've hand-picked the 3 games that will PRINT you money. Get ready for a winning Thursday!\n\n🗓️ BIG MATCHES (Nigerian Time, GMT+1):\n\n- AFCON (11:00 AM): 🇲🇦 Morocco vs. Mali 🇲🇱\n    - Our Pick: The Lions of Atlas Win!\n- PREMIER LEAGUE (3:30 PM): 🌳 Nott'm Forest vs. Man City 🏙️\n    - Our Pick: Goals, Goals, Goals (Over 2.5)!\n- PREMIER LEAGUE (7:00 PM): 🔴 Man United vs. Newcastle ⚫️\n    - Our Pick: Both Teams Will Score in the Showdown!\n\nSTOP WAITING. YOUR WINS ARE SCHEDULED. PLAY NOW! 👇\nhttps://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=line/football", "images": ["271.png"]},
{"date": "2026-01-02", "time": "23:00", "content": "⭐ UNLOCK THE NEXT LEVEL! Your 3rd Deposit Comes with a HUGE 75% Bonus!\n\nWe're fueling your play with a substantial boost on your third deposit. Don't miss out on this incredible value:\n\n🎉 Get a massive 75% Match Bonus on your 3rd deposit!\n💰 Claim up to $500 FREE!\n📈 Elevate your bankroll and chase those bigger wins.\n\n👇 JUMP STRAIGHT TO THE ACTION 👇\nHOTTEST GAMES: https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration\n\n🌐 Explore the Casino Lobby: https://fortunobet.com", "images": ["272.png"]},

{"date": "2026-01-03", "time": "23:00", "content": "💥 NEVER LOSE AGAIN! 💥\n\nPlace your 7+ leg accumulator. MISS ONE? GET 100% REFUND!\n\nIt's time to bet BIG with ZERO fear. Your safety net is LIVE.\n\n---\n\n🛡️ CLAIM YOUR REFUND SHIELD NOW! 🛡️\nGET REGISTERED NOW:https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration\n\n🌐 Official Partner Site: https://fortunobet.com", "images": ["282.png"]},
{"date": "2026-01-29", "time": "15:00", "content": "🚀 200% WELCOME BONUS! 🚀\n\nSTOP leaving money on the table.\n\nWe'll TRIPLE your bankroll instantly with a 200% Welcome Bonus! (e.g., Deposit $100 -> Get $300).\n\nYour biggest winning streak starts NOW. Don't miss out.\n\n---\n\n⚡ GET YOUR 200% BONUS! ⬇️\nhttps://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration\n\n🌐 Official Partner Site: https://fortunobet.com", "images": ["291.png"]},

{"date": "2025-12-30", "time": "23:00", "content": "💰 STOP! FREE MONEY ALERT! 💰\n\nYour MelBet bonuses on FortunoBet are unlocked! Grab up to 20% NFL Cash, 3% Weekly Sports Cashback (0x Wagering!), and massive Deposit Matches.\n\nWhy bet without a bonus? Claim your rewards NOW!\n\nYOUR BONUS ROUTE: 👇\nhttps://fortunobet.com/com/bonuses", "images": ["242.png"]},
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




