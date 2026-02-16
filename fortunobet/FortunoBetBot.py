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

# MONDAY
# 14:00 — Register & Deposit Guide (VALUE)
# 23:00 — Welcome Bonus (HYPE)

# TUESDAY  
# 14:00 — Withdrawal Guide (VALUE)
# 23:00 — Deposit Bonus (HYPE)

# WEDNESDAY
# 14:00 — How to Bet Example (VALUE)
# 23:00 — Sports Bonus (HYPE)

# THURSDAY
# 14:00 — Safe Betting Tips (VALUE)  
# 23:00 — Reload Bonus (HYPE)

# FRIDAY
# 15:00 — Weekend Betting Guide (VALUE)
# 23:30 — Weekend Bonus (HYPE)

# SATURDAY
# 13:00 — Live Bet Example (VALUE)
# 22:00 — Hot Bonus (HYPE)

# SUNDAY
# 14:00 — Withdraw + Tips (VALUE)
# 22:00 — Final Bonus (HYPE)

posts =[
{"date":"2026-02-16","time":"14:00","content":"💰 <b>2nd Deposit = 75% Extra Balance!</b>\n\nDeposit ₦5,000 → Play with ₦8,750\nDeposit ₦20,000 → Play with ₦35,000\n\nMin deposit: ₦1,000 only\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Claim now:</b> https://1wyuds.com/casino/list?open=register&p=cguo","images":["161.png"]},
{"date":"2026-02-16","time":"23:00","content":"🏆 <b>Win $4,700 Cash + iPhone 16 Pro!</b>\n\nBack FC Barcelona tonight\nOne bet = one prize draw ticket\n\n🎟 Tickets from $1.18 only\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Get ticket:</b> https://1wyuds.com/casino/list?open=register&p=cguo","images":["162.png"]},

{"date":"2026-02-17","time":"14:00","content":"⚽ <b>Girona vs Barcelona — LA LIGA BIG ODDS!</b>\n\nBarcelona is hunting the top spot, but Girona is a dangerous underdog at home! 😤\n\n📊 <b>Current Odds:</b>\n🏠 Girona: 6.00\n🤝 Draw: 5.50\n🚀 Barca: 1.40\n\n💰 <b>BIG DEPOSIT VIP BONUS:</b>\nDeposit ₦10,000 ➔ Play with <b>₦60,000</b>\nDeposit ₦50,000 ➔ Play with <b>₦300,000</b>\n\n⚡ <i>Instant withdrawal to Opay, Palmpay & Kuda. No stories!</i>\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Bet & Cashout Now:</b> https://1wkrii.life/v3/landing-page/football?p=5pe0","images":["171.png"]},
{"date":"2026-02-17","time":"23:00","content":"⚽ <b>Big Matches Tonight on 1WIN!</b>\n\nBet on live matches now\nNew players get 500% on first deposit\n\n💰 Deposit 2,000 → Play with 12,000\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Bet now:</b> https://1wkrii.life/v3/landing-page/football?p=5pe0","images":["172.png"]},

{"date":"2026-02-18","time":"14:00","content":"🎄 <b>Sweet Bonanza Xmas — Big Win Slot!</b>\n\nHigh volatility = massive wins\nTumble feature = multiple wins per spin\n\n💰 Deposit 2,000 → Play with 12,000\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Play now:</b> https://1wkrii.life/casino/list?open=register&p=cguo","images":["181.png"]},
{"date":"2026-02-18","time":"23:00","content":"🇳🇬 <b>Deposit & Withdraw in Nigeria — Easy!</b>\n\nOpay | Palmpay | Bank Transfer | USDT\n\n⚡ Deposit in 2 minutes\n⚡ Withdrawal same day\n\n💰 Deposit 2,000 → Play with 12,000\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Start now:</b> https://1wkrii.life/casino/list?open=register&p=cguo","images":["182.png"]},

{"date":"2026-02-19","time":"14:00","content":"🇳🇬 <b>1WIN Nigeria — Double Bonus!</b>\n\n🎁 1WIN: 500% on your deposit\n🎁 FortunoBet: +$3 on your account\n\nDeposit just $5 → get both!\n\n💰 2,000 → 12,000\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Register:</b> https://1wyuds.com/casino/list?open=register&p=cguo","images":["191.png"]},
{"date":"2026-02-20","time":"23:00","content":"🎯 <b>50 Free Bets — Every Single Day!</b>\n\nLogin → claim → bet free\nNo extra deposit needed\n\n💰 Deposit 2,000 → Play with 12,000\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Register:</b> https://1wyuds.com/casino/list?open=register&p=cguo","images":["192.png"]},

{"date":"2026-02-20","time":"15:00","content":"🇳🇬 <b>₦256,000,000 Prize Pool — Join Now!</b>\n\nBiggest draw in Nigeria this week\nOne deposit = one entry\n\n💰 Deposit 2,000 → Play with 12,000\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Join here:</b> https://1wyuds.com/casino/list?open=register&p=cguo","images":["201.png"]},
{"date":"2026-02-20","time":"23:00","content":"💰 <b>New to 1WIN? Here is your bonus!</b>\n\nFirst deposit = instant 500% match\n\n💰 Deposit 2,000 → Play with 12,000\n💰 Deposit 10,000 → Play with 60,000\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Register & claim:</b> https://1wkrii.life/casino/list?open=register&p=cguo","images":["202.png"]},

{"date":"2026-02-21","time":"13:00","content":"💸 <b>Lost today? 1WIN pays you back!</b>\n\nGet up to 30% cashback on losses\nEvery bet protected — win or lose\n\n💰 Deposit 2,000 → Play with 12,000\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Register:</b> https://1wyuds.com/casino/list?open=register&p=cguo","images":["211.png"]},
{"date":"2026-02-21","time":"22:00","content":"🎁 <b>1WIN rewards every deposit!</b>\n\n1st → 100% + 70 Free Spins\n2nd → 120% + 100 Free Spins\n3rd → 130% + 150 Free Spins\n4th → 150% + 180 Free Spins\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Start here:</b> https://1wyuds.com/casino/list?open=register&p=cguo","images":["212.png"]},

{"date":"2026-02-22","time":"14:00","content":"🎰 <b>500 Free Spins — Just for Depositing!</b>\n\n70 spins → 1st deposit\n100 spins → 2nd deposit\n150 spins → 3rd deposit\n180 spins → 4th deposit\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Claim spins:</b> https://1wyuds.com/casino/list?open=register&p=cguo","images":["221.png"]},
{"date":"2026-02-22","time":"22:00","content":"💰 <b>Start with ₦1,000 — Get ₦2,000!</b>\n\nMinimum deposit = ₦1,000 only\nInstant 100% bonus added\n\nPlus 70 Free Spins on top!\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Register now:</b> https://1wyuds.com/casino/list?open=register&p=cguo","images":["222.png"]},

{"date":"2026-02-23","time":"14:00","content":"🇳🇬 <b>Nigeria — Start with just ₦1,000!</b>\n\nDeposit ₦1,000 → Play with ₦2,000\nDeposit ₦5,000 → Play with ₦10,000\n\nBonus added instantly!\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Register:</b> https://1wyuds.com/casino/list?open=register&p=cguo","images":["231.png"]},
{"date":"2026-02-23","time":"23:00","content":"⏰ <b>Welcome Bonus — Limited Time Only!</b>\n\n100% + 70FS on first deposit\nUp to 500% across 4 deposits\n\nNew players only — claim before it ends!\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Register now:</b> https://1wyuds.com/casino/list?open=register&p=cguo","images":["232.png"]},

{"date":"2026-02-24","time":"14:00","content":"🏆 <b>Why 1WIN players keep coming back!</b>\n\n✅ 500% welcome bonus\n✅ 30% cashback on losses\n✅ 50 free bets daily\n✅ Same day withdrawals\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Join today:</b> https://1wyuds.com/casino/list?open=register&p=cguo","images":["241.png"]},

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