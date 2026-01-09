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
{"date":"2026-01-06","time":"21:00","content":"🎰 MEGA WIN ALERT! Spinomenal's Demi Gods V is LIVE! 💰🔥\nSTOP WASTING TIME! Free Spins and massive MULTIPLIERS are ready to explode your wins!\n\n3 SIMPLE STEPS TO PLAY & WIN:\n1. SIGN UP in ONE-CLICK — start instantly!\n2. TRIGGER FREE SPINS — the bigger the spins, the bigger the MULTIPLIERS!\n3. SPIN & WIN BIG — don’t miss out on today’s top slots action!\n\nDO IT NOW! YOUR ACCOUNT IS WAITING.\n\n👇 Play here: https://fortunobet.com/com","images":["062.png"]},

{"date":"2026-01-07","time":"10:30","content":"🎯 FRIDAY JACKPOT ALERT! 1XBET doubles your money! 💰🔥\nDON’T MISS OUT! Urgent accumulator bets for maximum bonus!\n\n3 SIMPLE STEPS TO CLAIM YOUR BONUS:\n1. SIGN UP in ONE-CLICK — fast & secure!\n2. DEPOSIT to trigger your 100% Reload Bonus — bigger bets, bigger wins!\n3. START PLAYING & WIN BIG — Friday’s jackpot is waiting!\n\nACT NOW! YOUR BONUS WON’T WAIT!\n\n👇 Play here: https://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=line/football","images":["071.png"]},
{"date":"2026-01-07","time":"21:00","content":"🎰 HUGE WIN ALERT! Sweet Bonanza 1000 is upgraded! 💰🔥\nDON’T WAIT! Buy the bonus for a massive 100X multiplier and spin for huge payouts!\n\n3 EASY STEPS TO PLAY & WIN:\n1. SIGN UP in ONE-CLICK — start instantly!\n2. BUY THE BONUS — unlock your 100X multiplier chance!\n3. SPIN & WIN BIG — huge payouts are ready!\n\nDO IT NOW! YOUR ACCOUNT IS WAITING.\n\n👇 Play here: https://fortunobet.com/com","images":["072.png"]},

{"date":"2026-01-08","time":"10:30","content":"🔥 CRUSH THE BOOKIES! 1XBET delivers the BEST ODDS! 💰⚡\nDON’T MISS OUT! Massive markets for instant, biggest payouts!\n\n3 SIMPLE STEPS TO WIN:\n1. SIGN UP in ONE-CLICK — fast & secure!\n2. PLACE YOUR BET — pick your markets for maximum payout!\n3. WIN BIG — your massive betting slip is waiting!\n\nACT NOW! BIG WINS WON’T WAIT!\n\n👇 Play here: https://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=line/football","images":["081.png"]},
{"date":"2026-01-08","time":"21:00","content":"⚡ STOP LOSING VALUE! MelBet gives you the WINNING EDGE! 💰🔥\nACT FAST! 1,500+ markets daily to secure your bets and maximize payouts!\n\n3 EASY STEPS TO PLAY & WIN:\n1. SIGN UP in ONE-CLICK — instant access!\n2. PICK YOUR MARKETS — football bets for maximum profit!\n3. WIN BIG — your daily advantage is ready!\n\nDO IT NOW! YOUR ACCOUNT WON’T WAIT!\n\n👇 Register here: https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration","images":["082.png"]},

{"date":"2026-01-09","time":"10:30","content":"💥 WEEKEND JACKPOT! 1XBET doubles your deposit! 💰🔥\nHURRY! 100% Reload Bonus is live — claim your FREE 300 EUR betting cash now!\n\n3 SIMPLE STEPS TO CLAIM & WIN:\n1. SIGN UP in ONE-CLICK — instant access!\n2. DEPOSIT to trigger your 100% Reload Bonus — bigger bets, bigger payouts!\n3. PLAY & WIN — weekend jackpots are waiting!\n\nDO IT NOW! YOUR BONUS WON’T WAIT!\n\n👇 Claim here: https://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=line/football","images":["091.png"]},
{"date":"2026-01-09","time":"21:00","content":"🎰 GET 100 FREE SPINS NOW! MelBet Friday VIP Treat! 💰🔥\nACT FAST! 50% Friday VIP bonus is live — claim your free casino spins immediately!\n\n3 SIMPLE STEPS TO PLAY & WIN:\n1. SIGN UP in ONE-CLICK — instant access!\n2. ACTIVATE YOUR VIP TREAT — 100 free spins ready!\n3. SPIN & WIN BIG — don’t miss today’s huge casino payouts!\n\nDO IT NOW! YOUR FREE SPINS WON’T WAIT!\n\n👇 Claim here: https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration","images":["092.png"]},

