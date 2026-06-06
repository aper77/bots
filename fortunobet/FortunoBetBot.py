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
{"date": "2026-06-01", "time": "12:00", "content": "🎾 <b>Karen Khachanov ✅ Roland Garros</b>\n\nRoland Garros Men. France. Odds 1.11. 🏆\n$100 → $111. Score 6-3 / 7-6 / 6-0. Dominated. 💸\n\nKhachanov clay form was elite. Baseline locked, serve clean.\nData was clear from start. E easy be. Mon ✅ Wed ✅ Fri ✅\n\nSTOP WATCHING. They collecting. JOIN NOW. 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>Join NOW:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["win1.png"]},
{"date": "2026-06-01", "time": "20:00", "content": "Chale I always check FortunoBet.com before I place anything 👀\nThe analysis dey always sharp. No dulling 🔥", "images": []},
{"date": "2026-06-01", "time": "23:55", "content": "💸 <b>GH₵750 MTN Mobile Money — Arrived instant ✅</b>\n\nMonday 01 June. 05:42 AM. Real phone notification. 💚\nGH₵750 (~$68 USD). ID: MTN-7732021. Same minute.\n\nKofi tested small first. Then scaled up big.\nNo delay. No wahala. Chale — just pure money. 💸\n\n1WIN pays. MTN confirms. Every single time. ✅\nYou can't collect what you never deposited. ACT NOW. 🔥\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 <b>Start NOW:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["withprogress01.png", "with01.png"]},

{"date": "2026-06-02", "time": "16:12", "content": "💡 <b>How smart bettors protect their bankroll</b>\n\nChale, most people deposit everything at once and lose. Here is how smart players do it.\n\nStep 1: Start GH₵50 only. Test system first. Easy read.\nStep 2: ONE sport you know well. No random gambling.\nStep 3: Withdraw MTN Mobile Money same day. 💸\n\nKofi did exactly this — withdrew same day, MTN instant. 🙏\nShare with 2 friends who bet! Test small first. Smart bettors don't rush.\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 <b>Start here:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["fortunoaviatorbot.jpg"]},
{"date": "2026-06-02", "time": "23:55", "content": "⚡ <b>GH₵750 MTN Mobile Money — Received instant ✅</b>\n\nMonday 01 June. 05:42 AM. Real MTN notification. 💚\nID: MTN-7732021. Arrived same minute. Zero fees. No wahala.\n\nNo waiting. No stories. Chale — 1WIN pays fast. Every time. 💸\nThey collecting while you dey watch. STOP WAITING. JOIN NOW. 🔥\n\nTest small first. Smart bettors don't rush. 🙏\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 https://r1wexmo.life/betting?open=register&p=t02b", "images": ["fast01.png"]},

{"date": "2026-06-03", "time": "12:00", "content": "🎮 <b>Team Spirit ✅ PGL Astana CS2</b>\n\nPGL Astana. Esports. Odds 1.37. 🏆\n$150 → $205.50. Maps 13-13-2. Controlled it. 💸\n\nTeam Spirit map control elite all series. H2H obvious. Chale.\nMOUZ had no answer. Data clear. Easy read. 🎯\n\nSTOP WATCHING. They collecting. JOIN NOW. 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>Join NOW:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["win1-1.png"]},
{"date": "2026-06-03", "time": "20:00", "content": "Been on FortunoBet.com checking the casino games 😂\nFortune Tiger dey call my name today 🎰", "images": []},
{"date": "2026-06-03", "time": "23:55", "content": "🚨 <b>GH₵39 paid today. Real MTN proof. Already confirmed. ✅</b>\n\nSome people still watching. Others already withdrew this week.\n\nKofi deposited Sunday. MTN confirmed Thursday 10:44 AM. 💸\nGH₵39. ID: MTN-7732022. Landed same minute. No dulling.\n\nThe opportunity is still open right now. How long will you wait? 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>NOW:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["fast04.png"]},

{"date": "2026-06-04", "time": "16:00", "content": "📊 <b>3 mistakes Ghana bettors make every week</b>\n\nChale, I see this every week. Stop making these mistakes.\n\n❌ Mistake 1: Betting big — no control. Lose everything fast.\n❌ Mistake 2: Random channels — no analysis. Pure luck.\n❌ Mistake 3: Chasing losses — emotion kills bankroll.\n\nKofi avoided all 3 — withdrew GH₵750 same day. They collecting. 💸\nFortunoBet community avoids all 3. JOIN NOW. Tag 2 friends. No dulling! 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>JOIN NOW:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["post6.jpeg"]},
{"date": "2026-06-04", "time": "23:55", "content": "💚 <b>Kofi tested GH₵50 → withdrew GH₵750 ✅</b>\n\nReal story. This week. Kofi, Accra.\n\nDeposited GH₵50 Sunday — just to test the system.\nBet tennis Monday. Clay form obvious. Won big. 💸\nWithdrew same day. MTN MoMo. ID: MTN-7732021. Instant.\n\n\"I tested small first. Chale — now I trust 1WIN.\" 🙏\nIf Kofi can do it — you can too.\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 <b>Test it:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": []},

{"date": "2026-06-05", "time": "12:00", "content": "🏀 <b>Oklahoma City Thunder ✅ USA NBA</b>\n\nUSA NBA Playoffs. Odds 1.49. 🏆\n$100 → $149. Final 127-114. Led every quarter. Chale. 💸\n\nOKC home court was elite. Defence locked Spurs down completely.\nData obvious. H2H clear. Easy read for smart bettors. 🎯\n\nSTOP WATCHING. They collecting. JOIN NOW. 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>Join NOW:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["win2.png"]},
{"date": "2026-06-05", "time": "20:00", "content": "FortunoBet.com community called this one early 💪\nWhen data is clear — e easy be. They collecting. 💸", "images": []},
{"date": "2026-06-05", "time": "23:55", "content": "💸 <b>GH₵39 MTN Mobile Money — Arrived instant ✅</b>\n\nThursday 04 June. 10:39 AM. Real phone notification. 💚\nGH₵39. ID: MTN-7732022. Same minute. Zero fees.\n\nStarted small. Tested the system. Withdrew same day.\nNo delay. No wahala. Chale — just pure money. 💸\n\n1WIN pays. MTN confirms. Every single time. ✅\nYou can't collect what you never deposited. ACT NOW. 🔥\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 <b>Start NOW:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["withprogress04.png", "withdrow04.png"]},

{"date": "2026-06-06", "time": "17:00", "content": "🏆 <b>Winning ticket Sunday.\n💸 Withdrawal Monday.</b>\n\nStake: $100 — Karen Khachanov. Roland Garros. ✅\nProfit: $111. Odds 1.11. MTN MoMo GH₵750. Instant. ✅\n\nWinning means nothing if you can't withdraw. This one paid.\nChale — people are collecting. You still watching? No dulling. 🔥\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 https://r1wexmo.life/betting?open=register&p=t02b", "images": ["win1.png", "fast01.png"]},
{"date": "2026-06-06", "time": "12:30", "content": "👀 Weekend slate looking good.\nA couple of picks catching my eye. Let's see what develops. 🎾", "images": []},
{"date": "2026-06-06", "time": "21:00", "content": "⚡ <b>GH₵440 MTN Mobile Money — Received instant ✅</b>\n\nFriday 06 June. 12:12 PM. Real MTN notification. 💚\nID: MTN-7732022. Arrived same minute. Zero fees. No wahala.\n\nNo waiting. No stories. Chale — 1WIN pays fast. Every time. 💸\nThey collecting while you dey watch. STOP WAITING. JOIN NOW. 🔥\n\nTest small first. Smart bettors don't rush. 🙏\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 https://r1wexmo.life/betting?open=register&p=t02b", "images": ["faste06.png"]},

{"date": "2026-06-07", "time": "16:00", "content": "💚 <b>This week. Real results. Full transparency. ✅</b>\n\nMon: $100 → $111 ✅ Khachanov — clay dominance. Easy read.\nWed: $150 → $205.50 ✅ Team Spirit — map control clear.\nFri: $100 → $149 ✅ OKC Thunder — led every quarter.\n\nGH₵750 + GH₵440 + GH₵39 = All MTN instant. 💸\nThey collected this week. Next week YOU start. NOW. 🔥\nChale — share with 2 betting friends! 💸\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>JOIN NOW:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["fast01.png", "fast04.png", "faste06.png"]},
{"date": "2026-06-07", "time": "23:55", "content": "🎰 <b>500% Bonus — LAST CHANCE TONIGHT! ❌</b>\n\n1WIN Casino. Fortune Tiger. Gates of Olympus. 💰\nDeposit GH₵50 → play with GH₵300 + 500 free spins. Chale.\n\nMTN Mobile Money. Zero fees. Withdraw tonight. ✅\nWeek closes MIDNIGHT. Bonus gone. They already collecting. 💸\n\nNo dulling. We test. We withdraw. We scale. JOIN NOW or miss it. 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>Play NOW:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["post14.jpeg"]}


{"date": "2026-06-08", "time": "16:00", "content": "🎾 <b>Aryna Sabalenka ✅ Roland Garros Women</b>\n\nRoland Garros Women. France. Odds 1.19. 🏆\n$100 → $119. Score 7-5 / 6-3. Dominated. 💸\n\nSabalenka clay form was elite. Serve locked, baseline clean.\nData was clear from start. E easy be. Mon ✅ Wed ✅ Fri ✅\n\nSTOP WATCHING. They collecting. JOIN NOW. 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>Join NOW:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["1win1.png"]},
{"date": "2026-06-08", "time": "20:00", "content": "Been on FortunoBet.com all morning 👀\nSabalenka on clay is something else chale. Pure class. 🎾", "images": []},
{"date": "2026-06-08", "time": "23:55", "content": "💸 <b>GH₵825 MTN Mobile Money — Arrived instant ✅</b>\n\nMonday 08 June. 06:00 AM. Real phone notification. 💚\nGH₵825 (~$55 USD). ID: 7732041. Same minute.\n\nKofi tested small first. Then scaled up big.\nNo delay. No wahala. Chale — just pure money. 💸\n\n1WIN pays. MTN confirms. Every single time. ✅\nAnother withdrawal confirmed today. You can't watch forever. ACT NOW. 🔥\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 <b>Start NOW:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["08waiting.png", "08completed.png"]},
{"date": "2026-06-09", "time": "16:00", "content": "💡 <b>How smart bettors protect their bankroll</b>\n\nChale, most people deposit everything at once and lose. Here is how smart players do it.\n\nStep 1: Start GH₵50 only. Test system first. Easy read.\nStep 2: Pick ONE sport you know well. No random gambling.\nStep 3: Withdraw MTN Mobile Money same day. 💸\n\nKofi did exactly this — withdrew same day, MTN instant. 🙏\nShare with 2 friends who bet! Test small first. Smart bettors don't rush.\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 <b>Start here:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["educashon.jpeg"]},
{"date": "2026-06-09", "time": "23:55", "content": "⚡ <b>GH₵825 MTN Mobile Money — Received instant ✅</b>\n\nMonday 08 June. 06:00 AM. Real MTN notification. 💚\nID: 7732041. Arrived same minute. Zero fees. No wahala.\n\nSome people still thinking about it.\nOthers already tested, withdrew and moved on. Chale. 💸\n\nWinning is important. Getting paid is more important.\nTest small first. Smart bettors don't rush. 🙏\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 https://r1wexmo.life/betting?open=register&p=t02b", "images": ["08fast.png"]},
{"date": "2026-06-10", "time": "12:00", "content": "🏀 <b>CSKA Moscow + Germany ✅ Multiple</b>\n\nVTB League + World Friendlies. Odds 1.42. 🏆\n$80 → $113.60. Both locked in. Controlled. 💸\n\nCSKA home dominance clear. Germany form obvious. H2H easy.\nData was sharp. Chale — e easy be. 🎯\n\nSTOP WATCHING. They collecting. JOIN NOW. 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>Join NOW:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["1win2.png"]},
{"date": "2026-06-10", "time": "20:00", "content": "😂 Not gonna lie the CSKA match was stressing me early.\nThen they just took over completely. Glad I entered. 💸", "images": []},
{"date": "2026-06-10", "time": "23:55", "content": "🚨 <b>Members already sharing winning slips this morning. ✅</b>\n\nGH₵825 confirmed Monday. MTN instant. Real proof. 💚\nChannel members dey collect — you dey watch from outside.\n\nKofi deposited Sunday. Withdrew Monday 06:00 AM. Same minute. 💸\nSocial proof don enter — smart bettors already inside.\n\nChale how long you go keep watching? JOIN NOW. 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>NOW:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["urgencyWed.jpeg"]},
{"date": "2026-06-11", "time": "16:00", "content": "📊 <b>3 mistakes Ghana bettors make every week</b>\n\nChale, I see this every week. Stop making these mistakes.\n\n❌ Mistake 1: Betting big — no control. Lose everything fast.\n❌ Mistake 2: Random channels — no analysis. Pure luck.\n❌ Mistake 3: Chasing losses — emotion kills bankroll.\n\nKofi avoided all 3 — withdrew GH₵825 same day. They collecting. 💸\nFortunoBet community avoids all 3. JOIN NOW. Tag 2 friends. No dulling! 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>JOIN NOW:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["Authority.jpeg"]},
{"date": "2026-06-11", "time": "23:55", "content": "💚 <b>Kofi tested GH₵50 → withdrew GH₵825 ✅</b>\n\nReal story. This week. Kofi, Accra.\n\nDeposited GH₵50 Sunday — just to test the system.\nBet tennis Monday. Clay form obvious. Won big. 💸\nWithdrew same day. MTN MoMo. ID: 7732041. Instant.\n\n\"I tested small first. Chale — now I trust 1WIN.\" 🙏\nIf Kofi can do it — you can too.\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 <b>Test it:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": []},
{"date": "2026-06-12", "time": "12:00", "content": "⚽ <b>Brazil ✅ World National Friendlies</b>\n\nWorld Friendlies. Odds 1.12. 🏆\n$100 → $112. Score 2-4 / 6 goals. Dominated. 💸\n\nBrazil home form was elite. Attack locked Panama completely.\nData obvious. H2H clear. Easy read for smart bettors. 🎯\n\nSTOP WATCHING. They collecting. JOIN NOW. 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>Join NOW:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["1win3.png"]},
{"date": "2026-06-12", "time": "20:00", "content": "FortunoBet.com community called this one early 💪\nWhen data is clear — e easy be. They collecting. 💸", "images": []},
{"date": "2026-06-12", "time": "23:55", "content": "🏆 <b>Winning ticket Sunday.\n💸 Withdrawal Monday.</b>\n\nStake: $100 — Aryna Sabalenka. Roland Garros. ✅\nProfit: $119. Odds 1.19. MTN MoMo GH₵825. Instant. ✅\n\nThis kind of odds won't stay available forever. Chale.\nSmart bettors enter early — data was clear from start. 🎯\n\nWinning means nothing if you can't withdraw. This one paid. 💸\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 https://r1wexmo.life/betting?open=register&p=t02b", "images": ["10waiting.png", "10complated.png"]},
{"date": "2026-06-13", "time": "16:00", "content": "🏆 <b>Winning ticket Sunday.\n💸 Withdrawal Monday.</b>\n\nStake: $100 — Aryna Sabalenka. Roland Garros. ✅\nProfit: $119. Odds 1.19. MTN MoMo GH₵825. Instant. ✅\n\nWinning means nothing if you can't withdraw. This one paid.\nChale — people are collecting. You still watching? No dulling. 🔥\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 https://r1wexmo.life/betting?open=register&p=t02b", "images": ["1win1.png", "08fast.png"]},
{"date": "2026-06-13", "time": "20:00", "content": "⚡ <b>GH₵650 MTN Mobile Money — Received instant ✅</b>\n\nFriday 12 June. 11:12 AM. Real MTN notification. 💚\nID: MTN-7732043. Arrived same minute. Zero fees. No wahala.\n\nWeekend fixtures already loading on 1WIN right now.\nOdds on top matches won't stay this high for long. Chale. 💸\n\nWindow is open now. Test small first. 🙏\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 https://r1wexmo.life/betting?open=register&p=t02b", "images": []},
{"date": "2026-06-13", "time": "21:00", "content": "⚡ <b>GH₵650 MTN Mobile Money — Received instant ✅</b>\n\nFriday 12 June. 11:12 AM. Real MTN notification. 💚\nID: MTN-7732043. Arrived same minute. Zero fees. No wahala.\n\nNo waiting. No stories. Chale — 1WIN pays fast. Every time. 💸\nThey collecting while you dey watch. STOP WAITING. JOIN NOW. 🔥\n\nTest small first. Smart bettors don't rush. 🙏\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 https://r1wexmo.life/betting?open=register&p=t02b", "images": ["12fast.png"]},
{"date": "2026-06-14", "time": "16:00", "content": "🎰 <b>500% Bonus — Only active today! ❌</b>\n\n1WIN Casino. Fortune Tiger. Gates of Olympus. 💰\nDeposit GH₵50 → play with GH₵300 + 500 free spins. Chale.\n\n500% promo code still works right now — not guaranteed tomorrow. ⚠️\nMTN Mobile Money. Zero fees. Withdraw tonight. ✅\n\nNo dulling. We test. We withdraw. We scale. JOIN NOW or miss it. 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>Play NOW:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["08fast.png", "10fast.png", "12fast.png"]},
{"date": "2026-06-14", "time": "23:55", "content": "🎰 <b>500% Bonus — LAST CHANCE TONIGHT! ❌</b>\n\n1WIN Casino. Fortune Tiger. Gates of Olympus. 💰\nDeposit GH₵50 → play with GH₵300 + 500 free spins. Chale.\n\nMTN Mobile Money. Zero fees. Withdraw tonight. ✅\nWeek closes MIDNIGHT. Bonus gone. They already collecting. 💸\nWhile you dey watch — others dey collect already. No dulling. 🔥\n\nWe test. We withdraw. We scale. JOIN NOW or miss it. 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>Play NOW:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["casinosun.jpeg"]},

{"date": "2026-06-15", "time": "16:00", "content": "🏀 <b>Oklahoma City Thunder ✅ USA NBA</b>\n\nUSA NBA Playoffs. Odds 1.49. 🏆\n$70 → $104.30. Final 127-114. Led every quarter. 💸\n\nOKC home court was elite. Defence locked Spurs completely.\nData clear. H2H obvious. Chale — e easy be. 🎯\n\nSTOP WATCHING. They collecting. JOIN NOW. 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>Join NOW:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["2win1.png"]},
{"date": "2026-06-15", "time": "20:00", "content": "Chale FortunoBet.com dey always have the sharp picks 👀\nOKC data was clear from morning. No dulling. 🏀", "images": []},
{"date": "2026-06-15", "time": "23:55", "content": "💸 <b>GH₵450 MTN Mobile Money — Arrived instant ✅</b>\n\nMonday 15 June. 05:10 AM. Real phone notification. 💚\nGH₵450 (~$30 USD). ID: MTN-7732023. Same minute.\n\nKofi tested small first. Then scaled up big.\nNo delay. No wahala. Chale — just pure money. 💸\n\nAnother withdrawal confirmed today. Proof is right here. ✅\nYou can't collect what you never deposited. ACT NOW. 🔥\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 <b>Start NOW:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["15waiting.png", "15fast.png"]},
{"date": "2026-06-16", "time": "16:00", "content": "💡 <b>How smart bettors protect their bankroll</b>\n\nChale, most people deposit everything at once and lose. Here is how smart players do it.\n\nStep 1: Start GH₵50 only. Test system first. Easy read.\nStep 2: Pick ONE sport you know well. No random gambling.\nStep 3: Withdraw MTN Mobile Money same day. 💸\n\nKofi did exactly this — withdrew same day, MTN instant. 🙏\nShare with 2 friends who bet! Test small first. Smart bettors don't rush.\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 <b>Start here:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["bonus1.jpeg"]},
{"date": "2026-06-16", "time": "23:55", "content": "⚡ <b>GH₵450 MTN Mobile Money — Received instant ✅</b>\n\nMonday 15 June. 05:10 AM. Real MTN notification. 💚\nID: MTN-7732023. Arrived same minute. Zero fees. No wahala.\n\nSome people still thinking about registering.\nOthers already tested, withdrew and trusted 1WIN. Chale. 💸\n\nWinning is important. Getting paid is more important.\nTest small first. Smart bettors don't rush. 🙏\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 https://r1wexmo.life/betting?open=register&p=t02b", "images": ["15fast.png"]},
{"date": "2026-06-17", "time": "12:00", "content": "🏀 <b>Dallas Wings W ✅ USA WNBA</b>\n\nUSA WNBA. Odds 1.15. 🏆\n$50 → $57.50. Final 79-56. Dominated all 4 quarters. 💸\n\nDallas Wings home form elite. Defence locked Seattle completely.\nData clear. H2H obvious. Chale — e easy be. 🎯\n\nSTOP WATCHING. They collecting. JOIN NOW. 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>Join NOW:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["2win2.png"]},
{"date": "2026-06-17", "time": "20:00", "content": "😂 Dallas Wings match was smooth from start.\nData was clear — no stress at all. Glad I entered. 💸", "images": []},
{"date": "2026-06-17", "time": "23:55", "content": "🚨 <b>Members already withdrew twice this week. ✅</b>\n\nGH₵450 confirmed Monday. MTN instant. Real proof. 💚\nChannel members dey collect — you dey watch from outside.\n\nKofi deposited Sunday. Withdrew Monday 05:10 AM. Same minute. 💸\nSocial proof don enter — smart bettors already inside.\n\nChale how long you go keep watching? JOIN NOW. 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>NOW:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["bonus2.jpeg"]},
{"date": "2026-06-18", "time": "16:00", "content": "📊 <b>3 mistakes Ghana bettors make every week</b>\n\nChale, I see this every week. Stop making these mistakes.\n\n❌ Mistake 1: Betting big — no control. Lose everything fast.\n❌ Mistake 2: Random channels — no analysis. Pure luck.\n❌ Mistake 3: Chasing losses — emotion kills bankroll.\n\nKofi avoided all 3 — withdrew GH₵450 same day. They collecting. 💸\nFortunoBet community avoids all 3. JOIN NOW. Tag 2 friends. No dulling! 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>JOIN NOW:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["bonus3.jpeg"]},
{"date": "2026-06-18", "time": "23:55", "content": "💚 <b>Kofi tested GH₵50 → withdrew GH₵450 ✅</b>\n\nReal story. This week. Kofi, Accra.\n\nDeposited GH₵50 Sunday — just to test the system.\nBet NBA Monday. Home court form obvious. Won big. 💸\nWithdrew same day. MTN MoMo. ID: MTN-7732023. Instant.\n\n\"I tested small first. Chale — now I trust 1WIN.\" 🙏\nIf Kofi can do it — you can too.\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 <b>Test it:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": []},
{"date": "2026-06-19", "time": "12:00", "content": "🎾 <b>Flavio Cobolli ✅ Roland Garros Men</b>\n\nRoland Garros Men. France. Odds 1.13. 🏆\n$90 → $101.70. Score 6-2 / 6-3 / 7-6. Dominated. 💸\n\nCobolli clay form was elite. Baseline locked, serve clean.\nData clear. H2H obvious. Chale — e easy be. 🎯\n\nSTOP WATCHING. They collecting. JOIN NOW. 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>Join NOW:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["2win3.png"]},
{"date": "2026-06-19", "time": "20:00", "content": "💸 <b>GH₵750 MTN Mobile Money — Arrived instant ✅</b>\n\nWednesday 17 June. 06:43 AM. Real phone notification. 💚\nGH₵750 (~$50 USD). ID: MTN-7732024. Same minute.\n\nStarted small. Stayed disciplined. Withdrew same day.\nNo delay. No wahala. Chale — just pure money. 💸\n\nFinal weekend matches loading tonight — last chance to position. ✅\nYou can't collect what you never deposited. ACT NOW. 🔥\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 <b>Start NOW:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": []},
{"date": "2026-06-19", "time": "23:55", "content": "🏆 <b>Winning ticket May.\n💸 Withdrawal Monday.</b>\n\nStake: $70 — OKC Thunder. USA NBA. ✅\nProfit: $104.30. Odds 1.49. MTN MoMo GH₵450. Instant. ✅\n\nThese NBA playoff odds won't stay this high for long. Chale.\nSmart bettors entered early — data was obvious from start. 🎯\n\nWinning means nothing if you can't withdraw. This one paid. 💸\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 https://r1wexmo.life/betting?open=register&p=t02b", "images": ["17waiting.png", "17fast.png"]},
{"date": "2026-06-20", "time": "16:00", "content": "🏆 <b>Winning ticket May.\n💸 Withdrawal Monday.</b>\n\nStake: $70 — OKC Thunder. USA NBA. ✅\nProfit: $104.30. Odds 1.49. MTN MoMo GH₵450. Instant. ✅\n\nWinning means nothing if you can't withdraw. This one paid.\nChale — people are collecting. You still watching? No dulling. 🔥\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 https://r1wexmo.life/betting?open=register&p=t02b", "images": ["2win1.png", "15fast.png"]},
{"date": "2026-06-20", "time": "20:00", "content": "⚡ <b>GH₵1,200 MTN Mobile Money — Received instant ✅</b>\n\nFriday 19 June. 11:32 AM. Real MTN notification. 💚\nID: MTN-7732025. Arrived same minute. Zero fees. No wahala.\n\nSunday fixtures already loading on 1WIN right now.\nOdds on top matches won't stay this high for long. Chale. 💸\n\nWindow is open now. Test small first. 🙏\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 https://r1wexmo.life/betting?open=register&p=t02b", "images": []},
{"date": "2026-06-20", "time": "21:00", "content": "⚡ <b>GH₵1,200 MTN Mobile Money — Received instant ✅</b>\n\nFriday 19 June. 11:32 AM. Real MTN notification. 💚\nID: MTN-7732025. Arrived same minute. Zero fees. No wahala.\n\nNo waiting. No stories. Chale — 1WIN pays fast. Every time. 💸\nThey collecting while you dey watch. STOP WAITING. JOIN NOW. 🔥\n\nTest small first. Smart bettors don't rush. 🙏\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 https://r1wexmo.life/betting?open=register&p=t02b", "images": ["19fast.png"]},
{"date": "2026-06-21", "time": "16:00", "content": "💚 <b>This week. Real results. Full transparency. ✅</b>\n\nMon: $70 → $104.30 ✅ OKC Thunder — home court clear.\nWed: $50 → $57.50 ✅ Dallas Wings — form obvious.\nFri: $90 → $101.70 ✅ Cobolli — clay dominance.\n\nGH₵450 + GH₵750 + GH₵1,200 = All MTN instant. 💸\nThey collected this week. Next week YOU start. NOW. 🔥\nChale — share with 2 betting friends! 💸\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>JOIN NOW:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["15fast.png", "17fast.png", "19fast.png"]},
{"date": "2026-06-21", "time": "23:55", "content": "🎰 <b>500% Bonus — Only active today! ❌</b>\n\n1WIN Casino. Fortune Tiger. Gates of Olympus. 💰\nDeposit GH₵50 → play with GH₵300 + 500 free spins. Chale.\n\n500% promo code still works right now — not guaranteed tomorrow. ⚠️\nMTN Mobile Money. Zero fees. Withdraw tonight. ✅\n\nNo dulling. We test. We withdraw. We scale. JOIN NOW or miss it. 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>Play NOW:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["bonus4.jpeg"]}

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