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
{"date":"2026-05-18","time":"16:00","content":"⚽ <b>$100 → $116.00. FC Bayern München ✅</b>\n\nGermany Bundesliga. Odds 1.16. 🇩🇪\n$16 profit. Bayern vs FC Koln. Completely dominant. 💸\n\nBayern top of league. Form was obvious. Easy read.\nMy guy — pure analysis, not luck. Already paid. ✅\n\nYou dey watch while others dey collect? STOP WATCHING. 🔥\n\nDeposit ₦3,000 → play with ₦18,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>Join NOW:</b> https://1wzpdo.life/v3/aggressive-casino?p=zusb","images":["win3.png"]},
{"date":"2026-05-18","time":"23:55","content":"💸 <b>₦150,000 PalmPay — Arrived instant ✅</b>\n\nMonday 18 May. 05:12 AM. Real phone notification. 💚\n₦150,000 (~$100). ID: PPW-9938904. Same minute.\n\nBryan tested small first. Then scaled up big.\nNo delay. No wahala. My guy — just pure money. 💸\n\n1WIN pays. PalmPay confirms. Every single time. ✅\n\nYou can't withdraw what you don't deposit. 🔥\n\nDeposit ₦5,000 → play with ₦30,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>Start NOW:</b> https://1wzpdo.life/v3/aggressive-casino?p=zusb","images":["withdrow.png"]},

{"date":"2026-05-19","time":"16:00","content":"💡 <b>How to use your 600% bonus correctly</b>\n\nMy guy, most people waste their bonus. Here is how smart bettors use it.\n\nStep 1: Register FREE → code FORTUNOBET\nStep 2: Deposit ₦3,000 → get ₦18,000 to play with\nStep 3: Place small bets only. Don't rush. 🙏\nStep 4: Withdraw profits to PalmPay. Same day. 💸\n\nChale — test small first. Smart bettors don't rush.\nFollow for more → FortunoBet.com\n\nDeposit ₦3,000 → play with ₦18,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>Start here:</b> https://1wzpdo.life/v3/aggressive-casino?p=zusb","images":["bonus2.jpeg"]},
{"date":"2026-05-19","time":"23:55","content":"🌐 <b>FortunoBet.com — Where Smart Bettors Win!</b>\n\n1WIN. Sports. Casino. Live games. All partners. 💰\nData-based. Transparent. Real results every week. ✅\n\n₦150,000 paid Monday. Real PalmPay proof. Not story.\nChale — join the winning community. Smart bettors here.\n\nThey don enter already. You still dey outside?? 🔥\n\nDeposit ₦10,000 → play with ₦60,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>Join community:</b> https://fortunobet.com\n👉 <b>Start here:</b> https://1wzpdo.life/v3/aggressive-casino?p=zusb","images":["bonus7.jpeg"]},

# {"date":"2026-05-20","time":"12:00","content":"🎾 <b>$150 → $193.50. Barrientos/Behar ✅</b>\n\nATP Challenger Doubles. Valencia. Spain. Clay. Odds 1.29. 🇪🇸\n$43.50 profit. Barrientos/Behar won 6-0, 6-7, 6-1. 💸\n\nStronger pair. H2H record was clear. Pure analysis.\nMon ✅ Tue ✅ Wed ✅ Pattern is real, my guy.\n\nSmart players follow. Scared ones watch forever. 🔥\n\nDeposit ₦5,000 → play with ₦30,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>Join NOW:</b> https://1wzpdo.life/v3/aggressive-casino?p=zusb","images":["win2.png"]},
{"date":"2026-05-20","time":"23:55","content":"⚠️ <b>600% Bonus — EXPIRES TONIGHT! ❌</b>\n\nRegistered Monday? Expires Wednesday 11:59 PM. NOW.\nRegistered Tuesday? Expires Thursday 11:59 PM. ⏰\n\n600% NOT lifetime. Gone in hours. Not days. HOURS.\nChale — after deadline: ❌ Gone forever. No second chance.\n\nNo dulling. Deposit NOW or lose it forever. 🔥\n\nDeposit ₦5,000 → play with ₦35,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>NOW:</b> https://1wzpdo.life/v3/aggressive-casino?p=zusb","images":["bonus1.jpeg"]},

{"date":"2026-05-21","time":"16:00","content":"📊 <b>3 mistakes Nigerian bettors make every week</b>\n\nChale, I see this every week. Don't be this person.\n\n❌ Mistake 1: Betting too much on one match — no bankroll control\n❌ Mistake 2: Following random channels — no real analysis\n❌ Mistake 3: Chasing losses — emotion beats data every time\n\nFortunoBet community does it different:\n✅ We test small. We use data. We withdraw consistently.\n\nMy guy — join the system, not just a bet. 🔥\n\n👉 <b>See full system:</b> https://fortunobet.com\n👉 <b>Start here:</b> https://1wzpdo.life/v3/aggressive-casino?p=zusb","images":["bonus4.jpeg"]},
{"date":"2026-05-21","time":"23:55","content":"💚 <b>₦2,500 test → ₦8,200 withdrawal ✅</b>\n\nReal story. This week. Emeka, Lagos.\n\nDeposited ₦2,500 Monday — just to test the system.\nBet Bundesliga Tuesday. Form was obvious. Won ₦5,700.\nWithdrew ₦8,200 Thursday. PalmPay. 4 minutes. 💸\n\n\"I tested small first. Chale — now I trust 1WIN.\" 🔥\nIf Emeka can do it — my guy, you can too.\n\nDeposit ₦2,500 → play with ₦15,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>Test it:</b> https://1wzpdo.life/v3/aggressive-casino?p=zusb","images":["bonus3.jpeg"]},

