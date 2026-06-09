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

{"date": "2026-06-08", "time": "16:00", "content": "🎾 <b>Aryna Sabalenka ✅ Roland Garros Women</b>\n\nRoland Garros. Odds 1.19. 🏆\n$100 → $119. Score 7-5 / 6-3. Dominated. 💸\n\nClay form elite. Data clear. E easy be. Kofi same type — won. 🎯\nSTOP WATCHING. They collecting. Pick ONE. Place it now. 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>PLACE YOUR BET:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["1win1.png"]},
{"date": "2026-06-08", "time": "20:00", "content": "🎯 Placing this now. Knicks vs Spurs. NBA. Odds 1.77.\nKnicks home strong. Spurs weak away. Entering now. 👀\n👉 https://one-vv858.com/betting/prematch/basketball-23?p=z4m5", "images": []},
{"date": "2026-06-08", "time": "23:55", "content": "💸 <b>GH₵825 from ONE bet. MTN instant. ✅</b>\n\nMonday 08 June. 06:00 AM. Real notification. 💚\nGH₵825 (~$55 USD). ID: 7732041. Same minute.\n\nONE bet. GH₵50. Placed. Won. Withdrew same day. Chale. 💸\n\nTry it yourself. ONE bet. GH₵50. See what happens. 🙏\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 <b>Test it yourself:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["08waiting.png", "08completed.png"]},
{"date": "2026-06-09", "time": "16:00", "content": "💡 <b>How to place your first bet — 30 seconds</b>\n\nChale, e simple. Here is what smart bettors do.\n\nOpen 1WIN → find ONE match → GH₵50 → place bet. 🎯\nWin → withdraw MTN same day. That is it. 💸\n\nChannel members doing this every week — you dey outside.\nKofi placed ONE bet. Withdrew GH₵825. Share with 2 friends! No dulling.\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 <b>Test it yourself:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["educashon.jpeg"]},
{"date": "2026-06-09", "time": "23:55", "content": "⚡ <b>GH₵825 from ONE bet. Arrived instant. ✅</b>\n\nMonday 08 June. 06:00 AM. Real MTN. 💚\nID: 7732041. Same minute. Zero fees. No wahala.\n\nSome still thinking. Kofi placed ONE bet — withdrew same day. Chale. 💸\n\nOne bet. GH₵50. Test it yourself. 🙏\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 <b>Test it yourself:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["08fast.png"]},

{"date": "2026-06-10", "time": "12:00", "content": "🏀 <b>CSKA Moscow + Germany ✅ Multiple</b>\n\nVTB + Friendlies. Odds 1.42. 🏆\n$80 → $113.60. Both locked. Controlled. 💸\n\nCSKA home clear. Germany H2H easy. Data sharp. E easy be. 🎯\nSTOP WATCHING. They collecting. Pick ONE. GO. 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>PLACE YOUR BET:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["1win2.png"]},
{"date": "2026-06-10", "time": "20:00", "content": "🎯 Placing this now. Live.\n\nNew York Knicks vs San Antonio Spurs. NBA.\nKnicks home strong. Spurs away weak. Odds 1.79.\n\nEntering on 1WIN now. 👀\n👉 https://one-vv858.com/betting/prematch/basketball-23?p=z4m5", "images": []}
{"date": "2026-06-10", "time": "23:55", "content": "🚨 <b>Weekend fixtures loading. Odds closing. ✅</b>\n\nBig matches Friday. Chale — window closing now. 💸\nGH₵825 Monday. ONE bet. Real proof. 💚\n\nKofi placed ONE match. Same chance open tonight.\nPick ONE. GH₵50. Place before odds move. No dulling. 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>PLACE YOUR BET:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["urgencyWed.jpeg"]},
{"date": "2026-06-11", "time": "16:00", "content": "📊 <b>Smart bettors pick ONE bet. Every week.</b>\n\nChale, wrong approach kills bankroll.\n\n❌ Many matches — lose control.\n❌ Random picks — pure luck.\n✅ ONE match. Clear data. GH₵50. Place it. Withdraw. 💸\n\nKofi did this — withdrew GH₵825. Weekend loading — odds closing.\nPick YOUR one bet NOW before odds drop. No dulling! 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>PLACE YOUR BET:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["Authority.jpeg"]},
{"date": "2026-06-11", "time": "23:55", "content": "💚 <b>Kofi placed ONE bet → withdrew GH₵825 ✅</b>\n\nReal story. This week. Kofi, Accra.\n\nONE tennis match. GH₵50. Clay form obvious. Won big. 💸\nWithdrew same day. ID: 7732041. Instant.\n\nSame odds open now — smart bettors always enter early.\nPlace your first bet today. 🙏\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 <b>Test it yourself:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["08fast.png"]},
{"date": "2026-06-12", "time": "12:00", "content": "⚽ <b>Brazil ✅ World Friendlies</b>\n\nWorld Friendlies. Odds 1.12. 🏆\n$100 → $112. Score 6-2. Dominated. 💸\n\nBrazil home elite. H2H clear. E easy be. 🎯\nSTOP WATCHING. They collecting. Pick ONE. GO. 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>PLACE YOUR BET:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["1win3.png"]},
{"date": "2026-06-12", "time": "20:00", "content": "😂 [REACTION — Fri June 12 — add your short reaction after today win]", "images": []},
{"date": "2026-06-12", "time": "23:55", "content": "🏆 <b>Placed Sunday. Withdrew Monday. Same day.</b>\n\nSabalenka. Roland Garros. Odds 1.19. ✅\nProfit $119. MTN GH₵825. ID: 7732041. Instant. ✅\n\nAnother withdrawal confirmed today — proof right here. 💚\nKofi ONE bet. Won. Withdrew Monday 06:00 AM. Chale. 💸\n\nSame chance NOW. Pick ONE. Place it. Withdraw tomorrow. 🔥\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 <b>Test it yourself:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["10waiting.png", "10complated.png"]},
{"date": "2026-06-13", "time": "16:00", "content": "⚡ <b>GH₵650 from ONE bet. Instant. ✅</b>\n\nFriday 12 June. 11:12 AM. Real MTN. 💚\nID: MTN-7732043. Same minute. Zero fees. No wahala.\n\nSunday matches loading now. Odds won't stay. Chale. 💸\n\nPick ONE Sunday match. GH₵50. Place before odds drop. 🔥\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 <b>Test it yourself:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["1win1.png", "08fast.png"]},
{"date": "2026-06-13", "time": "20:00", "content": "😂 [REACTION — Sat June 13 — add your short reaction about MTN payout]", "images": []},
{"date": "2026-06-13", "time": "21:00", "content": "🎰 <b>500% Bonus — active tonight only! ❌</b>\n\n1WIN Casino. Fortune Tiger. Gates of Olympus. 💰\nGH₵50 → play with GH₵300 + 500 free spins. Chale.\n\nPromo code works now — not guaranteed tomorrow. ⚠️\nKofi withdrew GH₵825 this week. No dulling. 💸\n\nPlace your casino bet tonight. JOIN NOW. 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>PLACE YOUR BET:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["12fast.png"]},
{"date": "2026-06-14", "time": "16:00", "content": "💚 <b>This week. 3 bets. 3 wins. Real. ✅</b>\n\nMon: $100→$119 ✅ Sabalenka. Clay data clear.\nWed: $80→$113.60 ✅ CSKA+Germany. H2H obvious.\nFri: $100→$112 ✅ Brazil. Home form locked.\n\nGH₵825 + GH₵930 + GH₵650 = ONE bet each. MTN instant. 💸\nSome watched all week. Others collected. You still watching? JOIN NOW. 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>PLACE YOUR BET:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["08fast.png", "10fast.png", "12fast.png"]},
{"date": "2026-06-14", "time": "23:55", "content": "🎰 <b>500% Bonus — active tonight only! ❌</b>\n\n1WIN Casino. Fortune Tiger. Gates of Olympus. 💰\nGH₵50 → play with GH₵300 + 500 free spins. Chale.\n\nPromo code works now — not guaranteed tomorrow. ⚠️\nKofi withdrew GH₵825. They collecting. No dulling. 💸\n\nPlace your bet before bonus expires. JOIN NOW. 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>PLACE YOUR BET:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["casinosun.jpeg"]},

{"date": "2026-06-15", "time": "12:00", "content": "🏀 <b>Oklahoma City Thunder ✅ USA NBA</b>\n\nNBA Playoffs. Odds 1.49. 🏆\n$70 → $104.30. Final 127-114. Dominated. 💸\n\nOKC home court elite. Data clear. H2H obvious. E easy be. 🎯\nSTOP WATCHING. They collecting. Pick ONE. Place it. GO. 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>PLACE YOUR BET:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["2win1.png"]},
{"date": "2026-06-15", "time": "20:00", "content": "🎯 [LIVE BET — Mon June 15 — add real game + league + odds]", "images": []},
{"date": "2026-06-15", "time": "23:55", "content": "💸 <b>GH₵450 MTN Mobile Money — Instant. ✅</b>\n\nMonday 15 June. 05:10 AM. Real notification. 💚\nGH₵450 (~$30 USD). ID: MTN-7732023. Same minute.\n\nAnother withdrawal confirmed today — proof right here. 💚\nKofi ONE bet. GH₵50. Withdrew same day. Chale. 💸\n\nTest it yourself. ONE bet. GH₵50. 🙏\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 <b>Test it yourself:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["15waiting.png", "15fast.png"]},
{"date": "2026-06-16", "time": "16:00", "content": "💡 <b>How to place your first bet — 30 seconds</b>\n\nChale, e simple. Here is what smart bettors do.\n\nOpen 1WIN → find ONE match → GH₵50 → place bet. 🎯\nWin → withdraw MTN same day. That is it. 💸\n\nChannel members doing this every week — you dey outside.\nKofi placed ONE bet. Withdrew GH₵450. Share with 2 friends! No dulling.\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 <b>Test it yourself:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["bonus1.jpeg"]},
{"date": "2026-06-16", "time": "23:55", "content": "⚡ <b>GH₵450 from ONE bet. Arrived instant. ✅</b>\n\nMonday 15 June. 05:10 AM. Real MTN. 💚\nID: MTN-7732023. Same minute. Zero fees. No wahala.\n\nSome still thinking. Kofi placed ONE bet — withdrew same day. Chale. 💸\n\nOne bet. GH₵50. See the result yourself. 🙏\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 <b>Test it yourself:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["15fast.png"]},
{"date": "2026-06-17", "time": "12:00", "content": "🏀 <b>Dallas Wings W ✅ USA WNBA</b>\n\nUSA WNBA. Odds 1.15. 🏆\n$50 → $57.50. Final 79-56. Dominated. 💸\n\nDallas home elite. H2H obvious. E easy be. Chale. 🎯\nSTOP WATCHING. They collecting. Pick ONE. GO. 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>PLACE YOUR BET:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["2win2.png"]},
{"date": "2026-06-17", "time": "20:00", "content": "😂 [REACTION — Wed June 17 — add your short reaction after today win]", "images": []},
{"date": "2026-06-17", "time": "23:55", "content": "🚨 <b>Members withdrew twice this week already. ✅</b>\n\nGH₵450 Monday. MTN instant. Real proof. 💚\nChannel members collecting — you dey watch outside.\n\nKofi withdrew Monday 05:10 AM. Same minute. Chale. 💸\nPick ONE bet tonight. GH₵50. How long you go watch? GO. 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>PLACE YOUR BET:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["bonus2.jpeg"]},
{"date": "2026-06-18", "time": "16:00", "content": "📊 <b>3 mistakes Ghana bettors make every week</b>\n\nChale, stop making these mistakes.\n\n❌ Betting big — lose everything fast.\n❌ Random channels — pure luck.\n❌ Chasing losses — emotion kills bankroll.\n\nKofi ONE bet — withdrew GH₵450. Weekend loading — odds closing.\nPick ONE match now before odds drop. No dulling! 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>PLACE YOUR BET:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["bonus3.jpeg"]},
{"date": "2026-06-18", "time": "23:55", "content": "💚 <b>Kofi placed ONE bet → withdrew GH₵450 ✅</b>\n\nReal story. This week. Kofi, Accra.\n\nONE NBA match. GH₵50. Home court obvious. Won big. 💸\nWithdrew same day. ID: MTN-7732023. Instant.\n\nSame odds open now — smart bettors always enter early. Chale.\nPlace your first bet today. 🙏\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 <b>Test it yourself:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["15fast.png"]},
{"date": "2026-06-19", "time": "12:00", "content": "🎾 <b>Flavio Cobolli ✅ Roland Garros Men</b>\n\nRoland Garros. Odds 1.13. 🏆\n$90 → $101.70. Score 6-2/6-3/7-6. Dominated. 💸\n\nClay form elite. Baseline locked. H2H clear. E easy be. 🎯\nSTOP WATCHING. They collecting. Pick ONE. GO. 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>PLACE YOUR BET:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["2win3.png"]},
{"date": "2026-06-19", "time": "20:00", "content": "😂 [REACTION — Fri June 19 — add your short reaction after today win]", "images": []},
{"date": "2026-06-19", "time": "23:55", "content": "💸 <b>GH₵750 MTN Mobile Money — Instant. ✅</b>\n\nWednesday 17 June. 06:43 AM. Real notification. 💚\nGH₵750 (~$50 USD). ID: MTN-7732024. Same minute.\n\nONE bet. Disciplined. GH₵50. Withdrew same day. Chale. 💸\nWeekend matches loading — last chance before odds drop.\n\nONE match. GH₵50. Test it yourself. 🙏\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 <b>Test it yourself:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["17waiting.png", "17fast.png"]},
{"date": "2026-06-20", "time": "16:00", "content": "🏆 <b>Placed May. Withdrew Monday. Same day.</b>\n\nOKC Thunder. NBA. Odds 1.49. ✅\nProfit $104.30. MTN GH₵450. ID: MTN-7732023. Instant. ✅\n\nKofi ONE bet. Withdrew Monday 05:10 AM. Chale. 💸\nOdds won't stay — enter before they close. No dulling. 🔥\n\nTest it yourself. ONE bet. GH₵50. 🙏\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 <b>Test it yourself:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["2win1.png", "15fast.png"]},
{"date": "2026-06-20", "time": "20:00", "content": "😂 [REACTION — Sat June 20 — add your short reaction about MTN payout]", "images": []},
{"date": "2026-06-20", "time": "21:00", "content": "⚡ <b>GH₵1,200 MTN Mobile Money — Instant. ✅</b>\n\nFriday 19 June. 11:32 AM. Real MTN. 💚\nID: MTN-7732025. Same minute. Zero fees. No wahala.\n\nSunday fixtures loading now. Odds won't stay. Chale. 💸\nKofi placed ONE bet — withdrew same day. Same chance open.\n\nPick ONE match. GH₵50. Test small first. 🙏\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 <b>Test it yourself:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["19fast.png"]},
{"date": "2026-06-21", "time": "16:00", "content": "💚 <b>This week. 3 bets. 3 wins. Real. ✅</b>\n\nMon: $70→$104.30 ✅ OKC. Home court clear.\nWed: $50→$57.50 ✅ Dallas Wings. Form obvious.\nFri: $90→$101.70 ✅ Cobolli. Clay data clear.\n\nGH₵450 + GH₵750 + GH₵1,200 = ONE bet each. MTN instant. 💸\nSome watched all week. Others collected. You still watching? JOIN NOW. 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>PLACE YOUR BET:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["15fast.png", "17fast.png", "19fast.png"]},
{"date": "2026-06-21", "time": "23:55", "content": "🎰 <b>500% Bonus — active tonight only! ❌</b>\n\n1WIN Casino. Fortune Tiger. Gates of Olympus. 💰\nGH₵50 → play with GH₵300 + 500 free spins. Chale.\n\nPromo code works now — not guaranteed tomorrow. ⚠️\nKofi withdrew GH₵1,200 this week. No dulling. 💸\n\nPlace your bet tonight before bonus expires. JOIN NOW. 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>PLACE YOUR BET:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["bonus4.jpeg"]}
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