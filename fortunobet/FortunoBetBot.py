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

{"date":"2026-02-16","time":"14:00","content":"💰 <b>You deposited once — now get 75% extra on your 2nd!</b>\n\nMost people sleep on this bonus. Don't be one of them.\n\nDeposit ₦5,000 → play with ₦8,750\nDeposit ₦20,000 → play with ₦35,000\n\n⚡ Min deposit: ₦1,000 only\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Claim it now:</b> https://1wyuds.com/casino/list?open=register&p=cguo","images":["161.png"]},
{"date":"2026-02-16","time":"23:00","content":"🏆 <b>Back Barcelona tonight — and enter to win $4,700 cash + iPhone 16 Pro</b>\n\nOne bet = one draw ticket. That simple.\nTickets start from just $1.18 — anyone can enter.\n\nYou're already watching the match. Might as well get paid for it. 👀\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Get your ticket:</b> https://1wyuds.com/casino/list?open=register&p=cguo","images":["162.png"]},

{"date":"2026-02-17","time":"14:00","content":"⚽ <b>Girona vs Barcelona — and the odds are JUICY</b>\n\nBarca wants top spot. Girona wants blood at home. 😤\nThis is not a walk in the park.\n\n📊 Today's odds:\n🏠 Girona win → 6.00\n🤝 Draw → 5.50\n🚀 Barcelona win → 1.40\n\nWhatever side you back — do it with MORE money:\n\nDeposit ₦10,000 → play with ₦60,000\nDeposit ₦50,000 → play with ₦300,000\n\n⚡ Instant cashout to Opay, Palmpay & Kuda. Zero wahala.\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Bet now:</b> https://1wkrii.life/v3/landing-page/football?p=5pe0","images":["171.png"]},

{"date":"2026-02-18","time":"14:00","content":"🎰 <b>Sweet Bonanza Xmas is eating people alive right now</b>\n\nHigh volatility. Tumble wins. One spin can change your whole day.\n\nThis slot doesn't play — it PAYS. 💥\n\nDeposit ₦2,000 → play with ₦12,000\nMore spins. More chances. More wins.\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Spin now:</b> https://1wkrii.life/casino/list?open=register&p=cguo","images":["181.png"]},
{"date":"2026-02-18","time":"23:00","content":"🇳🇬 <b>Nigerians — this platform was built for you</b>\n\nDeposit with what you use every day:\nOpay ✅  Palmpay ✅  Bank Transfer ✅  USDT ✅\n\nDeposit in under 2 minutes.\nWithdraw same day — no stories, no delays.\n\nDeposit ₦2,000 → play with ₦12,000\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Start today:</b> https://1wkrii.life/casino/list?open=register&p=cguo","images":["182.png"]},

{"date":"2026-02-19","time":"14:00","content":"🎁 <b>Register today and collect TWO bonuses at once</b>\n\nHere is exactly what you get:\n\n💥 1WIN gives you: 500% on your deposit\n💥 FortunoBet adds: $3 cash directly to your account\n\nDeposit just $5 — both bonuses hit instantly.\n₦2,000 becomes ₦12,000 before you place your first bet.\n\nDouble bonus. One account. Zero stress.\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Register here:</b> https://1wyuds.com/casino/list?open=register&p=cguo","images":["191.png"]},
{"date":"2026-02-19","time":"23:00","content":"🎯 <b>50 free bets. Every day. No extra deposit.</b>\n\nLogin → tap claim → bet for free.\nThat's it. Daily. Consistent. Real money.\n\nYou're leaving free money on the table every day you're not here.\n\nDeposit ₦2,000 → play with ₦12,000 to start.\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Claim your free bets:</b> https://1wyuds.com/casino/list?open=register&p=cguo","images":["192.png"]},

{"date":"2026-02-20","time":"15:00","content":"🇳🇬 <b>₦256,000,000 prize pool — this week only</b>\n\nThe biggest draw running in Nigeria right now.\nEvery deposit = one automatic entry. No separate registration needed.\n\nOne deposit could change everything. 🔥\n\nDeposit ₦2,000 → play with ₦12,000\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Enter now:</b> https://1wyuds.com/casino/list?open=register&p=cguo","images":["201.png"]},
{"date":"2026-02-20","time":"23:00","content":"💰 <b>First time on 1WIN? Your money is about to multiply.</b>\n\nThe welcome bonus hits the second you deposit:\n\nPut in ₦2,000 → play with ₦12,000\nPut in ₦10,000 → play with ₦60,000\n\nNo tricks. No long waits. Instant 500% match — straight to your account.\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Register & collect:</b> https://1wkrii.life/casino/list?open=register&p=cguo","images":["202.png"]},

