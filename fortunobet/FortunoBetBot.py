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


  {"date":"2026-07-13","time":"15:00","content":"🏀 <b>Dallas Wings W ✅ USA WNBA</b>\n\nUSA WNBA. Odds 1.34. 🏆\n$45 → $60.30. Final 108-95. Dominated. 💸\n\nDallas Wings elite form. Data clear. H2H obvious. It's too easy. 🎯\nSTOP WATCHING. We are winning. Pick ONE. Place it. GO. 🔥\n\nDeposit UGX 10,000 → play with UGX 60,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>PLACE YOUR BET:</b> https://r1wexmo.life/betting?open=register&p=t02b","images":["win3.png"]},
  {"date":"2026-07-13","time":"23:55","content":"💸 <b>UGX 112,000 MTN Mobile Money — Instant. ✅</b>\n\nMonday 13 July. 05:13 AM. Real notification. 💚\nUGX 112,000 (~$30 USD). ID: MM-7732211. Same minute.\n\nDallas Wings were elite at home. Toronto had no answers.\nBrian backed it early. Withdrew before morning. So simple. 💸\n\nSame quality data loads every week. Back it yourself. 🙏\n\nStart with UGX 10,000. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 <b>Test it yourself:</b> https://r1wexmo.life/betting?open=register&p=t02b","images":["withdrow1.png"]},

  {"date":"2026-07-14","time":"12:00","content":"💡 <b>How to place your first bet — 30 seconds</b>\n\nMy friend, it's simple. Here is what smart bettors do.\n\nOpen 1WIN → find ONE match → UGX 10,000 → place bet. 🎯\nWin → withdraw MTN same day. That is it. 💸\n\nChannel members doing this every week — you are missing out.\nBrian placed ONE bet. Withdrew UGX 112,000. Share with 2 friends! Don't sleep.\n\nStart with UGX 10,000. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 <b>Test it yourself:</b> https://r1wexmo.life/betting?open=register&p=t02b","images":["fortunobet1.jpeg"]},
  {"date":"2026-07-14","time":"18:00", "content": "🎰 <b>FortunoBet — All Games & All Bonuses in ONE Place! 🏆</b>\n\nWhy use separate sites? FortunoBet has it all! 💰\n\n⚽ Sports (WNBA, Premier League, Tennis)\n🎰 5,000+ Slots (Tower Rush, Aviator)\n♠️ Live Poker & Casino games\n\n⚡ <b>500% Welcome Bonus active now!</b>\n💸 Instant MTN & Airtel cashouts. It's too simple. 🎯\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>PLACE YOUR BET:</b> https://fortunobet.com/", "images": ["fortunobetVIP.jpeg"]},
  {"date":"2026-07-14","time":"22:30","content":"⚡ <b>UGX 112,000 arrived. Instant. No stress. ✅</b>\n\nMonday 13 July. 05:13 AM. Real MTN. 💚\nID: MM-7732211. Same minute. Zero fees.\n\nSome people are still scrolling. Brian already backed Dallas Wings — withdrew same morning. 💸\n\nThe platform works. The only question is when you will try it. 🙏\n\nStart with UGX 10,000. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 <b>Test it yourself:</b> https://r1wexmo.life/betting?open=register&p=t02b","images":["withdrow1.png"]},

  {"date":"2026-07-15","time":"12:00","content":"🎾 <b>Simona Waltert ✅ WTA 125K Bastad</b>\n\nWTA 125K Bastad. Sweden. Clay. Odds 1.42. 🏆\n$55 → $78.10. Final 2-0 (7-5, 6-2). Dominated. 💸\n\nClay form elite. Waltert baseline locked. It's too simple. 🎯\nSTOP WATCHING. They are collecting wins. Pick ONE. GO. 🔥\n\nDeposit UGX 10,000 → play with UGX 60,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>PLACE YOUR BET:</b> https://r1wexmo.life/betting?open=register&p=t02b","images":["win2.png"]},
  {"date":"2026-07-15","time":"19:00","content":"⚽ <b>CS U Craiova ✅ Champions League</b>\n\nCS U Craiova vs FC Maxline Vitebsk. Odds 1.28. 🏆\n$50 → $64. Craiova dominates at home. Easy money. 💸\n\nStop watching, join Kampala's biggest winners! It's simple. 🎯\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>PLACE YOUR BET:</b> https://r1wexmo.life/betting?open=register&p=t02b","images":[]},
  {"date":"2026-07-15","time":"22:30","content":"🚨 <b>Members withdrew twice this week already. ✅</b>\n\nUGX 112,000 Monday. UGX 120,000 today. MTN instant. Real proof. 💚\nChannel members are collecting — you are watching from the outside.\n\nDallas Wings paid. Simona Waltert paid. Two different sports. Same result.\nPick ONE match tonight before odds shift. How long will you watch? 🔥\n\nDeposit UGX 10,000 → play with UGX 60,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>PLACE YOUR BET:</b> https://r1wexmo.life/betting?open=register&p=t02b","images":["withdrow2.png"]},

  {"date":"2026-07-16","time":"12:00","content":"📊 <b>3 mistakes Uganda bettors make every week</b>\n\nMy friends, stop making these mistakes.\n\n❌ Betting big — lose everything fast.\n❌ Random channels — no data, pure luck.\n❌ Chasing losses — emotion kills bankroll.\n\nBrian's ONE pick — backed Dallas Wings home form. Withdrew UGX 112,000.\nWeekend fixtures loading — find yours before odds close. 🔥\n\nDeposit UGX 10,000 → play with UGX 60,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>PLACE YOUR BET:</b> https://r1wexmo.life/betting?open=register&p=t02b","images":["fortunobet3.jpeg"]},
  {"date":"2026-07-16","time":"18:00","content":"💬 Anybody collected this week?\n\nShow your MTN alert below 👇\nReal wins only. Let's see who is serious. 💸","images":[]},
  {"date":"2026-07-16","time":"22:30","content":"💚 <b>Brian backed Simona Waltert → withdrew UGX 120,000 ✅</b>\n\nReal story. This week. Brian, Kampala.\n\nWTA 125K Bastad. Clay form. Simona baseline elite.\nBrian read the data. Backed it Wednesday. Withdrew same morning. 💸\nID: MM-7732212. MTN. UGX 120,000. Instant.\n\nSame quality matches load every week. Find yours. Back it. 🙏\n\nStart with UGX 10,000. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 <b>Test it yourself:</b> https://r1wexmo.life/betting?open=register&p=t02b","images":["withdrow2.png"]},

    {"date":"2026-07-17","time":"12:00","content":"⚽ <b>Spain U19 ✅ U19 European Championship</b>\n\nEurope National Teams. Odds 1.33. 🏆\n$40 → $53.20. Final 2-0. Dominated. 💸\n\nSpain youth depth elite. Spain U19 dominated German U19. It's too simple. 🎯\nSTOP WATCHING. They are collecting wins. Pick ONE. GO. 🔥\n\nDeposit UGX 10,000 → play with UGX 60,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>PLACE YOUR BET:</b> https://r1wexmo.life/betting?open=register&p=t02b","images":["win1.png"]},
    {"date":"2026-07-17","time":"18:00","content":"🎰 <b>FortunoBet — All Games, One Place! 🏆</b>\n\nSports, 5,000+ slots & poker. No stress. 💰\n\n⚡ <b>Test with UGX 2,000 / KES 70:</b>\nRegister with Code: <code>fortunobet</code> & withdraw your wins instantly! 💸\n\n🎁 <b>500% Welcome Bonus Active!</b>\n👉 <b>PLAY NOW:</b> https://r1wexmo.life/betting?open=register&p=t02b","images":[]},
    {"date":"2026-07-17","time":"22:30","content":"💸 <b>UGX 198,000 / KES 6,800 MTN & M-Pesa — Instant. ✅</b>\n\nReal payout today! ID: MM-7732213. Same minute. 💚\nBrian backed Spain U19 form. Withdrew before morning.\n\nDon't sleep. Test the platform with just UGX 2,000 / KES 70 (price of 1 chapati) and see how fast MTN, Airtel & M-Pesa pay out! ⚡\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>Test Cashout Now:</b> https://r1wexmo.life/betting?open=register&p=t02b","images":["withdrow3.png"]},

    {"date":"2026-07-18","time":"12:00","content":"🏆 <b>Backed Wednesday. Withdrew same day. ✅</b>\n\nSimona Waltert WTA clay form was clear. 🎾\nWithdrew UGX 120,000 / KES 4,000 before morning! ID: MM-7732212.\n\nWhy watch from the outside? Test withdrawal yourself with UGX 2,000 / KES 70. It's too simple. 💸\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>Test It Now:</b> https://r1wexmo.life/betting?open=register&p=t02b","images":["win2.png","withdrow2.png"]},
    {"date":"2026-07-18","time":"18:00","content":"⚽ <b>EC Bahia ✅ Soccer Serie A</b>\n\nEC Bahia vs Chapecoense. Odds 1.42. 🏆\nChapecoense lost 6 of their last 8 away matches. 📉\n\nBahia home form is elite. Safe and obvious data pick to win easy. It's too simple. 🎯\nSTOP WATCHING. Pick Bahia to win. Let's collect together. 🔥\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>PLACE YOUR BET:</b> https://one-vv1153.com/betting/match/sport/ec-bahia-vs-chapecoense-37313846","images":["win3.png"]},
    {"date":"2026-07-18","time":"22:00","content":"♠️ <b>Free Poker Tournaments — Share $5,000 Weekly! 💰</b>\n\nNo entry fee required. Casual & pro players welcome! 🏆\nRegister, play, and win cash prizes sent straight to MTN, Airtel, or M-Pesa.\n\nDon't sleep on free money. Join poker now before slots fill! 🔥\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>JOIN FREE POKER:</b> https://r1wexmo.life/betting?open=register&p=t02b","images":["fortunobet2.jpeg"]},

    {"date":"2026-07-19","time":"12:00","content":"💚 <b>Weekly Recap: 3 sports. 3 picks. 3 WINS. ✅</b>\n\nMon: Dallas Wings ✅ (WNBA)\nWed: Simona Waltert ✅ (WTA)\nFri: Spain U19 ✅ (Euro U19)\n\nAll MTN, Airtel & M-Pesa cashouts processed instantly. 💸\nStop scrolling. Test withdrawal with UGX 2,000 / KES 70 today! 🎯\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>START WINNING:</b> https://r1wexmo.life/betting?open=register&p=t02b","images":["withdrow1.png","withdrow2.png","withdrow3.png"]},
    {"date":"2026-07-19","time":"18:00","content":"💬 Weekend done — who won?\n\nDrop your biggest win or mobile money alert below 👇\nNext week we go again. Who is ready? 🔥","images":[]},
    {"date":"2026-07-19","time":"22:30","content":"🎰 <b>500% Welcome Bonus — tonight only! ⚠️</b>\n\nPlay Tower Rush, Aviator, and 5,000+ slots with 500% extra on your first deposit! 💰\nBoost your balance instantly and try your luck with more security. 💸\n\nClaim it before it expires tonight!\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>CLAIM 500% BONUS:</b> https://r1wexmo.life/betting?open=register&p=t02b","images":["fortunobet.png","fortunobet.jpeg"]}

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