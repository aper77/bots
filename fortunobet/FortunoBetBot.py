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


  {"date":"2026-07-28","time":"12:00","content":"⚡ <b>500% BONUS + 10% MONTHLY CASHBACK! 💰</b>\n\nDouble your betting power! Get an instant <b>500% welcome bonus</b> on your 1st deposit + <b>10% monthly loss protection</b>! 🛡️\n\nMin deposit: UGX 2,000 / GH¢ 5 / ₦200 via MTN MoMo, Telecel & OPay.\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>CLAIM YOUR BONUS NOW:</b> https://r1wexmo.life/betting?open=register&p=t02b","images":["fortunobet2.jpeg"]},
  {"date":"2026-07-28","time":"16:30","content":"⚽ <b>CHAMPIONS LEAGUE PICK: Mjällby AIF Win (1.49 Odds) 🎯</b>\n\nLincoln Red Imps vs Mjällby AIF! Mjällby scored in 8 of last 10 away games. Lock in high-probability odds! 📊\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>BET NOW:</b> https://one-vv0954.life/betting/match/sport/lincoln-red-imps-fc-vs-mjallby-aif-37797997","images":[]},
  {"date":"2026-07-28","time":"23:55","content":"💸 <b>GH¢715.00 INSTANT CASHOUT PROOF! ✅</b>\n\nBryan just received GH¢715.00 (~$65 USD) directly to MTN Mobile Money in under 60 seconds! ID: 7732301. 💚\n\nNo verification delays. Deposit UGX 2,000 / GH¢ 5 / ₦200, win, and withdraw instantly! ⚡\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>REGISTER & CASH OUT NOW:</b> https://r1wexmo.life/betting?open=register&p=t02b","images":["with1.png"]},

  {"date":"2026-07-29","time":"12:00","content":"✅ <b>$85.00 PROFIT — UEFA CHAMPIONS LEAGUE WIN! ⚽</b>\n\nSabah Baku FK won 1-0! Single 1.70 Odds hit clean. $50 stake returned $85.00 cash! 🏆\n\nTotal Account Balance: <b>$907.00</b> 💸\n\nStop guessing! Register in 30 seconds and follow backed analytics.\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>LOCK IN TODAY'S WINNING ODDS:</b> https://r1wexmo.life/betting?open=register&p=t02b","images":["win3.png"]},
  {"date":"2026-07-29","time":"16:30","content":"❓ <b>QUICK QUESTION:</b>\n\nWhat is your #1 rule in soccer betting? ⚽\n\nA) Home team bias\nB) No emotional chasing\nC) Low-risk 1.3+ odds\n\nSmartest bettors strictly use B & C on FortunoBet to grow daily! 📈\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>JOIN THE WINNERS:</b> https://r1wexmo.life/betting?open=register&p=t02b","images":[]},
  {"date":"2026-07-29","time":"20:55","content":"💚 <b>GH¢440.00 RECEIVED VIA MTN MOMO! ⚡</b>\n\nEarly morning payout processed in 45 seconds! Bryan withdrew GH¢440.00 (~$40 USD). ID: 7732302. 💸\n\nZero withdrawal fees. Start with just UGX 2,000 / GH¢ 5 / ₦200 on MTN, Airtel, OPay, or PalmPay tonight!\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>SOAR AND CASH OUT NOW:</b> https://r1wexmo.life/betting?open=register&p=t02b","images":["with2.png"]},

  {"date":"2026-07-30","time":"12:00","content":"🛡️ <b>10% MONTHLY LOSS PROTECTION IS ACTIVE! 💰</b>\n\nNever lose alone. Take a screenshot of your monthly losses, send it to our channel, and we reload your balance with real cash! 💸\n\nPlus get a <b>500% bonus</b> on your 1st deposit! Min deposit: UGX 2,000 / GH¢ 5 / ₦200. ⚡\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>CLAIM CASHBACK & BONUS:</b> https://r1wexmo.life/betting?open=register&p=t02b","images":["fortunobet1.jpeg"]},
