import asyncio  # FIXED: Added this missing import
from telegram import Bot, InputMediaPhoto
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime, timedelta
import pytz
import os

# ====== CONFIG ======
BOT_TOKEN = "8758294585:AAGKPOwbpKN1jb8B7KIvUGcM2voJDPz5DPc"
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
{"date":"2026-05-11","time":"12:00","content":"🎾 <b>$100 → $126.00. Felix Auger-Aliassime ✅</b>\n\nATP Madrid. Spain. Clay. Odds 1.26. 🇪🇸\n$26 profit. Auger-Aliassime 6-3, 6-4. Dominated. 💸\n\nRanked higher. Recent form strong. Data was clear.\nMy guy — pure analysis, not luck. They followed. Already paid. ✅\n\nYou dey watch while others dey collect? STOP WATCHING. 🔥\n\nDeposit ₦3,000 → play with ₦18,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>Join NOW:</b> https://1wzpdo.life/v3/aggressive-casino?p=zusb","images":["win1.png"]},
{"date":"2026-05-11","time":"23:55","content":"💸 <b>₦73,000 PalmPay — Arrived instant ✅</b>\n\nMonday 11 May. 05:00 AM. Real phone notification. 💚\n₦73,000 (~$50). ID: PPW-9938902. Same minute.\n\nBryan tested small first. Then scaled up big.\nNo delay. No wahala. My guy — just pure money. 💸\n\n1WIN pays. PalmPay confirms. Every single time. ✅\nYou can't withdraw what you don't deposit. ACT NOW. 🔥\n\nDeposit ₦5,000 → play with ₦30,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>Start NOW:</b> https://1wzpdo.life/v3/aggressive-casino?p=zusb","images":["withdrow1.png"]},

{"date":"2026-05-12","time":"16:00","content":"💡 <b>How to withdraw to PalmPay — step by step</b>\n\nMy guy, here is exactly how money arrives in 3-5 minutes.\n\nStep 1: Go to 1WIN wallet. Click Withdraw.\nStep 2: Select PalmPay. Enter your number.\nStep 3: Enter amount. Confirm payment.\nStep 4: Check PalmPay. Money arrives instant. 💸\n\nChale — test small first. Smart bettors don't rush. 🙏\nScared people watch. Smart people ACT NOW. 🔥\n\nDeposit ₦3,000 → play with ₦18,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>Start here:</b> https://1wzpdo.life/v3/aggressive-casino?p=zusb","images":["EDUCATIONPOST.png"]},
# {"date":"2026-05-12","time":"23:55","content":"🌐 <b>FortunoBet.com — Where Smart Bettors Win!</b>\n\n1WIN. Sports. Casino. Live games. All partners. 💰\nData-based. Transparent. Real results every week. ✅\n\n₦73,000 paid Monday. Real PalmPay proof. Not story.\nChale — join the winning community. Smart bettors here.\n\nThey don enter already. You still dey outside?? 🔥\n\nDeposit ₦10,000 → play with ₦60,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>Join community:</b> https://fortunobet.com\n👉 <b>Start here:</b> https://1wzpdo.life/v3/aggressive-casino?p=zusb","images":["FortunoBet.png"]},

{"date":"2026-05-13","time":"12:00","content":"⚽ <b>$80 → $152.80. Manchester United ✅</b>\n\nEngland Premier League. Odds 1.91. 🏴󠁧󠁢󠁥󠁮󠁧󠁿\n$72.80 profit. Man United vs Brentford. Dominant. 💸\n\nMan United strong home form. Data was clear. Easy read.\nMon ✅ Tue ✅ Wed ✅ Pattern is real. No luck involved.\n\nSmart players follow. Scared ones watch forever. 🔥\n\nDeposit ₦5,000 → play with ₦30,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>Join NOW:</b> https://1wzpdo.life/v3/aggressive-casino?p=zusb","images":["win2.png"]},
{"date":"2026-05-13","time":"23:55","content":"⚠️ <b>600% Bonus — EXPIRES TONIGHT! ❌</b>\n\nRegistered Monday? Expires Wednesday 11:59 PM. NOW.\nRegistered Tuesday? Expires Thursday 11:59 PM. ⏰\n\n600% NOT lifetime. Gone in hours. Not days. HOURS.\nChale — after deadline: ❌ Gone forever. No second chance.\n\nNo dulling. Deposit NOW or lose it forever. 🔥\n\nDeposit ₦5,000 → play with ₦35,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>NOW:</b> https://1wzpdo.life/v3/aggressive-casino?p=zusb","images":["casion1.jpeg"]},

