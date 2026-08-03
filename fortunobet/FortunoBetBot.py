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


    # {"date":"2026-08-03","time":"20:55","content":"✅ <b>BOOM! WE WON AGAIN — LIVE BET REPLAY RESULT! 🏆</b>\n\nReplay to our live video bet! Lyon dominated Wolfsburg 2-0 as predicted. 📊\n\n⚽ Wolfsburg 0 - 2 Lyon \n🔥 Bet: $100 @ 1.50 Odds → $150.00 Profit! \n💰 Total Balance: <b>$872.00</b> 💸\n\nWhy watch from the sidelines while we cash out daily? 🚀\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>REGISTER & WIN TODAY:</b> https://r1wexmo.life/betting?open=register&p=t02b","images":["win1.png"]},


    {"date":"2026-08-04","time":"12:00","content":"🎰 <b>UNLOCK EGYPT'S TREASURES — 500% BONUS! 🏺</b>\n\nPlay Book of Dead on FortunoBet! Get an instant <b>500% welcome bonus</b> on your 1st deposit! 💰\n\nMin deposit: UGX 2,000 / GH¢ 5 / ₦200 via MTN MoMo, Telecel & OPay.\n\n1️⃣ Register with Code: <code>fortunobet</code>\n2️⃣ Deposit UGX 2,000 / GH¢ 5 / ₦200\n3️⃣ Get 500% Bonus + 10% Monthly Cashback! 🛡️\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>PLAY BOOK OF DEAD NOW:</b> https://r1wexmo.life/betting?open=register&p=t02b","images":["bonus2.jpeg"]},
    {"date":"2026-08-04","time":"16:30","content":"⚽ <b>CHAMPIONS LEAGUE BANKER PICK! 🎯</b>\n\nHigh-probability stats locked in! Backed by deep analytics with 85%+ win rate. 📊\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>LOCK IN TODAY'S ODDS:</b> https://r1wexmo.life/betting?open=register&p=t02b","images":[]},
    {"date":"2026-08-04","time":"23:55","content":"🏆 <b>$108.80 WINNER — TEAM FALCONS (1.32 ODDS)! 🎯</b>\n\nIEM Cologne Major locked in! $80 stake returned $108.80 profit. Account Balance: <b>$364.80</b>! 💸\n\nStop scrolling on the sidelines. Build your bankroll systematically! ⚡\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>JOIN THE WINNERS:</b> https://r1wexmo.life/betting?open=register&p=t02b","images":["win3.jpeg"]},

    {"date":"2026-08-05","time":"12:00","content":"⚡ <b>CONQUER OLYMPUS — 500% FIRST DEPOSIT BONUS! 🏛️</b>\n\nUnleash Zeus multipliers on Gates of 1Win! Double your betting power instantly! 💥\n\n1️⃣ Register with Code: <code>fortunobet</code>\n2️⃣ Deposit min UGX 2,000 / GH¢ 5 / ₦200\n3️⃣ Get 500% Bonus in under 30 seconds!\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>CLAIM 500% OLYMPUS BONUS:</b> https://r1wexmo.life/betting?open=register&p=t02b","images":["bonus4.jpeg"]},
    {"date":"2026-08-05","time":"16:30","content":"","images":[]},
    {"date":"2026-08-05","time":"23:55","content":"💸 <b>₦82,500.00 WEDNESDAY PALMPAY PAYOUT PROOF! ✅</b>\n\nMid-week cashout completed! Bryan withdrew ₦82,500.00 (~$55 USD) straight to PalmPay. ID: 7732305. Available Balance: ₦160,210.50! 💚\n\nWhatsApp member asked: <i>'When will be next analyses?'</i> — We keep winning together! ⚡\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>COLLECT WEDNESDAY WINS:</b> https://r1wexmo.life/betting?open=register&p=t02b","images":["with2.png"]},

    {"date":"2026-08-06","time":"12:00","content":"🏎️ <b>FEEL THE SPEED — +600% WELCOME BONUS! 🏁</b>\n\nFormula 1 speed on instant payouts! Get a massive <b>+600% bonus</b> on your first deposit! ⚡\n\nMin deposit: UGX 2,000 / GH¢ 5 / ₦200 via MoMo, OPay & PalmPay.\n\n1️⃣ Tap link & register with Code: <code>fortunobet</code>\n2️⃣ Deposit UGX 2,000 / GH¢ 5 / ₦200\n3️⃣ Instant +600% bonus credited!\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>CLAIM +600% SPEED BONUS:</b> https://r1wexmo.life/betting?open=register&p=t02b","images":["bonus5.jpeg"]},
    {"date":"2026-08-06","time":"16:30","content":"💡 <b>SMART BETTING RULE #1:</b>\n\nNever chase losses emotionally! Stick to 1.30–1.95 odds with backed analytics. 📈\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>LOCK IN THURSDAY ODDS:</b> https://r1wexmo.life/betting?open=register&p=t02b","images":[]},
    {"date":"2026-08-06","time":"23:55","content":"⚽ <b>$156.00 WINNER — SWEDEN VS TUNISIA (1.95 ODDS)! 🎯</b>\n\nWorld Cup prediction hit clean! $80 stake returned $156.00 cash profit. Balance: <b>$450.80</b>! 💸\n\nZero guesswork. Back real data and cash out instantly! ⚡\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>REGISTER & WIN TODAY:</b> https://r1wexmo.life/betting?open=register&p=t02b","images":["win2.jpeg"]},

    {"date":"2026-08-07","time":"12:00","content":"🏗️ <b>TOWER RUSH — CLIMB & CLAIM 500% BONUS! 🚀</b>\n\nClimb to the top and claim your prize with an instant <b>500% bonus</b> on your 1st deposit! 💸\n\nMin deposit: UGX 2,000 / GH¢ 5 / ₦200 via MTN MoMo, Telecel, OPay & PalmPay.\n\n1️⃣ Register with Code: <code>fortunobet</code>\n2️⃣ Deposit min UGX 2,000 / GH¢ 5 / ₦200\n3️⃣ Instant 500% bonus + no deposit fees!\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>PLAY TOWER RUSH NOW:</b> https://r1wexmo.life/betting?open=register&p=t02b","images":["bonus3.jpeg"]},
    {"date":"2026-08-07","time":"16:30","content":"⚽ <b>FRIDAY NIGHT BANKER ODDS! 🎯</b>\n\nWeekend matches starting tonight! Lock in 90%+ probability picks before kickoff. 📊\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>BET FRIDAY ODDS NOW:</b> https://r1wexmo.life/betting?open=register&p=t02b","images":[]},
    {"date":"2026-08-07","time":"23:55","content":"💸 <b>₦82,500.00 FRIDAY NIGHT CASHOUT PROOF! ✅</b>\n\nFriday night cash received! Bryan withdrew ₦82,500.00 (~$55 USD) straight to PalmPay. ID: 7732306. Balance: ₦160,210.50! 💚\n\nWhatsApp member says: <i>'Mr Bryan thanks for ideal week!!'</i> ⚡\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>COLLECT FRIDAY CASHOUTS:</b> https://r1wexmo.life/betting?open=register&p=t02b","images":["with3.png"]},

    {"date":"2026-08-08","time":"12:00","content":"🪙 <b>GET A 600% BONUS ON CRYPTO DEPOSITS! 🚀</b>\n\nDeposit via Crypto or Mobile Money and unlock a massive <b>600% welcome bonus</b>! 💰\n\nFast payouts, high multipliers, zero fees on deposits & withdrawals! ⚡\n\n1️⃣ Register with Code: <code>fortunobet</code>\n2️⃣ Deposit via MoMo, OPay or Crypto\n3️⃣ Instant 600% Bonus credited!\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>CLAIM 600% CRYPTO BONUS:</b> https://r1wexmo.life/betting?open=register&p=t02b","images":["bonus1.jpeg"]},
    {"date":"2026-08-08","time":"16:30","content":"","images":[]},

    {"date":"2026-08-09","time":"12:00","content":"🏆 <b>WEEKLY CASHOUT RECAP: OVER ₦232,000 PAID OUT! 💚</b>\n\n100% verified proof! All withdrawals processed in under 60 seconds straight to PalmPay & MoMo! ⚡\n\n✅ ₦67,500.00 (~$45 USD) — <b>PAID</b> (ID: 7732304)\n✅ ₦82,500.00 (~$55 USD) — <b>PAID</b> (ID: 7732305)\n✅ ₦82,500.00 (~$55 USD) — <b>PAID</b> (ID: 7732306)\n\nZero withdrawal fees. Start your new week with cash in hand! 🎯\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>REGISTER & CASH OUT NOW:</b> https://r1wexmo.life/betting?open=register&p=t02b","images":["with1.png","with2.png","with3.png"]},
    {"date":"2026-08-09","time":"16:30","content":"🔥 <b>SUNDAY STRATEGY TIP:</b>\n\nLock in high-probability 1.30+ odds before Sunday evening matches kick off! 🏆\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>LOCK IN SUNDAY ODDS:</b> https://r1wexmo.life/betting?open=register&p=t02b","images":[]},
    {"date":"2026-08-09","time":"23:55","content":"💸 <b>SUNDAY NIGHT PALMPAY CASHOUT PROOF! ✅</b>\n\n₦67,500.00 (~$45 USD) paid out instantly to PalmPay / Mobile Money! Transaction ID: 7732304. 💚\n\nZero withdrawal fees, zero queues. Start your new week as a winner! ⚡\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>REGISTER & CASH OUT NOW:</b> https://r1wexmo.life/betting?open=register&p=t02b","images":["with1.png"]}
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