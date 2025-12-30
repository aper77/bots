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

{"date":"2025-12-30","time":"15:00","content":"🏆 TUESDAY KNOCKOUT DAY! YOUR CHANCE TO WIN BIG. ⚽ The action is LIVE! We've got massive games today, including a huge London Derby and AFCON giants taking the field. Double your money on the biggest matches with the best odds on FortunoBet!\n\n🔥 TODAY'S TOP PICKS & ODDS:\n* Arsenal vs Palace: London Cup Drama! (Odds: 1.536)\n* Algeria vs Sudan: Mahrez on the hunt! (Algeria Win - Odds: 1.435)\n\n👇 PLACE YOUR BETS NOW! 👇\nBET ON TODAY'S GAMES: https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=line/football\n🌐 Official Site: https://fortunobet.com","images":["301.png"]},
{"date":"2025-12-30","time":"23:00","content":"🏆 UNLOCK ALL THE BONUSES! 🏆 Why choose one when you can have BOTH? FortunoBet has gathered the BEST offers from Melbet and 1xBet in one place. Stop missing out on rewards! Claim every bonus, including:\n* 🎁 Huge Welcome Matches\n* 💸 Daily Free Bets\n* 🛡️ Loyalty Cashback\n* 🎉 Special Casino Rewards\n\nYour rewards are waiting! Join our winning team and claim everything!\n\n👇 YOUR ALL-IN-ONE BONUS HUB IS HERE 👇\nCLAIM BONUSES NOW: https://fortunobet.com/com/bonuses","images":["302.png"]},

{"date":"2025-12-31","time":"15:00","content":"🎁 HAPPY HOLIDAYS, GLOBAL WINNERS! 🎉 The entire FortunoBet family wishes you peace, joy, and GREAT FORTUNE today and throughout the New Year! 🥂 Thank you for placing your trust with us this year. We look forward to celebrating even bigger wins with you in the future!\n\n👇 YOUR TRUSTED HOME FOR WINNINGS 👇\nVISIT US NOW: https://fortunobet.com/com","images":["311.png"]},
{"date":"2025-12-31","time":"23:00","content":"💥 FINAL HOUR: NEW YEAR'S $5 FREE CASH! 🎁 ⏰ ENDS AT MIDNIGHT! If you've registered but haven't made a deposit, FortunoBet has a gift to start your 2026! GET $5 FREE CASH IN 1 MINUTE:\n* Deposit just $3 or more right now.\n* We instantly gift you $5 EXTRA! 💰\nIt's the easiest $5 you will make today. Don't let this New Year's cash bonus expire!\n\n👇 CLAIM YOUR $5 BONUS NOW! 👇\nMELBET REGISTRATION: https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration\n1XBET REGISTRATION: https://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=registration\n🌐 Official Partner Site: https://fortunobet.com","images":["312.png"]},

{"date":"2026-01-01","time":"15:00","content":"🇳🇬 NIGERIA PLAYERS: SIGN UP IN 60 SECONDS! 🚀 Stop wasting time! The fastest way to get your $157 bonus is the 'One-Click' method. It takes less than a minute.\n\n⚡️ ONE-CLICK REGISTRATION GUIDE:\n1. CLICK HERE: Tap the link below (opens One-Click form).\n2. CODE! Enter Promo Code: 1x_4023125 (REQUIRED for max bonus).\n3. CONFIRM: Ensure NGN is selected. Hit 'REGISTER' to get your instant login.\n4. DEPOSIT: Fund your account and claim your $157 Welcome Bonus!\n\nDO IT NOW! YOUR ACCOUNT IS WAITING. 👇\nhttps://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=bonus/rules/1st\n\n(Powered by Fortunobet: https://www.fortunobet.com/com)","images":["011.png"]},
{"date":"2026-01-01","time":"23:00","content":"🔥 LATE NIGHT DEPOSIT: FREE CASH + FREE SPINS! 🔥 It's still New Year's Day! If you grabbed the first bonus, Melbet's Second Gift is waiting to double your fun before midnight!\n\nGET YOUR 2ND GIFT:\n* 50% BONUS: More funds for tonight's games!\n* 40 FREE SPINS: Hit a quick New Year's jackpot!\n\nEnd Day 1 as a winner! Claim your extra cash and spins instantly.\n\n👇 CLAIM YOUR MELBET REWARD! 👇\nGET BONUS HERE: https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration\n🌐 FortunoBet Promotions: https://fortunobet.com","images":["012.png"]},

