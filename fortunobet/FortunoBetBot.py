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

posts =
[
{"date":"2026-05-04","time":"16:00","content":"⚽ <b>$150 → $223.50. Arsenal ✅</b>\n\nEngland Premier League. Odds 1.46. 🏴󠁧󠁢󠁥󠁮󠁧󠁿\n$73.50 profit. Arsenal vs Newcastle. Dominated. 💸\n\nArsenal strong home form. Data was clear. Easy read.\nMy guy — pure analysis, not luck. They followed. Already paid. ✅\n\nYou dey watch while others dey collect? STOP WATCHING. 🔥\n\nDeposit ₦3,000 → play with ₦18,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>Join NOW:</b> https://1wzpdo.life/casino/list?open=register&p=z0ln","images":["win2.png"]},
{"date":"2026-05-04","time":"23:55","content":"💸 <b>₦117,600 PalmPay — Arrived instant ✅</b>\n\nMonday 4 May. 06:32 AM. Real phone notification. 💚\n₦117,600 (~$80). ID: PPW-9938861. Same minute.\n\nBryan tested small first. Then scaled up big.\nNo delay. No wahala. My guy — just pure money. 💸\n\n1WIN pays. PalmPay confirms. Every single time. ✅\nYou can't withdraw what you don't deposit. ACT NOW. 🔥\n\nDeposit ₦5,000 → play with ₦30,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>Start NOW:</b> https://1wzpdo.life/casino/list?open=register&p=z0ln","images":["withdrow2.png"]},

{"date":"2026-05-05","time":"16:00","content":"💡 <b>How to use your 600% bonus correctly</b>\n\nMy guy, most people waste their bonus. Here is how to use it right.\n\nStep 1: Register FREE → code FORTUNOBET.\nStep 2: Deposit ₦3,000 → play with ₦18,000.\nStep 3: Place small bets. Withdraw profits. PalmPay. 💸\n\nChale — test small first. Smart bettors don't rush. 🙏\nScared people watch. Smart people ACT. 🔥\n\nDeposit ₦3,000 → play with ₦18,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>Start here:</b> https://1wzpdo.life/casino/list?open=register&p=z0ln","images":["bonus3.jpeg"]},
{"date":"2026-05-05","time":"23:55","content":"🌐 <b>FortunoBet.com — Where Smart Bettors Win!</b>\n\n1WIN. Sports. Casino. Live games. All partners. 💰\nData-based. Transparent. Real results every week. ✅\n\n₦117,600 paid Monday. Real PalmPay proof. Not story.\nChale — join the winning community. Smart bettors here.\n\nThey don enter already. You still dey outside?? 🔥\n\nDeposit ₦10,000 → play with ₦60,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>Join community:</b> https://fortunobet.com\n👉 <b>Start here:</b> https://1wzpdo.life/casino/list?open=register&p=z0ln","images":["bonus7.jpeg"]},

{"date":"2026-05-06","time":"12:00","content":"⚽ <b>$100 → $146.00. Liverpool ✅</b>\n\nEngland Premier League. Odds 1.49. 🏴󠁧󠁢󠁥󠁮󠁧󠁿\n$46 profit. Liverpool vs Crystal Palace. Dominant. 💸\n\nLiverpool strong form. H2H was clear. Pure analysis.\nMon ✅ Tue ✅ Wed ✅ Pattern is real. No luck involved.\n\nSmart players follow. Scared ones watch forever. 🔥\n\nDeposit ₦5,000 → play with ₦30,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>Join NOW:</b> https://1wzpdo.life/casino/list?open=register&p=z0ln","images":["win1.png"]},
{"date":"2026-05-06","time":"23:55","content":"⚠️ <b>600% Bonus — EXPIRES TONIGHT! ❌</b>\n\nRegistered Monday? Expires Wednesday 11:59 PM. NOW.\nRegistered Tuesday? Expires Thursday 11:59 PM. ⏰\n\n600% NOT lifetime. Gone in hours. Not days. HOURS.\nChale — after deadline: ❌ Gone forever. No second chance.\n\nNo dulling. Deposit NOW or lose it forever. 🔥\n\nDeposit ₦5,000 → play with ₦35,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>NOW:</b> https://1wzpdo.life/casino/list?open=register&p=z0ln","images":["bonus4.jpeg"]},

{"date":"2026-05-07","time":"16:00","content":"📊 <b>Why 1WIN pays faster than every other site</b>\n\nChale, most sites delay your money. 1WIN does NOT.\n\n✅ PalmPay withdrawals arrive in 3-5 minutes\n✅ No hidden fees. No delays. No excuses.\n✅ PPW transaction ID proves every single payment.\n\nMy guy — this is why smart bettors LEFT other sites.\nStill on the slow site? No dulling — move NOW. 🔥\n\nDeposit ₦3,000 → play with ₦18,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>Start here:</b> https://1wzpdo.life/casino/list?open=register&p=z0ln","images":["bonus1.jpeg"]},
{"date":"2026-05-07","time":"23:55","content":"💚 <b>₦2,000 test → ₦7,500 withdrawal ✅</b>\n\nReal story. This week. Kofi, Accra.\n\nDeposited ₦2,000 Monday — just to test the system.\nBet Premier League Tuesday. Won ₦5,500. Easy pick.\nWithdrew ₦7,500 Thursday. PalmPay. 4 minutes. 💸\n\n\"I tested small first. Chale — now I trust 1WIN.\" 🔥\nIf Kofi can do it — my guy, you can too. ACT NOW.\n\nDeposit ₦2,000 → play with ₦12,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>Test it:</b> https://1wzpdo.life/casino/list?open=register&p=z0ln","images":["bonus5.jpeg"]},

{"date":"2026-05-08","time":"12:00","content":"🎾 <b>$100 → $127.00. Lorenzo Musetti ✅</b>\n\nATP Madrid. Spain. Clay. Odds 1.27. 🇪🇸\n$27 profit. Musetti 6-4, 7-5. Dominated completely. 💸\n\nRanked higher. Clay court specialist. Data was obvious.\nMon ✅ Wed ✅ Fri ✅ Three wins. Pure analysis. Every week.\n\nSTOP WATCHING. They collecting. You still looking. 🔥\n\nDeposit ₦5,000 → play with ₦30,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>Join NOW:</b> https://1wzpdo.life/casino/list?open=register&p=z0ln","images":["win3.png"]},
{"date":"2026-05-08","time":"23:55","content":"⚠️ <b>Bonus expires TOMORROW midnight! ❌</b>\n\nRegistered this week? Your 600% dies TOMORROW. ⏰\nAfter midnight: ❌ Gone. Forever. No exceptions.\n\nOne deposit activates EVERYTHING right now.\nPalmPay. Opay. Zero fees. Arrives same minute. ✅\n\nNo dulling my guy — last chance. Deposit NOW. 🔥\n\nDeposit ₦5,000 → play with ₦35,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>NOW:</b> https://1wzpdo.life/casino/list?open=register&p=z0ln","images":["bonus6.jpeg"]},

{"date":"2026-05-09","time":"16:00","content":"🌐 <b>FortunoBet.com — This week results inside! ✅</b>\n\n3 wins. 2 withdrawals. All verified. All real. 💸\n₦117,600 + ₦95,550 — Both PalmPay. Both instant.\n\nSports. Casino. All partners. One platform. No wahala.\nChale — no hidden fees. Real payouts. Every time. 💰\n\nSmart bettors manage bankroll. Only bet what you can afford. 🙏\n\n👉 <b>Join community:</b> https://fortunobet.com\n👉 <b>Start here:</b> https://1wzpdo.life/casino/list?open=register&p=z0ln","images":["fortunobet1.png"]},
{"date":"2026-05-09","time":"21:00","content":"💸 <b>₦95,550 PalmPay — Arrived Thursday ✅</b>\n\nThursday 7 May. 01:39 PM. Real phone notification. 💚\n₦95,550 (~$65). ID: PPW-9938862. Same minute.\n\nBryan withdrew Thursday afternoon. No delay. No wahala.\nMy guy — this is what consistent betting looks like. 💸\n\n1WIN pays every time. PalmPay confirms every time. ✅\nYou can't collect what you never deposited. 🔥\n\nDeposit ₦5,000 → play with ₦30,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>Start:</b> https://1wzpdo.life/casino/list?open=register&p=z0ln","images":["withdrow1.png"]},

{"date":"2026-05-10","time":"16:00","content":"💚 <b>This week. Real results. Full transparency. ✅</b>\n\nMon: $150 → $223.50 ✅ Arsenal — strong home form.\nWed: $100 → $146.00 ✅ Liverpool — H2H was clear.\nFri: $100 → $127.00 ✅ Musetti — clay specialist.\n\nROI this week: +40% 📊\n₦117,600 + ₦95,550 = Both PalmPay instant. 💸\n\nTest small first. Smart bettors don't rush. 🙏\nThey won this week. Next week YOU start. 🔥\n\nDeposit ₦10,000 → play with ₦60,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>NOW:</b> https://1wzpdo.life/casino/list?open=register&p=z0ln","images":["withdrow2.png","withdrow1.png"]},
{"date":"2026-05-10","time":"23:55","content":"🎰 <b>+500% Bonus — LAST CHANCE TONIGHT! ❌</b>\n\n1WIN Casino. Top slots. Live dealers. 💰\nDeposit ₦5,000 → play with ₦30,000 + 500 spins.\n\nPalmPay. Opay. Zero fees. Withdraw tonight. ✅\nWeek closes MIDNIGHT. Bonus gone after. No second chance.\n\nWe test. We withdraw. We scale. Join us NOW or miss it. 🔥\n\nDeposit ₦5,000 → play with ₦30,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>Play NOW:</b> https://1wzpdo.life/casino/list?open=register&p=z0ln","images":["bonus4.jpeg"]}
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