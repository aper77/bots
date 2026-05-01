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

{"date":"2026-04-25","time":"22:00","content":"💸 <b>₦72,000 PalmPay — Arrived tonight ✅</b>\n\nApril 23. 20:33. Real phone notification. 💚\n₦72,000 (~$48). ID: PPW-9938829. Same minute.\n\nKofi tested ₦3,000 first. Then deposited big.\nMy guy — ₦72,000 arrived instant. No wahala. 💸\n\n1WIN pays. PalmPay confirms. Every single time. ✅\n\nYou can't withdraw what you don't deposit. 🔥\n\nDeposit ₦5,000 → play with ₦30,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>Start:</b> https://1wzpdo.life/casino/list?open=register&p=z4m5","images":["withdrow2.png"]},

{"date":"2026-04-26","time":"14:30","content":"💚 <b>This week. Real results. Full transparency. ✅</b>\n\nSun: $80 → $106.40 ✅ Kuzuhara — ranked higher. Easy.\nMon: $80 → $92.80 ✅ Zink — form was clear.\nWed: $75 → $107.25 ✅ Express — pure analysis.\n\nROI this week: +38% 📊\n₦52,500 + ₦72,000 = Both PalmPay instant. 💸\n\nTest small first. Smart bettors don't rush. 🙏\nChale — next week starts Monday. Don't miss it. 🔥\n\nDeposit ₦10,000 → play with ₦60,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>Join FortunoBet community:</b> https://1wzpdo.life/casino/list?open=register&p=z4m5","images":["withdrow1.png","withdrow2.png"]},
# {"date":"2026-04-26","time":"23:55","content":"🎰 <b>+600% Bonus — Last chance this week! ✅</b>\n\n1WIN Casino. Top slots. Live dealers. 💰\nDeposit ₦5,000 → play with ₦35,000 + 500 spins.\n\nPalmPay. Opay. Zero fees. Withdraw tonight. ✅\nWeek closes midnight. No dulling — bonus gone after.\n\nWe test. We withdraw. We scale. My guy — join us. 🔥\n\nDeposit ₦5,000 → play with ₦35,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>Play NOW:</b> https://1wzpdo.life/casino/list?open=register&p=z4m5","images":["fortunobet3.jpeg"]},

{"date":"2026-04-27","time":"16:26","content":"🎾 <b>$100 → $111.00. Kristiana Sidorova ✅</b>\n\nITF Women Tokyo. Japan. Hard. Odds 1.11. 🇯🇵\n$11 profit. Sidorova 6-1, 6-0. Completely dominant. 💸\n\nRanked far higher. Form was obvious. Easy data read.\nMy guy — pure analysis, not luck. ✅\n\nYou dey watch while others dey collect? 🔥\n\nDeposit ₦3,000 → play with ₦18,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>Join NOW:</b> https://1wzpdo.life/casino/list?open=register&p=z0ln","images":["win1.png"]},
{"date":"2026-04-27","time":"23:55","content":"💸 <b>₦184,800 PalmPay — Arrived instant ✅</b>\n\nMonday 27 April. 10:32 AM. Real phone notification. 💚\n₦184,800 (~$120). ID: PPW-9938844. Same minute.\n\nBryan tested small first. Then scaled up.\nNo delay. No wahala. My guy — just pure money. 💸\n\n1WIN pays. PalmPay confirms. Every single time. ✅\n\nYou can't withdraw what you don't deposit. 🔥\n\nDeposit ₦5,000 → play with ₦30,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>Start NOW:</b> https://1wzpdo.life/casino/list?open=register&p=z0ln","images":["withdrow11.png"]},

