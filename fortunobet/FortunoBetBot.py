from telegram import Bot, InputMediaPhoto
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime, timedelta
import pytz
import os

# ====== CONFIG ======
BOT_TOKEN = "7924334103:AAHkeWr7KvmWpu9gFk7Eknd9_6NJn3S1WjA"
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

posts = [

# {"date":"2026-03-03","time":"23:00","content":"🎁 <b>First deposit = 500% bonus instantly</b>\n\n₦2,000 → ₦12,000 ⚡\n₦10,000 → ₦60,000 ⚡\n₦50,000 → ₦300,000 ⚡\n\nBonus hits your account immediately.\nWithdraw same day — proven multiple times. 💚\n\nNew players only.\nStart big from day one. 🔥\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Claim bonus:</b>\nhttps://1wfafs.life/casino/list?open=register&p=z4m5","images":["031.png"]},
# {"date":"2026-03-03","time":"14:00","content":"💚 <b>$250 → $365. Detroit Pistons ✅</b>\n\nUSA NBA. Odds 1.46 — safe bet, solid volume. 🏀\n\n$115 profit from one bet.\nThis is how consistent players win. 💸\n\nSmall bets = small wins.\nBig bets = big wins.\nWhich one you choosing? 🔥\n\nDeposit ₦80,000 → play with ₦480,000\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Join winners:</b>\nhttps://1wfafs.life/casino/list?open=register&p=z4m5","images":["win2.png"]},

# {"date":"2026-03-04","time":"23:00","content":"💰 <b>Start ₦1,000. Withdraw ₦10,000 next week.</b>\n\nMinimum deposit. Maximum opportunity. 💚\n\n₦1,000 → ₦2,000 + 70 spins instantly\n\nSmall start. Big results.\nStart today. See results by weekend.\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>Begin now:</b> https://1wfafs.life/casino/list?open=register&p=z4m5","images":["041.png"]},
# {"date":"2026-03-04","time":"14:00","content":"💚 <b>$300 → $333. Cleveland Cavaliers ✅</b>\n\nUSA NBA. Odds 1.11 — ultra safe, big volume. 🏀\n\n$33 profit. Clean and simple.\nDo this 10 times = $330 profit. 💸\n\nThis is how you build bankroll:\nSafe odds + Big stakes = Steady money. 💚\n\nDeposit ₦100,000 → play with ₦600,000\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Bet big:</b>\nhttps://1wfafs.life/casino/list?open=register&p=z4m5","images":["win3.png"]},

# {"date":"2026-03-05","time":"23:00","content":"🎰 <b>₦173,000,000 Slotopia tournament live</b>\n\n€105,000 prize pool. 🔥\n\nNo special entry.\nJust play Slotopia slots = you're in.\n\nDeposit ₦5,000 → play with ₦30,000\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Join tournament:</b>\nhttps://1wfafs.life/casino/list?open=register&p=z4m5","images":["052.png"]},
# {"date":"2026-03-05","time":"14:00","content":"💚 <b>$150 → $201. Dmytro Prylepa ✅</b>\n\nInternational Men. Setka Cup Tennis. 🎾\nOdds 1.34 — safe bet, solid profit.\n\n$51 profit from one tennis match.\nThis is how you win consistently. 💸\n\nTennis = steady money.\nSafe odds + Smart stakes = Daily profits. 🔥\n\nDeposit ₦50,000 → play with ₦300,000\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Start winning:</b>\nhttps://1wfafs.life/casino/list?open=register&p=z4m5","images":["win4.jpg"]},

# {"date":"2026-03-06","time":"14:00","content":"🏆 <b>₦12,100,000,000 Drops & Wins running</b>\n\n€7,350,000 prize pool across all games. 💰\n\nEvery spin counts.\nPragmatic Play slots = automatic entry.\n\nDeposit ₦5,000 → play with ₦30,000\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Enter now:</b>\nhttps://1wfafs.life/casino/list?open=register&p=z4m5","images":["061.png"]},
# {"date":"2026-03-06","time":"21:00","content":"💚 <b>$150 → $187.50. Nazar Danilyuk ✅</b>\n\nInternational Men. Setka Cup Tennis. 🎾\nOdds 1.25 — ultra safe, steady win.\n\n$37.50 profit. Clean and simple.\nTwo tennis wins back-to-back. 💸\n\nYesterday: $51 profit ✅\nToday: $37.50 profit ✅\nTotal: $88.50 in 24 hours. 🔥\n\nDeposit ₦50,000 → play with ₦300,000\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Join winners:</b>\nhttps://1wfafs.life/casino/list?open=register&p=z4m5","images":["win5.jpg"]},

# {"date":"2026-03-07","time":"13:00","content":"🚀 <b>₦6,600,000,000 Aviatrix prize pool live</b>\n\n$4,000,000 total jackpot. 🔥\n\nEvery round = chance to win big.\nCash out before it flies away. ⚡\n\nDeposit ₦5,000 → play with ₦30,000\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Play now:</b>\nhttps://fortunobet.com/1win","images":["071.png"]},
# #  importat withdow post for this day
# {"date":"2026-03-07","time":"21:00","content":"💸 <b>Withdrew ₦27,000 this afternoon — 15 minutes</b>\n\nRequested: 3:42 PM ✅\nArrived Opay: 3:57 PM ✅\n\nSame day. Zero wahala. Every time. 💚\n\nYou can't withdraw what you don't deposit.\nStart today. Withdraw this week.\n\nDeposit ₦5,000 → play with ₦30,000\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Start now:</b>\nhttps://fortunobet.com/1win","images":["072.png"]},

# {"date":"2026-03-08","time":"23:00","content":"💰 <b>30% cashback on every losing day</b>\n\nAutomatic. No claim needed. ✅\n\nLose ₦10,000 → ₦3,000 back next day\nLose ₦50,000 → ₦15,000 back next day\n\nEvery bet protected.\nSmart players protect bankroll. 💚\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Join protected:</b>\nhttps://fortunobet.com/1win","images":["081.png"]},
# {"date":"2026-03-08","time":"12:00","content":"💚 <b>This week: 5 bets, 5 wins, $388 total profit ✅</b>\n\nMarch 1: $380 → $479 (NBA) ✅\nMarch 1: $250 → $365 (NBA) ✅\nMarch 1: $300 → $333 (NBA) ✅\nMarch 3: $150 → $201 (Tennis) ✅\nMarch 3: $150 → $187 (Tennis) ✅\n\nTotal staked: $1,230\nTotal returned: $1,618\nNet profit: $388 💸\n\n100% win rate this week.\nNBA + Tennis = My winning formula. 🔥\n\nLast week you watched.\nThis week you watching again.\nNext week? Your turn to win. 💚\n\nDeposit ₦100,000 → play with ₦600,000\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Start Monday winning:</b>\nhttps://fortunobet.com/1win","images":["win1.jpeg","win2.png","win3.png","win4.jpg","win5.jpg"]},

# ========== MONDAY MARCH 9 ==========

{"date":"2026-03-09","time":"14:00","content":"💚 <b>$150 → $202.50. Arthur Fils ✅</b>\n\nATP Indian Wells. USA. Hard Court. 🎾\nOdds 1.35 — safe bet, solid profit.\n\n$52.50 profit from overnight tennis.\nThis is how you win while you sleep. 💸\n\nTennis never stops.\nI never stop winning. 🔥\n\nDeposit ₦50,000 → play with ₦300,000\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Start winning:</b>\nhttps://fortunobet.com/1win","images":["win6.png"]},
{"date":"2026-03-09","time":"23:30","content":"📊 <b>Last 7 days on this channel:</b>\n\n✅ 5 new members joined\n✅ 1 first deposit completed\n✅ 172% business growth\n✅ $3.33 total deposits (+382%)\n\nThey stopped watching. Started betting. Now winning.\nYou're still watching. 💸\n\nNew week. Fresh start.\nYour turn? 🔥\n\nDeposit ₦5,000 → play with ₦30,000\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Join now:</b>\nhttps://fortunobet.com/1win","images":["092.png"]},

# ========== TUESDAY MARCH 10 ==========

{"date":"2026-03-10","time":"14:00","content":"💸 <b>Withdrew ₦38,000 yesterday — 22 minutes</b>\n\nRequested: 3:15 PM ✅\nArrived Opay: 3:37 PM ✅\n\nSame day. Zero wahala. Every time. 💚\n\nThis is the 5th withdrawal this month.\nAll under 45 minutes. All arrived.\n\nYou can't withdraw what you don't deposit.\nStart today. Withdraw this week.\n\nDeposit ₦10,000 → play with ₦60,000\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Start now:</b>\nhttps://fortunobet.com/1win","images":["101.png"]},
{"date":"2026-03-10","time":"23:30","content":"💚 <b>$100 → $123. Felix Auger-Aliassime ✅</b>\n\nATP Indian Wells. USA. Hard Court. 🎾\nOdds 1.23 — ultra safe, steady cash.\n\n$23 profit. Clean and simple.\nTwo tennis wins in 1 hour. 💸\n\nYesterday: $52.50 profit ✅\nToday: $23 profit ✅\nTotal: $75.50 in 24 hours. 🔥\n\nDeposit ₦35,000 → play with ₦210,000\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Join now:</b>\nhttps://fortunobet.com/1win","images":["win7.png"]},

# ========== WEDNESDAY MARCH 11 ==========

{"date":"2026-03-11","time":"14:00","content":"🎁 <b>First deposit = 500% bonus instantly</b>\n\n₦2,000 → ₦12,000 ⚡\n₦10,000 → ₦60,000 ⚡\n₦50,000 → ₦300,000 ⚡\n\nBonus hits your account immediately.\nWithdraw same day — proven multiple times. 💚\n\nNew players only.\nStart big from day one. 🔥\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Claim bonus:</b>\nhttps://fortunobet.com/1win","images":["111.png"]},
{"date":"2026-03-11","time":"23:30","content":"💚 <b>$160 → $224. Cleveland Cavaliers ✅</b>\n\nCyberbasketball NBA. eSports Battle. 🏀\nOdds 1.12 — ultra safe, big volume bet.\n\n$64 profit from one cyber match.\nThis is how you stack wins consistently. 💸\n\neSports = 24/7 opportunities.\nReal NBA skills. Real profits. 🔥\n\nDeposit ₦50,000 → play with ₦300,000\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Join winners:</b>\nhttps://fortunobet.com/1win","images":["win8.png"]},
# ========== THURSDAY MARCH 12 ==========

{"date":"2026-03-12","time":"14:00","content":"💚 <b>Member result: Started ₦5,000 last week</b>\n\n\"Balance today: ₦47,000\nWithdrew ₦22,000 to Opay\nStill playing with ₦25,000\nThis is real.\" — Tunde, Lagos\n\nHe joined 9 days ago.\nDeposited ₦5,000.\nAlready withdrew profit. 💸\n\nLast week he was watching.\nToday he's winning. Your turn? 🔥\n\nDeposit ₦5,000 → play with ₦30,000\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Start today:</b>\nhttps://fortunobet.com/1win","images":["121.png"]},
{"date":"2026-03-12","time":"23:30","content":"💚 <b>$150 → $223.50. Jack Draper ✅</b>\n\nATP Indian Wells. USA. Hard Court. 🎾\nOdds 1.49 — safe bet, solid profit.\n\n$73.50 profit from tennis overnight.\nThree nights, three tennis wins. 💸\n\nMarch 9: $52.50 ✅\nMarch 10: $23 ✅\nMarch 12: $73.50 ✅\nTotal: $149 from tennis this week. 🔥\n\nDeposit ₦50,000 → play with ₦300,000\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Start winning:</b>\nhttps://fortunobet.com/1win","images":["win9.png"]},
# ========== FRIDAY MARCH 13 ==========

{"date":"2026-03-13","time":"14:00","content":"🇳🇬 <b>Why Nigerians choose 1WIN:</b>\n\n✅ Opay/Palmpay instant deposit\n✅ Same-day withdrawal (proven)\n✅ 30% cashback protection\n✅ 500% welcome bonus\n\nYour platform gives less? Switch today. 💸\n\nDeposit ₦2,000 → play with ₦12,000\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Join now:</b>\nhttps://fortunobet.com/1win","images":["131.png"]},
{"date":"2026-03-13","time":"23:30","content":"💚 <b>$160 → $224. Atlanta Hawks ✅</b>\n\nCyberbasketball NBA. eSports Battle. 🏀\nOdds 1.40 — safe cyber bet, solid return.\n\n$64 profit. Clean and simple.\nTwo cyber NBA wins this week. 💸\n\nWednesday: $64 ✅\nFriday: $64 ✅\nCyber NBA = consistent money. 🔥\n\nDeposit ₦50,000 → play with ₦300,000\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Bet cyber:</b>\nhttps://fortunobet.com/1win","images":["win10.png"]},
# ========== SATURDAY MARCH 14 ==========

{"date":"2026-03-14","time":"11:00","content":"💰 <b>30% cashback on every losing day</b>\n\nAutomatic. No claim needed. ✅\n\nLose ₦10,000 → ₦3,000 back next day\nLose ₦50,000 → ₦15,000 back next day\n\nEvery bet protected.\nSmart players protect bankroll. 💚\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Join protected:</b>\nhttps://fortunobet.com/1win","images":["141.png"]},
{"date":"2026-03-14","time":"19:00","content":"⚽ <b>Weekend here — all big leagues live</b>\n\nPremier League, La Liga, Serie A 🔥\n\n52 people from this channel placed weekend bets.\nMatches start tomorrow morning.\n\nYou watching or playing?\n\nDeposit ₦10,000 → play with ₦60,000\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Bet now:</b>\nhttps://fortunobet.com/1win","images":["142.png"]},

# ========== SUNDAY MARCH 15 ==========

{"date":"2026-03-15","time":"11:00","content":"💚 <b>This week: 10 bets, 10 wins, $540 total profit ✅</b>\n\nMarch 1: $380 → $479 (NBA) +$99 ✅\nMarch 1: $250 → $365 (NBA) +$115 ✅\nMarch 1: $300 → $333 (NBA) +$33 ✅\nMarch 3: $150 → $201 (Tennis) +$51 ✅\nMarch 3: $150 → $187 (Tennis) +$37.50 ✅\nMarch 9: $150 → $202 (Tennis) +$52.50 ✅\nMarch 10: $100 → $123 (Tennis) +$23 ✅\nMarch 11: $160 → $224 (Cyber NBA) +$64 ✅\nMarch 12: $150 → $223 (Tennis) +$73.50 ✅\nMarch 13: $160 → $224 (Cyber NBA) +$64 ✅\n\nTotal staked: $1,950\nTotal returned: $2,490\nNet profit: $540 💸\n\n100% win rate TWO weeks straight.\nNBA + Tennis + Cyber = My winning system. 🔥\n\nTwo weeks you watched.\nNext week? Your turn to win. 💚\n\nDeposit ₦100,000 → play with ₦600,000\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Start Monday winning:</b>\nhttps://fortunobet.com/1win","images":["win1.jpeg","win2.png","win3.png","win4.jpg","win5.jpg","win6.png","win7.png","win8.png","win9.png","win10.png"]},
{"date":"2026-03-15","time":"20:00","content":"🏆 <b>₦6,600,000,000 Aviatrix prize pool live</b>\n\n$4,000,000 total jackpot. 🔥\n\nEvery round = chance to win big.\nCash out before it flies away. ⚡\n\nDeposit ₦5,000 → play with ₦30,000\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Play now:</b>\nhttps://fortunobet.com/1win","images":["152.png"]},

]

