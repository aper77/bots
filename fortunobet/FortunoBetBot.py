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
{"date":"2026-02-03","time":"21:20","content":"⚽ MELBET SMART START: 2.20 ODDS TARGET 🎯\n\n🔥 The Plan: Single matches only. High probability. No chasing losses.\n\n💰 Payouts: Instant to M-Pesa or Bank.\n\n🎁 BONUS: 100% up to 150,000 NGN / 15,000 KES\n\n👇 ACTIVATE BONUS BEFORE KICKOFF\n👉 https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration","images":["032.png"]},

{"date":"2026-02-04","time":"15:00","content":"🏆 BARCELONA IN DANGER? 🇪🇸\n\n🔥 Match: Albacete vs Barcelona\n🚀 Strategy: Skip the 1.20 odds. The real value is BTTS (Both Teams to Score).\n\n💰 Payouts: Fast & Instant withdrawals.\n\n🎁 BONUS: 100% up to 150,000 NGN / 15,000 KES\n\n👇 CLAIM BONUS & VIEW PICK\n👉 https://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=registration","images":["041.jpg"]},
{"date":"2026-02-04","time":"21:00","content":"🏆 BARCELONA: RISK-FREE BET? 🇪🇸\n\n🔥 Match: Albacete vs Barcelona\n🛡️ Strategy: I use Correct Score Insurance. If the score is wrong, I get a FREE BET refund!\n\n💰 Payouts: Fast M-Pesa & OPay withdrawals.\n\n🎁 BONUS: 100% up to 150,000 NGN / 20,000 KES\n\n👇 GET YOUR INSURANCE & BONUS NOW\n👉 https://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=registration","images":["042.png"]},

{"date":"2026-02-05","time":"15:00","content":"🔥 MAN CITY vs NEWCASTLE: SEMI-FINAL 🏴󠁧󠁢󠁥󠁮󠁧󠁿\n\n🚀 Haaland vs The Magpies! \n🛡️ Strategy: Correct Score Insurance — if we miss the score, we get a FREE BET refund. No risk today.\n\n💰 Payouts: Instant OPay & M-Pesa withdrawals.\n\n🎁 BONUS: 100% up to 150,000 NGN / 20,000 KES\n\n👇 SECURE YOUR FREE BET REFUND\n👉 https://refpa58144.com/L?tag=d_4681275m_1599c_&site=4681275&ad=1599&r=registration","images":["051.png"]},
{"date":"2026-02-05","time":"21:00","content":"🚀 MELBET MEGA BONUS: 300% DEPOSIT MATCH 💰\n\n💎 The Strategy: I use this 300% bonus to triple my capital immediately. Play smart, grow steady, and protect your bankroll.\n\n💰 Withdrawals: Instant cashouts via OPay & M-Pesa.\n\n🎁 MEGA OFFER: 300% Bonus up to 180,000 NGN / 26,000 KES\n\n👇 CLAIM YOUR SIGN-UP GIFT NOW\n👉 https://refpa3665.com/L?tag=d_4681277m_2170c_&site=4681277&ad=2170&r=registration","images":["052.png"]},

