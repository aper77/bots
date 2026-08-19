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
# {"date": "2026-06-15", "time": "12:00", "content": "🏀 <b>Oklahoma City Thunder ✅ USA NBA</b>\n\nNBA Playoffs. Odds 1.49. 🏆\n$70 → $104.30. Final 127-114. Dominated. 💸\n\nOKC home court elite. Data clear. H2H obvious. E easy be. 🎯\nSTOP WATCHING. They collecting. Pick ONE. Place it. GO. 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>PLACE YOUR BET:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["2win1.png"]},
# {"date": "2026-06-15", "time": "18:00", "content": "🎯 Placing this now. Spain vs Cape Verde. World Cup 2026.\nSpain home machine. Won 8 of last 10 at home. Odds 1.08.\nEntering on 1WIN now. 👀\n👉 https://one-vv3184.com/betting/match/sport/spain-vs-cape-verde-31345118", "images": []},
# {"date": "2026-06-15", "time": "23:55", "content": "💸 <b>GH₵450 MTN Mobile Money — Instant. ✅</b>\n\nMonday 15 June. 05:10 AM. Real notification. 💚\nGH₵450 (~$30 USD). ID: MTN-7732023. Same minute.\n\nOKC were at home. Spurs had no answers all game.\nKwame backed it early. Withdrew before work. Chale. 💸\n\nSame quality data loads every week. Back it yourself. 🙏\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 <b>Test it yourself:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["15waiting.png", "15fast.png"]},
# {"date": "2026-06-16", "time": "12:00", "content": "💡 <b>How to place your first bet — 30 seconds</b>\n\nChale, e simple. Here is what smart bettors do.\n\nOpen 1WIN → find ONE match → GH₵50 → place bet. 🎯\nWin → withdraw MTN same day. That is it. 💸\n\nChannel members doing this every week — you dey outside.\nKwame placed ONE bet. Withdrew GH₵450. Share with 2 friends! No dulling.\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 <b>Test it yourself:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["bonus1.jpeg"]},
# {"date": "2026-06-16", "time": "17:00", "content": "🤔 Real talk chale —\n\nFootball or basketball? Where you dey find your easy picks?\nTell us below 👇 Let's compare. 💬", "images": []},
# {"date": "2026-06-16", "time": "23:55", "content": "⚡ <b>GH₵450 arrived. Instant. No wahala. ✅</b>\n\nMonday 15 June. 05:10 AM. Real MTN. 💚\nID: MTN-7732023. Same minute. Zero fees.\n\nSome people still scrolling. Kwame already backed OKC — withdrew same morning. Chale. 💸\n\nThe platform works. The only question is when you try it. 🙏\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 <b>Test it yourself:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["15fast.png"]},
# {"date": "2026-06-17", "time": "12:00", "content": "🏀 <b>Dallas Wings W ✅ USA WNBA</b>\n\nUSA WNBA. Odds 1.15. 🏆\n$50 → $57.50. Final 79-56. Dominated. 💸\n\nDallas home elite. H2H obvious. E easy be. Chale. 🎯\nSTOP WATCHING. They collecting. Pick ONE. GO. 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>PLACE YOUR BET:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["2win2.png"]},
# {"date": "2026-06-17", "time": "19:00", "content": "🎯 Placing this now. Iraq vs Norway. World Cup 2026.\nNorway strong away. Won 11 of last 15. Odds 1.19.\nEntering on 1WIN now. 👀\n👉 https://one-vv3184.com/betting/match/sport/iraq-vs-norway-34065697", "images": []},
# {"date": "2026-06-17", "time": "23:55", "content": "🚨 <b>Members withdrew twice this week already. ✅</b>\n\nGH₵450 Monday. GH₵750 today. MTN instant. Real proof. 💚\nChannel members collecting — you dey watch outside.\n\nOKC paid. Dallas Wings paid. Two different sports. Same result.\nPick ONE match tonight before odds shift. How long you go watch? 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>PLACE YOUR BET:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["bonus2.jpeg"]},
# {"date": "2026-06-18", "time": "12:00", "content": "📊 <b>3 mistakes Ghana bettors make every week</b>\n\nChale, stop making these mistakes.\n\n❌ Betting big — lose everything fast.\n❌ Random channels — no data, pure luck.\n❌ Chasing losses — emotion kills bankroll.\n\nKwame ONE pick — backed OKC home form. Withdrew GH₵450.\nWeekend fixtures loading — find yours before odds close. 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>PLACE YOUR BET:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["bonus3.jpeg"]},
# {"date": "2026-06-18", "time": "18:00", "content": "💬 Anybody collected this week?\n\nShow your MTN alert below 👇\nReal wins only. Let's see who dey serious. 💸", "images": []},
# {"date": "2026-06-18", "time": "23:55", "content": "💚 <b>Kwame backed OKC → withdrew GH₵450 ✅</b>\n\nReal story. This week. Kwame, Kumasi.\n\nNBA Playoffs. OKC at home. Defence elite all series. Chale.\nKwame read the data. Backed it Monday. Withdrew same morning. 💸\nID: MTN-7732023. MTN. GH₵450. Instant.\n\nSame quality matches load every week. Find yours. Back it. 🙏\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 <b>Test it yourself:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["15fast.png"]},
# {"date": "2026-06-19", "time": "12:00", "content": "🎾 <b>Flavio Cobolli ✅ Roland Garros Men</b>\n\nRoland Garros. Odds 1.13. 🏆\n$90 → $101.70. Score 6-2/6-3/7-6. Dominated. 💸\n\nClay form elite. Baseline locked. H2H clear. E easy be. 🎯\nSTOP WATCHING. They collecting. Pick ONE. GO. 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>PLACE YOUR BET:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["2win3.png"]},
# {"date": "2026-06-19", "time": "18:00", "content": "🎯 Placing this now. Mexico vs Republic of Korea.\nBacking Mexico to win. Entering on 1WIN now. 👀\n👉 https://one-vv3184.com/betting/match/sport/mexico-vs-republic-of-korea-32343469", "images": []},
# {"date": "2026-06-19", "time": "23:55", "content": "💸 <b>GH₵750 MTN Mobile Money — Instant. ✅</b>\n\nWednesday 17 June. 06:43 AM. Real notification. 💚\nGH₵750 (~$50 USD). ID: MTN-7732024. Same minute.\n\nDallas Wings at home. Seattle had no answers.\nKwame backed the form. Withdrew before morning. Chale. 💸\nWeekend matches loading — last chance before odds drop.\n\nBack yours today. No dulling. 🙏\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 <b>Test it yourself:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["17waiting.png", "17fast.png"]},
# {"date": "2026-06-20", "time": "12:00", "content": "🏆 <b>Backed Monday. Withdrew same day.</b>\n\nOKC Thunder. NBA Playoffs. Odds 1.49. ✅\nProfit $104.30. MTN GH₵450. ID: MTN-7732023. Instant. ✅\n\nOKC home record was clear all playoffs. Kwame read it early.\nWithdrew before Kumasi even woke up. Chale. 💸\n\nOdds won't stay. Find your pick now. No dulling. JOIN NOW. 🔥\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 <b>Test it yourself:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["2win1.png", "15fast.png"]},
# {"date": "2026-06-20", "time": "18:00", "content": "🎯 Placing this now. Brazil vs Haiti. World Cup 2026.\nBacking Brazil to win. Entering on 1WIN now. 👀\n👉 https://one-vv3184.com/betting/match/sport/brazil-vs-haiti-32433289", "images": []},
# {"date": "2026-06-20", "time": "21:00", "content": "⚡ <b>GH₵1,200 MTN Mobile Money — Instant. ✅</b>\n\nFriday 19 June. 11:32 AM. Real MTN. 💚\nID: MTN-7732025. Same minute. Zero fees. No wahala.\n\nCobolli on clay. Roland Garros. Form was elite.\nKwame backed it Friday. GH₵1,200 before lunch. 💸\n\nSunday fixtures loading. Find your pick. Test small first. 🙏\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 <b>Test it yourself:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["19fast.png"]},
# {"date": "2026-06-21", "time": "12:00", "content": "💚 <b>This week. 3 different picks. 3 wins. Real. ✅</b>\n\nMon: OKC Thunder ✅ NBA Playoffs. Home court dominant.\nWed: Dallas Wings ✅ WNBA. Form locked all 4 quarters.\nFri: Cobolli ✅ Roland Garros. Clay specialist at home.\n\nGH₵450 + GH₵750 + GH₵1,200 = All MTN. All instant. 💸\nThree sports. Three payouts. You still watching? JOIN NOW. 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>PLACE YOUR BET:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["15fast.png", "17fast.png", "19fast.png"]},
# {"date": "2026-06-21", "time": "18:00", "content": "😂 Weekend done — who won?\n\nDrop your biggest win below 👇\nNext week we go again. Chale who ready? 🔥", "images": []},
# {"date": "2026-06-21", "time": "23:55", "content": "🎰 <b>500% Bonus — active tonight only! ❌</b>\n\n1WIN Casino. Fortune Tiger. Gates of Olympus. 💰\nGH₵50 → play with GH₵300 + 500 free spins. Chale.\n\nPromo code works now — not guaranteed tomorrow. ⚠️\nThree payouts this week. GH₵450 + GH₵750 + GH₵1,200. No dulling. 💸\n\nPlace your bet before bonus expires. JOIN NOW. 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>PLACE YOUR BET:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["bonus4.jpeg"]},



  {"date":"2026-08-17","time":"17:06","content":"🚨 <b>ODDS MOVING — KICKOFF IN 25 MINS</b>\nBoth Palace & Wolves scored in last 4 meetings. Over 1.5 Goals @ 1.34. ⚡\nMarket line closing before kickoff. Lock selection now.\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>PLACE YOUR LIVE BET:</b> https://r1wttde.life/betting?open=register&p=t02b","images":[]},
  {"date":"2026-08-17","time":"22:30","content":"💸 <b>₦62,000 PALMPAY CASHOUT SETTLED ✅</b>\n\nID: <code>PPW-7732324</code>. Received at 06:34 AM in 48s. 📱\nBryan cashed out ₦62,000 straight to PalmPay with zero delays.\nStart with ₦200 / GH₵5 to test withdrawal speed yourself.\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>TEST CASHOUT SPEED:</b> https://r1wttde.life/betting?open=register&p=t02b","images":["with1.jpeg"]},

  {"date":"2026-08-18","time":"12:00","content":"🎁 <b>500% WELCOME BOOST: ₦1,000 → ₦6,000! ⚡</b>\n\nDeposit ₦1,000 → eligible bonus up to ₦6,000 (GH₵25 → GH₵150)! 💰\nInstant deposit via PalmPay, OPay & MTN MoMo in 30s. 📲\n10% monthly loss cashback insurance active on balance. 🛡️\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>CLAIM 500% WELCOME BOOST:</b> https://r1wttde.life/betting?open=register&p=t02b","images":["fortunobet.jpeg"]},