{"date":"2026-05-14","time":"16:00","content":"📊 <b>Why FortunoBet community wins more than solo bettors</b>\n\nChale, solo bettors lose because they guess alone.\nFortunoBet community does it different. 💡\n\n✅ Expert picks shared daily — no guessing\n✅ Real withdrawal proofs every week — no fake\n✅ Thousands winning together — not alone\n\nMy guy — join the system, not just a bet.\nStill betting solo? No dulling — move NOW. 🔥\n\nDeposit ₦3,000 → play with ₦18,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>Join us:</b> https://1wzpdo.life/v3/aggressive-casino?p=zusb","images":["AUTHORITYPOST.png"]},
{"date":"2026-05-14","time":"23:55","content":"💚 <b>₦3,000 test → ₦9,100 withdrawal ✅</b>\n\nReal story. This week. Tunde, Lagos.\n\nDeposited ₦3,000 Monday — just to test the system.\nBet Premier League Tuesday. Form was obvious. Won ₦6,100.\nWithdrew ₦9,100 Thursday. PalmPay. 4 minutes. 💸\n\n\"I tested small first. Chale — now I trust 1WIN.\" 🔥\nIf Tunde can do it — my guy, you can too. ACT NOW.\n\nDeposit ₦3,000 → play with ₦18,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>Test it:</b> https://1wzpdo.life/v3/aggressive-casino?p=zusb","images":["SUCCESSSTORY.png"]},

{"date":"2026-05-15","time":"12:00","content":"🎾 <b>$100 → $122.00. Karen Khachanov ✅</b>\n\nATP Madrid. Spain. Clay. Odds 1.22. 🇪🇸\n$22 profit. Khachanov 6-2, 6-3. Dominated. 💸\n\nRanked higher. H2H record was clear. Pure analysis.\nMon ✅ Wed ✅ Fri ✅ Three wins. Pure analysis, my guy.\n\nSTOP WATCHING. They collecting. You still looking. 🔥\n\nDeposit ₦5,000 → play with ₦30,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>Join NOW:</b> https://1wzpdo.life/v3/aggressive-casino?p=zusb","images":["win3.png"]},
{"date":"2026-05-15","time":"23:55","content":"⚠️ <b>Bonus expires TOMORROW midnight! ❌</b>\n\nRegistered this week? Your 600% dies TOMORROW. ⏰\nAfter midnight: ❌ Gone. Forever. No exceptions.\n\nOne deposit activates EVERYTHING right now.\nPalmPay. Opay. Zero fees. Arrives same minute. ✅\n\nNo dulling my guy — last chance. Deposit NOW. 🔥\n\nDeposit ₦5,000 → play with ₦35,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>NOW:</b> https://1wzpdo.life/v3/aggressive-casino?p=zusb","images":["casino2.jpeg"]},

{"date":"2026-05-16","time":"16:00","content":"🌐 <b>FortunoBet.com — This week results inside! ✅</b>\n\n3 wins. 2 withdrawals. All verified. All real. 💸\n₦73,000 + ₦114,646 — Both PalmPay. Both instant.\n\nSports. Casino. All partners. One platform. No wahala.\nChale — no hidden fees. Real payouts. Every time. 💰\n\nSmart bettors manage bankroll. Only bet what you can afford. 🙏\n\n👉 <b>Join community:</b> https://fortunobet.com\n👉 <b>Start here:</b> https://1wzpdo.life/v3/aggressive-casino?p=zusb","images":["FortunoBet.png"]},
{"date":"2026-05-16","time":"21:00","content":"💸 <b>₦114,646 PalmPay — Arrived Wednesday ✅</b>\n\nWednesday 13 May. 01:32 PM. Real phone notification. 💚\n₦114,646 (~$80). ID: PPW-9938903. Same minute.\n\nBryan withdrew Wednesday afternoon. No delay. No wahala.\nMy guy — this is what consistent betting looks like. 💸\n\n1WIN pays every time. PalmPay confirms every time. ✅\nYou can't collect what you never deposited. 🔥\n\nDeposit ₦5,000 → play with ₦30,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>Start:</b> https://1wzpdo.life/v3/aggressive-casino?p=zusb","images":["withdorw2.png"]},