{"date":"2026-02-05","time":"23:55","content":"💎 <b>1WIN x FORTUNOBET</b> 💎\n\n🚀 <b>500% BONUS ON YOUR DEPOSITS!</b>\nTurn ₦1,000 into ₦6,000 or 1,000 KES into 6,000 KES instantly!\n\n✅ Aviator, Football & Casino\n✅ 30% Weekly Cashback\n✅ Instant M-Pesa & OPay\n\n🔑 <b>PROMO CODE:</b> <code>fortunobet</code>\n*(Tap code to copy)*\n\n👇 <b>REGISTER & CLAIM BONUS</b>\n👉 https://1wpgwj.live/casino/list?open=register&p=cguo","images":["063.jpeg"]},
{"date":"2026-02-06","time":"14:00","content":"💎 <b>HOW TO JOIN 1WIN (STEP-BY-STEP)</b> 💎\n\n1️⃣ <b>CLICK OFFICIAL LINK</b>\n👉 https://1wpgwj.live/casino/list?open=register&p=cguo\n\n2️⃣ Select <b>\"Quick Registration\"</b>\n\n3️⃣ Enter your <b>Phone Number</b> & <b>Email</b>\n\n4️⃣ Click the blue <b>\"+\"</b> button next to <b>\"Add Promo Code\"</b>\n\n5️⃣ Type the Code: <code>fortunobet</code> \n*(Must use this code for the 500% Bonus!)*\n\n6️⃣ Click <b>\"Register\"</b> and you are ready!\n\n💰 <b>Min Deposit:</b> ₦500 / 100 KES\n💸 <b>Withdrawal:</b> Instant OPay / M-Pesa\n\n🔑 <b>PROMO CODE:</b> <code>fortunobet</code> \n*(Tap the code to copy it)*\n\n👇 <b>REGISTER HERE</b>\n👉 https://1wpgwj.live/casino/list?open=register&p=cguo","images":["062.png"]},
{"date":"2026-02-06","time":"21:00","content":"💰 <b>1WIN: FAST CASH & NO FEES</b> 🇳🇬🇰🇪\n\nThe easiest way to deposit and withdraw in Africa!\n\n🇳🇬 <b>NIGERIA:</b> Instant <b>OPay, PalmPay & Bank</b>.\n🇰🇪 <b>KENYA:</b> Instant <b>M-Pesa & Airtel</b>.\n\n🚀 <b>BENEFITS:</b>\n✅ <b>Min Deposit:</b> ₦500 / 150 KES\n✅ <b>Withdrawal:</b> Instant (0-45 mins)\n✅ <b>500% Bonus:</b> On your first 4 deposits!\n\n🔑 <b>PROMO CODE:</b> <code>fortunobet</code>\n*(Tap to copy code)*\n\n👇 <b>REGISTER & CASH OUT FAST</b>\n👉 https://1wpgwj.live/casino/list?open=register&p=cguo","images":["064.png"]},

{"date":"2026-02-07","time":"12:00","content":"🚀 <b>MAN UTD vs TOTTENHAM: OLD TRAFFORD</b> 🔴⚪️\n\n🔥 <b>Game of the Week!</b> \n🚀 <b>Strategy:</b> Skip the straight win. Both Teams to Score (BTTS) is the smart play for disciplined growth.\n\n💰 <b>Withdrawals:</b> Instant payouts to <b>M-Pesa / OPay</b>.\n\n🎁 <b>BONUS:</b> 500% Welcome Gift for all new players!\n\n🔑 <b>PROMO CODE:</b> <code>fortunobet</code>\n*(Tap to copy code)*\n\n👇 <b>SECURE YOUR BONUS BEFORE KICKOFF</b>\n👉 https://1wpgwj.live/betting?open=register&p=y627","images":["071.png"]},
{"date":"2026-02-07","time":"17:30","content":"🎡 <b>1WIN LUCKY WHEEL: €5,000 JACKPOT!</b> 🎁\n\n🚀 <b>Saturday Craziness:</b> I’m spinning for the €5,000 cash prize today. \n🛡️ <b>Strategy:</b> I play the Barcelona vs Mallorca match to earn my free entries. Stay smart, win steady.\n\n💰 <b>Withdrawals:</b> Fast as a Ferrari to <b>M-Pesa / OPay</b>.\n\n🎁 <b>MEGA BONUS:</b> Spin the Wheel + 500% Deposit Bonus!\n\n🔑 <b>PROMO CODE:</b> <code>fortunobet</code>\n*(Tap to copy code)*\n\n👇 <b>TAP TO SPIN & CLAIM YOUR JACKPOT</b>\n👉 https://1wpgwj.live/v3/4540/color-prediction?p=xo3e","images":["061.png"]},

