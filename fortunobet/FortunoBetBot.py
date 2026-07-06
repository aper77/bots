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



{"date": "2026-07-06", "time": "12:00", "content": "⚽ <b>Brazil vs Norway</b> 🇧🇷🇳🇴\nNorway won 7 of last 10 away runs, but Brazil holds the qualify baseline. 🔥\n👉 GG (1.62) | Over 1.5 (1.22) | Brazil to Qualify (1.40) ✅\nChale, lock your numbers early! 👇\n🔑 Code: <code>fortunobet</code>\n👉 <b>BET HERE:</b> https://one-vv2340.com/betting/match/sport/brazil-vs-norway-37015245?p=z4m5", "images": ["brazil.jpeg"]},
{"date": "2026-07-06", "time": "17:21", "content": "🎯 World Cup Knockout Phase. France locking up results! ⚽\n\nWorld FIFA World Cup 2026. Odds 1.20. 🏆\nStake $40 ➔ Return $48 profit. Straight domination over Paraguay. 💸\nData clear. France attack baseline completely clear. 🎯\nSTOP LAGGING. The squad is counting money inside. Pick ONE. GO. 🔥\n\n🇬🇭 Deposit GH₵50 → play with GH₵300\n🇺🇬 Deposit UGX 12,000 → play with UGX 72,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>PLACE YOUR BET:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["win1.png"]},
{"date": "2026-07-06", "time": "23:55", "content": "🎰 2000 USDT WELCOME MATRIX ACTIVATED! 💎\n\nStop playing with loose change, chale. The slots are completely unlocked tonight! 🇬🇭🇺🇬\n1WIN just dropped the ultimate welcome package up to 2000 USDT for the smartest players in the hub.\nZero commission on deposits, zero delays on withdrawals, and maximum multiplier volatility. 💸\nEnter the code, fund your wallet, and watch the triple 7s hit the baseline right now! 👇\n\n🔑 Registration Code: <code>fortunobet</code>\n👉 <b>CLAIM YOUR 2000 USDT NOW:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["bonus1.jpeg"]},

{"date": "2026-07-07", "time": "12:00", "content": "🎰 <b>The main hub is completely hot!</b> 💥\nStop hunting single slips. Casino, slots, and bonuses are locked on one dashboard! 🏆\nNo dulling chale, tap below, claim your bonus matrix, and start collecting! 👇\n🔑 Code: <code>fortunobet</code>\n👉 <b>EXPLORE MAIN HUB:</b> https://fortunobet.com", "images": ["fortunobetVIP.jpeg"]},
{"date": "2026-07-07", "time": "18:55", "content": "💚 Another clean withdrawal entry. Mobile Money Statement Approved ✅\n\nFriday morning target reached. 08:54 AM MoMo confirmation. 💸\n$40 USD cleared completely out of the system. Balance still rolling. 💸\nChannel members are cashing out cleanly while you sit back and watch, chale.\n\n🇬🇭 Start with GH₵50 | 🇺🇬 Start with UGX 12,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>Test it yourself:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["with1.png"]},

{"date": "2026-07-08", "time": "12:00", "content": "", "images": []},
{"date": "2026-07-08", "time": "17:00", "content": "⚽ World Cup Single Slip Smash! ✅ 1WIN\n\nWorld FIFA World Cup 2026. Odds 1.44. 🏆\nStake $50 ➔ Cash out $72 profit instantly. Clean work. 💸\nColombia locked the defense early. Baseline structure held clear. 🎯\nSTOP WATCHING from the outside. Members eating good. Pick ONE. GO. 🔥\n\n🇬🇭 Deposit GH₵50 → play with GH₵300\n🇺🇬 Deposit UGX 12,000 → play with UGX 72,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>PLACE YOUR BET:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["win2.png"]},
{"date": "2026-07-08", "time": "23:55", "content": "🥊 MULTIPLE BETS BOOSTER: WINNING STARTS WITH A PERFECT STRIKE! ⚡\n\nWhy secure single payouts when you can stack the multiplier strings to the heavens? 🇬🇭🇺🇬\nGet a massive extra percentage bonus added directly to your accumulator slips automatically! \nEvery extra match you lock into the system increases the direct bonus payout structure. \nNo extra charges, no hidden codes—just pure leverage on your predictions. Drop the code and strike hard! 👇\n\n🔑 Registration Code: <code>fortunobet</code>\n👉 <b>BOOST YOUR MULTIPLES NOW:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["bonus3.jpeg"]},

{"date": "2026-07-09", "time": "12:00", "content": "🚀 <b>Stop leaving your gaming profits to luck!</b> 💸\nLive tracking, verified partner platforms, and elite casino algorithms are ready on FortunoBet. 🎰\nGgwe, stop watching from the sidelines. Tap below and activate your account! 👇\n🔑 Code: <code>fortunobet</code>\n👉 <b>OPEN PLATFORM NOW:</b> https://fortunobet.com", "images": ["fortunobetVIP.jpeg"]},
{"date": "2026-07-09", "time": "23:55", "content": "💚 Midnight Mobile Money Alert verified successfully! ✅\n\nWednesday execution complete. 12:14 AM real transaction check. 💸\n$50 USD extracted cleanly into local networks while town was asleep. 💸\nSmart bettors read the analytics node and secured early profit margins. 🙏\n\n🇬🇭 Start with GH₵50 | 🇺🇬 Start with UGX 12,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>Test it yourself:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["with2.png"]},

{"date": "2026-07-10", "time": "12:00", "content": "", "images": []},
{"date": "2026-07-10", "time": "17:00", "content": "⚾ Elite Diamond Clearcut! Baseball Execution ✅\n\nUSA MLB Match setup. Odds 1.26. 🏆\nStake $40 ➔ Secure $50.40 total return. ✅\nBaltimore Orioles dominated Washington Nationals cleanly. 💸\nNo long stories, stop analyzing on your own. Copy the system. 🔥\n\n🇬🇭 Deposit GH₵50 → play with GH₵300\n🇺🇬 Deposit UGX 12,000 → play with UGX 72,000\n🔑 Code: <code>fortunobet</code>\n👉 <b>PLACE YOUR BET:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["win3.png"]},
{"date": "2026-07-10", "time": "23:55", "content": "♠️ THE ULTIMATE PRIZE FOR A ROYAL FLUSH IS WAITING! 💎\n\nFor the true card sharks and strategic masterminds across Accra and Kampala! 🇬🇭🇺🇬\nEnter the high-stakes elite casino lobbies where the big players secure their revenue.\nMassive multipliers, certified fair play algorithms, and instantaneous high-volume withdrawals straight to your wallet. \nDo not play small. Tap the link, use the promo code, and sit at the winner's table tonight. 👇\n\n🔑 Registration Code: <code>fortunobet</code>\n👉 <b>ENTER THE ELITE LOBBY:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["bonus5.jpeg"]},

{"date": "2026-07-11", "time": "12:00", "content": "💎 <b>Turn MoMo stakes into massive casino runs!</b> 🎰\nFortunoBet gives you direct access to elite slots and live crash games. 💸\nKati, stop lagging behind. Enter early, use the code, and clear the table tonight! 👇\n🔑 Code: <code>fortunobet</code>\n👉 <b>ACCESS CASINO HUB:</b> https://fortunobet.com", "images": ["fortunobetVIP.jpeg"]},
{"date": "2026-07-11", "time": "23:55", "content": "🔵 CHOOSE THE BEST: SUPPORT YOUR FAVORITE TEAM & WIN TOGETHER! ⚽\n\nElite clubs are hitting the pitches, and the smart squad is already making regular bank from the form parameters! 🇬🇭🇺🇬\nGet the highest possible odds margins on global football fixtures using the ultimate betting setup.\nFast payouts, secure no-fee deposits, and huge welcome rewards tailored for real winners. \nStop guessing on your own—join the system, activate the promo code, and win together! 👇\n\n🔑 Registration Code: <code>fortunobet</code>\n👉 <b>START WINNING TOGETHER:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["bonus5.jpeg"]}

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