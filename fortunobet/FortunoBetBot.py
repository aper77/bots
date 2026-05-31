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
{"date":"2026-05-25","time":"13:00","content":"🎮 <b>$150 → $205.50. Team Spirit ✅</b>\n\nPGL Astana. CS2 Esports. Odds 1.37. 🏆\n$55.50 profit. Team Spirit vs MOUZ. Dominated. 💸\n\nTeam Spirit stronger form. Data clear. Easy read.\nChale — Monday pick already paid. ✅\n\nYou dey watch while others dey collect? STOP WATCHING. 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>Join NOW:</b> https://1win.com/betting?open=register&p=10ov","images":["win1.png"]},
{"date":"2026-05-25","time":"23:55","content":"💸 <b>GH₵1,300 MTN Mobile Money — Arrived instant ✅</b>\n\nMonday 25 May. 05:12 AM. Real phone notification. 💚\nGH₵1,300 (~$110). ID: MTN-7732020. Same minute.\n\nKofi tested small first. Then scaled up big.\nNo delay. No wahala. Chale — just pure money. 💸\n\n1WIN pays. MTN confirms. Every single time. ✅\nYou can't collect what you never deposited. ACT NOW. 🔥\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 <b>Start NOW:</b> https://1win.com/betting?open=register&p=10ov","images":["withdrow1.png"]},
{"date":"2026-05-26","time":"16:00","content":"💡 <b>How to win big on 1WIN Casino — explained</b>\n\nChale, most people play wrong. Here is how smart players do it.\n\nStep 1: Start small — GH₵5 per spin only\nStep 2: Play Fortune Tiger or Gates of Olympus 🎰\nStep 3: Stop after doubling. Withdraw to MTN Mobile Money. Same day. 💸\n\nTest small first. Smart bettors don't rush. 🙏\nShare this with 2 friends who play casino! 🔥\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 <b>Start here:</b> https://1win.com/betting?open=register&p=10ov","images":["bonus7.jpeg"]},
{"date":"2026-05-26","time":"23:55","content":"🌐 <b>FortunoBet.com — Smart bettors already inside!</b>\n\n1WIN. Sports. Casino. Live games. All partners. 💰\nGH₵1,300 paid Monday. Real MTN proof. Not story. ✅\n\nWhile you dey read this — they dey collect. 💸\nChale — how long you go keep watching? 🔥\n\nThey don enter. You still dey outside. JOIN NOW.\n\nDeposit GH₵100 → play with GH₵600\n🔑 Code: <code>fortunobet</code>\n👉 <b>Join community:</b> https://fortunobet.com\n👉 <b>Start NOW:</b> https://1win.com/betting?open=register&p=10ov","images":["bonus3.jpeg"]},
{"date":"2026-05-27","time":"12:00","content":"⚽ <b>$100 → $154.00. Lens ✅</b>\n\nFrance Cup. Odds 1.54. 🇫🇷\n$54 profit. Lens vs Nice. Completely dominant. 💸\n\nLens strong home form. Data was clear. Easy read.\nMon ✅ Tue ✅ Wed ✅ Pattern is real, my guy.\n\nSTOP WATCHING. They collecting. JOIN NOW. 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>Join NOW:</b> https://1win.com/betting?open=register&p=10ov","images":["win2.png"]},
{"date":"2026-05-27","time":"23:55","content":"🚨 <b>Another withdrawal completed today. ✅</b>\n\nSome people are still watching.\nOthers already withdrew this week.\n\nKofi deposited Monday. Withdrew same day. MTN confirmed. 💸\nThe opportunity is still open right now.\n\nChale — how long you go keep waiting? No dulling. 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>NOW:</b> https://1win.com/betting?open=register&p=10ov","images":["bonus1.jpeg"]},
{"date":"2026-05-28","time":"16:00","content":"📊 <b>3 mistakes Ghanaian bettors make every week</b>\n\nChale, I see this every week. Stop making these mistakes.\n\n❌ Mistake 1: Betting big — no control. Lose everything.\n❌ Mistake 2: Random channels — no analysis. Pure luck.\n❌ Mistake 3: Chasing losses — emotion kills bankroll.\n\nFortunoBet community avoids all 3. Join NOW.\nTag 2 friends who dey make these mistakes. No dulling! 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>JOIN NOW:</b> https://1win.com/betting?open=register&p=10ov","images":["bonus5.jpeg"]},
{"date":"2026-05-28","time":"23:55","content":"💚 <b>GH₵200 test → GH₵650 withdrawal ✅</b>\n\nReal story. This week. Kwame, Accra.\n\nDeposited GH₵200 Monday — just to test the system.\nBet France Cup Wednesday. Form obvious. Won GH₵450.\nWithdrew GH₵650 Thursday. MTN Mobile Money. 4 minutes. 💸\n\n\"I tested small first. Chale — now I trust 1WIN.\" 🙏\nIf Kwame can do it — my guy, you can too.\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 <b>Test it NOW:</b> https://1win.com/betting?open=register&p=10ov","images":["bonus6.jpeg"]},
{"date":"2026-05-29","time":"12:00","content":"🎾 <b>Buse looked shaky first set. Chat nervous. 😂</b>\n\nATP Hamburg. Clay. Odds 1.29. 🇩🇪\nThen suddenly — complete domination. 6-1, 6-4. 💸\n\n$100 → $129.00. Glad I entered early. Cashout sweet. 💸\nMon ✅ Wed ✅ Fri ✅ Smart bettors already inside. 👀\n\nSTOP WATCHING. They collecting. JOIN NOW. 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>Join NOW:</b> https://r1wexmo.life/betting?open=register&p=t02b","images":["win3.png"]},
{"date":"2026-05-29","time":"15:00","content":"👀 This one still in \"reading phase\".\n\nPlayers testing each other on clay… no real control yet.\nWhoever breaks first will take momentum 🎾","images":[]},
{"date":"2026-05-29","time":"23:55","content":"💸 <b>GH₵1,050 MTN Mobile Money — Arrived instant ✅</b>\n\nFriday 29 May. Real phone notification. 💚\nGH₵1,050. ID: MTN confirmed. Same minute.\n\nOne deposit activates everything right now.\nMTN Mobile Money. Zero fees. Arrives same minute. ✅\n\n1WIN pays. MTN confirms. Every time. ✅\nYou can't collect what you never deposited. ACT NOW. 🔥\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 <b>NOW:</b> https://r1wexmo.life/betting?open=register&p=t02b","images":["bonus2.jpeg"]},
{"date":"2026-05-30","time":"16:00","content":"🌐 <b>FortunoBet.com — Results this week. All real. ✅</b>\n\n3 wins. 2 withdrawals. Verified. Real. Not story. 💸\nGH₵1,300 + GH₵1,050 — Both MTN Mobile Money. Instant.\n\nWhile you dey wait — they dey collect every week.\nChale — smart bettors don enter already. 🔥\n\nYou still dey outside? Last chance. JOIN NOW.\n\nDeposit GH₵100 → play with GH₵600\n🔑 Code: <code>fortunobet</code>\n👉 <b>Join community:</b> https://fortunobet.com\n👉 <b>Start NOW:</b> https://r1wexmo.life/betting?open=register&p=t02b","images":["bonus4.jpeg"]},
{"date":"2026-05-30","time":"21:00","content":"💸 <b>Kofi almost didn't deposit. Thought fake site. 😂</b>\n\nWednesday 27 May. 09:42 AM. Real MTN notification. 💚\nGH₵1,050 (~$89). ID: MTN-7732019. Arrived instant.\n\nTested GH₵50 first. Withdrew same day. Now he trusts.\nChale — that is exactly how smart bettors start. 🙏\n\n1WIN pays. MTN confirms. Every time. ✅\nYou can't collect what you never deposited. ACT NOW. 🔥\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 <b>Start NOW:</b> https://r1wexmo.life/betting?open=register&p=t02b","images":["withdrow2.png"]},
{"date":"2026-05-31","time":"14:00","content":"💚 <b>This week. Real results. Full transparency. ✅</b>\n\nMon: $150 → $205.50 ✅ Team Spirit — stronger form.\nWed: $100 → $154.00 ✅ Lens — strong home form.\nFri: $100 → $129.00 ✅ Buse — clay specialist.\n\nROI +38% 📊 GH₵1,300 + GH₵1,050 = Both MTN instant. 💸\n\nThey collected this week. Next week YOU start. NOW. 🔥\nChale — share with 2 betting friends! Help them join! 💸\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>JOIN NOW:</b> https://r1wexmo.life/betting?open=register&p=t02b","images":["withdrow1.png","withdrow2.png"]},
{"date":"2026-05-31","time":"23:55","content":"🎰 <b>500% Bonus — LAST CHANCE TONIGHT! ❌</b>\n\n1WIN Casino. Fortune Tiger. Gates of Olympus. 💰\nDeposit GH₵50 → play with GH₵300 + 500 spins.\n\nMTN Mobile Money. Zero fees. Withdraw tonight. ✅\nWeek closes MIDNIGHT. Bonus gone. No second chance.\n\nWe test. We withdraw. We scale. JOIN NOW or miss it. 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>Play NOW:</b> https://r1wexmo.life/betting?open=register&p=t02b","images":["bonus3.jpeg"]}
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