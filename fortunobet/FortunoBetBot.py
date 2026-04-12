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
 
# ========== MONDAY APRIL 13 (2 posts) ==========
{"date":"2026-04-13","time":"12:00","content":"⚽ <b>$100 → $184. West Ham United ✅</b>\n\nEngland Premier League. Odds 1.84. 🏴󠁧󠁢󠁥󠁮󠁧󠁿\n$84 profit. One match. Clean start. 💸\n\nWest Ham 3-0. Dominant win.\nThey followed Monday. Already in profit.\n\nYou're still watching? 🔥\n\nDeposit ₦10,000 → play with ₦60,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>Join NOW:</b> https://1wzpdo.life/casino/list?open=register&p=z4m5","images":["win1.png"]},
{"date":"2026-04-13","time":"00:00","content":"💸 <b>₦216,912 PalmPay — Arrived instant ✅</b>\n\nMarch 12, 10:32 PM. Real phone. 💚\n₦216,912 arrived same minute.\n\nNo delay. No wahala. Just money.\nWithdrawals work EVERY time.\n\nYou can't withdraw what you don't deposit. 🔥\n\nDeposit ₦10,000 → play with ₦60,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>Start:</b> https://1wzpdo.life/casino/list?open=register&p=z4m5","images":["with1.png"]},
 
# ========== TUESDAY APRIL 14 (2 posts) ==========
{"date":"2026-04-14","time":"22:00","content":"⚽ <b>$100 → $195. Manchester City ✅</b>\n\nEngland Premier League. Odds 1.95. 🏴󠁧󠁢󠁥󠁮󠁧󠁿\n$95 profit. One match. Pattern building. 💸\n\nMan City 3-0. Dominant performance.\nMon: $84 ✅ Wed: $95 ✅\n\nTwo days. Two wins. They're in profit.\nStill watching? 🔥\n\nDeposit ₦20,000 → play with ₦120,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>Join:</b> https://1wzpdo.life/casino/list?open=register&p=z4m5","images":["win2.png"]},
{"date":"2026-04-14","time":"12:00","content":"🎰 <b>RAKEBACK 50% — Lose? Get money back!</b>\n\nLose today? Get 50% back instantly. 💰\nNo other site does this.\n\nPromo: FORTUNOBET. Works now.\nThey're getting rakeback. You're watching. 🔥\n\nDeposit ₦20,000 → play with ₦120,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>Claim:</b> https://1wzpdo.life/casino/list?open=register&p=z4m5","images":["fortunobet5.jpeg"]},
 
# ========== WEDNESDAY APRIL 15 (2 posts) ==========
{"date":"2026-04-15","time":"12:00","content":"💚 <b>[WIN #3 - SEND SCREENSHOT TOMORROW]</b>\n\n[Sport]. Odds [X.XX]. 🏆\n$[XX] profit. Pattern continues. 💸\n\nMon: $84 ✅ Wed: $95 ✅ Fri: $[XX] ✅\nThree wins. All GREEN. Pattern proof.\n\nStill watching? 🔥\n\nDeposit ₦20,000 → play with ₦120,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>Join:</b> https://1wzpdo.life/casino/list?open=register&p=z4m5","images":["[WIN3]"]},
{"date":"2026-04-15","time":"00:00","content":"⚠️ <b>Bonus expires in 48 hours!</b>\n\nRegistered Monday? Expires Wed 11:59 PM.\nRegistered Tuesday? Expires Thu 11:59 PM. ⏰\n\n600% NOT lifetime. 48 hours only.\nAfter deadline: ❌ Gone forever.\n\nDeposit NOW or lose it. 🔥\n\nDeposit ₦5,000 → play with ₦35,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>NOW:</b> https://1wzpdo.life/casino/list?open=register&p=z4m5","images":["fortunobet1.jpeg"]},
 
# ========== THURSDAY APRIL 16 (2 posts) ==========
{"date":"2026-04-16","time":"12:00","content":"🎰 <b>500% BONUS — First deposits!</b>\n\n500% on your first deposit. 💰\nPromo: FORTUNOBET.\n\nFast payouts. High multipliers.\nThey deposited yesterday. Already playing. 🔥\n\nDeposit ₦10,000 → play with ₦60,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>Play:</b> https://1wzpdo.life/casino/list?open=register&p=z4m5","images":["fortunobet2.jpeg"]},
{"date":"2026-04-16","time":"00:00","content":"🎰 <b>PIÑATA WINS — 600% + 500FS!</b>\n\nCatch your win. 💰\n600% bonus + 500 free spins.\n\nFirst deposits only. Code: FORTUNOBET.\nThey're winning. You're watching. 🔥\n\nDeposit ₦10,000 → play with ₦70,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>Catch:</b> https://1wzpdo.life/casino/list?open=register&p=z4m5","images":["fortunobet.png"]},
 
