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
  "date": "2025-11-30",
  "time": "12:00",
  "content": "🛑 STOP SCROLLING! 🛑 You're about to miss the easiest way to double your money this Sunday.\n\nNew players at Fortunobet get a massive 100% Match Bonus on their first deposit, instantly boosting your bankroll up to $100!\n\nWhy Join Today?\n\n✅ 100% Match: Get up to $100 FREE when you deposit.\n✅ Double Play: Deposit $50, play with $100!\n✅ Simple & Fast: Claim the bonus right after registration.\n\nReady to play smart? Click to register now!\n\n⬇️ PLAY SMART NOW! ⬇️\n\nRegister Here:https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration\nVisit Fortunobet:🌐 https://fortunobet.com",
  "images": ["301.jpeg"]
},
{
  "date": "2025-11-30",
  "time": "20:00",
  "content": "🤯 STOP SCROLLING! HUGE 9.37 ODD ACCA IS LIVE! 🤯\n\nDon't bet alone this Sunday. We've hand-picked the best games from the Premier League and La Liga to deliver a single accumulator that multiplies your stake by over 9 times!\n\n🏆 4-STEP WINNING STRATEGY:\n* ✅ Tottenham (1) vs. Fulham\n* ✅ Atletico Madrid (1) vs. Real Oviedo\n* ✅ Liverpool (2) vs. West Ham\n* ✅ Aston Villa vs. Wolves: OVER 2.5 Goals\n\nThe Combined Odd is an insane 9.37!\n\nClick the link now to place this bet and cash in on the biggest matches of the weekend!\n\n⬇️ PLACE THE ACCA NOW! ⬇️\n\nPlace Bet Here:https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=line/football\nVisit Fortunobet:🌐 https://fortunobet.com",
  "images": ["302.jpg"]
},
  {
    "date": "2025-12-01",
    "time": "12:00",
    "content": "👑 CONQUER MONDAY! 100% DEPOSIT BONUS! 👑\n\nStart your week with a serious bankroll boost! Deposit any amount today and Fortunobet will DOUBLE IT with a 100% Match Bonus!\n\nHow to Claim Your Monday Boost:\n* 🚀 100% Match: Get up to the maximum bonus allowed by the casino!\n* ✅ Easy Deposit: The bonus is applied automatically upon deposit.\n* 📅 Today Only: This royal treatment is exclusive to Mondays!\n\nDon't face the week empty-handed. Claim your free cash now!\n\n⬇️ CLICK & DOUBLE YOUR MONDAY CASH!\nhttps://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration\n\n🌐 Official Website: https://fortunobet.com\n\n#MondayBonus #100PercentMatch #Fortunobet\n\nWhat game are you celebrating the start of the week with?",
    "images": ["011.jpg"]
  },
  {
    "date": "2025-12-01",
    "time": "20:00",
    "content": "💸 STOP SLOTTING! START SMASHING FOR X7777! 💸\n\nDiscover TAPINATA—the addictive clicker game from Turbo Games where every tap can lead to a massive win! This game features a Heat-Up Bar that increases your chance to hit the ultimate x7777 multiplier!\n\n🎯 BIG WIN STRATEGY:\n\n💰 Goal: Smash the pinata and collect instant cash wins (multipliers up to x10).\n🤯 Bonus Buy: Use the Bonus Buy feature to jump straight to Free Spins with multipliers boosted up to x70!\n⭐ Max Multiplier: Keep tapping to fill the Heat-Up Bar and chase the jackpot of up to x7777!\n\nWe have MORE great 'Crash' style games like Tapinata! Click now and see what you can smash!\n\n⬇️ SMASH YOUR WAY TO CASH NOW! ⬇️\n\nPlay Tapinata Here:https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration\n🌐 Official Website: https://fortunobet.com",
    "images": ["012.webp"]
  },
    {
    "date": "2025-12-02",
    "time": "16:26",
    "content": "🤯 STOP SCROLLING! $38,180 CASINO CASH IS WAITING! 💎\n\nYour rewards don't stop after the first deposit! Fortunobet has an Epic Deposit Series that offers incredible bonuses on your 2nd, 3rd, and 4th deposits, totaling up to $38,180 in bonus funds!\n\n💰 WHY KEEP DEPOSITING?\n* 🚀 $38,180 Max: The largest bonus pool available for loyal players.\n* 🥈 2nd Deposit: Claim a high-value match bonus.\n* 🥉 3rd & 4th: Keep boosting your balance with every funding round.\n\nLevel up your play and claim your share of this massive bonus pool today!\n\n⬇️ CLAIM YOUR NEXT BONUS NOW!\nhttps://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration\n\n🌐 Official Website: https://fortunobet.com",
    "images": ["021.png"]
  },
   {
    "date": "2025-12-02",
    "time": "20:00",
    "content": "👑 BECOME THE SPIN QUEEN! 🤑 Uncover the secrets to big wins in Mancala Gaming's exciting slot!\n\nSpin Queen isn't just beautiful—it's packed with features designed to pay out! Learn how to best play to unlock massive rewards and rule the reels!\n\n🎯 YOUR WINNING STRATEGY:\n* ✨ Wild Queens: The Spin Queen herself is WILD! Land her for huge substitution wins across paylines.\n* 💎 Scatter Rewards: Look for the Gem Scatter! 3 or more trigger the coveted FREE SPINS round.\n* 📈 Multipliers: During Free Spins, watch those multipliers soar! This is where your biggest payouts happen.\n* 🔄 Re-Spins: Special symbols can trigger re-spins for even more chances at big combinations!\n\nReady to take your throne and spin for glory?\n\n⬇️ PLAY SPIN QUEEN & WIN! ⬇️\n\nPlay Spin Queen Here:https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration\n🌐 Official Website: https://fortunobet.com",
    "images": ["022.jpg"]
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




