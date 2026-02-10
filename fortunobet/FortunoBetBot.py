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
{"date":"2026-02-09","time":"09:00","content":"👑 <b>PORTO vs SPORTING: DERBY DAY!</b> 🇵🇹\n🎁 <b>$8 FREE GIFT</b> for all players today!\n\n💰 <b>500% BONUS</b> + Weekly Cashback added!\n🛡 <b>RISK-FREE:</b> Win or get your money back! 💸\n⚡️ <b>FAST PAY:</b> OPay / M-Pesa (Instant)\n\n👇 <b>CLAIM YOUR $8 GIFT NOW:</b>\n👉 https://1wpgwj.live/betting?open=register&p=y627\n\n🎁 Promo: <code>fortunobet</code>","images":["5bonus.jpeg"]},
{"date":"2026-02-09","time":"21:00","content":"💰 <b>FREE MONEY: +500% BONUS</b> 💰\n\n💵 <b>PAY 2,000 ➜ GET 12,000</b>\n💵 <b>PAY 10,000 ➜ GET 60,000</b>\n\n🔑 <b>PROMO CODE:</b> <code>fortunobet</code>\n\n🚀 <b>CASH OUT INSTANTLY</b>\n👉 https://1whenu.com/v3/aggressive-casino?p=xomk","images":["092.png"]},

{"date":"2026-02-10","time":"15:00","content":"🐯 <b>FORTUNE TIGER: 500% HACK!</b> 🐯\n\n💰 <b>DEPOSIT 2,000 ➜ GET 12,000</b>\n💰 <b>DEPOSIT 10,000 ➜ GET 60,000</b>\n\n🔥 <b>The Tiger is giving BIG today!</b> \n🎁 <b>BONUS CODE:</b> <code>fortunobet</code>\n\n👇 <b>CLICK TO PLAY & WITHDRAW</b>\n👉 https://1wyuds.com/v3/fortune-tiger?p=69vl","images":["101.png"]},
{"date":"2026-02-10","time":"21:00","content":"🎨 <b>COLOR PREDICTION HACK: 500%</b> 🎨\n\n🔴 <b>RED</b> or ⚫️ <b>BLACK</b>?\n<b>1 WIN</b> is paying out <b>+500%</b> + <b>70 FREE SPINS!</b>\n\n💰 <b>PAY 2,000 ➜ GET 12,000</b>\n💰 <b>PAY 10,000 ➜ GET 60,000</b>\n\n🔑 <b>PROMO CODE:</b> <code>fortunobet</code>\n\n👇 <b>GUESS & WITHDRAW NOW</b>\n👉 https://1wyuds.com/v3/4540/color-prediction?p=xo3e","images":["102.png"]},

{"date":"2026-02-11","time":"15:00","content":"🫧 <b>BUBBLES GLITCH: +500% CASH</b> 🫧\n\n💰 <b>POP THE BUBBLE — WIN BIG!</b>\n<b>1WIN</b> is boosted! Get <b>500% BONUS</b> instantly.\n\n💵 <b>PAY 2,000 ➜ GET 12,000</b>\n💵 <b>PAY 10,000 ➜ GET 60,000</b>\n\n🔑 <b>PROMO CODE:</b> <code>fortunobet</code>\n\n👇 <b>TAP TO POP & WITHDRAW</b>\n👉 https://1wyuds.com/v3/5840/game-bubble-regform?p=1a5s","images":["111.png"]},
{"date":"2026-02-11","time":"21:00","content":"👑 <b>BIG CHANCE: 99% WIN RATE</b> 👑\n\n🔥 <b>DAILY SAFE GAMES ARE LIVE!</b>\nOur experts updated the <b>\"Big Chance\"</b> list. High winning probability—Low risk!\n\n💰 <b>PROFIT HACK:</b>\nUse code <code>fortunobet</code> for <b>+500% BONUS</b>\n<b>Pay 2,000 ➜ Get 12,000 to Bet!</b>\n\n👇 <b>GET TODAY'S SAFE WINS</b>\n👉 https://fortunobet.com/com/sports","images":["112.png"]},