{"date":"2026-01-02","time":"15:00","content":"💰 FORGET NEW YEAR'S RESOLUTIONS—START WITH NEW YEAR'S PROFITS! Stop guessing and start winning! We've done the work, analyzing all the data to bring you 3 GUARANTEED WINNERS for January 2nd. This is your chance to turn a small stake into a major payday!\n\n🔥 YOUR JANUARY 2ND WINNING TREBLE:\n* AFCON (11:00 AM): 🇲🇦 Morocco vs. Mali 🇲🇱 -> The Lions of Atlas Win!\n* Premier League (3:30 PM): 🌳 Nott'm Forest vs. Man City 🏙️ -> OVER 2.5 Goals!\n* Premier League (7:00 PM): 🔴 Man United vs. Newcastle ⚫️ -> Both Teams To Score!\n\nReady to cash out today?\n\nDon't wait! Click below and lock in your bets with confidence: 👇\nhttps://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=line/football\n\n(Powered by Fortunobet: https://www.fortunobet.com/com)","images":["021.png"]},
{"date":"2026-01-02","time":"23:00","content":"🚨 FREE CASH ALERT: 1XBET DOUBLES YOUR MONEY! 🚨 It's Friday! Deposit anything today and 1XBET instantly DOUBLES IT up to €300! Fuel your weekend bets with the house's money.\n\nMAX REWARD, MINIMUM WAGERING (x3). 24 HOURS ONLY!\n\nDOUBLE YOUR BANKROLL NOW! 👇\nhttps://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=promotions/lucky-friday\n\n(Powered by Fortunobet: https://www.fortunobet.com/com)","images":["022.png"]},

{"date":"2026-01-03","time":"15:00","content":"💰 STOP PAYING. 1XBET GIVES YOU $157 FREE! 🚀 NEW PLAYER WARNING! 1XBET instantly DOUBLES your first deposit 100% up to a massive $157! Start with twice the money.\n\nMinimum effort, maximum reward: Wager only 5X in accumulators to cash out.\n\nCLAIM YOUR FREE CASH AND CRUSH THE BOOKIES! 👇\nhttps://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=bonus/rules/1st\n\n(Powered by Fortunobet: https://www.fortunobet.com/com)","images":["031.png"]},
{"date":"2026-01-03","time":"23:00","content":"🚀 200% WELCOME BONUS! 🚀 STOP leaving money on the table. We'll TRIPLE your bankroll instantly with a 200% Welcome Bonus! (e.g., Deposit $100 -> Get $300).\n\nYour biggest winning streak starts NOW. Don't miss out.\n\n⚡ GET YOUR 200% BONUS! ⬇️\nhttps://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration\n\n🌐 Official Partner Site: https://fortunobet.com","images":["032.png"]},

{"date":"2026-01-04","time":"15:00","content":"🎁 $100,000 CASH GIVEAWAY IS LIVE! 💰 Happy New Year! Start 2026 by entering the biggest draw of the season. The Santa's Gift Draw gives you tickets toward a massive cash prize.\n\nSimply bet to win:\n* Prize: $100,000 CASH! (Plus amazing Tech!)\n* Get tickets by betting on sports or casino games today.\n\nWill you be our New Year millionaire? Claim your tickets now!\n\n👇 CLAIM FREE DRAW TICKETS HERE! 👇\nBONUS PAGE (1XBET): https://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=promotions/santas-gift\n🌐 FortunoBet Promotions: https://fortunobet.com","images":["041.png"]},
{"date":"2026-01-04","time":"23:00","content":"🎉 $5 FREE CASH GIFT: NEW YEAR'S COUNTDOWN! ⏳ URGENT: OFFER ENDS MIDNIGHT (23:59) TODAY! Did you sign up but not deposit? Fortunobet has partnered with 1XBET and MELBET to give you $5 FREE just for making a tiny first deposit.\n\n✅ HOW TO CLAIM YOUR $5 GIFT (1-MINUTE GUIDE):\n* 1. DEPOSIT: Fund your account with just $3 or more on *either* partner site below.\n* 2. REWARD: Fortunobet instantly sends you $5 EXTRA CASH! (Net Profit: $2!)\n* 3. MORE BONUSES: Once you're in, unlock countless other bonuses!\n\n👇 CLICK & DEPOSIT TO GET YOUR $5 NOW!\nMELBET: https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration\n1XBET: https://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=registration","images":["042.png"]},
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