#   {"date":"2026-08-18","time":"17:30","content":"","images":[]},
#   {"date":"2026-08-18","time":"22:30","content":"🎯 <b>REPLAY TO LIVE BET: TICKET WON! 🟢</b>\n\nValerenga vs Bodo/Glimt (1:2) — Double Chance WON. ✅\n₦150,000 Stake → <b>₦171,000 Payout</b> (ID: <code>298340586</code>). 💰\nLive video bet delivered profit. Reset for tomorrow!\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>COLLECT WINNINGS NOW:</b> https://r1wttde.life/betting?open=register&p=t02b","images":["win1.png"]},

  {"date":"2026-08-19","time":"12:00","content":"🎁 <b>UNLOCK 600% FIRST DEPOSIT BONUS + 500 SPINS! 🚀</b>\n\nDeposit ₦1,000 → Play with ₦7,000 (or GH₵25 → GH₵175)! ⚡\nZero withdrawal fees + 10% cashback insurance. 🛡️\nInstant fund via PalmPay, OPay & MTN MoMo in 30s. 📲\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>CLAIM 600% BONUS:</b> https://r1wttde.life/betting?open=register&p=t02b","images":["fortunobet1.jpeg"]},
#   {"date":"2026-08-19","time":"17:30","content":"👀 <b>THIS LINE JUST MOVED: Lille vs Slavia Prague</b>\nLille unbeaten in last 8 European home matches (2.1 goals/game). 1X @ 1.32. ⚡\nKickoff in 30 mins. Bookmaker dropping odds fast.\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>PLACE YOUR LIVE BET:</b> https://r1wttde.life/betting?open=register&p=t02b","images":[]},
  {"date":"2026-08-19","time":"22:30","content":"💸 <b>₦127,500 PALMPAY CASHOUT SETTLED ✅</b>\n\nID: <code>PPW-7732325</code>. Settled at 10:24 AM in under 45s. 📱\nBryan withdrew ₦127,500 (~GH₵1,300) straight to PalmPay. 💚\nStart small with ₦200 / GH₵5 to test withdrawal speed.\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>TEST CASHOUT SPEED:</b> https://r1wttde.life/betting?open=register&p=t02b","images":["with2.jpeg"]},

  {"date":"2026-08-20","time":"12:00","content":"🏆 <b>EUROPA LEAGUE 500% BOOST ACTIVATED! 🎯</b>\n\nDeposit ₦1,000 → Play with ₦6,000 (or GH₵25 → GH₵150). 💰\nFast deposit via PalmPay, OPay & MTN MoMo in 30s. 📲\nPlus 10% loss protection on all midweek fixtures. 🛡️\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>CLAIM 500% BOOST:</b> https://r1wttde.life/betting?open=register&p=t02b","images":["fortunobet3.jpeg"]},