{"date":"2026-02-12","time":"14:00","content":"🇳🇬 <b>1WIN NIGERIA: ₦1,000,000 BONUS!</b> 🇳🇬\n\n🚀 <b>FAST REGISTER — INSTANT WITHDRAW</b>\nGet <b>+500%</b> on your first deposit!\n\n💰 <b>PAY ₦2,000 ➜ GET ₦12,000</b>\n💰 <b>PAY ₦10,000 ➜ GET ₦60,000</b>\n\n🔑 <b>PROMO CODE:</b> <code>fortunobet</code>\n\n👇 <b>REGISTER & CLAIM BONUS</b>\n👉 https://1wyuds.com/casino/list?open=register&p=cguo","images":["121.png"]},
{"date":"2026-02-12","time":"21:00","content":"🚀 <b>FRIDAY NIGHT GLITCH: +500% ACTIVE</b> 🚀\n\n💰 <b>DEPOSIT ₦2,000 ➜ GET ₦12,000</b>\n💰 <b>DEPOSIT ₦10,000 ➜ GET ₦60,000</b>\n\n🔥 <b>BIG CHANCE</b> games are peaking tonight! \nDon't sleep—the Tiger is giving and the Odds are high!\n\n🎁 <b>BONUS CODE:</b> <code>fortunobet</code>\n(Valid for the next 5 hours only! ⏳)\n\n👇 <b>START YOUR WEEKEND WITH A WIN</b>\n👉 https://1wyuds.com/casino/list?open=register&p=cguo","images":["122.png"]},

{"date":"2026-02-13","time":"15:00","content":"⚡ <b>1WIN NIGERIA: INSTANT DEPOSIT</b> ⚡\n\n💰 <b>NO DELAYS! START PLAYING NOW</b>\nDeposit in 30 seconds using your favorite apps:\n\n🔸 <b>OPAY</b> (Instant)\n🔹 <b>PALMPAY</b> (Fast)\n🔸 <b>BANK TRANSFER</b> (Secure)\n\n🎁 <b>BONUS:</b> Use code <code>fortunobet</code> for <b>+500% BONUS!</b>\n<b>Pay ₦2,000 ➜ Get ₦12,000 instantly!</b>\n\n👇 <b>DEPOSIT & PLAY NOW</b>\n👉 https://1wyuds.com/casino/list?open=register&p=cguo","images":["131.png"]},
{"date":"2026-02-13","time":"21:00","content":"🇳🇬 <b>FAST REGISTER: 1-CLICK ACCESS</b> 🇳🇬\n\n🎁 <b>YOUR ₦1,000,000 WELCOME PACK IS READY!</b>\nRegister in 10 seconds and claim your <b>+500% BONUS</b> immediately.\n\n✅ <b>NO LONG FORMS</b>\n✅ <b>INSTANT ACCOUNT</b>\n✅ <b>AUTO-BONUS ACTIVE</b>\n\n💰 <b>PROMO CODE:</b> <code>fortunobet</code>\n\n👇 <b>REGISTER & GET YOUR 500% BONUS</b>\n👉 https://1wyuds.com/casino/list?open=register&p=cguo","images":["132.png"]},