{"date":"2026-02-08","time":"14:00","content":"🔥 <b>LIVERPOOL vs MAN CITY: THE TITLE WAR!</b> 🏆\n\n🚀 <b>Anfield Clash: Salah vs Haaland!</b> \n🛡️ <b>Strategy:</b> I use Correct Score Insurance for this battle. If the score is wrong, I get a FREE BET refund. No risk, just smart play.\n\n💰 <b>Withdrawals:</b> Instant payouts to <b>OPay / M-Pesa</b>.\n\n🎁 <b>MEGA BONUS:</b> 500% Welcome Bonus for all new players!\n\n🔑 <b>PROMO CODE:</b> <code>fortunobet</code>\n*(Tap to copy code)*\n\n👇 <b>SECURE YOUR RISK-FREE BET NOW</b>\n👉 https://1wpgwj.live/betting?open=register&p=y627","images":["081.png"]},
{"date":"2026-02-08","time":"19:00","content":"🏈 <b>SUPER BOWL 60: THE ULTIMATE WAR!</b> 🇺🇸\n\n🔥 <b>Patriots vs Seahawks: The legendary rematch!</b> \n🛡️ <b>Strategy:</b> I’m playing with 3% Weekly Cashback tonight. Win or lose, you get a money-back refund automatically. Smart growth only.\n\n💰 <b>Withdrawals:</b> Fast & Priority processing for the Big Game via <b>M-Pesa / OPay</b>.\n\n🎁 <b>MEGA BONUS:</b> 500% Welcome Gift + 3% Weekly Cashback!\n\n🔑 <b>PROMO CODE:</b> <code>fortunobet</code>\n*(Tap to copy code)*\n\n👇 <b>SECURE YOUR CASHBACK BEFORE KICKOFF</b>\n👉 https://1wpgwj.live/v3/aggressive-casino?p=xomk","images":["082.png"]},

{"date":"2026-02-09","time":"09:00","content":"👑 <b>ROYAL MONDAY: $8 BONUS + DERBY DAY!</b> 🎁\n\n🔥 <b>Porto vs Sporting CP: The Battle for 1st Place!</b>\n\n🚀 <b>Strategy:</b> This is a high-stakes Derby. I use the $8 Free Gift to play it safe and grow my bankroll with zero risk.\n\n💰 <b>Payouts:</b> Guaranteed safe & official withdrawals via <b>M-Pesa / OPay</b>.\n\n🎁 <b>ROYAL GIFT:</b> 500% Welcome Bonus + Weekly Cashback!\n\n🔑 <b>PROMO CODE:</b> <code>fortunobet</code>\n*(Tap the code to copy it)*\n\n👇 <b>CLAIM YOUR DERBY GIFT NOW</b>\n👉 https://1wpgwj.live/betting?open=register&p=y627","images":["5bonus.jpeg"]},
]

# ====== FUNCTION TO SEND POSTS ======
def send_post(post):
    try:
        # We use HTML mode to support <b>bold</b> and <code>tap-to-copy</code>
        P_MODE = "HTML"

        if "images" in post and post["images"]:
            # If multiple images, send as album
            if len(post["images"]) > 1:
                media_group = []
                for idx, img_file in enumerate(post["images"]):
                    if os.path.exists(img_file):
                        if idx == 0:
                            # Apply HTML formatting to the caption
                            media_group.append(InputMediaPhoto(open(img_file, "rb"), caption=post["content"], parse_mode=P_MODE))
                        else:
                            media_group.append(InputMediaPhoto(open(img_file, "rb")))
                if media_group:
                    bot.send_media_group(chat_id=CHANNEL_ID, media=media_group)
            else:
                # Single image
                img_file = post["images"][0]
                if os.path.exists(img_file):
                    with open(img_file, "rb") as photo:
                        # Apply HTML formatting to the photo caption
                        bot.send_photo(chat_id=CHANNEL_ID, photo=photo, caption=post["content"], parse_mode=P_MODE)
                else:
                    # Fallback to text if image missing
                    bot.send_message(chat_id=CHANNEL_ID, text=post["content"], parse_mode=P_MODE)
        else:
            # Text only
            bot.send_message(chat_id=CHANNEL_ID, text=post["content"], parse_mode=P_MODE)

        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Posted Successfully")
    except Exception as e:
        print(f"Failed to post: {e}")

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