{"date":"2026-04-28","time":"16:00","content":"💡 <b>Why small deposits are smarter — explained</b>\n\nMy guy, hear this. Most people lose because they start too big.\n\nStep 1: Deposit ₦500-2,000 only. Test the system.\nStep 2: Place one small bet. See how it works.\nStep 3: Withdraw to PalmPay. Confirm it arrives.\nStep 4: Now you trust. Now you deposit bigger. 💸\n\nChale — test small first. Smart bettors don't rush. 🙏\n\nDeposit ₦3,000 → play with ₦18,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>Start here:</b> https://1wzpdo.life/casino/list?open=register&p=z0ln","images":["partner1.jpeg"]},
{"date":"2026-04-28","time":"23:55","content":"🌐 <b>FortunoBet.com — Where Smart Bettors Win!</b>\n\n1WIN. Sports. Casino. Live games. All partners. 💰\nData-based. Transparent. Real results every week. ✅\n\n₦184,800 paid Monday. Real PalmPay proof. Not story.\nChale — join the winning community. Smart bettors here. 🔥\n\nThey don enter. You still dey outside?\n\nDeposit ₦10,000 → play with ₦60,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>Join community:</b> https://fortunobet.com\n👉 <b>Start here:</b> https://1wzpdo.life/casino/list?open=register&p=z0ln","images":["partner6.jpeg"]},

{"date":"2026-04-29","time":"12:00","content":"🎾 <b>$80 → $97.60. Karen Khachanov ✅</b>\n\nATP Madrid. Spain. Clay. Odds 1.22. 🇪🇸\n$17.60 profit. Khachanov 6-2, 6-3. Dominant. 💸\n\nRanked higher. H2H record was clear. Pure analysis.\nMon ✅ Tue ✅ Wed ✅ Pattern is real, my guy.\n\nSmart players follow. Scared ones watch. 🔥\n\nDeposit ₦5,000 → play with ₦30,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>Join NOW:</b> https://1wzpdo.life/casino/list?open=register&p=z0ln","images":["win2.png"]},
{"date":"2026-04-29","time":"23:55","content":"⚠️ <b>600% Bonus — your deadline is coming! ❌</b>\n\nRegistered Monday? Expires Wednesday 11:59 PM.\nRegistered Tuesday? Expires Thursday 11:59 PM. ⏰\n\n600% NOT lifetime. 48 hours only.\nChale — after deadline: ❌ Gone forever.\n\nNo dulling. Deposit NOW or lose it. 🔥\n\nDeposit ₦5,000 → play with ₦35,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>NOW:</b> https://1wzpdo.life/casino/list?open=register&p=z0ln","images":["partner4.jpeg"]},

{"date":"2026-04-30","time":"12:00","content":"📊 <b>What most Nigerian bettors do wrong</b>\n\nChale, let me be honest with you. Most people fail because:\n\n❌ They bet too much on one match — no bankroll control\n❌ They follow random channels — no real analysis\n❌ They chase losses — emotion over data\n\nWhat FortunoBet community does different:\n✅ We test small. We use data. We withdraw consistently.\n\nMy guy — join the system, not just a bet. 🔥\n\nDeposit ₦3,000 → play with ₦18,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>Start here:</b> https://1wzpdo.life/casino/list?open=register&p=z0ln","images":["partner5.jpeg"]},
{"date":"2026-05-01","time":"22:45","content":"💚 <b>₦3,000 test → ₦8,500 withdrawal ✅</b>\n\nReal story. This week. Emeka, Lagos.\n\nDeposited ₦3,000 Monday — just to test the system.\nBet tennis Wednesday. Form was obvious. Won ₦5,500.\nWithdrew ₦8,500 Thursday. PalmPay. 3 minutes. 💸\n\n\"I tested small first. Chale — now I trust 1WIN.\" 🔥\n\nDeposit ₦3,000 → play with ₦18,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>Test it:</b> https://1wzpdo.life/casino/list?open=register&p=z0ln","images":["partner2.jpeg"]},

