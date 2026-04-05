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

{"date":"2026-03-30","time":"14:00","content":"💚 <b>We predicted it. It landed. $100 → $149 ✅</b>\n\nSV Werder Bremen W. Germany Bundesliga. ⚽\nOur call: Werder Bremen W to win. Odds 1.49.\n\nFull time: Werder Bremen 2 — SGS Essen 1.\nExact result. $49 profit. One match. 💸\n\nThis is not luck. This is analysis.\nEvery week we call it. Every week it lands.\n\nYou watched last week. They deposited and won.\nStill watching this week? 🔥\n\nDeposit ₦10,000 → play with ₦60,000\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Join the winning side:</b>\nhttps://1wfafs.life/casino/list?open=register&p=z4m5","images":["win1.png"]},
{"date":"2026-03-30","time":"23:30","content":"💸 <b>₦67,522 in my PalmPay. This morning. ✅</b>\n\nMon 30 March. 06:30 AM.\nPalmPay alert. Real phone. Real notification. 💚\n\n₦67,522 arrived same minute I requested.\nNo delay. No form. No wahala.\n\nThis is how easy withdrawal is:\nClick withdraw on 1WIN → money in PalmPay in 60 seconds.\n\nYou can't withdraw what you don't deposit. 🔥\n\nDeposit ₦10,000 → play with ₦60,000\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Start tonight:</b>\nhttps://1wfafs.life/casino/list?open=register&p=z4m5","images":["withdrow1.png"]},

{"date":"2026-03-31","time":"14:00","content":"📲 <b>Watch this. Deposit done in 60 seconds. ✅</b>\n\nOpay. Palmpay. MTN MoMo. All work.\nI recorded every step. Watch the video.\n\nOpen 1WIN. Click deposit. Choose Palmpay.\nEnter ₦500. Confirm. Done. Balance shows instantly. ⚡\n\nNo bank visit. No form. No wahala.\n₦500 minimum — less than one plate of food.\n\nSmart players test first. Scared players keep watching. 🔥\n\nDeposit ₦500 → play with ₦3,000\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Try it now:</b>\nhttps://1wfafs.life/casino/list?open=register&p=z4m5","images":[]},
{"date":"2026-03-31","time":"23:30","content":"🎰 <b>Crazy Time hitting 20,000x multipliers tonight</b>\n\nLive dealer. Real money. Real withdrawals.\nOne spin changed lives this week. 💰\n\nCasino players win bigger and faster than sports bettors.\nSame platform. Same PalmPay withdrawal you saw this morning.\n\nDeposit ₦5,000 → spin with ₦30,000.\n500 Free Spins waiting with our code.\n\nAre you in or still watching? 🔥\n\nDeposit ₦5,000 → play with ₦30,000\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Spin now:</b>\nhttps://1wfafs.life/casino/list?open=register&p=z4m5","images":["fortunobet1.jpeg"]},

{"date":"2026-04-01","time":"14:00","content":"💚 <b>$90 → $130.50. Turkey. World Cup Qualifier. ✅</b>\n\nEurope FIFA WC 2026 Qualification. ⚽\nOur call: Turkey to win. Odds 1.45.\n\nFull time: Turkey 1 — Romania 0.\nAnother prediction. Another win. $40.50 profit. 💸\n\nMonday: $49 ✅\nWednesday: $40.50 ✅\nTwo calls. Two wins. Analysis working.\n\nThey deposited Monday. Already in profit. You? 🔥\n\nDeposit ₦20,000 → play with ₦120,000\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Join NOW:</b>\nhttps://1wfafs.life/casino/list?open=register&p=z4m5","images":["win2.png"]},
{"date":"2026-04-01","time":"23:30","content":"⚠️ <b>Bonus expires 48 hours after registration</b>\n\n1WIN. 500% on first deposit. 500 Free Spins.\nRegister with code fortunobet — bonus activates instantly. ✅\n\nRegistered Monday? Expires Wednesday 11:59 PM.\nRegistered Tuesday? Expires Thursday 11:59 PM.\n\n500% isn't lifetime. You have 48 hours. ⏰\n\nAfter deadline:\n❌ No 500% bonus. Regular deposit only. You missed it.\n\nDeposit before midnight or lose it forever. 🔥\n\nDeposit ₦5,000 → play with ₦30,000\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Deposit NOW:</b>\nhttps://1wfafs.life/casino/list?open=register&p=z4m5","images":["fortunobet13.jpeg"]},

