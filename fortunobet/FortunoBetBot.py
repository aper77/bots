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

posts = [

# ========== MONDAY APRIL 6 ==========
{"date":"2026-04-06","time":"14:00","content":"💚 <b>$100 → $128. Rafael Jodar ✅</b>\n\nATP Marrakech. Morocco. Clay. 🎾\nOdds 1.28 — safe tennis bet.\n\n$28 profit. One match. Clean start.\nNew week. First prediction. GREEN. 💸\n\nLast week: 4 wins, 0 losses, 10 deposits.\nThis week: Already winning.\n\nSTOP WATCHING. Start winning. 🔥\n\nDeposit ₦10,000 → play with ₦60,000\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Join NOW:</b>\nhttps://1wfafs.life/casino/list?open=register&p=z4m5","images":["win1.png"]},
{"date":"2026-04-06","time":"23:30","content":"💸 <b>₦66,200 PalmPay — Arrived instant ✅</b>\n\nMarch 5, 12:37 PM.\nPalmPay notification. Real phone. 💚\n\n₦66,200 arrived same minute.\nNo delay. No wahala. Just money.\n\nWithdrawals work EVERY time.\nYou can't withdraw what you don't deposit. 🔥\n\nDeposit ₦10,000 → play with ₦60,000\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Start:</b>\nhttps://1wfafs.life/casino/list?open=register&p=z4m5","images":["withdrow1.png"]},

# ========== TUESDAY APRIL 7 ==========
{"date":"2026-04-07","time":"14:00","content":"🎰 <b>PLAY POKER — Bonus waiting on 1WIN!</b>\n\nTexas Hold'em. Live tables. Real players. 💰\nYour bonus is waiting. Promo code ready.\n\nFast payouts. High multipliers.\nNo fees on deposits or withdrawals. ✅\n\nSTOP WATCHING. Start playing. 🔥\n\nDeposit ₦20,000 → play with ₦120,000\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Play NOW:</b>\nhttps://1wfafs.life/casino/list?open=register&p=z4m5","images":["fortunobet.jpeg"]},
{"date":"2026-04-07","time":"23:30","content":"🎰 <b>PIÑATA WINS — 600% + 500 FREE SPINS!</b>\n\nCatch your win in Piñata. 💰\nWelcome bonus: 600% + 500FS.\n\nFirst deposits only. Code FORTUNOBET.\nFast payouts. High multipliers. 🔥\n\nDeposit ₦10,000 → play with ₦70,000\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Claim NOW:</b>\nhttps://1wfafs.life/casino/list?open=register&p=z4m5","images":["fortunobet.png"]},

# ========== WEDNESDAY APRIL 8 ==========
{"date":"2026-04-08","time":"14:00","content":"💚 <b>$100 → $118. Ugo Humbert ✅</b>\n\nATP Monte-Carlo. Monaco. Clay. 🎾\nOdds 1.18 — ultra safe.\n\n$18 profit. One match.\nTwo days. Two wins. Pattern building. 💸\n\nMon: $28 ✅ Wed: $18 ✅\nThey deposited Monday. Already in profit.\n\nYou're still watching? 🔥\n\nDeposit ₦20,000 → play with ₦120,000\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Join:</b>\nhttps://1wfafs.life/casino/list?open=register&p=z4m5","images":["win2.png"]},
{"date":"2026-04-08","time":"23:30","content":"⚠️ <b>Bonus expires 48 hours after registration!</b>\n\nRegistered Monday? Expires Wednesday 11:59 PM.\nRegistered Tuesday? Expires Thursday 11:59 PM.\n\n600% bonus NOT lifetime. 48 hours only. ⏰\n\nAfter deadline: ❌ No bonus. Gone forever.\n\nDeposit before midnight or lose it. 🔥\n\nDeposit ₦5,000 → play with ₦35,000\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Deposit NOW:</b>\nhttps://1wfafs.life/casino/list?open=register&p=z4m5","images":["fortunobet.png"]},

# ========== THURSDAY APRIL 9 ==========
{"date":"2026-04-09","time":"13:00","content":"🎰 <b>TOWER RUSH — Climb & claim your prize!</b>\n\n500% on first deposits. ⚡\nClimb to the top. Win big.\n\nFast payouts. High multipliers.\nNo fees. Code FORTUNOBET. 🔥\n\nDeposit ₦10,000 → play with ₦60,000\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Climb NOW:</b>\nhttps://1wfafs.life/casino/list?open=register&p=z4m5","images":["fortunobet1.jpeg"]},
{"date":"2026-04-09","time":"19:00","content":"🎰 <b>FORTUNOSLOTS IS LIVE — 99% RTP</b>\n\nNo apps. Just Click & Play. ⚡️\nOpay, Palmpay, MoMo instant payouts. 💸\n\n🎁 FIRST 5 PLAYERS NOW:\nGet 5 FREE SPINS instantly. 📈\n\nSTOP WATCHING. Your turn NOW. 🔥\n\n👉 <b>PLAY:</b>\nhttps://t.me/FortunoSlotsbot","images":["fortunoslotsbot.jpg"]},
{"date":"2026-04-09","time":"23:30","content":"🚀 <b>ROCKET X — 500% first deposits!</b>\n\nRocket X by 1WIN. Blast off. 💰\n500% bonus. Promo code: FORTUNOBET.\n\nFast payouts. High multipliers.\nNo fees deposits or withdrawals. 🔥\n\nDeposit ₦10,000 → play with ₦60,000\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Launch NOW:</b>\nhttps://1wfafs.life/casino/list?open=register&p=z4m5","images":["fortunobet2.jpeg"]},

# ========== FRIDAY APRIL 10 ==========
{"date":"2026-04-10","time":"14:00","content":"💚 <b>[EMPTY - ADD 3RD WIN HERE]</b>\n\n[Sport/Event details]\n[Odds details]\n\n[Profit line]\n[Week context: Mon + Wed + Fri wins]\n\n[Aggressive challenge] 🔥\n\nDeposit ₦20,000 → play with ₦120,000\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Join:</b>\nhttps://1wfafs.life/casino/list?open=register&p=z4m5","images":["[win3.png - ADD TOMORROW]"]},
{"date":"2026-04-10","time":"23:30","content":"🎰 <b>BOOK OF DEAD — Unlock Egypt's treasures!</b>\n\n500% on first deposits. ⚡\nEnter promo code: FORTUNOBET.\n\nPlay now. Unlock treasures.\nFast payouts. High multipliers. 💰\n\nDeposit ₦10,000 → play with ₦60,000\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Unlock NOW:</b>\nhttps://1wfafs.life/casino/list?open=register&p=z4m5","images":["fortunobet3.jpeg"]},

# ========== SATURDAY APRIL 11 ==========
{"date":"2026-04-11","time":"11:00","content":"💸 <b>₦70,560 PalmPay — Instant arrival ✅</b>\n\nMarch 7, 14:04 PM.\nPalmPay notification. Real money. 💚\n\n₦70,560 arrived same minute.\nThis week: ₦66k + ₦70k = Both instant.\n\nTwo withdrawals. Both arrived. Pattern proof. 🔥\n\nYou can't withdraw what you don't deposit.\n\nDeposit ₦10,000 → play with ₦60,000\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Start:</b>\nhttps://1wfafs.life/casino/list?open=register&p=z4m5","images":["withdrow2.png"]},
{"date":"2026-04-11","time":"19:00","content":"🎰 <b>FORTUNOSLOTS IS LIVE — 99% RTP</b>\n\nNo apps. Just Click & Play. ⚡️\nOpay, Palmpay, MoMo instant payouts. 💸\n\n🎁 FIRST 5 PLAYERS NOW:\nGet 5 FREE SPINS instantly. 📈\n\nSTOP WATCHING. Your turn NOW. 🔥\n\n👉 <b>PLAY:</b>\nhttps://t.me/FortunoSlotsbot","images":["fortunoslotsbot.jpg"]},
{"date":"2026-04-11","time":"23:00","content":"🎰 <b>PLAY POKER — Your winnings waiting!</b>\n\nLive poker. Real tables. Real money. 💰\nPromo code FORTUNOBET active.\n\nFast payouts. High multipliers.\nNo fees. Welcome bonuses ready. 🔥\n\nDeposit ₦20,000 → play with ₦120,000\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Play NOW:</b>\nhttps://1wfafs.life/casino/list?open=register&p=z4m5","images":["fortunobet4.jpeg"]},

# ========== SUNDAY APRIL 12 ==========
{"date":"2026-04-12","time":"11:00","content":"💚 <b>Week 7 results. Honest. Everything. ✅</b>\n\nMon: $100 → $128 ✅\nWed: $100 → $118 ✅\nFri: [ADD 3RD WIN] ✅\n\n[UPDATE: Three wins this week when ready]\nTwo withdrawals: ₦66,200 + ₦70,560 = Both instant. 💸\n\nShowed everything. Wins. Withdrawals. Real results.\nThey deposited Monday. Already withdrew profits.\n\nYou watched all week. STOP WATCHING. 🔥\n\nDeposit ₦100,000 → play with ₦600,000\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Your turn NOW:</b>\nhttps://1wfafs.life/casino/list?open=register&p=z4m5","images":["withdrow1.png","withdrow2.png"]},
{"date":"2026-04-12","time":"22:00","content":"⏰ <b>Last chance. Bonus expires tonight!</b>\n\nRegistered this week? 48-hour closing:\n\n⚠️ Fri register = Expires Sun 11:59 PM\n⚠️ Sat register = Expires Mon 11:59 PM\n\nAfter midnight: ❌ No 600% bonus. Gone forever.\n\nDeposit before midnight or lose it all. 🔥\n\nDeposit ₦10,000 → play with ₦70,000\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Last chance:</b>\nhttps://1wfafs.life/casino/list?open=register&p=z4m5","images":["fortunobet3.jpeg"]},

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