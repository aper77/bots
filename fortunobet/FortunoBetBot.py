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
{"date":"2026-05-25","time":"13:00","content":"🎮 <b>$150 → $205.50. Team Spirit ✅</b>\n\nPGL Astana. CS2 Esports. Odds 1.37. 🏆\n$55.50 profit. Team Spirit vs MOUZ. Dominated. 💸\n\nTeam Spirit stronger form. Data clear. Easy read.\nChale, my guy — Monday pick already paid. ✅\n\nYou dey watch while others dey collect? STOP WATCHING. 🔥\n\nDeposit GH₵50 / ₦3,000 → play with 6x more\n🔑 Code: <code>fortunobet</code>\n👉 <b>Join NOW:</b> https://1wzpdo.life/betting?open=register&p=80te","images":["win1.png"]},
{"date":"2026-05-25","time":"23:55","content":"💸 <b>GH₵1,300 / ₦150,000 — Arrived instant ✅</b>\n\nMonday 25 May. 05:12 AM. Real phone notification. 💚\nGH₵1,300 (~$110). ID: MTN-7732020. Same minute.\n\nKofi tested small first. Then scaled up big.\nNo delay. No wahala. Chale my guy — just pure money. 💸\n\n1WIN pays. MTN. PalmPay. Every single time. ✅\nYou can't collect what you never deposited. ACT NOW. 🔥\n\nDeposit GH₵50 / ₦3,000 → play with 6x more\n🔑 Code: <code>fortunobet</code>\n👉 <b>Start NOW:</b> https://1wzpdo.life/betting?open=register&p=80te","images":["withdrow1.png"]},

{"date":"2026-05-26","time":"16:00","content":"💡 <b>How to win big on 1WIN Casino — explained</b>\n\nChale my guy, most people play wrong. Here is how smart players do it.\n\nStep 1: Start small — GH₵5 / ₦500 per spin only\nStep 2: Play Fortune Tiger or Gates of Olympus 🎰\nStep 3: Stop after doubling your amount. Withdraw. 💸\nStep 4: MTN Mobile Money or PalmPay. Same day. ✅\n\nTest small first. Smart bettors don't rush. 🙏\nShare this with 2 friends who play casino! 🔥\n\nDeposit GH₵50 / ₦3,000 → play with 6x more\n🔑 Code: <code>fortunobet</code>\n👉 <b>Start here:</b> https://1wzpdo.life/betting?open=register&p=80te","images":["bonus7.jpeg"]},
{"date":"2026-05-26","time":"23:55","content":"🌐 <b>FortunoBet.com — Smart bettors already inside!</b>\n\n1WIN. Sports. Casino. Live games. All partners. 💰\nGH₵1,300 paid Monday. Real proof. Not story. ✅\n\nWhile you dey read this — they dey collect. 💸\nChale, my guy — how long you go keep watching? 🔥\n\nThey don enter. You still dey outside. JOIN NOW.\n\nDeposit GH₵100 / ₦6,000 → play with 6x more\n🔑 Code: <code>fortunobet</code>\n👉 <b>Join community:</b> https://fortunobet.com\n👉 <b>Start NOW:</b> https://1wzpdo.life/betting?open=register&p=80te","images":["bonus3.jpeg"]},

{"date":"2026-05-27","time":"12:00","content":"⚽ <b>$100 → $154.00. Lens ✅</b>\n\nFrance Cup. Odds 1.54. 🇫🇷\n$54 profit. Lens vs Nice. Completely dominant. 💸\n\nLens strong home form. Data was clear. Easy read.\nMon ✅ Tue ✅ Wed ✅ Pattern is real, my guy.\n\nSTOP WATCHING. They collecting. JOIN NOW. 🔥\n\nDeposit GH₵50 / ₦3,000 → play with 6x more\n🔑 Code: <code>fortunobet</code>\n👉 <b>Join NOW:</b> https://1wzpdo.life/betting?open=register&p=80te","images":["win2.png"]},
{"date":"2026-05-27","time":"23:55","content":"⚠️ <b>600% Bonus — EXPIRES TONIGHT! ❌</b>\n\nRegistered Monday? Expires Wednesday 11:59 PM. NOW.\nRegistered Tuesday? Expires Thursday 11:59 PM. ⏰\n\n600% NOT lifetime. Gone in hours. Not days. HOURS.\nChale — after deadline: ❌ Gone forever. No second chance.\n\nNo dulling my guy. Deposit NOW or lose it forever. 🔥\n\nDeposit GH₵50 / ₦3,000 → play with 6x more\n🔑 Code: <code>fortunobet</code>\n👉 <b>NOW:</b> https://1wzpdo.life/betting?open=register&p=80te","images":["bonus1.jpeg"]},

{"date":"2026-05-28","time":"16:00","content":"📊 <b>3 mistakes bettors make every week</b>\n\nChale my guy, I see this every week. Stop now.\n\n❌ Mistake 1: Betting big — no control. Lose everything.\n❌ Mistake 2: Random channels — no analysis. Pure luck.\n❌ Mistake 3: Chasing losses — emotion kills bankroll.\n\nFortunoBet community avoids all 3. Join NOW.\nTag 2 friends who dey make these mistakes. No dulling! 🔥\n\nDeposit GH₵50 / ₦3,000 → play with 6x more\n🔑 Code: <code>fortunobet</code>\n👉 <b>JOIN NOW:</b> https://1wzpdo.life/betting?open=register&p=80te","images":["bonus5.jpeg"]},
{"date":"2026-05-28","time":"23:55","content":"💚 <b>GH₵200 / ₦30,000 test → withdrawal ✅</b>\n\nReal story. This week. Kwame, Accra.\n\nDeposited small Monday — just to test the system.\nBet France Cup Wednesday. Form obvious. Won big.\nWithdrew Thursday. MTN Mobile Money. 4 minutes. 💸\n\n\"I tested small first. Chale — now I trust 1WIN.\" 🙏\nIf Kwame can do it — my guy, you can too.\n\nDeposit GH₵200 / ₦12,000 → play with 6x more\n🔑 Code: <code>fortunobet</code>\n👉 <b>Test it:</b> https://1wzpdo.life/betting?open=register&p=80te","images":["bonus6.jpeg"]},

