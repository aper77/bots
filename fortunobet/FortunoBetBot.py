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
{"date": "2026-06-08", "time": "23:55", "content": "💸 <b>GH₵825 from ONE bet. MTN instant. ✅</b>\n\nMonday 08 June. 06:00 AM. Real notification. 💚\nGH₵825 (~$55 USD). ID: 7732041. Same minute.\n\nSabalenka was on clay. Roland Garros. Form was obvious.\nKofi backed it. Won. Withdrew before breakfast. Chale. 💸\n\nSame kind of match loads every week. Back it yourself. 🙏\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 <b>Test it yourself:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["08waiting.png", "08completed.png"]},
{"date": "2026-06-09", "time": "16:00", "content": "💡 <b>Why smart bettors start small every time</b>\n\nChale, the mistake most people make is rushing. Here is what works.\n\nFind ONE match you actually understand. Football. Tennis. NBA. 🎯\nBack it with GH₵50. Watch what happens. Withdraw same day. 💸\n\nChannel members doing this every week — you dey outside.\nKofi backed Sabalenka. Withdrew GH₵825. Share with 2 friends! No dulling.\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 <b>Test it yourself:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["educashon.jpeg"]},
{"date": "2026-06-09", "time": "23:55", "content": "⚡ <b>GH₵825 arrived. Instant. No wahala. ✅</b>\n\nMonday 08 June. 06:00 AM. Real MTN. 💚\nID: 7732041. Same minute. Zero fees.\n\nSome people still overthinking. Kofi just backed the form — withdrew same morning. Chale. 💸\nWhile they thinking — he collected. The platform works.\n\nBack it yourself. Find out. 🙏\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 <b>Test it yourself:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["08fast.png"]},

{"date": "2026-06-10", "time": "12:00", "content": "🏀 <b>CSKA Moscow + Germany ✅ Multiple</b>\n\nVTB + Friendlies. Odds 1.42. 🏆\n$80 → $113.60. Both locked. Controlled. 💸\n\nCSKA home clear. Germany H2H easy. Data sharp. E easy be. 🎯\nSTOP WATCHING. They collecting. Pick ONE. GO. 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>PLACE YOUR BET:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["1win2.png"]},
{"date": "2026-06-10", "time": "20:00", "content": "🎯 Placing this now. Knicks vs Spurs. NBA. Odds 1.79.\nKnicks home strong. Spurs weak away. Entering now. 👀\n👉 https://one-vv858.com/betting/prematch/basketball-23?p=z4m5", "images": []},
{"date": "2026-06-10", "time": "23:55", "content": "🚨 <b>Weekend fixtures loading. Odds closing. ✅</b>\n\nBig matches Friday. Chale — window closing now. 💸\nSabalenka paid Monday. CSKA paid today. Real proof. 💚\n\nTwo wins. Two withdrawals. Same week. Same platform.\nPick ONE match tonight before the odds shift. No dulling. 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>PLACE YOUR BET:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["urgencyWed.jpeg"]},
{"date": "2026-06-11", "time": "16:00", "content": "📊 <b>Smart bettors pick ONE bet. Every week.</b>\n\nChale, wrong approach kills bankroll.\n\n❌ Many matches — lose control.\n❌ Random picks — pure luck.\n✅ Back what you understand. Small. Disciplined. Withdraw. 💸\n\nKofi backed clay tennis — form was obvious. Withdrew GH₵825.\nWeekend loading — find YOUR match before odds close. 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>PLACE YOUR BET:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["Authority.jpeg"]},
{"date": "2026-06-11", "time": "23:55", "content": "💚 <b>Kofi backed Sabalenka → withdrew GH₵825 ✅</b>\n\nReal story. This week. Kofi, Accra.\n\nRoland Garros. Clay surface. Sabalenka dominant all tournament.\nKofi watched the data, backed it, withdrew Monday morning. 💸\nID: 7732041. MTN. Instant.\n\nSame quality matches load every week on 1WIN.\nFind yours. Back it. See what happens. 🙏\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 <b>Test it yourself:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["08fast.png"]},
{"date": "2026-06-12", "time": "12:00", "content": "⚽ <b>Brazil ✅ World Friendlies</b>\n\nWorld Friendlies. Odds 1.12. 🏆\n$100 → $112. Score 6-2. Dominated. 💸\n\nBrazil home elite. H2H clear. E easy be. 🎯\nSTOP WATCHING. They collecting. Pick ONE. GO. 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>PLACE YOUR BET:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["1win3.png"]},
{"date": "2026-06-12", "time": "20:00", "content": "😂 [REACTION — Fri June 12 — add your short reaction after today win]", "images": []},
{"date": "2026-06-12", "time": "23:55", "content": "🏆 <b>Backed Sunday. Withdrew Monday. Same day.</b>\n\nSabalenka. Roland Garros. Odds 1.19. ✅\nGH₵825 withdrawn. ID: 7732041. MTN instant. ✅\n\nAnother withdrawal confirmed today — proof right here. 💚\nKofi backed clay form. Won. Withdrew before breakfast. Chale. 💸\n\nSome still watching. Smart bettors backed already. JOIN NOW. 🔥\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 <b>Test it yourself:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["10waiting.png", "10complated.png"]},
{"date": "2026-06-13", "time": "16:00", "content": "⚡ <b>GH₵650 from ONE bet. Instant. ✅</b>\n\nFriday 12 June. 11:12 AM. Real MTN. 💚\nID: MTN-7732043. Same minute. Zero fees. No wahala.\n\nBrazil at home. Panama had no chance. Form was clear from warmup.\nKofi read it right. Backed it. GH₵650 before midday. 💸\n\nSunday fixtures up now. Find your pick before odds drop. 🔥\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 <b>Test it yourself:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["1win1.png", "08fast.png"]},
{"date": "2026-06-13", "time": "20:00", "content": "😂 [REACTION — Sat June 13 — add your short reaction about MTN payout]", "images": []},
{"date": "2026-06-13", "time": "21:00", "content": "🎰 <b>500% Bonus — active tonight only! ❌</b>\n\n1WIN Casino. Fortune Tiger. Gates of Olympus. 💰\nGH₵50 → play with GH₵300 + 500 free spins. Chale.\n\nPromo code works now — not guaranteed tomorrow. ⚠️\nKofi withdrew GH₵825 this week. No dulling. 💸\n\nPlace your casino bet tonight. JOIN NOW. 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>PLACE YOUR BET:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["12fast.png"]},
{"date": "2026-06-14", "time": "16:00", "content": "💚 <b>This week. 3 different picks. 3 wins. Real. ✅</b>\n\nMon: Sabalenka ✅ Roland Garros. Clay form obvious.\nWed: CSKA + Germany ✅ VTB + Friendlies. H2H data clear.\nFri: Brazil ✅ World Friendlies. Home dominance locked.\n\nGH₵825 + GH₵930 + GH₵650 = All MTN. All instant. 💸\nSome watched all week. Others collected. You still watching? JOIN NOW. 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>PLACE YOUR BET:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["08fast.png", "10fast.png", "12fast.png"]},
{"date": "2026-06-14", "time": "23:55", "content": "🎰 <b>500% Bonus — active tonight only! ❌</b>\n\n1WIN Casino. Fortune Tiger. Gates of Olympus. 💰\nGH₵50 → play with GH₵300 + 500 free spins. Chale.\n\nPromo code works now — not guaranteed tomorrow. ⚠️\nThree payouts this week. GH₵825 + GH₵930 + GH₵650. No dulling. 💸\n\nPlace your bet before bonus expires. JOIN NOW. 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>PLACE YOUR BET:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["casinosun.jpeg"]},

{"date": "2026-06-15", "time": "16:00", "content": "🏀 <b>Oklahoma City Thunder ✅ USA NBA</b>\n\nNBA Playoffs. Odds 1.49. 🏆\n$70 → $104.30. Final 127-114. Dominated. 💸\n\nOKC home court elite. Data clear. H2H obvious. E easy be. 🎯\nSTOP WATCHING. They collecting. Pick ONE. Place it. GO. 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>PLACE YOUR BET:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["2win1.png"]},
{"date": "2026-06-15", "time": "20:00", "content": "🎯 [LIVE BET — Mon June 15 — add real game + league + odds]", "images": []},
{"date": "2026-06-15", "time": "23:55", "content": "💸 <b>GH₵450 MTN Mobile Money — Instant. ✅</b>\n\nMonday 15 June. 05:10 AM. Real notification. 💚\nGH₵450 (~$30 USD). ID: MTN-7732023. Same minute.\n\nOKC were at home. Spurs had no answers all game.\nKwame backed it early. Withdrew before work. Chale. 💸\n\nSame quality data loads every week. Back it yourself. 🙏\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 <b>Test it yourself:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["15waiting.png", "15fast.png"]},
{"date": "2026-06-16", "time": "16:00", "content": "💡 <b>How to place your first bet — 30 seconds</b>\n\nChale, e simple. Here is what smart bettors do.\n\nOpen 1WIN → find ONE match → GH₵50 → place bet. 🎯\nWin → withdraw MTN same day. That is it. 💸\n\nChannel members doing this every week — you dey outside.\nKwame placed ONE bet. Withdrew GH₵450. Share with 2 friends! No dulling.\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 <b>Test it yourself:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["bonus1.jpeg"]},
{"date": "2026-06-16", "time": "23:55", "content": "⚡ <b>GH₵450 arrived. Instant. No wahala. ✅</b>\n\nMonday 15 June. 05:10 AM. Real MTN. 💚\nID: MTN-7732023. Same minute. Zero fees.\n\nSome people still scrolling. Kwame already backed OKC — withdrew same morning. Chale. 💸\n\nThe platform works. The only question is when you try it. 🙏\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 <b>Test it yourself:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["15fast.png"]},
{"date": "2026-06-17", "time": "12:00", "content": "🏀 <b>Dallas Wings W ✅ USA WNBA</b>\n\nUSA WNBA. Odds 1.15. 🏆\n$50 → $57.50. Final 79-56. Dominated. 💸\n\nDallas home elite. H2H obvious. E easy be. Chale. 🎯\nSTOP WATCHING. They collecting. Pick ONE. GO. 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>PLACE YOUR BET:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["2win2.png"]},
{"date": "2026-06-17", "time": "20:00", "content": "😂 [REACTION — Wed June 17 — add your short reaction after today win]", "images": []},
{"date": "2026-06-17", "time": "23:55", "content": "🚨 <b>Members withdrew twice this week already. ✅</b>\n\nGH₵450 Monday. GH₵750 today. MTN instant. Real proof. 💚\nChannel members collecting — you dey watch outside.\n\nOKC paid. Dallas Wings paid. Two different sports. Same result.\nPick ONE match tonight before odds shift. How long you go watch? 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>PLACE YOUR BET:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["bonus2.jpeg"]},
{"date": "2026-06-18", "time": "16:00", "content": "📊 <b>3 mistakes Ghana bettors make every week</b>\n\nChale, stop making these mistakes.\n\n❌ Betting big — lose everything fast.\n❌ Random channels — no data, pure luck.\n❌ Chasing losses — emotion kills bankroll.\n\nKwame ONE pick — backed OKC home form. Withdrew GH₵450.\nWeekend fixtures loading — find yours before odds close. 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>PLACE YOUR BET:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["bonus3.jpeg"]},
{"date": "2026-06-18", "time": "23:55", "content": "💚 <b>Kwame backed OKC → withdrew GH₵450 ✅</b>\n\nReal story. This week. Kwame, Kumasi.\n\nNBA Playoffs. OKC at home. Defence elite all series. Chale.\nKwame read the data. Backed it Monday. Withdrew same morning. 💸\nID: MTN-7732023. MTN. GH₵450. Instant.\n\nSame quality matches load every week. Find yours. Back it. 🙏\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 <b>Test it yourself:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["15fast.png"]},
{"date": "2026-06-19", "time": "12:00", "content": "🎾 <b>Flavio Cobolli ✅ Roland Garros Men</b>\n\nRoland Garros. Odds 1.13. 🏆\n$90 → $101.70. Score 6-2/6-3/7-6. Dominated. 💸\n\nClay form elite. Baseline locked. H2H clear. E easy be. 🎯\nSTOP WATCHING. They collecting. Pick ONE. GO. 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>PLACE YOUR BET:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["2win3.png"]},
{"date": "2026-06-19", "time": "20:00", "content": "😂 [REACTION — Fri June 19 — add your short reaction after today win]", "images": []},
{"date": "2026-06-19", "time": "23:55", "content": "💸 <b>GH₵750 MTN Mobile Money — Instant. ✅</b>\n\nWednesday 17 June. 06:43 AM. Real notification. 💚\nGH₵750 (~$50 USD). ID: MTN-7732024. Same minute.\n\nDallas Wings at home. Seattle had no answers.\nKwame backed the form. Withdrew before morning. Chale. 💸\nWeekend matches loading — last chance before odds drop.\n\nBack yours today. No dulling. 🙏\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 <b>Test it yourself:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["17waiting.png", "17fast.png"]},
{"date": "2026-06-20", "time": "16:00", "content": "🏆 <b>Backed Monday. Withdrew same day.</b>\n\nOKC Thunder. NBA Playoffs. Odds 1.49. ✅\nProfit $104.30. MTN GH₵450. ID: MTN-7732023. Instant. ✅\n\nOKC home record was clear all playoffs. Kwame read it early.\nWithdrew before Kumasi even woke up. Chale. 💸\n\nOdds won't stay. Find your pick now. No dulling. JOIN NOW. 🔥\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 <b>Test it yourself:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["2win1.png", "15fast.png"]},
{"date": "2026-06-20", "time": "20:00", "content": "😂 [REACTION — Sat June 20 — add your short reaction about MTN payout]", "images": []},
{"date": "2026-06-20", "time": "21:00", "content": "⚡ <b>GH₵1,200 MTN Mobile Money — Instant. ✅</b>\n\nFriday 19 June. 11:32 AM. Real MTN. 💚\nID: MTN-7732025. Same minute. Zero fees. No wahala.\n\nCobolli on clay. Roland Garros. Form was elite.\nKwame backed it Friday. GH₵1,200 before lunch. 💸\n\nSunday fixtures loading. Find your pick. Test small first. 🙏\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 <b>Test it yourself:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["19fast.png"]},
{"date": "2026-06-21", "time": "16:00", "content": "💚 <b>This week. 3 different picks. 3 wins. Real. ✅</b>\n\nMon: OKC Thunder ✅ NBA Playoffs. Home court dominant.\nWed: Dallas Wings ✅ WNBA. Form locked all 4 quarters.\nFri: Cobolli ✅ Roland Garros. Clay specialist at home.\n\nGH₵450 + GH₵750 + GH₵1,200 = All MTN. All instant. 💸\nThree sports. Three payouts. You still watching? JOIN NOW. 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>PLACE YOUR BET:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["15fast.png", "17fast.png", "19fast.png"]},
{"date": "2026-06-21", "time": "23:55", "content": "🎰 <b>500% Bonus — active tonight only! ❌</b>\n\n1WIN Casino. Fortune Tiger. Gates of Olympus. 💰\nGH₵50 → play with GH₵300 + 500 free spins. Chale.\n\nPromo code works now — not guaranteed tomorrow. ⚠️\nThree payouts this week. GH₵450 + GH₵750 + GH₵1,200. No dulling. 💸\n\nPlace your bet before bonus expires. JOIN NOW. 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>PLACE YOUR BET:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["bonus4.jpeg"]}
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