{"date":"2026-05-17","time":"16:00","content":"💚 <b>This week. Real results. Full transparency. ✅</b>\n\nMon: $100 → $126.00 ✅ Auger-Aliassime — ranked higher.\nWed: $80 → $152.80 ✅ Man United — strong home form.\nFri: $100 → $122.00 ✅ Khachanov — H2H was clear.\n\nROI this week: +33% 📊\n₦73,000 + ₦114,646 = Both PalmPay instant. 💸\n\nTest small first. Smart bettors don't rush. 🙏\nThey won this week. Next week YOU start. 🔥\n\nDeposit ₦10,000 → play with ₦60,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>NOW:</b> https://1wzpdo.life/v3/aggressive-casino?p=zusb","images":["withdrow1.png","withdorw2.png"]},
{"date":"2026-05-17","time":"23:55","content":"🎰 <b>500% Bonus — LAST CHANCE TONIGHT! ❌</b>\n\n1WIN Casino. Top slots. Live dealers. 💰\nDeposit ₦5,000 → play with ₦30,000 + 500 spins.\n\nPalmPay. Opay. Zero fees. Withdraw tonight. ✅\nWeek closes MIDNIGHT. Bonus gone after. No second chance.\n\nWe test. We withdraw. We scale. Join us NOW or miss it. 🔥\n\nDeposit ₦5,000 → play with ₦30,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>Play NOW:</b> https://1wzpdo.life/v3/aggressive-casino?p=zusb","images":["casino3.jpeg"]},
]



async def send_post_async(post):
    try:
        P_MODE = "HTML"
        # IMPORTANT: In new Python Telegram, we MUST use 'async with' or a local bot instance
        async with Bot(token=BOT_TOKEN) as temp_bot:
            if "images" in post and post["images"]:
                if len(post["images"]) > 1:
                    media_group = []
                    for idx, img_file in enumerate(post["images"]):
                        if os.path.exists(img_file):
                            file_handle = open(img_file, "rb")
                            if idx == 0:
                                media_group.append(InputMediaPhoto(file_handle, caption=post["content"], parse_mode=P_MODE))
                            else:
                                media_group.append(InputMediaPhoto(file_handle))
                    if media_group:
                        # ADDED 'await' HERE
                        await temp_bot.send_media_group(chat_id=CHANNEL_ID, media=media_group)
                else:
                    img_file = post["images"][0]
                    if os.path.exists(img_file):
                        with open(img_file, "rb") as photo:
                            # ADDED 'await' HERE
                            await temp_bot.send_photo(chat_id=CHANNEL_ID, photo=photo, caption=post["content"], parse_mode=P_MODE)
            else:
                # ADDED 'await' HERE
                await temp_bot.send_message(chat_id=CHANNEL_ID, text=post["content"], parse_mode=P_MODE)
        
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Posted Successfully")
    except Exception as e:
        print(f"Failed to post: {e}")

# This wrapper bridges the Scheduler to the Async function
def job_wrapper(post):
    asyncio.run(send_post_async(post))

# ====== SCHEDULE JOBS ======
for post in posts:
    post_date = datetime.strptime(post["date"], "%Y-%m-%d")
    hour, minute = map(int, post["time"].split(":"))

    scheduler.add_job(
        job_wrapper, # Use the wrapper here
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

print("Bot is starting with Async Fix...")
scheduler.start()