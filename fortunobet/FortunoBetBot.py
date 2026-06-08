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

{"date": "2026-06-08", "time": "12:00", "content": "🎾 <b>Aryna Sabalenka ✅ Roland Garros Women</b>\n\nRoland Garros Women. France. Odds 1.19. 🏆\n$100 → $119. Score 7-5 / 6-3. Dominated. 💸\n\nSabalenka clay form was elite. Serve locked, baseline clean.\nData was clear from start. E easy be. Mon ✅ Wed ✅ Fri ✅\n\nSTOP WATCHING. They collecting. JOIN NOW. 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>Join NOW:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["1win1.png"]},
{"date": "2026-06-08", "time": "17:00", "content": "🎯 Placing this now. Live.\n\nNew York Knicks vs San Antonio Spurs. NBA.\nKnicks home court strong. Spurs away form weak. Odds 1.77.\n\nEntering on 1WIN now. 👀\n👉 https://one-vv858.com/betting/prematch/basketball-23?p=z4m5", "images": []},
{"date": "2026-06-08", "time": "23:55", "content": "💸 <b>GH₵825 MTN Mobile Money — Arrived instant ✅</b>\n\nMonday 08 June. 06:00 AM. Real phone notification. 💚\nGH₵825 (~$55 USD). ID: 7732041. Same minute.\n\nKofi tested small first. Then scaled up big.\nNo delay. No wahala. Chale — just pure money. 💸\n\n1WIN pays. MTN confirms. Every single time. ✅\nAnother withdrawal confirmed today. You can't watch forever. ACT NOW. 🔥\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 <b>Start NOW:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["08waiting.png", "08completed.png"]},
{"date": "2026-06-09", "time": "16:00", "content": "💡 <b>How smart bettors protect their bankroll</b>\n\nChale, most people deposit everything at once and lose. Here is how smart players do it.\n\nStep 1: Start GH₵50 only. Test system first. Easy read.\nStep 2: Pick ONE sport you know well. No random gambling.\nStep 3: Withdraw MTN Mobile Money same day. 💸\n\nKofi did exactly this — withdrew same day, MTN instant. 🙏\nChannel members already doing this every week. Share with 2 friends!\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 <b>Start here:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["educashon.jpeg"]},
{"date": "2026-06-09", "time": "23:55", "content": "⚡ <b>GH₵825 MTN Mobile Money — Received instant ✅</b>\n\nMonday 08 June. 06:00 AM. Real MTN notification. 💚\nID: 7732041. Arrived same minute. Zero fees. No wahala.\n\nSome people still thinking. Kofi already tested and withdrew. Chale. 💸\nSmall test or big — 1WIN pays every single time. They collecting.\n\nWinning is important. Getting paid is more important. 🙏\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 https://r1wexmo.life/betting?open=register&p=t02b", "images": ["08fast.png"]},
{"date": "2026-06-10", "time": "12:00", "content": "🏀 <b>CSKA Moscow + Germany ✅ Multiple</b>\n\nVTB League + World Friendlies. Odds 1.42. 🏆\n$80 → $113.60. Both locked in. Controlled. 💸\n\nCSKA home dominance clear. Germany form obvious. H2H easy.\nData was sharp. Chale — e easy be. 🎯\n\nSTOP WATCHING. They collecting. JOIN NOW. 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>Join NOW:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["1win2.png"]},
{"date": "2026-06-10", "time": "20:00", "content": "😂 [REACTION — Wed June 10 — add your short reaction after today win]", "images": []},
{"date": "2026-06-10", "time": "23:55", "content": "🚨 <b>Members already sharing winning slips this morning. ✅</b>\n\nGH₵825 confirmed Monday. MTN instant. Real proof. 💚\nChannel members dey collect — you dey watch from outside.\n\nKofi deposited Sunday. Withdrew Monday 06:00 AM. Same minute. 💸\nSocial proof don enter — smart bettors already inside.\n\nChale how long you go keep watching? JOIN NOW. 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>NOW:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["urgencyWed.jpeg"]},
{"date": "2026-06-11", "time": "16:00", "content": "📊 <b>3 mistakes Ghana bettors make every week</b>\n\nChale, I see this every week. Stop making these mistakes.\n\n❌ Mistake 1: Betting big — no control. Lose everything fast.\n❌ Mistake 2: Random channels — no analysis. Pure luck.\n❌ Mistake 3: Chasing losses — emotion kills bankroll.\n\nKofi avoided all 3 — withdrew GH₵825 same day. They collecting. 💸\nWeekend fixtures loading — smart bettors positioning now. No dulling! 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>JOIN NOW:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["Authority.jpeg"]},
{"date": "2026-06-11", "time": "23:55", "content": "💚 <b>Kofi tested GH₵50 → withdrew GH₵825 ✅</b>\n\nReal story. This week. Kofi, Accra.\n\nDeposited GH₵50 Sunday — just to test the system.\nBet tennis Monday. Clay form obvious. Won big. 💸\nWithdrew same day. MTN MoMo. ID: 7732041. Instant.\n\nKofi entered early while odds were still favourable. Chale.\n\"I tested small first. Now I trust 1WIN.\" 🙏\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 <b>Test it:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["08fast.png"]},
{"date": "2026-06-12", "time": "12:00", "content": "⚽ <b>Brazil ✅ World National Friendlies</b>\n\nWorld Friendlies. Odds 1.12. 🏆\n$100 → $112. Score 2-4 / 6 goals. Dominated. 💸\n\nBrazil home form was elite. Attack locked Panama completely.\nData obvious. H2H clear. Easy read for smart bettors. 🎯\n\nSTOP WATCHING. They collecting. JOIN NOW. 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>Join NOW:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["1win3.png"]},
{"date": "2026-06-12", "time": "20:00", "content": "😂 [REACTION — Fri June 12 — add your short reaction after today win]", "images": []},
{"date": "2026-06-12", "time": "23:55", "content": "💸 <b>GH₵930 MTN Mobile Money — Arrived instant ✅</b>\n\nTuesday 10 June. 01:00 PM. Real phone notification. 💚\nGH₵930 (~$62 USD). ID: MTN-7732042. Same minute.\n\nStarted small. Stayed disciplined. Withdrew same day.\nNo delay. No wahala. Chale — just pure money. 💸\n\nAnother withdrawal confirmed today. Proof right here. ✅\nYou can't collect what you never deposited. ACT NOW. 🔥\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 <b>Start NOW:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["10waiting.png", "10complated.png"]},
{"date": "2026-06-13", "time": "16:00", "content": "🏆 <b>Winning ticket Sunday.\n💸 Withdrawal Monday.</b>\n\nStake: $100 — Aryna Sabalenka. Roland Garros. ✅\nProfit: $119. Odds 1.19. MTN MoMo GH₵825. ID: 7732041. Instant. ✅\n\nKofi won Sunday. Withdrew Monday 06:00 AM. Same minute. Chale. 💸\nThese clay odds won't stay forever — smart bettors entered early. 🎯\n\nWinning means nothing if you can't withdraw. This one paid. 🔥\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 https://r1wexmo.life/betting?open=register&p=t02b", "images": ["1win1.png", "08fast.png"]},
{"date": "2026-06-13", "time": "20:00", "content": "😂 [REACTION — Sat June 13 — add your short reaction about MTN payout]", "images": []},
{"date": "2026-06-13", "time": "21:00", "content": "⚡ <b>GH₵650 MTN Mobile Money — Received instant ✅</b>\n\nFriday 12 June. 11:12 AM. Real MTN notification. 💚\nID: MTN-7732043. Arrived same minute. Zero fees. No wahala.\n\nSunday fixtures loading on 1WIN right now. Chale.\nOdds won't stay this high for long — window open now. 💸\n\nThey collecting while you dey watch. Test small first. 🙏\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 https://r1wexmo.life/betting?open=register&p=t02b", "images": ["12fast.png"]},
{"date": "2026-06-14", "time": "16:00", "content": "💚 <b>This week. Real results. Full transparency. ✅</b>\n\nMon: $100 → $119 ✅ Sabalenka — clay dominance. Easy read.\nWed: $80 → $113.60 ✅ CSKA + Germany — data clear.\nFri: $100 → $112 ✅ Brazil — home form locked in.\n\nGH₵825 + GH₵930 + GH₵650 = All MTN instant. 💸\nSome people watched all week. Others collected. No dulling. 🔥\nChale — share with 2 betting friends! Next week YOU start.\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>JOIN NOW:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["08fast.png", "10fast.png", "12fast.png"]},
{"date": "2026-06-14", "time": "23:55", "content": "🎰 <b>500% Bonus — Only active today! ❌</b>\n\n1WIN Casino. Fortune Tiger. Gates of Olympus. 💰\nDeposit GH₵50 → play with GH₵300 + 500 free spins. Chale.\n\n500% promo code still works right now — not guaranteed tomorrow. ⚠️\nKofi withdrew GH₵825 this week. They collecting. No dulling. 💸\n\nWe test. We withdraw. We scale. JOIN NOW or miss it. 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>Play NOW:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["casinosun.jpeg"]},

{"date": "2026-06-15", "time": "12:00", "content": "🏀 <b>Oklahoma City Thunder ✅ USA NBA</b>\n\nUSA NBA Playoffs. Odds 1.49. 🏆\n$70 → $104.30. Final 127-114. Led every quarter. 💸\n\nOKC home court was elite. Defence locked Spurs completely.\nData clear. H2H obvious. Chale — e easy be. 🎯\n\nSTOP WATCHING. They collecting. JOIN NOW. 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>Join NOW:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["2win1.png"]},
{"date": "2026-06-15", "time": "20:00", "content": "🎯 [LIVE BET — Mon June 15 — add real game + league + odds]", "images": []},
{"date": "2026-06-15", "time": "23:55", "content": "💸 <b>GH₵450 MTN Mobile Money — Arrived instant ✅</b>\n\nMonday 15 June. 05:10 AM. Real phone notification. 💚\nGH₵450 (~$30 USD). ID: MTN-7732023. Same minute.\n\nKofi tested small first. Then scaled up big.\nNo delay. No wahala. Chale — just pure money. 💸\n\nAnother withdrawal confirmed today. Proof is right here. ✅\nYou can't collect what you never deposited. ACT NOW. 🔥\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 <b>Start NOW:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["15waiting.png", "15fast.png"]},
{"date": "2026-06-16", "time": "16:00", "content": "💡 <b>How smart bettors protect their bankroll</b>\n\nChale, most people deposit everything at once and lose. Here is how smart players do it.\n\nStep 1: Start GH₵50 only. Test system first. Easy read.\nStep 2: Pick ONE sport you know well. No random gambling.\nStep 3: Withdraw MTN Mobile Money same day. 💸\n\nKofi did exactly this — withdrew same day, MTN instant. 🙏\nChannel members already doing this every week. Share with 2 friends!\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 <b>Start here:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["bonus1.jpeg"]},
{"date": "2026-06-16", "time": "23:55", "content": "⚡ <b>GH₵450 MTN Mobile Money — Received instant ✅</b>\n\nMonday 15 June. 05:10 AM. Real MTN notification. 💚\nID: MTN-7732023. Arrived same minute. Zero fees. No wahala.\n\nSome people still thinking. Kofi already tested and withdrew. Chale. 💸\nSmall test or big — 1WIN pays every single time. They collecting.\n\nWinning is important. Getting paid is more important. 🙏\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 https://r1wexmo.life/betting?open=register&p=t02b", "images": ["15fast.png"]},
{"date": "2026-06-17", "time": "12:00", "content": "🏀 <b>Dallas Wings W ✅ USA WNBA</b>\n\nUSA WNBA. Odds 1.15. 🏆\n$50 → $57.50. Final 79-56. Dominated all 4 quarters. 💸\n\nDallas Wings home form elite. Defence locked Seattle completely.\nData clear. H2H obvious. Chale — e easy be. 🎯\n\nSTOP WATCHING. They collecting. JOIN NOW. 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>Join NOW:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["2win2.png"]},
{"date": "2026-06-17", "time": "20:00", "content": "😂 [REACTION — Wed June 17 — add your short reaction after today win]", "images": []},
{"date": "2026-06-17", "time": "23:55", "content": "🚨 <b>Members already withdrew twice this week. ✅</b>\n\nGH₵450 confirmed Monday. MTN instant. Real proof. 💚\nChannel members dey collect — you dey watch from outside.\n\nKofi deposited Sunday. Withdrew Monday 05:10 AM. Same minute. 💸\nSocial proof don enter — smart bettors already inside.\n\nChale how long you go keep watching? JOIN NOW. 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>NOW:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["bonus2.jpeg"]},
{"date": "2026-06-18", "time": "16:00", "content": "📊 <b>3 mistakes Ghana bettors make every week</b>\n\nChale, I see this every week. Stop making these mistakes.\n\n❌ Mistake 1: Betting big — no control. Lose everything fast.\n❌ Mistake 2: Random channels — no analysis. Pure luck.\n❌ Mistake 3: Chasing losses — emotion kills bankroll.\n\nKofi avoided all 3 — withdrew GH₵450 same day. They collecting. 💸\nWeekend fixtures loading — smart bettors positioning now. No dulling! 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>JOIN NOW:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["bonus3.jpeg"]},
{"date": "2026-06-18", "time": "23:55", "content": "💚 <b>Kofi tested GH₵50 → withdrew GH₵450 ✅</b>\n\nReal story. This week. Kofi, Accra.\n\nDeposited GH₵50 Sunday — just to test the system.\nBet NBA Monday. Home court form obvious. Won big. 💸\nWithdrew same day. MTN MoMo. ID: MTN-7732023. Instant.\n\nKofi entered early while odds were still favourable. Chale.\n\"I tested small first. Now I trust 1WIN.\" 🙏\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 <b>Test it:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["15fast.png"]},
{"date": "2026-06-19", "time": "12:00", "content": "🎾 <b>Flavio Cobolli ✅ Roland Garros Men</b>\n\nRoland Garros Men. France. Odds 1.13. 🏆\n$90 → $101.70. Score 6-2 / 6-3 / 7-6. Dominated. 💸\n\nCobolli clay form was elite. Baseline locked, serve clean.\nData clear. H2H obvious. Chale — e easy be. 🎯\n\nSTOP WATCHING. They collecting. JOIN NOW. 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>Join NOW:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["2win3.png"]},
{"date": "2026-06-19", "time": "20:00", "content": "😂 [REACTION — Fri June 19 — add your short reaction after today win]", "images": []},
{"date": "2026-06-19", "time": "23:55", "content": "💸 <b>GH₵750 MTN Mobile Money — Arrived instant ✅</b>\n\nWednesday 17 June. 06:43 AM. Real phone notification. 💚\nGH₵750 (~$50 USD). ID: MTN-7732024. Same minute.\n\nStarted small. Stayed disciplined. Withdrew same day.\nFinal weekend matches loading tonight — last chance to position. ✅\nNo delay. No wahala. Chale — just pure money. 💸\n\nYou can't collect what you never deposited. ACT NOW. 🔥\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 <b>Start NOW:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["17waiting.png", "17fast.png"]},
{"date": "2026-06-20", "time": "16:00", "content": "🏆 <b>Winning ticket May.\n💸 Withdrawal Monday.</b>\n\nStake: $70 — OKC Thunder. USA NBA. ✅\nProfit: $104.30. Odds 1.49. MTN MoMo GH₵450. ID: MTN-7732023. Instant. ✅\n\nKofi won May. Withdrew Monday 05:10 AM. Same minute. Chale. 💸\nNBA playoff odds won't stay this high — smart bettors entered early. 🎯\n\nWinning means nothing if you can't withdraw. This one paid. 🔥\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 https://r1wexmo.life/betting?open=register&p=t02b", "images": ["2win1.png", "15fast.png"]},
{"date": "2026-06-20", "time": "20:00", "content": "😂 [REACTION — Sat June 20 — add your short reaction about MTN payout]", "images": []},
{"date": "2026-06-20", "time": "21:00", "content": "⚡ <b>GH₵1,200 MTN Mobile Money — Received instant ✅</b>\n\nFriday 19 June. 11:32 AM. Real MTN notification. 💚\nID: MTN-7732025. Arrived same minute. Zero fees. No wahala.\n\nSunday fixtures already loading on 1WIN right now. Chale.\nOdds on top matches won't stay this high for long. 💸\n\nThey collecting while you dey watch. Test small first. 🙏\n\nStart with GH₵50. Test withdrawal yourself.\n🔑 Code: <code>fortunobet</code>\n👉 https://r1wexmo.life/betting?open=register&p=t02b", "images": ["19fast.png"]},
{"date": "2026-06-21", "time": "16:00", "content": "💚 <b>This week. Real results. Full transparency. ✅</b>\n\nMon: $70 → $104.30 ✅ OKC Thunder — home court clear.\nWed: $50 → $57.50 ✅ Dallas Wings — form obvious.\nFri: $90 → $101.70 ✅ Cobolli — clay dominance.\n\nGH₵450 + GH₵750 + GH₵1,200 = All MTN instant. 💸\nSome people watched all week. Others collected. No dulling. 🔥\nChale — share with 2 betting friends! Next week YOU start.\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>JOIN NOW:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["15fast.png", "17fast.png", "19fast.png"]},
{"date": "2026-06-21", "time": "23:55", "content": "🎰 <b>500% Bonus — Only active today! ❌</b>\n\n1WIN Casino. Fortune Tiger. Gates of Olympus. 💰\nDeposit GH₵50 → play with GH₵300 + 500 free spins. Chale.\n\n500% promo code still works right now — not guaranteed tomorrow. ⚠️\nKofi withdrew GH₵1,200 this week. They dey collect. No dulling. 💸\n\nWe test. We withdraw. We scale. JOIN NOW or miss it. 🔥\n\nDeposit GH₵50 → play with GH₵300\n🔑 Code: <code>fortunobet</code>\n👉 <b>Play NOW:</b> https://r1wexmo.life/betting?open=register&p=t02b", "images": ["bonus4.jpeg"]}

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