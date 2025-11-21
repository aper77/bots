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
  "time": "11:00",
  "content": "🔥🏆 FORTUNOBET SATURDAY MEGA ACCUMULATOR! 🏆🔥\nThe biggest weekend of football is here! Load this 4-Match slip NOW for a HUGE potential payout! Don't miss the kick-offs!\n\n💰 THE HIGH-VALUE 4-LEG SLIP:\n1. 🏴󠁧󠁢󠁥󠁮󠁧󠁿 **Liverpool** vs Nottm Forest: **Liverpool Win & Over 2.5 Goals**\n   ➡️ *Tipster Note: Liverpool is clinical at home, expecting a comfortable 3-1 or 4-1 scoreline.*\n2. 🇩🇪 **Bayern Munich** vs Freiburg: **Bayern to Win (1)**\n   ➡️ *Tipster Note: Bayern is unstoppable and needs to protect their league lead. A strong home win is guaranteed.*\n3. 🇪🇸 **Barcelona** vs Athletic Bilbao: **Both Teams To Score (BTTS) - YES**\n   ➡️ *Tipster Note: Bilbao is in great scoring form, and Barça's defense has been shaky. Expect goals at both ends!* \n4. 🏴󠁧󠁢󠁥󠁮󠁧󠁿 Burnley vs **Chelsea**: **Chelsea to Win**\n   ➡️ *Tipster Note: Chelsea MUST win to climb the table. They have the quality to beat Burnley.*\n\nTOTAL ACCUMULATOR ODDS: **Approx. 6.10** 🚀\nBet ₦10,000 / KES 1,000 and WIN over **₦61,000 / KES 6,100!**\n\n⏳ **DON'T WAIT! First Match Kicks Off at 5:30 PM AST!** ⏳\nTap the link below to load this winning slip instantly and place your bet!\n\n⬇️ **LOCK IN YOUR WIN (Direct to Football Section):** ⬇️\nhttps://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=line/football\n\n➡️ **(Check out the main site here: FortunoBet)**\nhttps://fortunobet.com",
  "images": ["22-1.png"]
},
{
  "date": "2025-11-22",
  "time": "16:00",
  "content": "🔥💰 DOUBLE YOUR MONEY & INSURE YOUR BET! 🛡️\nWatching the games? It's time to join FortunoBet and claim the best Welcome Offer in Kenya & Nigeria!\n\nNew players get an UNBEATABLE two-part deal:\n\n1️⃣ **100% FIRST DEPOSIT MATCH!**\n    * We double your money up to **$130!**\n    * Deposit ₦15,000, get ₦30,000 to bet!\n    * Deposit KES 3,000, get KES 6,000 to bet!\n\n2️⃣ **FREE ACCUMULATOR INSURANCE!**\n    * Place a 7-leg Acca: If only ONE selection loses, you get **100% OF YOUR STAKE REFUNDED!** (No more painful near-misses!)\n\nStop watching with zero stakes! Start betting with **double your money** and **no fear of losing** your weekend slip!\n\n⬇️ **SIGN UP NOW to Claim BOTH OFFERS!** ⬇️\nhttps://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration\n\n➡️ Visit FortunoBet (Main Site):\nhttps://fortunobet.com",
  "images": ["22-2.png"]
},
{
  "date": "2025-11-22",
  "time": "21:00",
  "content": "🐷 **GOOD MORNING! Time to Check-In & Get Lucky!** 💰\nWe all need a bit of weekend luck, and today we’re trusting the richest piggies around: **Piggy Cash Hold and Win!**\n\nThis slot is built on trust, fun, and easy winning mechanics!\n\n✅ **TRUST FACTOR: The Piggy Promise!**\n* The game is fair, fun, and designed for excitement. No complicated rules, just pure spin-and-win action.\n\n🌟 **HOW TO WIN BIG:**\nThe magic is in the **Hold and Win** feature!\n1. Land 6 or more Money Symbols to lock them in place.\n2. You get **Re-spins** to fill the screen with CASH!\n3. Fill all 15 spots to win the **INCREDIBLE JACKPOT!**\n\n🗓️ **DAILY REMINDER: Don't Forget Your Check-IN!**\nMake it a habit! Log into FortunoBet every day to catch your latest bonuses, free spins, and rewards. Consistency is key to winning!\n\n👉 **Play Piggy Cash & Check-In Here:**\nhttps://fortunobet.com/com",
  "images": ["22-3.png"]
},
 {
  "date": "2025-11-23",
  "time": "11:00",
  "content": "✨🦌 **TONIGHT'S GOLDEN OPPORTUNITY: GOLDHORN WILD HERD!** 🦌✨\n\nReady for a thrilling adventure with the majestic Goldhorn? This Barbara Bang slot is packed with features for HUGE wins, and we'll show you how to chase them!\n\n✅ **TRUST FACTOR: Barbara Bang Quality!**\n* Known for engaging slots with fair play and big payout potential. This game is built for excitement and trust.\n\n🌟 **HOW TO PLAY FOR BIG WINS:**\n1. **Wild Herd Feature:** Watch for the golden deer! When Wilds land, they can expand and trigger re-spins, leading to massive combinations.\n2. **Free Spins Multipliers:** Aim for the Scatter symbols to unlock the Free Spins round, where every win can be multiplied for epic payouts.\n3. **Bet Strategy:** Start with a comfortable bet and consider increasing it during a winning streak, but always play responsibly!\n\n💡 **Pro Tip:**\n* The Expanding Wilds are your best friend here! Focus on landing them to trigger the re-spins and fill your screen with golden prizes!\n\n⬇️ **PLAY GOLDHORN WILD HERD & WIN BIG TONIGHT!** ⬇️\nhttps://fortunobet.com/com\n",
  "images": ["23-1.png"]
},
{
  "date": "2025-11-23",
  "time": "16:00",
  "content": "🏆💰 **SUNDAY'S LAST CHANCE ACCUMULATOR!** 💰🏆\n\nFootball is still delivering HUGE payouts! We have selected four high-confidence wins across Europe for you to load NOW before the evening games begin.\n\n💰 THE WINNING 4-LEG SLIP:\n1. 🇫🇷 **Paris Saint-Germain** vs Le Havre: **PSG Win & Over 2.5 Goals**\n   ➡️ *Tipster Note: PSG is highly dominant at home and should score at least three goals comfortably.*\n2. 🇪🇸 **Real Betis** vs Girona: **Real Betis Win (1)** \n   ➡️ *Tipster Note: Betis is strong and consistent at home. This is a must-win fixture for their European hopes.*\n3. 🇮🇹 **Lazio** vs Lecce: **Lazio Win (1)**\n   ➡️ *Tipster Note: Lazio has the quality and home advantage to handle this mid-table side with ease.*\n4. 🇪🇸 Getafe vs **Atletico Madrid**: **Atletico Madrid Win (2)**\n   ➡️ *Tipster Note: Atletico is defensively solid and superior in quality. They are banking three points here.*\n\nTOTAL ACCUMULATOR ODDS: **Approx. 6.86** 🚀\nBet ₦10,000 / KES 1,000 and WIN over **₦68,600 / KES 6,860!**\n\n⏳ **LOCK IN NOW! These Games Kick Off Soon!** ⏳\n\n⬇️ **LOAD THE SLIP HERE (Direct to Football Section):** ⬇️\nhttps://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=line/football\n\n➡️ (Visit FortunoBet):\nhttps://fortunobet.com",
  "images": ["23-2.png"]
},
{
  "date": "2025-11-23",
  "time": "20:00",
  "content": "⚡️ **FINAL CALL! LOWEST DEPOSIT, BIGGEST BONUS!** ⚡️\n\nWe’ve partnered with FortunoBet to bring our clients the most flexible and rewarding sign-up offer for the end of the weekend!\n\n**✅ THE $3 HOOK:**\nOur players can start betting with a minimum deposit of just **$3** (or local currency equivalent)! Risk almost nothing and start winning immediately.\n\n**🎁 OUR EXCLUSIVE BONUS STACK (Must Use Code!):**\nWhen you register, use our special partner promo code to unlock THREE offers:\n\n1️⃣ **100% Match up to $130!** Double your money for free!\n2️⃣ **Accumulator Insurance:** Get your stake back if only one leg loses!\n3️⃣ **Access to all FortunoBet bonuses!**\n\n⭐ **YOUR EXCLUSIVE PROMO CODE:**\n🔥 **ML_1577703** 🔥\n\n**HOW TO CLAIM:**\n1. Tap the link below to register.\n2. **Type in the Promo Code ML_1577703** during sign-up.\n3. Make a first deposit (minimum $3) and your bonus is credited instantly!\n\n⏳ **DON'T MISS THE DEADLINE! CLAIM YOUR $3 DEPOSIT DEAL NOW!** ⏳\n\n⬇️ **REGISTER & USE CODE:**\nhttps://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration\n\n➡️ **Visit FortunoBet:**\nhttps://fortunobet.com\n",
  "images": ["23-3.png"]
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