{"date":"2026-02-14","time":"15:00","content":"💎 <b>1WIN VIP ACCESS: +500% ACTIVE</b> 💎\n\n🔥 <b>THE BIGGEST PAYOUT IN NIGERIA!</b>\nOur system is boosted today. Join <b>14,500+</b> players winning right now!\n\n💰 <b>INVEST ₦2,000 ➜ GET ₦12,000</b>\n💰 <b>INVEST ₦10,000 ➜ GET ₦60,000</b>\n\n⚡ <b>FASTEST WITHDRAWAL (OPAY/PALMPAY)</b>\n\n🔑 <b>PROMO CODE:</b> <code>fortunobet</code>\n\n👇 <b>REGISTER & CLAIM YOUR FORTUNE</b>\n👉 https://1wyuds.com/casino/list?open=register&p=cguo","images":["141.png"]},
{"date":"2026-02-14","time":"20:45","content":"🍭 <b>SWEET BONANZA: 100x BOMBS ACTIVE!</b> 🍭\n\n🔥 <b>WIN 21,000x YOUR BET!</b>\nThe glitch is live—one spin, huge profit!\n\n💰 <b>PROFIT:</b> Pay ₦2,000 ➜ Get ₦12,000\n🎁 <b>CODE:</b> <code>fortunobet</code> (+500% Bonus)\n\n👇 <b>CLICK TO SPIN & WIN NOW</b>\n👉 https://1wyuds.com/casino/list?open=register&p=cguo","images":["142.png"]},

{"date":"2026-02-15","time":"14:45","content":"💰 <b>DOUBLE YOUR MONEY — START WITH $1!</b> 💰\n\n🎁 <b>100% BONUS ACTIVE</b>\nDeposit <b>$1</b> ➜ Play with <b>$2</b>\nDeposit <b>$130</b> ➜ Play with <b>$260</b>\n\n✅ <b>EASY 5X WAGER</b>\n✅ <b>INSTANT CASHOUT</b>\n\n🔑 <b>CODE:</b> <code>fortunobet</code>\n\n👇 <b>CLAIM YOUR BONUS NOW</b>\n👉 https://1wyuds.com/casino/list?open=register&p=cguo","images":["151.png"]},
{"date":"2026-02-15","time":"20:59","content":"💰 <b>DOUBLE YOUR MONEY — START WITH $1.10!</b> 💰\n\n🎁 <b>100% FIRST DEPOSIT BONUS ACTIVE</b>\nDeposit <b>$1.10</b> ➜ Play with <b>$2.20</b>\nDeposit <b>$157</b> ➜ Play with <b>$314</b>\n\n✅ <b>EASY 5X WAGER</b>\n✅ <b>INSTANT CASHOUT</b>\n✅ <b>30 DAYS TIME LIMIT</b>\n\n🔑 <b>CODE:</b> <code>fortunobet</code>\n\n👇 <b>CLAIM YOUR BONUS NOW</b>\n👉 https://1wyuds.com/casino/list?open=register&p=cguo","images":["152.png"]},

{"date":"2026-02-16","time":"14:15","content":"🥈 <b>GET 75% EXTRA CASH – 2ND DEPOSIT!</b> 🥈\n\nDon't stop now! Boost your next deposit and keep winning big. 💸\n\n💰 <b>Deposit $20 ➜ Play with $35</b>\n💰 <b>Deposit $134 ➜ Play with $234</b>\n\n✅ <b>5X WAGER (Easy!)</b>\n✅ <b>INSTANT CASH OUT</b>\n✅ <b>MIN DEPOSIT: $5</b>\n\n👇 <b>GRAB YOUR BONUS BEFORE IT EXPIRES</b>\n👉 https://1wyuds.com/casino/list?open=register&p=cguo","images":["161.png"]},
{"date":"2026-02-16","time":"20:25","content":"💙❤️ <b>WIN $4,700 CASH + iPHONE 17 PRO MAX!</b> ❤️💙\n\nSupport <b>FC Barcelona</b> and win big! Just one bet gets you a ticket to the massive prize draw. 🏆\n\n💰 <b>$4,700 GRAND PRIZE</b>\n📱 <b>iPhones, PS5 Pros & More</b>\n🎟 <b>Tickets from only $1.18!</b>\n\n👇 <b>GET YOUR WINNING TICKET:</b>\n👉 https://1wyuds.com/casino/list?open=register&p=cguo","images":["barca_short_3d.png"]},

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