# ========== FRIDAY APRIL 17 (2 posts) ==========
# {"date":"2026-04-17","time":"18:00","content":"📲 <b>Deposit ₦500 in 60 seconds ✅</b>\n\nOpay. Palmpay. MTN MoMo. All work. ⚡\nVideo shows every step. Real time.\n\n₦500 = less than one plate of food.\n₦500 → ₦3,000 (bonus works!) 💰\n\nSmart players test. Scared watch. 🔥\n\nDeposit ₦500 → play with ₦3,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>Test:</b> https://1wzpdo.life/casino/list?open=register&p=z4m5","images":["[YOUR VIDEO]"]},
{"date":"2026-04-17","time":"00:00","content":"🎰 <b>600% CRYPTO BONUS!</b>\n\nFirst crypto deposits get 600%. 💰\nBitcoin. Ethereum. USDT. All work.\n\nPromo: FORTUNOBET. Fast payouts.\nNo fees. They're depositing. You? 🔥\n\nDeposit ₦10,000 → play with ₦70,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>Claim:</b> https://1wzpdo.life/casino/list?open=register&p=z4m5","images":["fortunobet3.jpeg"]},
 
# ========== SATURDAY APRIL 18 (2 posts) ==========
{"date":"2026-04-18","time":"12:00","content":"🎰 <b>600% WELCOME BONUS!</b>\n\nNew players get 600% + bonuses. 💰\nPromo: FORTUNOBET.\n\nFast payouts. No fees.\nWeekend players already winning. 🔥\n\nDeposit ₦20,000 → play with ₦140,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>Play:</b> https://1wzpdo.life/casino/list?open=register&p=z4m5","images":["fortunobet.jpeg"]},
{"date":"2026-04-18","time":"00:00","content":"💸 <b>₦114,646 PalmPay — Instant ✅</b>\n\nMarch 14, 14:33. Real money. 💚\n₦114,646 arrived same minute.\n\nThis week: ₦216k + ₦114k = Both instant.\nTwo withdrawals. Pattern proof. 🔥\n\nYou can't withdraw what you don't deposit.\n\nDeposit ₦10,000 → play with ₦60,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>Start:</b> https://1wzpdo.life/casino/list?open=register&p=z4m5","images":["with2.png"]},
 
# ========== SUNDAY APRIL 19 (3 posts) ==========
{"date":"2026-04-19","time":"12:00","content":"🏆 <b>FORTUNOBET VIP — 95% Win Rate!</b>\n\n2+ expert picks daily. All sports. 💰\n\n✅ Exact odds · Exact picks\n✅ Pre-match analysis\n✅ Track record daily\n\n💎 <b>JOIN:</b>\n⚡ 7 Days — $1 (50 Stars)\n💎 30 Days — $3 (150 Stars)\n🎁 FREE: Share with 5 friends!\n\nThey're winning. You're watching. 🔥\n\n👉 <b>VIP:</b> https://t.me/FortunoVIPbot","images":["vip.jpg"]},
{"date":"2026-04-19","time":"17:00","content":"💚 <b>Week 8 summary. All results. ✅</b>\n\nMon: $100 → $184 ✅\nWed: $100 → $195 ✅\nFri: $100 → $[XX] ✅\n\nThree wins. Two withdrawals.\n₦216,912 + ₦114,646 = Both instant. 💸\n\nThey deposited Monday. Withdrew profits Friday.\nYou watched all week. 🔥\n\nDeposit ₦100,000 → play with ₦600,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>NOW:</b> https://1wzpdo.life/casino/list?open=register&p=z4m5","images":["with1.png","with2.png"]},
{"date":"2026-04-19","time":"00:00","content":"⏰ <b>Bonus expires TONIGHT!</b>\n\nRegistered this week? ⚠️ Last hours:\n\nFri register = Expires 11:59 PM tonight\nSat register = Expires Mon 11:59 PM\n\nAfter midnight: ❌ No 600%. Gone.\n\nDeposit NOW or lose it forever. 🔥\n\nDeposit ₦10,000 → play with ₦70,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>LAST CHANCE:</b> https://1wzpdo.life/casino/list?open=register&p=z4m5","images":["fortunobet4.jpeg"]},
 
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