#   {"date":"2026-08-20","time":"17:30","content":"","images":[]},
#   {"date":"2026-08-20","time":"22:30","content":"🎯 <b>REPLAY TO LIVE BET: TICKET WON! 🟢</b>\n\nSabah Baku FK vs Aarhus AGF (4:0) — Handicap 1 WON. ✅\n₦150,000 Stake → <b>₦165,000 Payout</b> (ID: <code>299632435</code>). 💰\nLive video bet delivered green again!\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>COLLECT WINNINGS NOW:</b> https://r1wttde.life/betting?open=register&p=t02b","images":["win2.png"]},

  {"date":"2026-08-21","time":"12:00","content":"🔥 <b>WEEKEND OPENER: 500% BOOST ACTIVATED! 🎯</b>\n\nDeposit ₦1,000 → Play with ₦6,000 (or GH₵25 → GH₵150)! ⚡\nScale your weekend bankroll via PalmPay, OPay & MTN MoMo. 📲\nInstant credit in 30s. Zero processing fees.\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>CLAIM 500% BOOST:</b> https://r1wttde.life/betting?open=register&p=t02b","images":["fortunobet4.jpeg"]},
  {"date":"2026-08-21","time":"17:30","content":"⚡ <b>LIVE MARKET WATCH: Marseille vs Strasbourg</b>\nMarseille scored 2+ in last 5 home games; Strasbourg conceded in 6 straight. ⚡\nOver 1.5 Goals @ 1.35. Kickoff in 20 mins. Line closing soon!\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>PLACE YOUR LIVE BET:</b> https://r1wttde.life/betting?open=register&p=t02b","images":[]},
  {"date":"2026-08-21","time":"22:30","content":"💸 <b>FRIDAY NIGHT CASHOUT: ₦88,550 PALMPAY! ✅</b>\n\nID: <code>PPW-7732326</code>. Settled at 09:24 AM in 42s. 📱\nBryan withdrew ₦88,550 (~GH₵900) directly to PalmPay. 💚\nTest withdrawal speed yourself with ₦200 / GH₵5.\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>TEST CASHOUT SPEED:</b> https://r1wttde.life/betting?open=register&p=t02b","images":["with3.jpeg"]},

  {"date":"2026-08-22","time":"12:00","content":"⚽ <b>SATURDAY PREMIER LEAGUE 500% BOOST! 🎯</b>\n\nDeposit ₦1,000 → Play with ₦6,000 (or GH₵25 → GH₵150)! 💰\nInstant funding via PalmPay, OPay & MTN MoMo in 30s. 📲\nLock your boost before Saturday 12:30 kickoff!\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>CLAIM 500% BOOST:</b> https://r1wttde.life/betting?open=register&p=t02b","images":["fortunobet.jpeg"]},
  {"date":"2026-08-22","time":"17:30","content":"⏰ <b>LAST CHECK BEFORE KICKOFF: Brentford vs Spurs</b>\nSpurs averaging 1.8 goals away; Brentford scored in 9 of last 10 at home. ⚡\nOver 1.5 Total Goals @ 1.34. Kickoff in 25 mins!\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>PLACE YOUR LIVE BET:</b> https://r1wttde.life/betting?open=register&p=t02b","images":[]},