{"date":"2026-05-22","time":"12:00","content":"🎮 <b>$150 → $205.50. Team Spirit ✅</b>\n\nPGL Astana. CS2 Esports. Odds 1.37. 🏆\n$55.50 profit. Team Spirit vs MOUZ. Dominant win. 💸\n\nTeam Spirit stronger form. Data was clear. Easy read.\nMon ✅ Wed ✅ Fri ✅ Three wins. Pure analysis, my guy.\n\nSTOP WATCHING. They collecting. You still looking. 🔥\n\nDeposit ₦5,000 → play with ₦30,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>Join NOW:</b> https://1wzpdo.life/v3/aggressive-casino?p=zusb","images":["win1.png"]},
{"date":"2026-05-22","time":"23:55","content":"⭐ <b>FREE PICK — This Weekend</b>\n\nFC Barcelona vs Villarreal. La Liga. Saturday. 🇪🇸\n\nOur analysis:\n✅ Barcelona strong home form: 5 wins in last 5\n✅ Villarreal away record weak: 1 win in last 8 away\n✅ Barcelona top motivation — title race\n\nOur lean: Barcelona to win. Odds around 1.40-1.50\n\nSmall stake only. Smart bankroll always. 🙏\nFollow for more free picks → FortunoBet.com","images":["bonus5.jpeg"]},

{"date":"2026-05-23","time":"16:00","content":"🌐 <b>FortunoBet.com — This week results inside! ✅</b>\n\n3 wins. 2 withdrawals. All verified. All real. 💸\n₦150,000 + ₦165,000 — Both PalmPay. Both instant.\n\nSports. Casino. All partners. One platform. No wahala.\nChale — no hidden fees. Real payouts. Every time. 💰\n\nSmart bettors manage bankroll. Only bet what you can afford. 🙏\n\n👉 <b>Join community:</b> https://fortunobet.com\n👉 <b>Start here:</b> https://1wzpdo.life/v3/aggressive-casino?p=zusb","images":["bonus6.jpeg"]},
{"date":"2026-05-23","time":"21:00","content":"💸 <b>₦165,000 PalmPay — Arrived Wednesday ✅</b>\n\nWednesday 20 May. 12:43 PM. Real phone notification. 💚\n₦165,000 (~$110). ID: PPW-9938905. Same minute.\n\nBryan withdrew Wednesday afternoon. No delay. No wahala.\nMy guy — this is what consistent betting looks like. 💸\n\n1WIN pays every time. PalmPay confirms every time. ✅\nYou can't collect what you never deposited. 🔥\n\nDeposit ₦5,000 → play with ₦30,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>Start:</b> https://1wzpdo.life/v3/aggressive-casino?p=zusb","images":["withdrow2.png"]},

{"date":"2026-05-24","time":"16:00","content":"💚 <b>This week. Real results. Full transparency. ✅</b>\n\nMon: $100 → $116.00 ✅ Bayern Munich — top of league.\nWed: $150 → $193.50 ✅ Barrientos/Behar — H2H clear.\nFri: $150 → $205.50 ✅ Team Spirit — stronger form.\n\nROI this week: +35% 📊\n₦150,000 + ₦165,000 = Both PalmPay instant. 💸\n\nTest small first. Smart bettors don't rush. 🙏\nThey won this week. Next week YOU start. 🔥\n\nDeposit ₦10,000 → play with ₦60,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>NOW:</b> https://1wzpdo.life/v3/aggressive-casino?p=zusb","images":["withdrow.png","withdrow2.png"]},
{"date":"2026-05-24","time":"23:55","content":"🎰 <b>500% Bonus — LAST CHANCE TONIGHT! ❌</b>\n\n1WIN Casino. Top slots. Live dealers. 💰\nDeposit ₦5,000 → play with ₦30,000 + 500 spins.\n\nPalmPay. Opay. Zero fees. Withdraw tonight. ✅\nWeek closes MIDNIGHT. Bonus gone after. No second chance.\n\nWe test. We withdraw. We scale. Join us NOW or miss it. 🔥\n\nDeposit ₦5,000 → play with ₦30,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>Play NOW:</b> https://1wzpdo.life/v3/aggressive-casino?p=zusb","images":["bonus8.jpeg"]}
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