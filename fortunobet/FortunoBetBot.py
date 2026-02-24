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
{"date":"2026-02-24","time":"23:00","content":"🌙 <b>Live matches, live odds, live money</b>\n\nFirst deposit = 500% instantly ⚡\n₦2,000 → ₦12,000 tonight. Don’t wait.\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>Jump in:</b> https://1wkrii.life/v3/landing-page/football?p=5pe0","images":["172.png"]},

{"date":"2026-02-25","time":"15:00","content":"⏰ <b>Welcome bonus won’t stay forever</b>\n\n100% + 70 spins first deposit → up to 500% across 4 deposits 🔥\nThose inside are already playing bigger.\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>Join before it ends:</b> https://1wffxn.life/v3/aggressive-casino?p=xomk","images":["232.png"]},
{"date":"2026-02-25","time":"21:00","content":"🏆 <b>₦173,000,000 Slotopia prize pool — live now</b>\n\nEvery spin counts toward the jackpot. 💰\nNo special entry needed — just play and win.\n\n€105,000 total prize pool closing soon.\n\nDeposit ₦2,000 → play with ₦12,000\nMore spins = better chances.\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>Enter now:</b> https://1wfafs.life/casino/list?open=register&p=z4m5","images":["251.png"]},

{"date":"2026-02-26","time":"14:00","content":"⚽ <b>My pick tonight: Newcastle -1.5 goals</b>\n\nQarabag is weak. Newcastle needs this win badly.\n\nOdds at 1.52 = solid value. 💰\nI'm putting ₦10,000 on this.\n\nDeposit ₦2,000 → play with ₦12,000\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>Bet with me:</b> https://1wfafs.life/casino/list?open=register&p=z4m5","images":["261.png"]},
{"date":"2026-02-26","time":"21:00","content":"🎰 <b>Sweet Bonanza 1000 — bigger wins, same chaos</b>\n\nUpgraded version. Higher multipliers. Bigger tumbles. 💥\n\nSomeone just hit ₦220,000 on this 3 hours ago. Real money. ✅\n\nDeposit ₦2,000 → play with ₦12,000\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>Spin now:</b> https://1wfafs.life/casino/list?open=register&p=z4m5","images":["262.png"]},

{"date":"2026-02-27","time":"14:00","content":"💰 <b>Cashback up to 30% — losing hurts less here</b>\n\nEvery bet protected. Win or lose. ✅\n\nLose ₦10,000 → get ₦3,000 back automatically.\nNo manual claim. Just play smart.\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>Start protected:</b> https://1wfafs.life/casino/list?open=register&p=z4m5","images":["271.png"]},
{"date":"2026-02-27","time":"21:00","content":"🎁 <b>2nd deposit = 120% + 100 Free Spins</b>\n\nMost platforms stop at the first bonus.\n1WIN keeps rewarding. 💚\n\n487 Nigerians claimed this yesterday.\nYour turn now.\n\nDeposit ₦5,000 → play with ₦11,000 + 100 spins\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>Claim yours:</b> https://1wfafs.life/casino/list?open=register&p=z4m5","images":["272.png"]},

{"date":"2026-02-28","time":"14:00","content":"🏆 <b>₦6,600,000,000 Aviatrix prize pool — closes Sunday</b>\n\nCash out before it flies away. 🚀\nEvery round is a chance to win big.\n\nLast 3 days to enter.\n\nDeposit ₦2,000 → play with ₦12,000\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>Play now:</b> https://1wfafs.life/casino/list?open=register&p=z4m5","images":["281.png"]},
{"date":"2026-02-28","time":"21:00","content":"🇳🇬 <b>Withdraw same day — Opay, Palmpay, Bank, USDT</b>\n\nNo delays. No excuses. No stories. ✅\n\nWin today → cash in your account tonight.\n\nDeposit ₦2,000 → play with ₦12,000\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>Start now:</b> https://1wfafs.life/casino/list?open=register&p=z4m5","images":["282.png"]},

{"date":"2026-03-01","time":"14:00","content":"⚽ <b>My weekend pick: Inter Milan both halves at 2.1</b>\n\nBodo/Glimt can't handle Inter's pressure.\n\nBoth halves win = juicy odds. 💰\nI'm backing this with ₦8,000.\n\nDeposit ₦2,000 → play with ₦12,000\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>Bet now:</b> https://1wfafs.life/casino/list?open=register&p=z4m5","images":["011.png"]},
{"date":"2026-03-01","time":"21:00","content":"💸 <b>Lost this week? 30% comes back automatically</b>\n\nBad week happens. Smart players recover. 💚\n\nLose ₦20,000 → get ₦6,000 back.\nNo claim needed. Just protection.\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>Join now:</b> https://1wfafs.life/casino/list?open=register&p=z4m5","images":["012.png"]},

{"date":"2026-03-02","time":"14:00","content":"⚽ <b>Weekend football — bet bigger with bonus</b>\n\nPremier League. La Liga. Serie A. All live. 🔥\n\n152 people from this channel placed bets yesterday.\nYou watching or playing?\n\nDeposit ₦10,000 → play with ₦60,000\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>Bet now:</b> https://1wfafs.life/casino/list?open=register&p=z4m5","images":["021.png"]},
{"date":"2026-03-02","time":"21:00","content":"⏰ <b>3rd deposit bonus — 48 hours left</b>\n\n130% + 150 Free Spins. Expires Monday midnight. 🔥\n\nYou're already playing. Why not play bigger? 💰\n\nDeposit ₦5,000 → play with ₦11,500 + 150 spins\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>Claim before it ends:</b> https://1wfafs.life/casino/list?open=register&p=z4m5","images":["022.png"]},

{"date":"2026-03-03","time":"14:00","content":"🎰 <b>Demi Gods VI — mythology meets massive payouts</b>\n\nHigh volatility. Big multipliers. One spin changes everything. ⚡\n\nSomeone won ₦340,000 on this yesterday. ✅\n\nDeposit ₦2,000 → play with ₦12,000\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>Your turn:</b> https://1wfafs.life/casino/list?open=register&p=z4m5","images":["031.png"]},
{"date":"2026-03-03","time":"21:00","content":"🏆 <b>4th deposit = 150% + 180 Free Spins — biggest bonus</b>\n\nFinal bonus in the series. Don't miss it. 🔥\n\nOnly 300 players claimed this last week.\nBe one of them.\n\nDeposit ₦5,000 → play with ₦12,500 + 180 spins\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>Unlock now:</b> https://1wfafs.life/casino/list?open=register&p=z4m5","images":["032.png"]},

{"date":"2026-03-04","time":"14:00","content":"💰 <b>Start with ₦1,000 — walk away with more</b>\n\nMinimum deposit. Maximum opportunity. 💚\n\n₦1,000 → ₦2,000 instantly + 70 spins\nSmall risk. Big upside.\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>Start today:</b> https://1wfafs.life/casino/list?open=register&p=z4m5","images":["041.png"]},
{"date":"2026-03-04","time":"21:00","content":"⏰ <b>Welcome bonus expires this Friday</b>\n\n100% + 70 spins first deposit. Last 2 days. 🔥\n\nThose inside are already playing bigger.\nDon't wait until it's gone.\n\nDeposit ₦2,000 → play with ₦4,000 + 70 spins\n\n🔑 Code: <code>fortunobet</code>\n👉 <b>Claim now:</b> https://1wfafs.life/casino/list?open=register&p=z4m5","images":["042.png"]},

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