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

{"date": "2026-06-08", "time": "16:00", "content": "🎾 <b>Aryna Sabalenka ✅ Roland Garros Women</b>\n\nRoland Garros Women. France. Odds 1.19. 🏆\n$100 → $119. Score 7-5 / 6-3. Dominated. 💸\n\nSabalenka clay form elite. Data clear from start. E easy be. 🎯\nI placed this bet — Kofi placed same type — both withdrew same day.\n\nOpen 1WIN. Pick ONE match. Place your bet. GH₵50. Now. 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>PLACE YOUR BET:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["1win1.png"]},
{"date": "2026-06-08", "time": "20:00", "content": "🎯 Placing this now. Knicks vs Spurs. NBA. Odds 1.77.\nKnicks home strong. Spurs weak away. Entering now. 👀\n👉 https://one-vv858.com/betting/prematch/basketball-23?p=z4m5", "images": []},
{"date": "2026-06-08", "time": "23:55", "content": "💸 <b>GH₵825 from ONE bet. MTN confirmed instant. ✅</b>\n\nMonday 08 June. 06:00 AM. Real phone notification. 💚\nGH₵825 (~$55 USD). ID: 7732041. Same minute.\n\nThis came from ONE single bet. GH₵50 stake. That is all.\nKofi placed it. Won. Withdrew same day. Chale — e easy be. 💸\n\nThis came from ONE bet. GH₵50. Try it yourself. 🙏\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 <b>Test it yourself:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["08waiting.png", "08completed.png"]},
{"date": "2026-06-09", "time": "16:00", "content": "💡 <b>How to place your first bet in 30 seconds</b>\n\nChale, e simple. Here is exactly what smart bettors do.\n\nStep 1: Open 1WIN — register FREE with code FORTUNOBET\nStep 2: Find ONE sport. Tennis. Football. NBA.\nStep 3: GH₵50 only. Place the bet. Win. Withdraw MTN same day. 💸\n\nKofi placed ONE bet — withdrew GH₵825 same day. Channel members doing this every week. Share with 2 friends!\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 <b>PLACE YOUR FIRST BET:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["educashon.jpeg"]},
{"date": "2026-06-09", "time": "23:55", "content": "⚡ <b>GH₵825 — arrived from ONE bet. Instant. ✅</b>\n\nMonday 08 June. 06:00 AM. Real MTN notification. 💚\nID: 7732041. Arrived same minute. Zero fees. No wahala.\n\nSome people still thinking about placing their first bet.\nKofi placed ONE bet GH₵50 — withdrew same day. Chale. 💸\n\nOne bet. GH₵50. Test it yourself. See what happens. 🙏\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 <b>Test it yourself:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["08fast.png"]},
{"date": "2026-06-10", "time": "12:00", "content": "🏀 <b>CSKA Moscow + Germany ✅ Multiple</b>\n\nVTB League + World Friendlies. Odds 1.42. 🏆\n$80 → $113.60. Both locked in. Controlled. 💸\n\nCSKA home dominance clear. Germany H2H easy. Data was sharp.\nKofi placed same type — e easy be. They collecting. Chale. 🎯\n\nPick ONE match. Same data loads every week. Place it. GO. 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>PLACE YOUR BET:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["1win2.png"]},
{"date": "2026-06-10", "time": "20:00", "content": "😂 [REACTION — Wed June 10 — add your short reaction after today win]", "images": []},
{"date": "2026-06-10", "time": "23:55", "content": "🚨 <b>Weekend fixtures loading. Odds closing fast. ✅</b>\n\nBig matches Friday and Saturday. Chale — window closing.\nSmart bettors placing NOW before odds drop. 💸\n\nGH₵825 confirmed Monday. Came from ONE bet. Real proof. 💚\nKofi placed ONE match. Same chance open for you tonight.\n\nPick ONE match. GH₵50. Place it before odds move. No dulling. 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>PLACE YOUR BET NOW:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["urgencyWed.jpeg"]},
{"date": "2026-06-11", "time": "16:00", "content": "📊 <b>How smart bettors pick ONE bet every week</b>\n\nChale, I see this every week. Wrong approach kills bankroll.\n\n❌ Wrong: Betting many matches — no control, lose everything.\n❌ Wrong: Random picks — no data, pure luck.\n✅ Right: ONE match. Clear data. GH₵50. Place it. Withdraw. 💸\n\nKofi placed ONE bet — withdrew GH₵825 same day. That is it.\nWeekend fixtures loading — pick YOUR ONE bet now. No dulling! 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>PLACE YOUR BET:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["Authority.jpeg"]},
{"date": "2026-06-11", "time": "23:55", "content": "💚 <b>Kofi placed ONE bet GH₵50 → withdrew GH₵825 ✅</b>\n\nReal story. This week. Kofi, Accra.\n\nOpened 1WIN Sunday. Found ONE tennis match. Placed GH₵50.\nClay form was obvious. Won big. 💸\nWithdrew same day. MTN MoMo. ID: 7732041. Instant.\n\n\"I just placed ONE bet. Chale — now I trust 1WIN.\" 🙏\nSame chance open for you now. Place your first bet today. 🙏\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 <b>Test it yourself:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["08fast.png"]},
{"date": "2026-06-12", "time": "12:00", "content": "⚽ <b>Brazil ✅ World National Friendlies</b>\n\nWorld Friendlies. Odds 1.12. 🏆\n$100 → $112. Score 6-2. Dominated. 💸\n\nBrazil home form elite. Data obvious. H2H clear. E easy be. 🎯\nI placed this bet — same data loads every weekend.\n\nPick ONE match this weekend. GH₵50. Place it now. Same easy. 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>PLACE YOUR BET:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["1win3.png"]},
{"date": "2026-06-12", "time": "20:00", "content": "💸 <b>GH₵930 from ONE bet. MTN instant. ✅</b>\n\nTuesday 10 June. 01:00 PM. Real phone notification. 💚\nGH₵930 (~$62 USD). ID: MTN-7732042. Same minute.\n\nOne bet. Disciplined. GH₵50 stake. Withdrew same day.\nNo wahala. No delay. Chale — ONE bet did this. 💸\n\nPlace your ONE bet now. GH₵50. Same result possible. ACT NOW. 🔥\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 <b>PLACE YOUR BET:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": []},
{"date": "2026-06-12", "time": "23:55", "content": "🏆 <b>Placed bet Sunday. Withdrew Monday. Same day.</b>\n\nStake: $100 — Aryna Sabalenka. Roland Garros. ✅\nProfit: $119. Odds 1.19. MTN MoMo GH₵825. ID: 7732041. Instant. ✅\n\nKofi placed ONE bet. Won Sunday. Withdrew Monday 06:00 AM. Chale.\nClay odds won't stay — smart bettors placed early. They collecting. 💸\n\nSame chance NOW. Pick ONE match. Place your bet. Withdraw tomorrow. 🔥\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 <b>PLACE YOUR BET:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["10waiting.png", "10complated.png"]},
{"date": "2026-06-13", "time": "16:00", "content": "⚡ <b>GH₵650 from ONE bet. Received instant. ✅</b>\n\nFriday 12 June. 11:12 AM. Real MTN notification. 💚\nID: MTN-7732043. Arrived same minute. Zero fees. No wahala.\n\nSunday matches loading on 1WIN right now. Chale.\nOdds won't stay this high — window open now. 💸\n\nPick ONE Sunday match. GH₵50. Place it before odds drop. 🔥\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 <b>Test it yourself:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["1win1.png", "08fast.png"]},
{"date": "2026-06-13", "time": "20:00", "content": "💚 <b>This week. 3 bets. 3 wins. Full transparency. ✅</b>\n\nMon: $100→$119 ✅ ONE bet. Sabalenka. Clay data clear.\nWed: $80→$113.60 ✅ ONE bet. CSKA+Germany. H2H obvious.\nFri: $100→$112 ✅ ONE bet. Brazil. Home form locked.\n\nGH₵825 + GH₵930 + GH₵650 = All from ONE bet each. 💸\nNext week — place YOUR one bet. Chale — share with 2 friends! 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>PLACE YOUR BET:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": []},
{"date": "2026-06-13", "time": "21:00", "content": "🎰 <b>Place your first casino bet tonight! ❌</b>\n\n1WIN Casino. Fortune Tiger. Gates of Olympus. 💰\nDeposit GH₵50 → play with GH₵300 + 500 free spins. Chale.\n\n500% promo code still works now — not guaranteed tomorrow. ⚠️\nKofi placed ONE bet this week. Withdrew GH₵825. No dulling. 💸\n\nPlace your first bet tonight. Test it yourself. 🙏\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>Test it yourself:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["12fast.png"]},
{"date": "2026-06-14", "time": "16:00", "content": "💚 <b>This week. 3 bets. 3 wins. Full transparency. ✅</b>\n\nMon: $100→$119 ✅ ONE bet. Sabalenka. Clay data clear.\nWed: $80→$113.60 ✅ ONE bet. CSKA+Germany. H2H obvious.\nFri: $100→$112 ✅ ONE bet. Brazil. Home form locked.\n\nGH₵825 + GH₵930 + GH₵650 = All from ONE bet each. 💸\nNext week — place YOUR one bet. Chale — share with 2 friends! 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>PLACE YOUR BET:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["08fast.png", "10fast.png", "12fast.png"]},
{"date": "2026-06-14", "time": "23:55", "content": "🎰 <b>Place your first casino bet tonight! ❌</b>\n\n1WIN Casino. Fortune Tiger. Gates of Olympus. 💰\nDeposit GH₵50 → play with GH₵300 + 500 free spins. Chale.\n\n500% promo code still works now — not guaranteed tomorrow. ⚠️\nKofi placed ONE bet this week. Withdrew GH₵825. No dulling. 💸\n\nPlace your bet tonight before bonus expires. JOIN NOW. 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>PLACE YOUR BET:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["casinosun.jpeg"]},

{"date": "2026-06-15", "time": "12:00", "content": "🏀 <b>Oklahoma City Thunder ✅ USA NBA</b>\n\nUSA NBA Playoffs. Odds 1.49. 🏆\n$70 → $104.30. Final 127-114. Led every quarter. 💸\n\nOKC home court was elite. Defence locked Spurs completely.\nData clear. H2H obvious. Chale — e easy be. 🎯\n\nSTOP WATCHING. Pick ONE match. Place it. They collecting. JOIN NOW. 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>PLACE YOUR BET:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["2win1.png"]},
{"date": "2026-06-15", "time": "20:00", "content": "🎯 [LIVE BET — Mon June 15 — add real game + league + odds]", "images": []},
{"date": "2026-06-15", "time": "23:55", "content": "💸 <b>GH₵450 MTN Mobile Money — Arrived instant ✅</b>\n\nMonday 15 June. 05:10 AM. Real phone notification. 💚\nGH₵450 (~$30 USD). ID: MTN-7732023. Same minute.\n\nKofi tested small first. Then scaled up big.\nNo delay. No wahala. Chale — just pure money. 💸\n\nAnother withdrawal confirmed today. Proof is right here. ✅\nONE bet. GH₵50. Same as Kofi. Test it yourself. 🙏\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 <b>Test it yourself:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["15waiting.png", "15fast.png"]},
{"date": "2026-06-16", "time": "16:00", "content": "💡 <b>How smart bettors protect their bankroll</b>\n\nChale, most people deposit everything at once and lose. Here is how smart players do it.\n\nStep 1: Start GH₵50 only. Test system first. Easy read.\nStep 2: Pick ONE sport you know well. No random gambling.\nStep 3: Withdraw MTN Mobile Money same day. 💸\n\nKofi did exactly this — withdrew same day, MTN instant. 🙏\nChannel members already doing this every week. Share with 2 friends!\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 <b>PLACE YOUR FIRST BET:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["bonus1.jpeg"]},
{"date": "2026-06-16", "time": "23:55", "content": "⚡ <b>GH₵450 MTN Mobile Money — Received instant ✅</b>\n\nMonday 15 June. 05:10 AM. Real MTN notification. 💚\nID: MTN-7732023. Arrived same minute. Zero fees. No wahala.\n\nSome people still thinking. Kofi already tested and withdrew. Chale. 💸\nSmall test or big — 1WIN pays every single time. They collecting.\n\nWinning is important. Getting paid is more important. 🙏\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 <b>Test it yourself:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["15fast.png"]},
{"date": "2026-06-17", "time": "12:00", "content": "🏀 <b>Dallas Wings W ✅ USA WNBA</b>\n\nUSA WNBA. Odds 1.15. 🏆\n$50 → $57.50. Final 79-56. Dominated all 4 quarters. 💸\n\nDallas Wings home form elite. Defence locked Seattle completely.\nData clear. H2H obvious. Chale — e easy be. 🎯\n\nPick ONE match. Same data available. Place it now. GO. 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>PLACE YOUR BET:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["2win2.png"]},
{"date": "2026-06-17", "time": "20:00", "content": "😂 [REACTION — Wed June 17 — add your short reaction after today win]", "images": []},
{"date": "2026-06-17", "time": "23:55", "content": "🚨 <b>Members already withdrew twice this week. ✅</b>\n\nGH₵450 confirmed Monday. MTN instant. Real proof. 💚\nChannel members dey collect — you dey watch from outside.\n\nKofi deposited Sunday. Withdrew Monday 05:10 AM. Same minute. 💸\nSocial proof don enter — smart bettors already inside.\n\nPick ONE bet tonight. GH₵50. Chale — how long you go keep watching? JOIN NOW. 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>PLACE YOUR BET NOW:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["bonus2.jpeg"]},
{"date": "2026-06-18", "time": "16:00", "content": "📊 <b>3 mistakes Ghana bettors make every week</b>\n\nChale, I see this every week. Stop making these mistakes.\n\n❌ Mistake 1: Betting big — no control. Lose everything fast.\n❌ Mistake 2: Random channels — no analysis. Pure luck.\n❌ Mistake 3: Chasing losses — emotion kills bankroll.\n\nKofi avoided all 3 — withdrew GH₵450 same day. They collecting. 💸\nWeekend fixtures loading — pick ONE match now. Smart bettors placing. No dulling! 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>PLACE YOUR BET:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["bonus3.jpeg"]},
{"date": "2026-06-18", "time": "23:55", "content": "💚 <b>Kofi tested GH₵50 → withdrew GH₵450 ✅</b>\n\nReal story. This week. Kofi, Accra.\n\nDeposited GH₵50 Sunday — just to test the system.\nBet NBA Monday. Home court form obvious. Won big. 💸\nWithdrew same day. MTN MoMo. ID: MTN-7732023. Instant.\n\nKofi placed ONE bet GH₵50 — same odds open now. Place yours. Chale. 💸\n\"I tested small first. Now I trust 1WIN.\" 🙏\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 <b>Test it yourself:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["15fast.png"]},
{"date": "2026-06-19", "time": "12:00", "content": "🎾 <b>Flavio Cobolli ✅ Roland Garros Men</b>\n\nRoland Garros Men. France. Odds 1.13. 🏆\n$90 → $101.70. Score 6-2 / 6-3 / 7-6. Dominated. 💸\n\nCobolli clay form was elite. Baseline locked, serve clean.\nData clear. H2H obvious. Chale — e easy be. 🎯\n\nSame data today. Pick ONE match. Place it. Stop watching. GO. 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>PLACE YOUR BET:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["2win3.png"]},
{"date": "2026-06-19", "time": "20:00", "content": "😂 [REACTION — Fri June 19 — add your short reaction after today win]", "images": []},
{"date": "2026-06-19", "time": "23:55", "content": "💸 <b>GH₵750 MTN Mobile Money — Arrived instant ✅</b>\n\nWednesday 17 June. 06:43 AM. Real phone notification. 💚\nGH₵750 (~$50 USD). ID: MTN-7732024. Same minute.\n\nStarted small. Stayed disciplined. Withdrew same day.\nFinal weekend matches loading tonight — last chance to position. ✅\nNo delay. No wahala. Chale — just pure money. 💸\n\nONE match this weekend. GH₵50. Place it now. Test it yourself. 🙏\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 <b>Test it yourself:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["17waiting.png", "17fast.png"]},
{"date": "2026-06-20", "time": "16:00", "content": "🏆 <b>Winning ticket May.\n💸 Withdrawal Monday.</b>\n\nStake: $70 — OKC Thunder. USA NBA. ✅\nProfit: $104.30. Odds 1.49. MTN MoMo GH₵450. ID: MTN-7732023. Instant. ✅\n\nKofi won May. Withdrew Monday 05:10 AM. Same minute. Chale. 💸\nNBA playoff odds won't stay this high — smart bettors entered early. 🎯\n\nSame bet available now. ONE pick. GH₵50. No dulling — enter before odds close. 🔥\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 <b>Test it yourself:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["2win1.png", "15fast.png"]},
{"date": "2026-06-20", "time": "20:00", "content": "😂 [REACTION — Sat June 20 — add your short reaction about MTN payout]", "images": []},
{"date": "2026-06-20", "time": "21:00", "content": "⚡ <b>GH₵1,200 MTN Mobile Money — Received instant ✅</b>\n\nFriday 19 June. 11:32 AM. Real MTN notification. 💚\nID: MTN-7732025. Arrived same minute. Zero fees. No wahala.\n\nSunday fixtures already loading on 1WIN right now. Chale.\nOdds on top matches won't stay this high for long. 💸\n\nPick ONE match. GH₵50. Place it. Test small first. 🙏\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 <b>Test it yourself:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["19fast.png"]},
{"date": "2026-06-21", "time": "16:00", "content": "💚 <b>This week. Real results. Full transparency. ✅</b>\n\nMon: $70 → $104.30 ✅ OKC Thunder — home court clear.\nWed: $50 → $57.50 ✅ Dallas Wings — form obvious.\nFri: $90 → $101.70 ✅ Cobolli — clay dominance.\n\nGH₵450 + GH₵750 + GH₵1,200 = All MTN instant. 💸\nSome people watched all week. Others collected. No dulling. 🔥\nChale — share with 2 betting friends! Next week YOU start.\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>PLACE YOUR BET:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["15fast.png", "17fast.png", "19fast.png"]},
{"date": "2026-06-21", "time": "23:55", "content": "🎰 <b>500% Bonus — Only active today! ❌</b>\n\n1WIN Casino. Fortune Tiger. Gates of Olympus. 💰\nDeposit GH₵50 → play with GH₵300 + 500 free spins. Chale.\n\n500% promo code still works right now — not guaranteed tomorrow. ⚠️\nKofi withdrew GH₵1,200 this week. They dey collect. No dulling. 💸\n\nWe test. We withdraw. We scale. JOIN NOW or miss it. 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>PLACE YOUR BET:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["bonus4.jpeg"]}

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