{"date":"2026-05-01","time":"12:00","content":"🎾 <b>$80 → $97.60. Felix Auger-Aliassime ✅</b>\n\nATP Madrid. Spain. Clay. Odds 1.26. 🇪🇸\n$17.60 profit. Auger-Aliassime 6-3, 6-4. Dominated. 💸\n\nRanked higher. Recent form strong. Easy read.\nMon ✅ Wed ✅ Fri ✅ Three wins. Pure analysis, my guy.\n\nSTOP WATCHING. 🔥\n\nDeposit ₦5,000 → play with ₦30,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>Join NOW:</b> https://1wzpdo.life/casino/list?open=register&p=z0ln","images":["win3.png"]},
{"date":"2026-05-01","time":"01:30","content":"⚠️ <b>Bonus expires TOMORROW — last chance! ❌</b>\n\nRegistered this week? Your 600% expires soon. ⏰\nAfter tomorrow midnight: ❌ Gone forever.\n\nOne deposit activates everything.\nPalmPay. Opay. Zero fees. Instant. ✅\n\nNo dulling my guy — deposit NOW or miss it. 🔥\n\nDeposit ₦5,000 → play with ₦35,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>NOW:</b> https://1wzpdo.life/casino/list?open=register&p=z0ln","images":["partner7.jpeg"]},

{"date":"2026-05-02","time":"16:00","content":"🌐 <b>FortunoBet.com — This week results inside! ✅</b>\n\n3 wins. 2 withdrawals. All verified this week. 💸\n₦184,800 + ₦241,760 — Both PalmPay. Both instant.\n\nSports. Casino. All top partners. One platform.\nChale — no hidden fees. No wahala. Real payouts. 💰\n\nSmart bettors manage their bankroll. Only bet what you can afford. 🙏\n\n👉 <b>Join the community:</b> https://fortunobet.com\n👉 <b>Start here:</b> https://1wzpdo.life/casino/list?open=register&p=z0ln","images":["fortunobet1.png"]},
{"date":"2026-05-02","time":"21:00","content":"💸 <b>₦241,760 PalmPay — Arrived Saturday ✅</b>\n\nSaturday May 2. 09:42 AM. Real phone notification. 💚\n₦241,760 (~$160). ID: PPW-9938845. Same minute.\n\nBryan withdrew Saturday morning. No delay. No wahala.\nMy guy — this is what consistent betting looks like. 💸\n\n1WIN pays. PalmPay confirms. Every single time. ✅\n\nYou can't withdraw what you don't deposit. 🔥\n\nDeposit ₦5,000 → play with ₦30,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>Start:</b> https://1wzpdo.life/casino/list?open=register&p=z0ln","images":["withdrow22.png"]},

{"date":"2026-05-03","time":"16:00","content":"💚 <b>This week. Real results. Full transparency. ✅</b>\n\nMon: $100 → $111.00 ✅ Sidorova — dominant form.\nWed: $80 → $97.60 ✅ Khachanov — H2H was clear.\nFri: $80 → $97.60 ✅ Auger-Aliassime — ranked higher.\n\nROI this week: +24% 📊\n₦184,800 + ₦241,760 = Both PalmPay instant. 💸\n\nTest small first. Smart bettors don't rush. 🙏\nChale — next week starts Monday. Don't miss it. 🔥\n\nDeposit ₦10,000 → play with ₦60,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>NOW:</b> https://1wzpdo.life/casino/list?open=register&p=z0ln","images":["withdrow11.png","withdrow22.png"]},
{"date":"2026-05-03","time":"23:55","content":"🎰 <b>+600% Bonus — Last chance this week! ✅</b>\n\n1WIN Casino. Top slots. Live dealers. 💰\nDeposit ₦5,000 → play with ₦35,000 + 500 spins.\n\nPalmPay. Opay. Zero fees. Withdraw tonight. ✅\nWeek closes midnight. No dulling — bonus gone after.\n\nWe test. We withdraw. We scale. My guy — join us. 🔥\n\nDeposit ₦5,000 → play with ₦35,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>Play NOW:</b> https://1wzpdo.life/casino/list?open=register&p=z0ln","images":["partner3.jpeg"]}

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