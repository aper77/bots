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

[
{"date":"2026-04-20","time":"22:00","content":"🎾 <b>$80 → $92.80. Tyler Zink ✅</b>\n\nATP Challenger Savannah. USA. Odds 1.16. 🇺🇸\nZink ranked higher. Recent form: 4 wins in last 5. Easy read. 💸\n\nWon 6-3, 6-3. Dominant. Pure data — not luck.\nMy guy, they followed Monday. Already in profit. ✅\n\nYou dey watch while others dey collect? 🔥\n\nDeposit ₦3,000 → play with ₦18,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>Join NOW:</b> https://1wzpdo.life/casino/list?open=register&p=z4m5","images":["win1.png"]},

{"date":"2026-04-21","time":"14:00","content":"🎰 <b>500% Bonus + 500 Free Spins — 1WIN Casino!</b>\n\nTop slots. Live dealers. Best odds tonight. 💰\nDeposit ₦5,000 → play with ₦35,000 + 500 spins.\n\nPalmPay. Opay. Zero fees. Withdraw same day. ✅\nChale — Promo FORTUNOBET. Tonight only.\n\nThey don enter. You still dey watch? 🔥\n\nDeposit ₦5,000 → play with ₦35,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>Play NOW:</b> https://1wzpdo.life/casino/list?open=register&p=z4m5","images":["fortunobet3.jpeg"]},
{"date":"2026-04-21","time":"21:00","content":"💸 <b>₦52,500 PalmPay — Arrived instant ✅</b>\n\nApril 20. 12:32 PM. Real phone notification. 💚\n₦52,500 arrived same minute. ID: PPW-9938829.\n\nNo delay. No wahala. My guy — just pure money.\nChale, 1WIN pays. PalmPay confirms. Every single time. ✅\n\nYou can't withdraw what you don't deposit. 🔥\n\nDeposit ₦5,000 → play with ₦30,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>Start NOW:</b> https://1wzpdo.life/casino/list?open=register&p=z4m5","images":["withdrow1.png"]},

{"date":"2026-04-22","time":"13:00","content":"🎾 <b>$75 → $107.25. Express Bet ✅</b>\n\n2 matches. ATP Challengers. Odds 1.43. 🎾\n$32.25 profit. Both picks won. Form was clear. 💸\n\nFeldbausch ✅ Cerundolo ✅ — Pure analysis, not luck.\nMon ✅ Tue ✅ Wed ✅ Pattern is real, my guy.\n\nYou dey watch while others dey collect? 🔥\n\nDeposit ₦5,000 → play with ₦30,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>Join:</b> https://1wzpdo.life/casino/list?open=register&p=z4m5","images":["win3.png"]},
{"date":"2026-04-23","time":"01:43","content":"🌐 <b>FortunoBet.com — Where Smart Bettors Win!</b>\n\n1WIN. Sports. Casino. Live games. All partners. 💰\nData-based. Transparent. Real results every week. ✅\n\nThousands of Nigerians and Ghanaians winning daily.\nChale — all verified. Join the winning community.\n\nThey dey win. You still dey outside? 🔥\n\nDeposit ₦10,000 → play with ₦60,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>Join the community:</b> https://fortunobet.com","images":["fortunobet1.png"]},

{"date":"2026-04-23","time":"12:00","content":"🎰 <b>1WIN Sport — Top Leagues. Best Odds Tonight!</b>\n\nPremier League. Champions League. Real odds. 💰\nDeposit ₦3,000 → play with ₦21,000 + 500 spins.\n\nPalmPay. Opay. No fees. Instant withdrawals. ✅\nFastest withdrawal this week: 5 minutes. No dulling.\n\nSmart guys don enter. You still dey think? 🔥\n\nDeposit ₦3,000 → play with ₦21,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>Bet NOW:</b> https://1wzpdo.life/casino/list?open=register&p=z4m5","images":["1winpromosport.jpeg"]},
{"date":"2026-04-23","time":"23:55","content":"💚 <b>₦4,000 test → ₦11,500 withdrawal ✅</b>\n\nReal story. This week. Emmanuel, Lagos.\n\nDeposited ₦4,000 Monday — just to test the system.\nBet tennis Tuesday. Form was obvious. Won ₦7,500.\nWithdrew ₦11,500 Wednesday. PalmPay. 4 minutes. 💸\n\n\"I tested small first. Chale — now I trust 1WIN.\" 🔥\n\nDeposit ₦4,000 → play with ₦24,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>Test it:</b> https://1wzpdo.life/casino/list?open=register&p=z4m5","images":["fortunobetpromo4.png"]},

{"date":"2026-04-24","time":"12:00","content":"🎾 <b>$80 → $106.40. Bruno Kuzuhara ✅</b>\n\nATP Challenger Savannah. USA. Odds 1.33. 🇺🇸\n$26.40 profit. Kuzuhara 7-5, 6-2. Ranked higher. Easy read. 💸\n\nMon ✅ Tue ✅ Fri ✅ Three wins. Pure analysis.\nMy guy — this na skill, not luck.\n\nSmart players follow. Scared ones watch. 🔥\n\nDeposit ₦5,000 → play with ₦30,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>Join NOW:</b> https://1wzpdo.life/casino/list?open=register&p=z4m5","images":["win2.png"]},
{"date":"2026-04-24","time":"23:55","content":"⚠️ <b>600% Bonus expires in 48 hours!</b>\n\nRegistered Monday? Expires Wed 11:59 PM.\nRegistered Tuesday? Expires Thu 11:59 PM. ⏰\n\n600% NOT lifetime. 48 hours only.\nChale — after deadline: ❌ Gone forever.\n\nNo dulling. Deposit NOW or lose it. 🔥\n\nDeposit ₦5,000 → play with ₦35,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>NOW:</b> https://1wzpdo.life/casino/list?open=register&p=z4m5","images":["fortunobet1.jpeg"]},

{"date":"2026-04-25","time":"13:00","content":"🌐 <b>FortunoBet.com — This week results inside! ✅</b>\n\n3 wins. 2 withdrawals. All verified this week. 💸\n₦52,500 + ₦72,000 — Both PalmPay. Both instant.\n\nSports. Casino. All top partners. One platform.\nChale — no hidden fees. No wahala. Real payouts. 💰\n\nSmart bettors manage their bankroll. Only bet what you can afford. 🙏\n\n👉 <b>Join the winning community:</b> https://fortunobet.com","images":["fortunobet1.png"]},
{"date":"2026-04-25","time":"22:00","content":"💸 <b>₦72,000 PalmPay — Arrived tonight ✅</b>\n\nApril 23. 20:33. Real phone notification. 💚\n₦72,000 (~$48). ID: PPW-9938829. Same minute.\n\nNo delay. No wahala. My guy — just pure money.\n1WIN pays. PalmPay confirms. Every single time. ✅\n\nYou can't withdraw what you don't deposit. 🔥\n\nDeposit ₦5,000 → play with ₦30,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>Start:</b> https://1wzpdo.life/casino/list?open=register&p=z4m5","images":["withdrow2.png"]},

{"date":"2026-04-26","time":"12:00","content":"💚 <b>This week summary. Real results. ✅</b>\n\nMon: $80 → $106.40 ✅ Kuzuhara — ranked higher. Easy.\nTue: $80 → $92.80 ✅ Zink — form was clear.\nWed: $75 → $107.25 ✅ Express — 2 picks, both won.\n\n₦52,500 + ₦72,000 = Both PalmPay instant. 💸\nChale — they deposited Monday. Withdrew Friday.\n\nYou watched all week. 🔥\n\nDeposit ₦10,000 → play with ₦60,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>NOW:</b> https://1wzpdo.life/casino/list?open=register&p=z4m5","images":["withdrow1.png","withdrow2.png"]},
{"date":"2026-04-26","time":"23:55","content":"🎰 <b>+600% Bonus — Last chance this week! ✅</b>\n\n1WIN Casino. Top slots. Live dealers. 💰\nDeposit ₦5,000 → play with ₦35,000 + 500 spins.\n\nPalmPay. Opay. Zero fees. Withdraw tonight. ✅\nWeek closes midnight. No dulling — bonus gone after.\n\nMy guy, deposit NOW or miss it forever. 🔥\n\nDeposit ₦5,000 → play with ₦35,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>Play NOW:</b> https://1wzpdo.life/casino/list?open=register&p=z4m5","images":["fortunobet2.jpeg"]}
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