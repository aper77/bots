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
{"date":"2026-05-18","time":"16:00","content":"⚽ <b>$100 → $116.00. FC Bayern München ✅</b>\n\nGermany Bundesliga. Odds 1.16. 🇩🇪\n$16 profit. Bayern vs FC Koln. Completely dominant. 💸\n\nBayern top of league. Form was obvious. Easy read.\nMy guy — Monday pick already paid. ✅\n\nYou dey watch while others dey collect? STOP WATCHING. 🔥\n\nDeposit ₦3,000 → play with ₦18,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>Join NOW:</b> https://1wzpdo.life/v3/aggressive-casino?p=zusb","images":["win3.png"]},
{"date":"2026-05-18","time":"23:55","content":"💸 <b>₦150,000 PalmPay — Arrived instant ✅</b>\n\nMonday 18 May. 05:12 AM. Real phone notification. 💚\n₦150,000 (~$100). ID: PPW-9938904. Same minute.\n\nBryan tested small. Scaled big. No delay. No wahala. 💸\n1WIN pays. PalmPay confirms. Every single time. ✅\n\nYou can't collect what you never deposited. ACT NOW. 🔥\n\nDeposit ₦5,000 → play with ₦30,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>Start NOW:</b> https://1wzpdo.life/v3/aggressive-casino?p=zusb","images":["withdrow.png"]},

{"date":"2026-05-19","time":"16:00","content":"💡 <b>How to use your 600% bonus correctly</b>\n\nMy guy, most people waste their bonus. Here is exactly how.\n\nStep 1: Register FREE → code FORTUNOBET\nStep 2: Deposit ₦3,000 → get ₦18,000 to play with\nStep 3: Place small bets only. Don't rush. 🙏\nStep 4: Withdraw profits to PalmPay. Same day. 💸\n\nChale — test small first. Smart bettors don't rush. 🙏\n\nDeposit ₦3,000 → play with ₦18,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>Start here:</b> https://1wzpdo.life/v3/aggressive-casino?p=zusb","images":["bonus2.jpeg"]},
{"date":"2026-05-19","time":"23:55","content":"🌐 <b>FortunoBet.com — Smart bettors already inside!</b>\n\n1WIN. Sports. Casino. Live games. All partners. 💰\n₦150,000 paid Monday. Real PalmPay proof. Not story. ✅\n\nWhile you dey read this — they dey collect. 💸\nChale — how long you go keep watching? 🔥\n\nThey don enter. You still dey outside. JOIN NOW.\n\nDeposit ₦10,000 → play with ₦60,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>Join community:</b> https://fortunobet.com\n👉 <b>Start NOW:</b> https://1wzpdo.life/v3/aggressive-casino?p=zusb","images":["bonus7.jpeg"]},

{"date":"2026-05-20","time":"12:05","content":"🎾 <b>$150 → $193.50. Barrientos/Behar ✅</b>\n\nATP Challenger Doubles. Valencia. Spain. Clay. Odds 1.29. 🇪🇸\n$43.50 profit. Barrientos/Behar won 6-0, 6-7, 6-1. 💸\n\nStronger pair. H2H clear. Pure analysis. No luck.\nMon ✅ Tue ✅ Wed ✅ Pattern is real, my guy. ✅\n\nSTOP WATCHING. They collecting. JOIN NOW. 🔥\n\nDeposit ₦5,000 → play with ₦30,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>Join NOW:</b> https://1wzpdo.life/v3/aggressive-casino?p=zusb","images":["win2.png"]},
{"date":"2026-05-20","time":"23:55","content":"⚠️ <b>600% Bonus — EXPIRES TONIGHT! ❌</b>\n\nRegistered Monday? Expires Wednesday 11:59 PM. NOW.\nRegistered Tuesday? Expires Thursday 11:59 PM. ⏰\n\n600% NOT lifetime. Gone in hours. Not days. HOURS.\nChale — after deadline: ❌ Gone forever. No second chance.\n\nNo dulling. Deposit NOW or lose it forever. 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>NOW:</b> https://1wzpdo.life/v3/aggressive-casino?p=zusb","images":["bonus1.jpeg"]},