{"date":"2026-01-10","time":"10:30","content":"🎰 COINSPIN FEVER – A SMART JACKPOT SLOT ON MELBET 💰\n\nStill spinning random slots and hoping for luck? CoinSpin Fever is built differently. This game is designed for players who want real jackpot potential, not empty spins.\n\n💡 Why CoinSpin Fever Stands Out:\n✅ Hold & Spin Feature – Lock special symbols and respin for explosive payouts.\n✅ Massive 5000X Potential – One strong bonus round can change your balance instantly.\n✅ Fast & High-Action Gameplay – Pure jackpot hunting.\n\n🎯 Smart Way to Play (Pro Tip):\n• Use balanced bets to stay in the game until Hold & Spin triggers\n• Early special symbols often signal a strong session\n• Let the bonus rounds play out – patience is rewarded\n\nThis is not a spin-and-pray slot. It’s a strategy-based game built for serious wins.\n\n👇 PLAY COINSPIN FEVER ON MELBET NOW:\nhttps://fortunobet.com/com\n\n🌐 Explore more jackpot slots in the Casino Lobby\nWhat’s the biggest multiplier you’ve ever hit? 👇","images":["101.png"]},
{"date":"2026-01-10","time":"21:00","content":"🎰 SWEET BONANZA XMAS – WHY PLAYERS CHASE THIS MULTIPLIER MONSTER 💰\n\nSweet Bonanza Xmas is not a normal slot. This game is famous for sudden explosions of multipliers and massive Free Spins payouts when the bonus hits.\n\n💡 Why Sweet Bonanza Xmas Is Special:\n✅ Free Spins Feature – Where the real money drops\n✅ 100X Multiplier Potential – One spin can turn small bets into big wins\n✅ Buy Bonus Option – Skip the wait and jump straight into action\n\n🎯 Smart Play Tip:\n• Use steady bets or Buy Bonus if bankroll allows\n• Multipliers stack fast during Free Spins — patience pays\n• High volatility means fewer wins, but much bigger payouts\n\nThis slot rewards timing and discipline, not blind spinning.\n\n👇 PLAY SWEET BONANZA XMAS NOW:\nhttps://fortunobet.com/com\n\n🌐 Explore more high-multiplier slots in the Casino Lobby\nWhat’s the biggest multiplier you’ve ever hit? 👇","images":["102.png"]},

{"date":"2026-01-11","time":"10:30","content":"🎉 1XBET $100,000 NEW YEAR GIVEAWAY – HERE’S HOW SMART PLAYERS ENTER 💰\n\n1xBet is running a massive $100,000 New Year prize draw, and players can join simply by placing regular bets. No extra cost, no complicated rules — just play and earn free tickets automatically.\n\n💡 Why This Giveaway Is Worth Joining:\n✅ $100,000 Total Prize Pool – One draw can change everything\n✅ Free Tickets for Real Bets – You don’t need to buy anything extra\n✅ Trusted Platform – 1xBet is a global sportsbook with huge markets\n\n🎯 Smart Way to Enter:\n• Place your normal bets to collect free draw tickets\n• The more active you are, the more chances you earn\n• Don’t wait until the last minute — entries close fast\n\nThis is one of those promos where you play as usual and get a real chance at a life-changing prize.\n\n👇 ENTER THE $100,000 GIVEAWAY NOW:\nhttps://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=promotions/santas-gift\n\n⏰ Hurry — the draw closes soon\nWould you rather win the jackpot or daily profits? 👇","images":["041.png"]},
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