{"date":"2026-05-29","time":"12:00","content":"🎾 <b>$100 → $129.00. Ignacio Buse ✅</b>\n\nATP Hamburg. Germany. Clay. Odds 1.29. 🇩🇪\n$29 profit. Buse vs Kovacevic. 6-1, 6-4. Dominated. 💸\n\nBuse ranked higher. Clay form obvious. Easy read.\nMon ✅ Wed ✅ Fri ✅ Three wins. Pure analysis.\n\nSTOP WATCHING. They collecting. You still looking. 🔥\n\nDeposit GH₵50 / ₦3,000 → play with 6x more\n🔑 Code: <code>fortunobet</code>\n👉 <b>Join NOW:</b> https://1wzpdo.life/betting?open=register&p=80te","images":["win3.png"]},
{"date":"2026-05-29","time":"23:55","content":"⚠️ <b>Bonus expires TOMORROW midnight! ❌</b>\n\nRegistered this week? Your 600% dies TOMORROW. ⏰\nAfter midnight: ❌ Gone. Forever. No exceptions.\n\nOne deposit activates EVERYTHING right now.\nMTN Mobile Money. PalmPay. Zero fees. Same minute. ✅\n\nNo dulling my guy — last chance. Deposit NOW. 🔥\n\nDeposit GH₵50 / ₦3,000 → play with 6x more\n🔑 Code: <code>fortunobet</code>\n👉 <b>NOW:</b> https://1wzpdo.life/betting?open=register&p=80te","images":["bonus2.jpeg"]},

{"date":"2026-05-30","time":"16:00","content":"🌐 <b>FortunoBet.com — Results this week. All real. ✅</b>\n\n3 wins. 2 withdrawals. Verified. Real. Not story. 💸\nGH₵1,300 + GH₵1,050 — MTN Mobile Money. Both instant.\n\nWhile you dey wait — they dey collect every week.\nChale my guy — smart bettors don enter already. 🔥\n\nYou still dey outside? Last chance. JOIN NOW.\n\nDeposit GH₵100 / ₦6,000 → play with 6x more\n🔑 Code: <code>fortunobet</code>\n👉 <b>Join community:</b> https://fortunobet.com\n👉 <b>Start NOW:</b> https://1wzpdo.life/betting?open=register&p=80te","images":["bonus4.jpeg"]},
{"date":"2026-05-30","time":"21:00","content":"💸 <b>GH₵1,050 MTN — Arrived Wednesday ✅</b>\n\nWednesday 27 May. 09:42 AM. Real phone notification. 💚\nGH₵1,050 (~$89). ID: MTN-7732019. Same minute.\n\nKofi withdrew Wednesday. No delay. No wahala. 💸\n1WIN pays. MTN. PalmPay. Every single time. ✅\n\nYou can't collect what you never deposited. ACT NOW. 🔥\n\nDeposit GH₵50 / ₦3,000 → play with 6x more\n🔑 Code: <code>fortunobet</code>\n👉 <b>Start NOW:</b> https://1wzpdo.life/betting?open=register&p=80te","images":["withdrow2.png"]},

{"date":"2026-05-31","time":"16:00","content":"💚 <b>This week. Real results. Full transparency. ✅</b>\n\nMon: $150 → $205.50 ✅ Team Spirit — stronger form.\nWed: $100 → $154.00 ✅ Lens — strong home form.\nFri: $100 → $129.00 ✅ Buse — clay specialist.\n\nROI this week: +38% 📊\nGH₵1,300 + GH₵1,050 = MTN instant. 💸\n\nThey collected. Next week YOU start. NOW. 🔥\nShare with 2 betting friends! Chale my guy — help them join! 💸\n\nDeposit GH₵100 / ₦6,000 → play with 6x more\n🔑 Code: <code>fortunobet</code>\n👉 <b>JOIN NOW:</b> https://1wzpdo.life/betting?open=register&p=80te","images":["withdrow1.png","withdrow2.png"]},
{"date":"2026-05-31","time":"23:55","content":"🎰 <b>500% Bonus — LAST CHANCE TONIGHT! ❌</b>\n\n1WIN Casino. Fortune Tiger. Gates of Olympus. 💰\nDeposit GH₵50 / ₦3,000 → play with 6x more + 500 spins.\n\nMTN Mobile Money. PalmPay. Zero fees. Tonight. ✅\nWeek closes MIDNIGHT. Bonus gone. No second chance.\n\nWe test. We withdraw. We scale. JOIN NOW or miss it. 🔥\n\nDeposit GH₵50 / ₦3,000 → play with 6x more\n🔑 Code: <code>fortunobet</code>\n👉 <b>Play NOW:</b> https://1wzpdo.life/betting?open=register&p=80te","images":["bonus3.jpeg"]}
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