{"date":"2026-05-21","time":"16:00","content":"📊 <b>3 mistakes Ghanaian bettors make every week</b>\n\nChale, I see this every week. Stop making these mistakes.\n\n❌ Mistake 1: Betting big — no control. Lose everything.\n❌ Mistake 2: Random channels — no analysis. Pure luck.\n❌ Mistake 3: Chasing losses — emotion kills bankroll.\n\nFortunoBet community avoids all 3. Join the system NOW.\nStop watching. Stop losing. JOIN NOW. 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>JOIN NOW:</b> https://1wzpdo.life/v3/aggressive-casino?p=zusb","images":["bonus4.jpeg"]},
{"date":"2026-05-21","time":"23:55","content":"💚 <b>GH₵200 test → GH₵650 withdrawal ✅</b>\n\nReal story. This week. Kwame, Accra.\n\nDeposited GH₵200 Monday — just to test the system.\nBet Bundesliga Tuesday. Form obvious. Won GH₵450.\nWithdrew GH₵650 Thursday. MTN Mobile Money. 4 minutes. 💸\n\n\"I tested small first. Chale — now I trust 1WIN.\" 🙏\nIf Kwame can do it — my guy, you can too.\n\nDeposit GH₵200 → play with GH₵1,200\n🔑 Code: <code>fortunobet</code>\n👉 <b>Test it:</b> https://1wzpdo.life/v3/aggressive-casino?p=zusb","images":["bonus3.jpeg"]},

{"date":"2026-05-22","time":"12:00","content":"🎮 <b>$150 → $205.50. Team Spirit ✅</b>\n\nPGL Astana. CS2 Esports. Odds 1.37. 🏆\n$55.50 profit. Team Spirit vs MOUZ. Dominated. 💸\n\nTeam Spirit stronger form. Data clear. Easy read.\nMon ✅ Wed ✅ Fri ✅ Three wins. Pure analysis, my guy.\n\nSTOP WATCHING. They collecting. You still looking. 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>Join NOW:</b> https://1wzpdo.life/v3/aggressive-casino?p=zusb","images":["win1.png"]},
{"date":"2026-05-22","time":"23:55","content":"⚠️ <b>Bonus expires TOMORROW midnight! ❌</b>\n\nRegistered this week? Your 600% dies TOMORROW. ⏰\nAfter midnight: ❌ Gone. Forever. No exceptions.\n\nOne deposit activates EVERYTHING right now.\nMTN Mobile Money. Zero fees. Arrives same minute. ✅\n\nNo dulling my guy — last chance. Deposit NOW. 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>NOW:</b> https://1wzpdo.life/v3/aggressive-casino?p=zusb","images":["bonus5.jpeg"]},

{"date":"2026-05-23","time":"16:00","content":"🌐 <b>FortunoBet.com — Results this week. All real. ✅</b>\n\n3 wins. 2 withdrawals. Verified. Real. Not story. 💸\nGH₵1,050 + GH₵1,150 — Both MTN Mobile Money. Both instant.\n\nWhile you dey wait — they dey collect every week.\nChale — smart bettors don enter already. 🔥\n\nYou still dey outside? Last chance this week. JOIN NOW.\n\nDeposit GH₵100 → play with GH₵600\n🔑 Code: <code>fortunobet</code>\n👉 <b>Join community:</b> https://fortunobet.com\n👉 <b>Start NOW:</b> https://1wzpdo.life/v3/aggressive-casino?p=zusb","images":["bonus6.jpeg"]},
{"date":"2026-05-23","time":"21:00","content":"💸 <b>GH₵1,150 MTN Mobile Money — Arrived Wednesday ✅</b>\n\nWednesday 20 May. 12:43 PM. Real phone notification. 💚\nGH₵1,150 (~$110). ID: PPW-9938905. Same minute.\n\nBryan withdrew Wednesday. No delay. No wahala. 💸\n1WIN pays. MTN confirms. Every single time. ✅\n\nYou can't collect what you never deposited. ACT NOW. 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>Start NOW:</b> https://1wzpdo.life/v3/aggressive-casino?p=zusb","images":["withdrow2.png"]},

{"date":"2026-05-24","time":"16:00","content":"💚 <b>This week. Real results. Full transparency. ✅</b>\n\nMon: $100 → $116.00 ✅ Bayern — top of league.\nWed: $150 → $193.50 ✅ Barrientos/Behar — H2H clear.\nFri: $150 → $205.50 ✅ Team Spirit — stronger form.\n\nROI this week: +35% 📊\nGH₵1,050 + GH₵1,150 = Both MTN Money instant. 💸\n\nThey collected this week. Next week YOU start. NOW. 🔥\n\nDeposit GH₵100 → play with GH₵600\n🔑 Code: <code>fortunobet</code>\n👉 <b>JOIN NOW:</b> https://1wzpdo.life/v3/aggressive-casino?p=zusb","images":["withdrow.png","withdrow2.png"]},
{"date":"2026-05-24","time":"23:55","content":"🎰 <b>500% Bonus — LAST CHANCE TONIGHT! ❌</b>\n\n1WIN Casino. Top slots. Live dealers. 💰\nDeposit GH₵50 → play with GH₵300 + 500 spins.\n\nMTN Mobile Money. Zero fees. Withdraw tonight. ✅\nWeek closes MIDNIGHT. Bonus gone. No second chance.\n\nWe test. We withdraw. We scale. JOIN NOW or miss it. 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>Play NOW:</b> https://1wzpdo.life/v3/aggressive-casino?p=zusb","images":["bonus8.jpeg"]}
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