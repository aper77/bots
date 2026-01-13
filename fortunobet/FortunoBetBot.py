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
{"date":"2026-01-14","time":"10:30","content":"🚨 URGENT: YOUR BALANCE IS ABOUT TO DOUBLE! 🚨\n\nStop betting with half a bankroll!\nFortunoBet (powered by 1xBet) has unlocked the Friday Reload. Deposit now and get the official 1xBet 100% bonus up to €300 💰\n\n🔥 THE POWER DEAL:\n✅ Deposit €300 ➡️ Play with €600\n✅ Valid for EVERY FortunoBet user today\n✅ Low x3 wagering – faster withdrawals\n\n⚠️ Offer expires at midnight. Miss it and lose free money.\n\n🌐 FortunoBet Official Website:\nfortunobet.com\n\n🚀 Activate Bonus Now:\nhttps://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=registration","images":["141.jpg"]},
{"date":"2026-01-14","time":"21:00","content":"🛡️ NO MORE DEPOSIT WORRIES – FORTUNOBET HAS YOUR BACK! 🛡️\n\nTired of betting sites that ignore you? At FortunoBet, you get bonuses + 24/7 VIP PROTECTION.\n\n⚡️ THE FORTUNOBET GUARANTEE:\n✅ Instant resolution: Bet problem? We fix it.\n✅ Fast-track deposits: Your money, no delays.\n✅ VIP partner access: Direct support via 1xBet & MelBet.\n\n💎 VIP TREATMENT: Issues solved in minutes, not days.\n\n🎁 CLAIM YOUR BONUSES:\n💎 MelBet: https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=1599&r=registration\n💎 1xBet: https://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=registration\n\n🌍 Official Site / 24/7 Support: fortunobet.com\n\n🚀 REGISTER & GET PROTECTED NOW!","images":["142.jpg"]},

{"date":"2026-01-15","time":"10:30","content":"🚨 STOP SCROLLING! DOUBLE YOUR MONEY NOW! 🚨\n\nDon’t bet with half a bankroll. FortunoBet + MelBet are giving 100% MATCH BONUSES to every new player today 💰\n\n💎 EXCLUSIVE DEAL:\n✅ Deposit $130 → Play with $260\n✅ Instant credit — play immediately\n✅ Best odds guaranteed for all 2026 matches\n\n⚠️ Limited to first 100 players today — don’t miss out!\n\n🌐 Official Site: fortunobet.com\n\n🚀 CLAIM YOUR $130 BONUS NOW: https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration","images":["151.png"]},
{"date":"2026-01-15","time":"21:00","content":"✨ STOP EVERYTHING – STARBURST IS PAYING OUT BIG! ✨\n\nExperience the legendary 1xBet STARBURST (NetEnt) – the most explosive slot in the world! FortunoBet users are hitting massive wins right now.\n\n💎 WHY PLAY STARBURST TODAY?\n✅ Wild Respins – watch the stars expand for huge wins\n✅ Both Ways Pay – win from left to right AND right to left\n✅ High RTP – constant action and frequent payouts\n\n🚀 Pro Tip: Use your Welcome Bonus to get FREE SPINS and turn small bets into a galaxy of cash!\n\n🌐 Official Website: fortunobet.com\n\n🎰 PLAY STARBURST DIRECTLY HERE: https://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=slots/game/123199/1xbet-starburst","images":["152.jpg"]},

{"date":"2026-01-16","time":"10:30","content":"💰 THE WINNING DOESN'T STOP! GET 75% EXTRA ON YOUR 2ND DEPOSIT! 💰\n\nFinished your first bonus? FortunoBet keeps the cash flowing! We are adding a MASSIVE 75% bonus to your second deposit.\n\n🔥 RELOAD POWER:\n✅ Deposit $100 → Play with $175\n✅ Keep the profit — use extra funds for bigger bets\n✅ No limits — valid for all sports and events\n\n🚀 Pro tip: Smart players never bet without a bonus. Grab your second boost before the big games start!\n\n🌐 Official Website: fortunobet.com\n\n🚀 ACTIVATE YOUR 2ND BONUS NOW: https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration","images":["161.jpg"]},
{"date":"2026-01-16","time":"21:00","content":"🍭 SWEET BONANZA 1000 IS BLOWING UP – 1,000x MULTIPLIERS! 🍭\n\nThe world's favorite candy slot just got SUPERCHARGED! FortunoBet players are hitting the 25,000x Max Win right now — are you next?\n\n🔥 WHY PLAY SWEET BONANZA 1000?\n✅ Huge Multipliers – 1,000x bombs in bonus round\n✅ Max Win – up to 25,000x your stake\n✅ Buy Bonus – jump straight into Free Spins\n\n💰 Cash out big — turn a small bet into a mountain of sugar!\n\n🌐 Official Website: fortunobet.com\n\n🎰 PLAY SWEET BONANZA 1000 NOW: https://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=slots/game/95425/sweet-bonanza-1000","images":["162.png"]},

