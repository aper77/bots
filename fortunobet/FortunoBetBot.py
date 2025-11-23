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
  "date": "2025-11-21",
  "time": "20:00",
  "content": "🎰 UNLOCK THE MAGIC OF 9 MASKS OF VOODOO! 🎰\n\nReady to spin and WIN BIG? Here’s how to play smart and maximize your chances in this mystical slot adventure!\n\n🌀 **How to Play:**\n1. Set your bet according to your bankroll — start small and increase wisely.\n2. Watch for the special VOODOO MASK symbols — they trigger FREE SPINS!\n3. Activate BONUS rounds whenever possible — that’s where the BIG wins hide!\n\n💡 **Pro Tips:**\n- Always spin with patience — don’t chase losses.\n- Check the paytable to know the highest paying symbols.\n- Use free demo spins to practice before betting real money.\n\n👉 Play 9 Masks of Voodoo here:\nhttps://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=slot/9masksofvoodoo\n\n💥 Dive into the magic, spin wisely, and let the Voodoo masks bring you fortune! 🍀💰\n\n#SlotsTips #VoodooWins #BigWins #SpinAndWin",
  "images": ["9mas.png"]
},
{
  "date": "2025-11-22",
  "time": "12:04",
  "content": "🔥🏆 FORTUNOBET SATURDAY MEGA ACCA! 🏆🔥\n\n4-Leg High-Value Slip:\n1️⃣ Liverpool vs Nottm Forest – Liverpool Win & Over 2.5\n2️⃣ Bayern vs Freiburg – Bayern Win\n3️⃣ Barcelona vs Bilbao – BTTS (YES)\n4️⃣ Burnley vs Chelsea – Chelsea Win\n\n💰 Total Odds: ~6.10\nBet ₦10,000 / KES 1,000 → Win ₦61,000 / KES 6,100!\n\n⏳ First kick-off: 5:30 PM AST!\n\n👇 Load the slip:\nhttps://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=line/football\n\nFortunoBet:\nhttps://fortunobet.com",
  "images": ["221.png"]
},
  {
    "date": "2025-11-22",
    "time": "16:00",
    "content": "🔥💰 DOUBLE YOUR MONEY & INSURE YOUR BET! 🛡️\nWatching the games? It's time to join FortunoBet and claim the best Welcome Offer in Kenya & Nigeria!\n\nNew players get an UNBEATABLE two-part deal:\n\n1️⃣ **100% FIRST DEPOSIT MATCH!**\n    * We double your money up to **$130!**\n    * Deposit ₦15,000, get ₦30,000 to bet!\n    * Deposit KES 3,000, get KES 6,000 to bet!\n\n2️⃣ **FREE ACCUMULATOR INSURANCE!**\n    * Place a 7-leg Acca: If only ONE selection loses, you get **100% OF YOUR STAKE REFUNDED!** (No more painful near-misses!)\n\nStop watching with zero stakes! Start betting with **double your money** and **no fear of losing** your weekend slip!\n\n⬇️ **SIGN UP NOW to Claim BOTH OFFERS!** ⬇️\nhttps://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration\n\n➡️ Visit FortunoBet (Main Site):\nhttps://fortunobet.com",
    "images": ["222.png"]
  },
  {
    "date": "2025-11-22",
    "time": "21:00",
    "content": "🐷 **GOOD MORNING! Time to Check-In & Get Lucky!** 💰\nWe all need a bit of weekend luck, and today we’re trusting the richest piggies around: **Piggy Cash Hold and Win!**\n\nThis slot is built on trust, fun, and easy winning mechanics!\n\n✅ **TRUST FACTOR: The Piggy Promise!**\n* The game is fair, fun, and designed for excitement. No complicated rules, just pure spin-and-win action.\n\n🌟 **HOW TO WIN BIG:**\nThe magic is in the **Hold and Win** feature!\n1. Land 6 or more Money Symbols to lock them in place.\n2. You get **Re-spins** to fill the screen with CASH!\n3. Fill all 15 spots to win the **INCREDIBLE JACKPOT!**\n\n🗓️ **DAILY REMINDER: Don't Forget Your Check-IN!**\nMake it a habit! Log into FortunoBet every day to catch your latest bonuses, free spins, and rewards. Consistency is key to winning!\n\n👉 **Play Piggy Cash & Check-In Here:**\nhttps://fortunobet.com/com",
    "images": ["223.png"]
  },
  {
    "date": "2025-11-23",
    "time": "13:24",
  "content": "✨🦌 **TONIGHT'S GOLDEN ENERGY: RISE LIKE THE WILD HERD!** 🦌✨\n\nReady for a thrilling adventure of focus and momentum? Channel the strength of the mighty Goldhorn and push toward your goals!\n\n🌟 **HOW TO LEVEL UP TONIGHT:**\n1. Pick one goal and lock in.\n2. Build momentum with small steps.\n3. Stay consistent — progress grows fast once you start.\n\n💡 **Pro Tip:**\nMomentum is powerful. Once you catch it, let it carry you forward!\n\n⬇️ **Check it out here:**\nhttps://fortunobet.com/com",
    "images": ["231.png"]
  },
  {
    "date": "2025-11-23",
    "time": "16:00",
  "content": "🏆⚽ **SUNDAY FOOTBALL HIGHLIGHTS!** ⚽🏆\n\nFootball action across Europe today! Here are four exciting matches to follow:\n\n🌟 **MATCH SPOTLIGHT:**\n1. 🇫🇷 **Paris Saint-Germain** vs Le Havre\n   ➡️ *PSG are strong at home — watch for an energetic game.*\n2. 🇪🇸 **Real Betis** vs Girona\n   ➡️ *Betis look solid and consistent this season.*\n3. 🇮🇹 **Lazio** vs Lecce\n   ➡️ *Lazio have home advantage and key players to watch.*\n4. 🇪🇸 **Getafe** vs Atletico Madrid\n   ➡️ *Atletico bring strong defense and exciting plays.*\n\n⏳ **Kick-off times coming up — don’t miss the action!** ⏳\n\n⬇️ **Follow the matches here:**\nhttps://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=line/football\n\n➡️ **Visit FortunoBet for more info:**\nhttps://fortunobet.com",
    "images": ["232.png"]
  },
  {
    "date": "2025-11-23",
    "time": "20:00",
  "content": "⚡️ **FINAL CALL! EXCLUSIVE WEEKEND OPPORTUNITY!** ⚡️\n\nCheck out some exciting updates and special content for the end of the weekend!\n\n**✅ QUICK START:**\nDiscover new features and tools with minimal effort — jump in and explore!\n\n**🎁 SPECIAL WEEKEND REWARDS:**\nUnlock exclusive content and surprises when you check the links below:\n\n1️⃣ **Exclusive Content Access**\n2️⃣ **Special Tips & Updates**\n3️⃣ **All Weekend Highlights in One Place**\n\n⭐ **YOUR WEEKEND CODE:**\n🔥 **ML_1577703** 🔥\n\n**HOW TO ACCESS:**\n1. Tap the link below.\n2. Enter the code **ML_1577703** to unlock the content.\n3. Enjoy the special updates and surprises!\n\n⏳ **DON'T MISS OUT! Check it now!** ⏳\n\n⬇️ **ACCESS HERE:**\nhttps://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration\n\n➡️ **Visit FortunoBet:**\nhttps://fortunobet.com",
    "images": ["233.png"]
  }
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




