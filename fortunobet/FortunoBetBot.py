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
  {
  "date": "2025-12-09",
  "time": "12:13",
  "content": "REAL TALK—ARE YOU SITTING ON THE SIDELINES? 🤨💸\n\nI noticed some of the crew signed up for FortunoBet but haven't made a move yet. If you're waiting for a sign, this is it! I reached out to my partner contacts at Fortuno and told them we need to treat our group right.\n\n🔥 THE 'GET STARTED' PUSH:\nIf you’ve registered but haven’t deposited, you are missing out on the tiered Welcome Package that hits $1,750 + 290 Free Spins. That bankroll is sitting there waiting for YOU. \n\nDon't let your account collect dust. We have big games this weekend and the slots are hitting. As your partner here, I’m 24/7 in the chat to make sure your first deposit goes through smooth and fast.\n\n👇 GO FROM REGISTERED TO WINNING:\nhttps://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration\n\n🌐 Check the Bonus Balance here:\nhttps://fortunobet.com\n\nBe free to DM me if you’re having trouble with the deposit—I got you. Let’s get you in the game! 🤜🤛",
  "images": [
    "122.png"
  ]
},
{
  "date": "2025-12-09",
  "time": "20:00",
  "content": "🏆 THE GIANTS ARE COLLIDING TONIGHT! 🏆\n\nAre you ready to turn your football knowledge into cash? The UEFA Champions League is back, and the action is massive! 🇳🇬\n\n⚽️ Bayern Munich vs. Sporting CP\nNigeria Time: 6:45 PM\nBetting Tip: Bayern Home Win (Odds 1.21) — Can the German machine be stopped?\n\n⚽️ Inter Milan vs. Liverpool\nNigeria Time: 9:00 PM\nBetting Tip: Both Teams to Score (Odds 1.60) — Expect a night of pure fireworks!\n\nGet the highest odds and instant payouts today on Fortunobet!\n\n🎯 PLACE YOUR BETS HERE:\n👉 https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=line/football\n\n🌐 VISIT FORTUNOBET:\n👉 https://fortunobet.com",
  "images": [
    "092.jpg"
  ]
},
{
  "date": "2025-12-10",
  "time": "12:00",
  "content": "BRO, DON'T MISS THIS. 😤💰\n\nI’m looking at the board for the weekend and Wednesday’s games, and FortunoBet is literally GIVING money away right now. If you aren't using these two hacks, you’re leaving serious cash on the table.\n\nI don't care if you're a sports guy or a slots addict, listen up:\n\n🔥 HACK #1 (The Safety Net): Building a parlay? Go for 7+ picks. If ONE team lets you down, you get 100% of your money back. It’s a risk-free shot at a massive payday.\n\n🔥 HACK #2 (The Weekly Boost): If you're betting NFL, they are dropping a 20% Weekly Bonus in your account. That’s free betting credit just for playing.\n\nREAL TALK: I’ve been checking their payouts—they are fast, trusted, and legit. Don't be the guy watching everyone else post their winning slips on Sunday. Get your account ready today.\n\nDIRECT LINKS:\n👉 Register Here: https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration\n🌐 Visit Fortunobet: https://fortunobet.com\n\n💸 Let’s get this bread. See you at the top! 🤜🤛",
  "images": ["101.jpg"]
},
{
  "date": "2025-12-10",
  "time": "20:00",
  "content": "🎲 MASTER THE DICE: YOUR PRO STRATEGY TO WIN! 🎲\n\nStop guessing and start winning! Lucky Dice by Pragmatic Play is one of the most exciting games on Fortunobet, but to win big, you need to understand the math. 📈\n\nMaster these 3 Pro Rules to dominate the table:\n\n💎 **Play the Totals:** Totals of **7, 8, and 9** have the highest probability. Betting on middle numbers is the secret to consistent bankroll growth!\n⚖️ **The Small/Big Edge:** Bet on **Small (4-10)** or **Big (11-17)** for a payout that gives you nearly **50% winning odds**—it’s like Roulette but faster!\n🚀 **Smart Multipliers:** Chasing triples pays **180 to 1**, but only allocate **5%** of your bankroll for these risky, high-reward shots.\n\nBuild your strategy, keep your cool, and watch those winning rolls hit the board!\n\n🎯 **REGISTER & PLAY HERE:**\n👉 https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration\n\n🌐 **VISIT FORTUNOBET:**\n👉 https://fortunobet.com",
  "images": [
  "102.jpg"
  ]
},
{
  "date": "2025-12-11",
  "time": "12:00",
  "content": "STOP SCROLLING—THE LOOT IS REAL! 🎁💰\n\nIf you're still waiting for a sign, this is it. While everyone else is waiting for the weekend, my inner circle is already deep in the **Casino Welcome Package.** We are talking about massive bankroll growth here.\n\n🔥 **THE 5-DEPOSIT HACK:**\nFortunoBet is handing out a tiered package that adds up to a staggering **$1,750 + 290 FREE SPINS.** 🎰🔥\n\nI’ve been testing the slots today and the hit rate is insane. Don't leave these spins on the table. You want to walk into the weekend with a loaded account, not an empty pocket.\n\n**REAL TALK:** I don't care if you've never played slots—with 290 free spins, the odds are stacked in YOUR favor. \n\n👇 **CLAIM YOUR 290 SPINS NOW:**\nhttps://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration\n\n🌐 **Browse the Casino:**\nhttps://fortunobet.com\n\n💸 Let’s turn those spins into cold hard cash. See you inside! 🤜🤛",
  "images": [
    "111.png"
  ]
},
{
  "date": "2025-12-11",
  "time": "20:00",
  "content": "WE’VE GOT YOUR BACK, 24/7. 🛡️🤝\n\nBetting with us means you never bet alone. As an official FortunoBet Partner, we don't just give you the best bonuses—we provide a safety net for our players that others simply don't offer.\n\nWhy our circle is growing so fast:\n✅ Direct 24/7 Support: Having trouble? We are here to resolve any issues instantly.\n✅ Exclusive Bonuses: Get access to the $1,750 Welcome Package and 100% Acca Insurance.\n✅ Trusted Payouts: Verified fast withdrawals so you get your wins when you want them.\n\nJoin the family where the player always comes first. Let’s win together.\n\n🌐 Visit FortunoBet:\nhttps://fortunobet.com\n\n*Is there anything you need help with today? Drop a message in the chat, we’re online!* 💬👇", 
  "images": [
  "112.jpeg"
  ]
},
{
  "date": "2025-12-12",
  "time": "12:13",
  "content": "GO BIG OR GO HOME—RISK FREE! 🛡️💰\n\nI’m looking at the board for this weekend’s massive football slate, and FortunoBet is literally GIVING us a safety net. If you aren't building an Acca tonight, you’re missing the easiest win of the month.\n\n🔥 THE WEEKEND HACK:\nBuild a parlay with 7+ picks. If ONE team lets you down, you get **100% OF YOUR MONEY BACK.** One bad apple won't spoil your payout! 🍎❌\n\nREAL TALK: I’ve checked the payouts this week—they are fast and legit. Don't be the guy watching everyone else post their winning slips on Sunday. Get your risk-free slip in right now.\n\n👇 **LOCK IN YOUR INSURANCE HERE:**\nhttps://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration\n\n🌐 **Visit the Platform:**\nhttps://fortunobet.com\n\n💸 Let’s get this bread risk-free. See you at the top! 🤜🤛",
  "images": [
    "121.png"
  ]
},
  {
  "date": "2025-12-12",
  "time": "12:00",
  "content": "🤯 STOP LOSING! WIN MORE on Velvet Games Today! 💡\n\nKnowledge is power! Master the strategies pros use to maximize profits and minimize losses on Velvet Games by Evoplay—it's time to play smarter.\n\nEnter our promo code: ML_1577703 for potential extra rewards!\n\nHere are 3 expert tips to help you secure a win:\n\n* ✅ Money Management: Never chase losses! Set a strict limit and stick to it; consistency beats impulsive betting every time.\n* 📈 Smart Scaling: Start small to find the game's rhythm. Only increase your stake when you are confidently ahead.\n* 🎯 Target Multipliers: Dedicate a specific, safe bankroll to chase those huge X-wins or bonus features—that's where the BIG money is!\n\nStart using these techniques now to build your winning bankroll!\n\n👉 Play Velvet Games & Start Winning! 👇\n\nPlay Velvet Games Here: https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration\n🌐 Official Website: https://fortunobet.com\n\nReady to try these tips? Let us know when you hit that first big win! 🏆",
  "images": [
    "082.png"
  ]
},

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