#   {"date":"2026-08-22","time":"22:30","content":"🎯 <b>REPLAY TO LIVE BET: TICKET WON! 🟢</b>\n\nElche CF vs Barcelona FC (0:3) — Barcelona Win WON. ✅\n₦150,000 Stake → <b>₦160,500 Payout</b> (ID: <code>302272063</code>). 💰\nLive video bet delivered straight profit!\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>COLLECT WINNINGS NOW:</b> https://r1wttde.life/betting?open=register&p=t02b","images":["win3.png"]},

  {"date":"2026-08-23","time":"12:00","content":"🏆 <b>SUNDAY 600% MEGA BOOST + 500 FREE SPINS! 🚀</b>\n\nDeposit ₦1,000 → Play with ₦7,000 (or GH₵25 → GH₵175)! ⚡\nNo withdrawal fees + 10% monthly loss insurance. 🛡️\nInstant funding via PalmPay, OPay & MTN MoMo in 30s. 📲\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>CLAIM 600% BONUS:</b> https://r1wttde.life/betting?open=register&p=t02b","images":["fortunobet2.jpeg"]},
  {"date":"2026-08-23","time":"17:30","content":"📊 <b>WHY THIS MATCH STANDS OUT: Atletico vs Villarreal</b>\nAtletico unbeaten in last 6 home games; Villarreal conceded in 4 of last 5 away. ⚡\n1X @ 1.30 Odds. Kickoff in 30 mins. Line closing soon!\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>PLACE YOUR LIVE BET:</b> https://r1wttde.life/betting?open=register&p=t02b","images":[]},
  {"date":"2026-08-23","time":"22:30","content":"💸 <b>WEEKLY CASHOUT WRAP: ALL WITHDRAWALS SETTLED! ✅</b>\n\nOver ₦278,050 / GH₵2,850 paid out this week in under 60s! 💚\nVerified on PalmPay & MTN MoMo (IDs: <code>PPW-7732324/5/6</code>). 📱\nStart new week small with ₦200 / GH₵5. Test speed yourself. 🙏\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>TEST CASHOUT SPEED:</b> https://r1wttde.life/betting?open=register&p=t02b","images":["with1.jpeg","with2.jpeg"]}
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