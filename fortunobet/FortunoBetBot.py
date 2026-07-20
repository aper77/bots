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

    {"date":"2026-07-21","time":"18:00","content":"⚽ <b>UEFA Champions League Qualifier Pick! 🏆</b>\n\nMjallby AIF is in unstoppable home form tonight. Odds 1.14 is our absolute premium banker to secure easy growth. 💰\n\n$100 bet on the platform yields $114 return with zero risk. H2H data is completely clear. 🎯\n\nDon't let free money pass you by. Lock in your pick before kickoff!\n\n🔑 Promo Code: <code>fortunobet</code>\n👉 <b>GET HIGHEST ODDS:</b> https://r1wexmo.life/betting?open=register&p=t02b","images":["proggress.png"]},
    {"date":"2026-07-21","time":"23:55","content":"✈️ <b>Aviator Hit 85.42x Multiplier Tonight! Cash Out Success! 🎰</b>\n\nUnbelievable flight! A tiny UGX 2,000 deposit turned into UGX 170,840 in just 15 seconds. 💸\n\nUGX 150,000 withdrawn instantly to MTN Mobile Money flat! ID: 7732224. 💛\n\nStop watching the red plane climb from the sidelines. Click CASHOUT before it flies away, and withdraw straight to your MoMo wallet instantly!\n\n🔑 Promo Code: <code>fortunobet</code>\n👉 <b>FLY AND CASHOUT INSTANTLY:</b> https://r1wexmo.life/betting?open=register&p=t02b","images":["withdrow1.png"]},

    {"date":"2026-07-22","time":"12:00","content":"🏀⚽ <b>WNBA & Brazil Serie A Double Ticket — Success! ✅</b>\n\nAtlanta Dream won easily at home, and EC Bahia dominated as predicted! Odds 1.82. 🏆\n$50 bet → $91 clean profit. It's too easy when you follow analytical data. 💸\n\nNo guessing, no room for emotions. Only pure data and high-value odds. 🎯\n\n🔑 Promo Code: <code>fortunobet</code>\n👉 <b>LOCK IN EVENING ODDS:</b> https://r1wexmo.life/betting?open=register&p=t02b","images":["win1.png"]},
    {"date":"2026-07-22","time":"18:00","content":"🎰 <b>Claim Your Massive 500% Welcome Package Today! 🏆</b>\n\nMaximize your funds on FortunoBet! Get a huge 500% bonus on your first deposits to play over 5,000 slots and games. 💰\n\nSimply register with the promo code and deposit via MTN, Airtel, or Telecel to double your start. ⚡\n\n🔑 Promo Code: <code>fortunobet</code>\n👉 <b>CLAIM 500% SIGN-UP BONUS:</b> https://r1wexmo.life/betting?open=register&p=t02b","images":["fortunobet.jpeg"]},
    {"date":"2026-07-22","time":"23:55","content":"💸 <b>GH¢ 1,020 Paid Out in Ghana — Instant MoMo! ✅</b>\n\nAccra is winning big tonight! S. Mensah withdrew GH¢ 1,020 straight to MTN MoMo. 🇬🇭\nTransaction completed in under 1 minute. Zero hidden fees. ID: 7732225. 💚\n\nWhile others are sleeping, smart players are cashing out. The statistics don't lie. 🙏\n\nStart with just GH¢ 5 and feel the lightning payout speed yourself!\n\n🔑 Promo Code: <code>fortunobet</code>\n👉 <b>SOAR AND CASH OUT NOW:</b> https://r1wexmo.life/betting?open=register&p=t02b","images":["withdrow2.png"]},

    {"date":"2026-07-23","time":"12:00","content":"🎾 <b>WTA Bastad Clay Tennis Winner! Simona Waltert. ✅</b>\n\nOur analytical slips delivered spectacular profits on Sweden's clay court. Simona Waltert dominated Kaitlin Quevedo easily! 🏆\n\nOdds 1.42. $55 bet turned into $78.10 clean profit. Total payout $133.10 straight to wallet. 💸\n\nStop gambling blindly. Follow the numbers and build your bankroll systematically. 🎯\n\n🔑 Promo Code: <code>fortunobet</code>\n👉 <b>PLACE YOUR WINNING BET:</b> https://r1wexmo.life/betting?open=register&p=t02b","images":["win2.png"]},
    {"date":"2026-07-23","time":"18:00","content":"💡 <b>How to Register & Play in 30 Seconds — Easy Guide:</b>\n\n1️⃣ Click the link & register with Code: <code>fortunobet</code>\n2️⃣ Deposit as little as UGX 2,000 / GH¢ 5 (price of 1 chapati) using MTN, Airtel, or Telecel\n3️⃣ Get your 500% welcome bonus credited automatically!\n\nStop scrolling and start earning today. It's too simple! 🎯\n\n🔑 Promo Code: <code>fortunobet</code>\n👉 <b>REGISTER YOUR ACCOUNT NOW:</b> https://r1wexmo.life/betting?open=register&p=t02b","images":["fortunobet1.jpeg"]},
    {"date":"2026-07-23","time":"23:55","content":"🎈 <b>1Win Balloon Reached 20.35x Multiplier Tonight! 🏆</b>\n\nThe easiest cash game on the internet right now. Press, hold to inflate the balloon, watch the multiplier rise, and release to cashout instantly! 💰\n\nDon't let it pop before you collect! Turn a simple UGX 2,000 into UGX 40,700 in seconds and withdraw straight to MoMo! 💸\n\nYour 500% Welcome Bonus is waiting. Claim it tonight and play with zero stress! ⚡\n\n🔑 Promo Code: <code>fortunobet</code>\n👉 <b>PLAY BALLOON AND CASH OUT:</b> https://r1wexmo.life/betting?open=register&p=t02b","images":["withdrow1.png"]},

    {"date":"2026-07-24","time":"12:00","content":"🏀 <b>WNBA Main Pick: Dallas Wings vs Toronto Tempo! ✅</b>\n\nDallas Wings dominated the court in style! High-value analytical slip wins again. 🏆\n\nOdds 1.34. $45.00 bet returned $60.30 pure profit (Total payout $105.30). 💸\n\nOur research makes winning simple. Don't waste money guessing. Follow the data! 🎯\n\n🔑 Promo Code: <code>fortunobet</code>\n👉 <b>GET BEST VALUE ODDS TODAY:</b> https://r1wexmo.life/betting?open=register&p=t02b","images":["win3.png"]},
    {"date":"2026-07-24","time":"18:00","content":"💡 <b>How to Start and Win in 30 Seconds — Step-by-Step:</b>\n\n1️⃣ Click the link & register with Code: <code>fortunobet</code>\n2️⃣ Deposit as little as UGX 2,000 / GH¢ 5 (price of 1 chapati)\n3️⃣ Play Aviator, Balloon, or back a top soccer match and withdraw instantly to MoMo! ⚡\n\n🎁 <b>Our 500% welcome package matches your first deposits automatically!</b>\n\nWhy watch from the sidelines? Start your winning journey today. It's too simple. 🎯\n\n🔑 Promo Code: <code>fortunobet</code>\n👉 <b>REGISTER YOUR ACCOUNT NOW:</b> https://r1wexmo.life/betting?open=register&p=t02b","images":["fortunobet.jpeg"]},
    {"date":"2026-07-24","time":"23:55","content":"💸 <b>$75.00 USD Mobile Money Payout — Instant! ✅</b>\n\nFriday night cashout has arrived! Transaction MM-7732226 processed in 45 seconds flat. 💚\n\nYour mobile money wallet is ready to grow. Zero withdrawal fees, zero bank queues.\n\nBrian backed our Simona Waltert tennis prediction and woke up to a sweet $75 balance. It's too easy. 🎯\n\nStart your weekend with just UGX 2,000 / GH¢ 5 today! ⚡\n\n🔑 Promo Code: <code>fortunobet</code>\n👉 <b>COLLECT FRIDAY CASHOUTS:</b> https://r1wexmo.life/betting?open=register&p=t02b","images":["withdrow3.png"]},

    {"date":"2026-07-25","time":"12:00","content":"♠️ <b>Free Poker Tournaments — Share $5,000 Weekly! 💰</b>\n\nAbsolutely zero buy-in required! Casual players and poker pros are both welcome to the tables. 🏆\n\nRegister with our promo code, participate, and win real cash prizes sent straight to your MTN, Airtel, or Telecel Mobile Money wallet.\n\nDon't sleep on free money. Tournament seats fill up fast! 🔥\n\n🔑 Promo Code: <code>fortunobet</code>\n👉 <b>JOIN FREE POKER TOURNAMENT:</b> https://r1wexmo.life/betting?open=register&p=t02b","images":["fortunobet2.jpeg"]},
    {"date":"2026-07-25","time":"18:00","content":"🔥 <b>[SATURDAY EXPERT SLIP] Perfect Predictor Active! 🎯</b>\n\nWeekend sports are in full swing! Our analytics team has locked in a premium basketball prediction for today. 📊\n\n<b>• Fixture:</b> WNBA Dallas Wings Match\n<b>• Analysis:</b> Elite home record vs struggle-prone away defense\n<b>• Prediction:</b> Dallas Wings Winner (incl. OT)\n<b>• Best Odds:</b> 1.34 on the platform\n\nJoin the winners and build your bankroll. Don't guess, follow the metrics. 🎯\n\n🔑 Promo Code: <code>fortunobet</code>\n👉 <b>PLACE YOUR SATURDAY BET:</b> https://r1wexmo.life/betting?open=register&p=t02b","images":["win3.png"]},
    {"date":"2026-07-25","time":"23:55","content":"🐹🚀 <b>Save the Hamster Cashout! Multipliers Flying High Tonight! 🏆</b>\n\nOur favorite flying hamster is soaring to crazy multiplier heights tonight! Tap to save him before the crash and claim your multiplier. 💰\n\nUGX 198,000 (~$53 USD) paid instantly to Mobile Money tonight! Transaction ID: MM-7732213. 💚\n\nNo stressful bank delays, no tedious verification. Turn a minor UGX 2,000 deposit into big weekend cash!\n\n🔑 Promo Code: <code>fortunobet</code>\n👉 <b>PLAY SAVE THE HAMSTER NOW:</b> https://r1wexmo.life/betting?open=register&p=t02b","images":["withdrow3.png"]},


    {"date":"2026-07-26","time":"12:00","content":"🎰 <b>Sunday Slots & Crash Games Special! 🏆</b>\n\nMake your Sunday rewarding with our premium slots and high-multiplier games! Turn a tiny deposit into a massive bankroll builder. 💰\n\nRegister with our promo code and claim your massive 500% sign-up bonus package today! ⚡\n\n🔑 Promo Code: <code>fortunobet</code>\n👉 <b>CLAIM 500% SIGN-UP BONUS:</b> https://r1wexmo.life/betting?open=register&p=t02b","images":["fortunobet2.jpeg"]},
    {"date":"2026-07-26","time":"18:00","content":"⚽ <b>[SUNDAY ELITE FIXTURE] Spain U19 vs Germany U19! ✅</b>\n\nSpain U19 proved their dominance on the European stage with a clean 2-0 victory! Analytical slip wins again! 🏆\n\nOdds 1.33. $40.00 stake returned a beautiful $53.20 profit. Total payout $93.20! 💸\n\nStop scrolling. Focus on ONE solid match with backed analytics, place your bet, and win. 🔥\n\n🔑 Promo Code: <code>fortunobet</code>\n👉 <b>PLACE YOUR SUNDAY BETS:</b> https://r1wexmo.life/betting?open=register&p=t02b","images":["win1.png"]},
    {"date":"2026-07-26","time":"23:55","content":"✈️ <b>Night Multipliers are Hitting Extreme Peaks on Aviator! 🎰</b>\n\nWe saw multipliers soar past 85x tonight. Just one well-timed flight can multiply your wallet balance instantly! 💰\n\nUGX 112,000 deposited instantly straight to MTN Mobile Money wallet! ID: MM-7732211. 💛\n\nDeposit via MTN, Airtel, or Telecel, claim your massive 500% Welcome Bonus, and experience the most rewarding crash game online today. 🔥\n\n🔑 Promo Code: <code>fortunobet</code>\n👉 <b>FLY AND WIN NOW:</b> https://r1wexmo.life/betting?open=register&p=t02b","images":["withdrow1.png"]},

    {"date":"2026-07-27","time":"12:00","content":"💡 <b>Kickstart Your Week with 500% Match Bonus! 🏆</b>\n\nDon't let the Monday blues get you down. Sign up with our code, deposit via MTN, Airtel, or Telecel, and watch your balance grow immediately with our 500% bonus! ⚡\n\n🔑 Promo Code: <code>fortunobet</code>\n👉 <b>CLAIM MONDAY SIGN-UP BONUSES:</b> https://r1wexmo.life/betting?open=register&p=t02b","images":["fortunobet1.jpeg"]},
    {"date":"2026-07-27","time":"18:00","content":"📝 <b>[MONDAY ANALYSIS] Tennis Clay Court Selection! 🏆</b>\n\nKickstart your week with a clean, low-risk analytics pick on tennis! Simona Waltert is back in action. 📊\n\n<b>• Fixture:</b> Simona Waltert vs Kaitlin Quevedo\n<b>• Selection:</b> Winner, Simona Waltert\n<b>• Best Odds:</b> 1.42 on FortunoBet\n\nWhy wait? Register, back our expert prediction, and secure an early week cashout. It's too simple. 🎯\n\n🔑 Promo Code: <code>fortunobet</code>\n👉 <b>PLACE YOUR MONDAY BET:</b> https://r1wexmo.life/betting?open=register&p=t02b","images":["win2.png"]},
    {"date":"2026-07-27","time":"23:55","content":"🎈 <b>Blow Up Your Mobile Money Balance on 1Win Balloon! 🏆</b>\n\nEasy wins are hitting tonight with over 20x multipliers! Hold to inflate, release to cash out instantly straight to your MTN or Airtel wallet. 💰\n\nUGX 120,000.00 processed in 1 minute flat with zero fees. Transaction ID: MM-7732212. 🇺🇬\n\nClaim your massive 500% deposit package tonight to start playing with zero stress! ⚡\n\n🔑 Promo Code: <code>fortunobet</code>\n👉 <b>BOOST YOUR MULTIPLIER NOW:</b> https://r1wexmo.life/betting?open=register&p=t02b","images":["withdrow2.png"]},

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