{"date":"2026-02-21","time":"13:00","content":"💸 <b>Lost on a bet today? 1WIN sends 30% of it back.</b>\n\nYes — you read that right.\n\nEvery losing bet is protected. Up to 30% cashback lands in your account automatically.\n\nWin → you collect.\nLose → 1WIN cushions the fall.\n\nDeposit ₦2,000 → play with ₦12,000.\nEven losing hits different here. 😏\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Register now:</b> https://1wyuds.com/casino/list?open=register&p=cguo","images":["211.png"]},
{"date":"2026-02-21","time":"22:00","content":"🎁 <b>1WIN keeps rewarding you — not just the first time</b>\n\nMost platforms ghost you after the welcome bonus. Not here.\n\n1st deposit → 100% bonus + 70 Free Spins\n2nd deposit → 120% bonus + 100 Free Spins\n3rd deposit → 130% bonus + 150 Free Spins\n4th deposit → 150% bonus + 180 Free Spins\n\nEvery reload hits harder than the last. 💪\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Start earning:</b> https://1wyuds.com/casino/list?open=register&p=cguo","images":["212.png"]},

{"date":"2026-02-22","time":"14:00","content":"🎰 <b>500 free spins — included with your first 4 deposits</b>\n\nThis is not a gimmick. It is built into the bonus structure:\n\n1st deposit → 70 spins\n2nd deposit → 100 spins\n3rd deposit → 150 spins\n4th deposit → 180 spins\n\nThat is 500 chances to win — just for depositing what you were going to deposit anyway.\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Claim your spins:</b> https://1wyuds.com/casino/list?open=register&p=cguo","images":["221.png"]},
{"date":"2026-02-22","time":"22:00","content":"💰 <b>₦1,000 is enough to start — and it doubles immediately</b>\n\nMinimum deposit: ₦1,000 only.\nBonus added instantly: 100%.\nFree spins on top: 70.\n\nYou put in ₦1,000 — you play with ₦2,000 + 70 spins.\nThat is a full session for the price of lunch. 🍗\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Start with ₦1,000:</b> https://1wyuds.com/casino/list?open=register&p=cguo","images":["222.png"]},

{"date":"2026-02-23","time":"14:00","content":"🇳🇬🇰🇪 <b>Nigeria & Kenya — low entry, big upside</b>\n\nYou do not need big money to start winning big.\n\nDeposit ₦1,000 → play with ₦2,000\nDeposit ₦5,000 → play with ₦10,000\n\nBonus added the second you deposit — no manual claim needed.\nWithdraw whenever you want. No excuses. No wahala.\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Register & start:</b> https://1wyuds.com/casino/list?open=register&p=cguo","images":["231.png"]},
{"date":"2026-02-23","time":"23:00","content":"⏰ <b>This welcome bonus is not permanent — just so you know</b>\n\nNew players only. And it will not be here forever.\n\nFirst deposit: 100% bonus + 70 Free Spins\nKeep going: up to 500% across 4 deposits\n\nThe people who registered last week are already playing with 5x their money.\nThe people waiting are still waiting. ⌛\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Register before it closes:</b> https://1wyuds.com/casino/list?open=register&p=cguo","images":["232.png"]},

{"date":"2026-02-24","time":"14:00","content":"🏆 <b>Why thousands of Nigerians and Kenyans choose 1WIN every single day</b>\n\nNot just words — real reasons:\n\n✅ 500% welcome bonus on first deposit\n✅ 30% cashback on every losing day\n✅ 50 free bets available daily — no deposit needed\n✅ Same-day withdrawal to Opay, Palmpay, M-Pesa and more\n\nIf your current platform is not giving you all four — you are in the wrong place. 👀\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Switch today:</b> https://1wyuds.com/casino/list?open=register&p=cguo","images":["241.png"]},
{"date":"2026-02-24","time":"23:00","content":"🌙 <b>The night matches are live — are you in?</b>\n\nRight now on 1WIN — live games, live odds, live money.\n\nNew player? Your first deposit gets 500% instantly.\nPut in ₦2,000 → you play with ₦12,000. Tonight.\n\nNot tomorrow. Not next week. RIGHT NOW. ⏱\n\n🔑 Code: <code>fortunobet</code>\n\n👉 <b>Jump in:</b> https://1wkrii.life/v3/landing-page/football?p=5pe0","images":["172.png"]},

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