{"date":"2026-01-17","time":"10:30","content":"🎁 LAST CHANCE: WIN A MACBOOK OR SHARE OF $100,000! 🎁\n\nThe 1xBet 'Santa’s Gift' is reaching its peak at FortunoBet! We are giving away Apple MacBooks, iPhone 17s, and massive cash prizes right now.\n\n🔥 THE WEEKEND STEAL:\n✅ Every bet earns you tickets to the SUPERPRIZE draw\n✅ Win high-tech gadgets: MacBook Air M4 & Samsung S25 Ultra\n✅ Guaranteed bonuses just for collecting 'candies' and 'lollipops'\n\n⚠️ THE CLOCK IS TICKING! Don't let the weekend end without your share of the $100,000 prize pool. Play now or watch someone else win!\n\n🌐 Official Website: https://fortunobet.com/com\n\n🚀 ENTER THE $100,000 DRAW NOW: https://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=promotions/santas-gift","images":["171.png"]},
{"date":"2026-01-17","time":"21:00","content":"💎 UNLOCK THE $38,180 EPIC DEPOSIT SERIES! 💎\n\nStop playing for small change. FortunoBet has unlocked the ultimate MelBet series where you can claim a total of $38,180 in bonuses across your deposits!\n\n⚡️ THE EPIC BREAKDOWN:\n✅ Huge Match Bonuses on your 1st, 2nd, 3rd, and 4th deposits\n✅ Maximum rewards for weekend high-rollers\n✅ Instant VIP status for all series participants\n\n🚀 Your journey to the $38K jackpot starts with one click. Are you ready to play like a pro?\n\n🌐 OFFICIAL WEBSITE: https://fortunobet.com/com\n\n🚀 START THE EPIC SERIES NOW: https://refpa3365.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration","images":["172.png"]},
 
{"date":"2026-01-18","time":"10:30","content":"🥂 SUNDAY VIP TREAT: 50% BONUS + 100 FREE SPINS! 🥂\n\nFinish the weekend as a winner! FortunoBet and MelBet are dropping a VIP RELOAD into your account right now. More cash, more spins, more wins!\n\n🔥 THE VIP BUNDLE:\n✅ 50% EXTRA CASH on your Sunday deposit\n✅ 100 FREE SPINS on the top-paying slots\n✅ Faster weekend withdrawals for all VIPs\n\n🎰 Hunt those multipliers today! This offer is valid for 24 hours only. Don't leave your spins on the table!\n\n🌐 OFFICIAL WEBSITE: https://fortunobet.com/com\n\n🚀 CLAIM YOUR SUNDAY VIP TREAT: https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration","images":["181.png"]},
{"date":"2026-01-18","time":"21:00","content":"🛡️ BET ON THE BIG GAMES WITH 100% PROTECTION! 🛡️\n\nTired of losing on a last-minute goal? FortunoBet and 1xBet have your back with the 'NO RISK BET' guarantee for this weekend's top matches!\n\n💎 HOW IT WORKS:\n✅ Place a 'Correct Score' bet on the featured match\n✅ If your bet loses, you get a 100% REFUND as a Free Bet\n✅ Zero risk. Pure profit potential.\n\n💰 Why sweat the result? With FortunoBet, even if you lose, you win your money back to try again!\n\n🌐 OFFICIAL WEBSITE: https://fortunobet.com/com\n\n🚀 PLACE YOUR RISK-FREE BET: https://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=promotions/no-risk-bet","images":["182.png"]},

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