# ====== FUNCTION TO SEND POSTS ======
def send_post(post):
    try:
        # We use HTML mode to support <b>bold</b> and <code>tap-to-copy</code>
        P_MODE = "HTML"

        if "images" in post and post["images"]:
            # If multiple images, send as album
            if len(post["images"]) > 1:
                media_group = []
                for idx, img_file in enumerate(post["images"]):
                    if os.path.exists(img_file):
                        if idx == 0:
                            # Apply HTML formatting to the caption
                            media_group.append(InputMediaPhoto(open(img_file, "rb"), caption=post["content"], parse_mode=P_MODE))
                        else:
                            media_group.append(InputMediaPhoto(open(img_file, "rb")))
                if media_group:
                    bot.send_media_group(chat_id=CHANNEL_ID, media=media_group)
            else:
                # Single image
                img_file = post["images"][0]
                if os.path.exists(img_file):
                    with open(img_file, "rb") as photo:
                        # Apply HTML formatting to the photo caption
                        bot.send_photo(chat_id=CHANNEL_ID, photo=photo, caption=post["content"], parse_mode=P_MODE)
                else:
                    # Fallback to text if image missing
                    bot.send_message(chat_id=CHANNEL_ID, text=post["content"], parse_mode=P_MODE)
        else:
            # Text only
            bot.send_message(chat_id=CHANNEL_ID, text=post["content"], parse_mode=P_MODE)

        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Posted Successfully")
    except Exception as e:
        print(f"Failed to post: {e}")

# ====== SCHEDULE JOBS ======
for post in posts:
    # Convert string date to real datetime
    post_date = datetime.strptime(post["date"], "%Y-%m-%d")
    hour, minute = map(int, post["time"].split(":"))

    # Schedule EXACT date + time
    scheduler.add_job(
        send_post,
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


# ====== START BOT ======
print("Bot is running and will post messages automatically...")
scheduler.start()