#   {"date":"2026-07-30","time":"16:30","content":"","images":[]},
  {"date":"2026-07-30","time":"23:55","content":"✈️ <b>AVIATOR HIT 85x MULTIPLIER TONIGHT! 🚀</b>\n\nTurn a tiny UGX 2,000 / GH¢ 5 / ₦200 deposit into UGX 170,000 / GH¢ 425 / ₦17,000 in seconds! 💸\n\nCash out before the plane flies away and withdraw straight to MoMo or OPay! ⚡\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>FLY AND CASH OUT NOW:</b> https://r1wexmo.life/betting?open=register&p=t02b","images":["fortunobet.jpeg"]},

  {"date":"2026-07-31","time":"12:00","content":"✅ <b>$91.20 WINNER — MJALLBY AIF (1.14 ODDS)! ⚽</b>\n\nChampions League qualifier locked in! $80 stake returned $91.20 profit. Total Balance: <b>$918.20</b>! 🏆\n\nStop scrolling on the sidelines. Build your weekend bankroll systematically! 💸\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>LOCK IN FRIDAY ODDS:</b> https://r1wexmo.life/betting?open=register&p=t02b","images":["win2.png"]},
#   {"date":"2026-07-31","time":"16:30","content":"💡 <b>SMART BETTING TIP:</b>\n\nNever risk rent money! Start small with UGX 2,000 / GH¢ 5 / ₦200 on FortunoBet. Instant 500% bonus doubles your power! ⚡\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>DEPOSIT & START WINNING:</b> https://r1wexmo.life/betting?open=register&p=t02b","images":[]},
  {"date":"2026-07-31","time":"21:38","content":"💸 <b>GH¢770.00 FRIDAY NIGHT CASHOUT PROOF! ✅</b>\n\nFriday night cash received! Bryan just got GH¢770.00 (~$70 USD) straight to MTN Mobile Money. ID: 7732303. Balance: GH¢1,004.50! 💚\n\nStart your weekend with instant payouts on MoMo, OPay & PalmPay! ⚡\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>COLLECT FRIDAY CASHOUTS:</b> https://r1wexmo.life/betting?open=register&p=t02b","images":["with3.png"]},

  {"date":"2026-08-01","time":"12:00","content":"🏆 <b>WEEKLY WINS RECAP: 100% SUCCESS RATE! 📊</b>\n\nEvery single banker bet hit this week! Total account balance soared to <b>$918.20</b>! 💸\n\n✅ Wolfsburg vs Lyon (0-2) — <b>WON (1.50)</b>\n✅ Sabah Baku FK vs KuPS — <b>WON (1.70)</b>\n✅ Mjällby AIF vs Lincoln — <b>WON (1.14)</b>\n✅ Simona Waltert Clay — <b>WON (1.42)</b>\n\nStop guessing on the sidelines. Back analytical picks on FortunoBet! 🎯\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>JOIN THE WINNERS:</b> https://r1wexmo.life/betting?open=register&p=t02b","images":["win3.png","win2.png"]},
  {"date":"2026-08-01","time":"16:30","content":"","images":[]},
  {"date":"2026-08-01","time":"23:55","content":"🎈 <b>20x MULTIPLIERS FLYING ON 1WIN BALLOON! 🚀</b>\n\nTurn UGX 2,000 / GH¢ 5 / ₦200 into UGX 40,000 / GH¢ 100 / ₦4,000 in under 20 seconds! 💸\n\nHold to inflate, release to cash out, and withdraw instantly to MoMo/OPay! ⚡\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>PLAY BALLOON AND WIN:</b> https://r1wexmo.life/betting?open=register&p=t02b","images":["fortunobet1.jpeg"]},

  {"date":"2026-08-02","time":"12:00","content":"💸 <b>WEEKLY CASHOUT RECAP: OVER $300 PAID OUT! 💚</b>\n\nReal proof! All player withdrawals processed in under 60 seconds straight to MTN Mobile Money & OPay! ⚡\n\n✅ GH¢715.00 (~$65 USD) — <b>PAID</b> (ID: 7732301)\n✅ GH¢440.00 (~$40 USD) — <b>PAID</b> (ID: 7732302)\n✅ GH¢770.00 (~$70 USD) — <b>PAID</b> (ID: 7732303)\n\nZero withdrawal fees. Start your new week with cash in hand! 🎯\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>REGISTER & CASH OUT NOW:</b> https://r1wexmo.life/betting?open=register&p=t02b","images":["with1.png","with2.png","with3.png"]},
  {"date":"2026-08-02","time":"23:55","content":"💸 <b>SUNDAY NIGHT MOMO CASHOUT PROOF! ✅</b>\n\nGH¢770.00 (~$70 USD) paid out instantly to Mobile Money / OPay! Transaction ID: 7732303. 💚\n\nZero withdrawal fees, zero queues. Start your new week as a winner! ⚡\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>REGISTER & CASH OUT NOW:</b> https://r1wexmo.life/betting?open=register&p=t02b","images":["with3.png"]}
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