{"date":"2026-04-02","time":"13:00","content":"🎰 <b>Piñata Wins — Super Mega Win dropping tonight</b>\n\n1WIN Casino. High multipliers. 💰\nOne spin. Life changed. 🔥\n\nLose today? 30% cashback automatic.\nNo claim needed. 💚\n\nOther platforms = lose forever. ❌\nHere = 30% back tomorrow. \nSmart players choose protection.\n\nDeposit ₦20,000 → play with ₦120,000\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Play now:</b>\nhttps://1wfafs.life/casino/list?open=register&p=z4m5","images":["fortunobet12.png"]},
{"date":"2026-04-02","time":"19:00","content":"🎰 <b>FORTUNOSLOTS IS LIVE — 99% RTP</b>\n\nNo apps. No codes. Just Click & Play. ⚡️\nOpay, Palmpay, & MoMo instant payouts. 💸\nHighest win rate in Nigeria & Ghana. 🇳🇬🇬🇭\n\n🎁 <b>FIRST 5 PLAYERS RIGHT NOW:</b>\nGet 5 FREE SPINS instantly.\nOne spin. Life changed. 📈\n\nStop watching from the sidelines.\nYour turn to win NOW. 🔥\n\n👉 <b>CLAIM SPINS & PLAY:</b>\nhttps://t.me/FortunoSlotsbot","images":["Slot4.jpg"]},
{"date":"2026-04-02","time":"23:30","content":"💚 <b>$100 → $131. Alexander Zverev ✅</b>\n\nATP Miami. USA. Hard. 🎾\nOdds 1.31 — safe tennis.\n\n$31 profit. One match.\n3rd win this week. All GREEN. 💸\n\nMon: $49 ✅ Wed: $40.50 ✅ Thu: $31 ✅\nHow many more wins do you need to see?\nSTOP WATCHING. 🔥\n\nDeposit ₦10,000 → play with ₦60,000\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Join the streak:</b>\nhttps://1wfafs.life/casino/list?open=register&p=z4m5","images":["win3.png"]},

{"date":"2026-04-03","time":"14:57","content":"💚 <b>$120 → $186. Friday Night Win. ✅</b>\n\nAnother prediction landed. $66 profit.\nWe call the wins before they happen.\n\nFour wins this week. Zero losses. 💸\nStop doubting. Start winning with us.\n\nDeposit ₦10,000 → play with ₦60,000\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Join the winning side:</b>\nhttps://1wfafs.life/casino/list?open=register&p=z4m5","images":["win4.png"]},
{"date":"2026-04-03","time":"23:30","content":"🏏 <b>IPL 2026 is live. Cricket Duel running hot. 🔥</b>\n\nBiggest cricket season of the year.\nEvery match = betting opportunity.\nEvery spin on Cricket Duel = multiplier chance. 💰\n\n600% bonus + 500 Free Spins still active.\nDeposit ₦10,000 → play with ₦70,000.\n\nPeople who joined Monday already bet 4 times this week.\nWhere are you?\n\nDeposit ₦10,000 → play with ₦70,000\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Play now:</b>\nhttps://1wfafs.life/casino/list?open=register&p=z4m5","images":["fortunobet2.jpeg"]},

{"date":"2026-04-04","time":"11:00","content":"💸 <b>₦42,000 payout. Saturday mood. ✅</b>\n\nPalmPay alert just hit. Fast and clean. 💚\nWe win on sports, we win on slots, we withdraw instantly.\n\nProof is right here. Real money. Real results.\nWithdrawal took less than 2 minutes. ⚡\n\nDeposit ₦5,000 → play with ₦30,000\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Start winning:</b>\nhttps://1wfafs.life/casino/list?open=register&p=z4m5","images":["withdrow2.png"]},
{"date":"2026-04-04","time":"19:00","content":"🎰 <b>FORTUNOSLOTS IS LIVE — 99% RTP</b>\n\nNo apps. No codes. Just Click & Play. ⚡️\nOpay, Palmpay, & MoMo instant payouts. 💸\nHighest win rate in Nigeria & Ghana. 🇳🇬🇬🇭\n\n🎁 <b>FIRST 5 PLAYERS RIGHT NOW:</b>\nGet 5 FREE SPINS instantly.\nOne spin. Life changed. 📈\n\nStop watching from the sidelines.\nYour turn to win NOW. 🔥\n\n👉 <b>CLAIM SPINS & PLAY:</b>\nhttps://t.me/FortunoSlotsbot","images":["Slot4.jpg"]},
{"date":"2026-04-04","time":"23:00","content":"🔥 <b>CLAIM 600% BONUS — FIRST DEPOSIT!</b>\n\n1WIN. 600% on first deposits. 💰\n+ 500 Free Spins with code FORTUNOBET.\n\nFast payouts. High multipliers.\nNo fees on deposits or withdrawals. ✅\n\nWelcome bonuses active NOW.\nDeposit ₦10,000 → play with ₦70,000. 🔥\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Claim NOW:</b>\nhttps://1wfafs.life/casino/list?open=register&p=z4m5","images":["fortunobet.jpeg"]},

{"date":"2026-04-05","time":"11:00","content":"💚 <b>Week 6 results. Everything. Honest. ✅</b>\n\nMon: $100 → $149 ✅\nWed: $90 → $130.50 ✅\nThu: $100 → $131 ✅\nFri: $120 → $186 ✅\n\nTwo withdrawals this week. PalmPay. Both arrived instant.\n\n4 wins. Showed every result. Showed every withdrawal.\nThey deposited Monday. Already withdrew profits. 💸\n\nYou watched the whole week. STOP WATCHING.\n\nDeposit ₦100,000 → play with ₦600,000\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Your turn NOW:</b>\nhttps://1wfafs.life/casino/list?open=register&p=z4m5","images":["withdrow1.png","withdrow2.png"]},
{"date":"2026-04-05","time":"22:00","content":"🎰 <b>PLAY NOW & CONQUER OLYMPUS!</b>\n\nGates of Olympus. 500% on first deposits. ⚡\nEnter promo code: FORTUNOBET\n\nFast payouts. High multipliers.\nNo fees on deposits or withdrawals. 💰\n\nOne spin. Life changed.\nDeposit ₦10,000 → play with ₦60,000. 🔥\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Conquer NOW:</b>\nhttps://1wfafs.life/casino/list?open=register&p=z4m5","images":["fortunobet052.jpeg"]}
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