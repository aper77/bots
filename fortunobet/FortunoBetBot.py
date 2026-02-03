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

# Monday

# 15:00 (3:00 PM) — Register & Deposit Guide

# 21:00 (9:00 PM) —  Welcome Bonus

# Tuesday

# 15:00 (3:00 PM) — Withdrawal Guide 

# 21:30 (9:30 PM) —  Deposit Bonus

# Wednesday

# 15:00 (3:00 PM) — How to Bet (Example)

# 21:30 (9:30 PM) — Sports Bonus

# Thursday

# 15:00 (3:00 PM) — Safe Betting Tips

# 21:00 (9:00 PM) — Reload Bonus

# Friday

# 16:00 (4:00 PM) — Weekend Betting Guide

# 22:00 (10:00 PM) — Weekend Bonus

# Saturday

# 13:00 (1:00 PM) — Live Bet Example

# 17:30 (5:30 PM) — Hot Bonus

# Sunday

# 14:00 (2:00 PM) — Withdraw + Tips

# 19:00 (7:00 PM) — Final Bonus

posts =[
{"date":"2026-02-02","time":"15:00","content":"🇳🇬🇰🇪 UDINESE vs ROMA: The Battle of Italy! ⚽\n🔥 Kickoff: 20:45 (NG) / 22:45 (KE). Don't miss the action!\n🦅 Maduka Okoye vs the Roma Giants — Who wins tonight?\n🎁 1XBET EXCLUSIVE: Get your 300% Bonus before kickoff!\n📘 Easy Registration & Instant M-Pesa / OPay Deposits.\n💰 Huge Odds: Roma (2.01) | Draw (3.39) | Udinese (4.47)\n⏰ Time is running out — claim your welcome gift now!\n⚠️ 18+ | Bet Responsibly\n👉 Register & Claim: https://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=registration","images":["021.png"]},
{"date":"2026-02-02","time":"20:00","content":"👑 ROYAL MONDAY MADNESS: 100% RELOAD BONUS! 💰\n🔥 Match Tonight: Udinese vs Roma (Serie A) 🇮🇹\n🚀 Monday special: Deposit now and MelBet will DOUBLE your money!\n🎁 Bonus: 100% up to $100 / 15,000 KES / 150,000 NGN\n📘 How to claim: Deposit via M-Pesa or Instant Bank before midnight!\n💰 Use your extra cash to back Roma at 2.01 odds today!\n⏰ Hurry — this offer disappears at 23:59 tonight! \n⚠️ 18+ | Play Responsibly\n👉 Claim Royal Monday Bonus: https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration","images":["022.png"]},

{"date":"2026-02-03","time":"15:00","content":"🎰 STARBURST SECRET: RAINBOW STRATEGY 💎\n\n🚀 The Trick: Small stakes → Wait for Re-spin → Cash out.\n\n💰 Withdrawal: Instant to M-Pesa/OPay.\n\n🔥 LIMITED: 300% BONUS + FREE SPINS 🎁\n\n👇 TAP TO PLAY NOW (Expires Tonight)\n👉 https://www.fortunobet.com/com","images":["031.png"]},
{"date":"2026-02-03","time":"21:30","content":"⚽ MELBET SMART START: 2.20 ODDS TARGET 🎯\n\n🔥 The Plan: Single matches only. High probability. No chasing losses.\n\n💰 Payouts: Instant to M-Pesa or Bank.\n\n🎁 BONUS: 100% up to 150,000 NGN / 15,000 KES\n\n👇 ACTIVATE BONUS BEFORE KICKOFF\n👉 https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration","images":["032.png"]},

{"date":"2026-02-04","time":"15:00","content":"🏆 BARCELONA IN DANGER? 🇪🇸\n\n🔥 Match: Albacete vs Barcelona\n🚀 Strategy: Skip the 1.20 odds. The real value is BTTS (Both Teams to Score).\n\n💰 Payouts: Fast & Instant withdrawals.\n\n🎁 BONUS: 100% up to 150,000 NGN / 15,000 KES\n\n👇 CLAIM BONUS & VIEW PICK\n👉 https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration","images":["041.jpg"]},
{"date":"2026-02-04","time":"15:00","content":"🏆 BARCELONA: RISK-FREE BET? 🇪🇸\n\n🔥 Match: Albacete vs Barcelona\n🛡️ Strategy: I use Correct Score Insurance. If the score is wrong, I get a FREE BET refund!\n\n💰 Payouts: Fast M-Pesa & OPay withdrawals.\n\n🎁 BONUS: 100% up to 150,000 NGN / 20,000 KES\n\n👇 GET YOUR INSURANCE & BONUS NOW\n👉 https://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=registration","images":["042.png"]},

{"date":"2026-02-05","time":"15:00","content":"🔥 MAN CITY vs NEWCASTLE: SEMI-FINAL 🏴󠁧󠁢󠁥󠁮󠁧󠁿\n\n🚀 Haaland vs The Magpies! \n🛡️ Strategy: Correct Score Insurance — if we miss the score, we get a FREE BET refund. No risk today.\n\n💰 Payouts: Instant OPay & M-Pesa withdrawals.\n\n🎁 BONUS: 100% up to 150,000 NGN / 20,000 KES\n\n👇 SECURE YOUR FREE BET REFUND\n👉 https://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=registration","images":["051.png"]},
{"date":"2026-02-05","time":"21:00","content":"🚀 MELBET MEGA BONUS: 300% DEPOSIT MATCH 💰\n\n💎 The Strategy: I use this 300% bonus to triple my capital immediately. Play smart, grow steady, and protect your bankroll.\n\n💰 Withdrawals: Instant cashouts via OPay & M-Pesa.\n\n🎁 MEGA OFFER: 300% Bonus up to 180,000 NGN / 26,000 KES\n\n👇 CLAIM YOUR SIGN-UP GIFT NOW\n👉 https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration","images":["052.png"]},

{"date":"2026-02-06","time":"16:00","content":"🥂 FRIDAY VIP: WINTER OLYMPICS OPENING 🇮🇹\n\n🎁 The Gift: 50% Cash Bonus + 100 FREE SPINS.\n🚀 Strategy: I use the cash for Olympic Gold bets and the 100 Spins to hunt the Friday Jackpot.\n\n💰 Payouts: Fast & Instant to M-Pesa / OPay.\n\n🔥 VIP TREAT: 100 Spins active for next 500 players!\n\n👇 CLAIM YOUR OLYMPIC GIFT BEFORE MIDNIGHT\n👉 https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration","images":["061.png"]},
{"date":"2026-02-06","time":"22:00","content":"🔥 BETIS vs ATLETICO MADRID: QUARTER-FINAL 🇪🇸\n\n🚀 Huge Match! \n🛡️ Strategy: I play with Weekly Cashback. Win or lose, I get a money-back refund every week. No fear, just growth.\n\n💰 Withdrawals: Instant payouts in 60 seconds to M-Pesa / OPay.\n\n🎁 BONUS: 100% up to 150,000 NGN / 20,000 KES\n\n👇 ACTIVATE YOUR CASHBACK & BONUS\n👉 https://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=registration","images":["062.png"]},

{"date":"2026-02-07","time":"12:00","content":"🚀 MAN UTD vs TOTTENHAM: OLD TRAFFORD 🔴⚪️\n\n🔥 Game of the Week! \n🚀 Strategy: Skip the straight win. Both Teams to Score (BTTS) is the smart play for disciplined growth.\n\n💰 Withdrawals: Instant payouts to M-Pesa / OPay.\n\n🎁 BONUS: 100% up to 150,000 NGN / 20,000 KES\n\n👇 SECURE YOUR BONUS BEFORE EARLY KICKOFF\n👉 https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration","images":["071.png"]},
{"date":"2026-02-07","time":"17:30","content":"🎡 1XBET LUCKY WHEEL: €5,000 JACKPOT! 🎁\n\n🚀 Saturday Craziness: I’m spinning for the €5,000 cash prize today. \n🛡️ Strategy: I play the Barcelona vs Mallorca match to earn my free entries. Stay smart, win steady.\n\n💰 Withdrawals: Fast as a Ferrari to M-Pesa / OPay.\n\n🎁 MEGA BONUS: Spin the Wheel + €3,000 Casino Package!\n\n👇 TAP TO SPIN & CLAIM YOUR JACKPOT\n👉 https://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=registration","images":["072.png"]},

{"date":"2026-02-08","time":"14:00","content":"🔥 LIVERPOOL vs MAN CITY: THE TITLE WAR! 🏆\n\n🚀 Anfield Clash: Salah vs Haaland! \n🛡️ Strategy: I use Correct Score Insurance for this battle. If the score is wrong, I get a FREE BET refund. No risk, just smart play.\n\n💰 Withdrawals: Instant payouts to OPay / M-Pesa.\n\n🎁 MEGA BONUS: 100% up to 150,000 NGN / 20,000 KES\n\n👇 SECURE YOUR RISK-FREE BET NOW\n👉 https://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=registration","images":["081.png"]},
{"date":"2026-02-08","time":"19:00","content":"🏈 SUPER BOWL 60: THE ULTIMATE WAR! 🇺🇸\n\n🔥 Patriots vs Seahawks: The legendary rematch! \n🛡️ Strategy: I’m playing with 3% Weekly Cashback tonight. Win or lose, you get a money-back refund automatically. Smart growth only.\n\n💰 Withdrawals: Fast & Priority processing for the Big Game.\n\n🎁 MEGA BONUS: 100% Match + 3% Weekly Cashback\n\n👇 SECURE YOUR CASHBACK BEFORE KICKOFF\n👉 https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration","images":["082.png"]},

{"date":"2026-02-09","time":"09:00","content":"👑 ROYAL MONDAY: $8 BONUS + DERBY DAY! 🎁\n\n🔥 Porto vs Sporting CP: The Battle for 1st Place!\n🚀 Strategy: This is a high-stakes Derby. I use the $8 Free Gift to play it safe and grow my bankroll with zero risk.\n\n💰 Payouts: Guaranteed safe & official withdrawals via M-Pesa / OPay.\n\n🎁 ROYAL GIFT: $8 FREE ($3 Melbet + $5 Partner Bonus)\n\n👇 CLAIM YOUR DERBY GIFT NOW\n👉 https://www.fortunobet.com/com","images":["5bonus.jpeg"]},]





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




