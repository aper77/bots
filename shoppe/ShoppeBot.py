from telegram import Bot, InputMediaPhoto
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime, timedelta
import pytz
import os

# ====== CONFIG ======
BOT_TOKEN = "8492868444:AAEdwQLkyk8tI23n6faJ6sYMnLxh5XN0Ew4"
CHANNEL_ID = "@shoppeboom"  # Your channel username
TIMEZONE = pytz.timezone('Asia/Yerevan')  # Armenia timezone

bot = Bot(token=BOT_TOKEN)
scheduler = BlockingScheduler()

# ====== TEXT & IMAGE POSTS SCHEDULE ======
posts = [
      # --- DAY 1: 29 NOV 2025 ---
    {"date": "2025-11-29", "time": "11:00", "content": "✨ Burberry BU10001 Men’s Watch – The Classic Horseferry Gold\n💵 Now only $239.99 (was $670)\n⚡ Limited stock: only 64 pieces available!\n\nLuxurious gold finish with iconic Burberry elegance – perfect for any occasion.\n\n👉 Buy now: https://shoppeboom.coxm/product/brand/burberry", "images": ["b12.webp","b11.webp","b13.webp","b14.webp"]},
    {"date": "2025-11-29", "time": "17:00", "content": "✨ Burberry BU10010 Men’s Watch – Check Stamped Round Dial 40mm\n💵 Only $289.99 (was $520!)\n⚡ Limited stock: only 44 pieces available!\n\nClassic Burberry check design with premium craftsmanship – a statement of style and luxury.\n\n👉 Buy now: https://shoppeboom.com/product/brand/burberry", "images": ["b21.webp","b22.webp","b23.webp"]},
    {"date": "2025-11-30", "time": "00:00",  "content": "✨ Burberry BU9014 Women’s Watch – Tan Dial Leather Strap\n💵 Only $259.99 (was $700!)\n⚡ Limited stock: only 63 pieces available!\n\nLuxury leather strap and iconic Burberry design – perfect for daily elegance or special occasions.\n\n👉 Buy now: https://shoppeboom.com/product/brand/burberry", "images": ["b41.webp","b42.webp","b43.webp"]},

    # --- DAY 2: 30 NOV 2025 ---
    {"date": "2025-11-30", "time": "11:00", "content": "👠 CHIKO Cherris Pointy Toe Wedge Pumps\n💵 Only $129\n⚡ Stylish, comfortable, and perfect for day or night!\n\nStep up your fashion game with these elegant wedges.\n\n👉 Buy now: https://shoppeboom.com/product/brand/chiko", "images": ["ch11.jpg","ch12.jpg","ch13.jpg"]},
    {"date": "2025-11-30", "time": "17:00", "content": "👢 CHIKO Chione Round Toe Block Heels Ankle Boots\n💵 Only $163\n⚡ Stylish, versatile, and perfect for any outfit!\n\nStep out in confidence and comfort with these chic ankle boots.\n\n👉 Buy now: https://shoppeboom.com/product/brand/chiko", "images": ["ch21.jpg","ch22.jpg","ch23.jpg"]},
    {"date": "2025-11-01", "time": "21:00", "content": "👠 CHIKO Chimamanda Square Toe Wedge Mary Jane Shoes\n💵 Only $129\n⚡ Elegant, stylish, and comfortable – perfect for every occasion!\n\nStep up your fashion game with these chic Mary Jane wedges.\n\n👉 Buy now: https://shoppeboom.com/product/brand/chiko", "images": ["ch31.jpg","ch32.jpg","ch33.jpg"]},

    # --- DAY 3: 1 DEC 2025 ---
    {"date": "2025-12-01", "time": "11:00", "content": "👠 CHIKO Cheche Pointy Toe Kitten Heels Pumps Shoes\n⚡ Elegant, stylish, and perfect for day or night!\n\nStep out with confidence and chic comfort in these kitten heels.\n\n👉 Buy now: https://shoppeboom.com/product/brand/chiko", "images": ["ch51.jpg","ch52.jpg","ch53.jpg","ch54.jpg"]},
    {"date": "2025-12-01", "time": "17:00","content": "❄️ Winter Deals Are Here at ShoppeBoom! ❄️\n\nGet amazing discounts on your favorite brands — fashion, watches, shoes, tech, and more! 🛍️\n\nDon’t miss out — limited stock, big savings!\n\n👉 Shop now: https://shoppeboom.com\n\nStay stylish this winter with ShoppeBoom! 💖", "images": ["sb3.png"]},
    {"date": "2025-12-02", "time": "00:00", "content": "👠 CHIKO Cherish Round Toe Wedge Mary Jane Shoes\n⚡ Elegant, stylish, and perfect for any occasion!\n\nStep out in confidence and chic comfort with these Mary Jane wedges.\n\n👉 Buy now: https://shoppeboom.com/product/brand/chiko", "images": ["ch71.jpg","ch72.jpg","ch73.jpg"]},

    # --- DAY 4: 2 DEC 2025 ---
    {"date": "2025-12-02", "time": "11:00", "content": "✨ Burberry BU10114 Women’s Watch – Classic Round\n💵 Now only $349.99 (was $450!)\n⚡ Limited stock: only 22 pieces available!\n\nElegant and timeless design with signature Burberry quality – perfect for every occasion.\n\n👉 Buy now: https://shoppeboom.com/product/brand/burberry", "images": ["b31.webp","b32.webp","b33.webp"]},
    {"date": "2025-12-02", "time": "17:00", "content": "✨ GUESS W0989L1 Women’s Watch\n💵 Now only $149.99 (was $280)\n🔥 Premium design, elegant finish, and perfect for any outfit.\n\nOnly a few pieces available — grab yours before it's gone!\n\n👉 Buy now: https://shoppeboom.com/product/brand/guess", "images": ["guess21.webp","guess22.webp"]},
    {"date": "2025-12-03", "time": "00:00", "content": "👞 CHIKO Chickoa Square Toe Flatforms Oxfords Shoes\n⚡ Stylish, bold, and comfortable – perfect for any outfit!\n\nStep up your style with these trendy flatform oxfords.\n\n👉 Buy now: https://shoppeboom.com/product/brand/chiko", "images": ["ch41.jpg","ch42.jpg","ch43.jpg"]},

    # --- DAY 5: 3 DEC 2025 ---
    {"date": "2025-12-03", "time": "11:00", "content": "🌟 Discover the World of Top Brands at ShoppeBoom! 🌟\n\nFrom luxury to everyday style, we have something for everyone:\n👟 Nike, Adidas, Puma\n👜 Gucci, Jimmy Choo, Michael Kors, CHIKO\n⌚ Burberry, Fossil, Casio, Swatch\n📱 Apple, Samsung\n🕶️ Ray-Ban, Persol\n💎 Swarovski, Style# Brooklyn\n…and many more! 😍\n\nShop the latest trends, enjoy unbeatable prices, and get your favorites delivered straight to your door.\n\n👉 Explore now: https://shoppeboom.com\n\nShoppeBoom — Your destination for ORIGINAL brands, all in one place! 💖", "images": ["sb1.png"]},
    {"date": "2025-12-03", "time": "17:00",  "content": "🔥 GUESS W0864G6 Men’s Watch\n💵 Only $209.99\n⚠️ Only 1 piece available — don’t miss out!\n\nElegant blue dial, premium stainless steel, and signature GUESS luxury design.\n\n👉 Buy now: https://shoppeboom.com/product/brand/guess", "images": ["guess1.webp","guess2.webp","guess3.webp"]},
    {"date": "2025-12-04", "time": "00:00",  "content": "👠 CHIKO Cherida Pointy Toe Wedge Pumps Shoes\n⚡ Stylish, comfortable, and perfect for any occasion!\n\nStep up your fashion game with these elegant wedges.\n\n👉 Buy now: https://shoppeboom.com/product/brand/chiko", "images": ["ch61.jpg","ch62.jpg","ch63.jpg","ch64.jpg"]},

    # --- DAY 6: 04 DEC 2025 ---
    {"date": "2025-12-04", "time": "11:00", "content": "✨ Michael Kors MK6485 Ritz Chronograph Ladies Watch\n💵 Now only $179.99 (was $350!)\n⚡ Limited stock: only 49 pieces available!\n\nElegant, stylish, and perfect for every occasion — make a statement with Michael Kors.\n\n👉 Buy now: https://shoppeboom.com/product/brand/michael-kors", "images": ["mk12.webp","mk11.webp","mk13.webp"]},
    {"date": "2025-12-04", "time": "17:00", "content": "✨ Michael Kors MK6314 Women’s Watch\n⚡ Elegant, stylish, and perfect for any occasion!\n\nStep out in confidence with this iconic Michael Kors design.\n\n👉 Buy now: https://shoppeboom.com/product/brand/michael-kors", "images": ["mk22.webp","mk21.webp"]},
    {"date": "2025-12-05", "time": "00:00", "content": "🎁 Follow ShoppeBoom and be the first to see new fashion arrivals! 😍\n\nExclusive bonuses, gifts, and special discounts are waiting for our followers. 🛍️✨\n\nDon’t miss out — join us now!\n\n👉 Follow & shop: https://shoppeboom.com\n\nShoppeBoom — Your VIP access to the best brands and deals! 💖", "images": ["sb4.png"]},

      # --- DAY 7: 5 DEC 2025 ---
    {"date": "2025-12-05", "time": "11:00","content": "🛍️ ShoppeBoom has it all! Hundreds of top-quality products at unbeatable prices. 😍\n\nFrom fashion to tech, we bring you the best brands and deals in one place.\n\n👉 Check it out now: https://shoppeboom.com\n\nShop smart, shop original — only at ShoppeBoom! 💖", "images": ["sb2.png"]},
    {"date": "2025-12-05", "time": "21:00", "content": "✨ GUESS W0954L3 Women’s Watch\n💵 Only $189.99\n🌟 Stunning rose-gold tone with a luxurious crystal finish.\n\nPerfect for everyday elegance or a special gift.\n\n👉 Buy now: https://shoppeboom.com/product/brand/guess", "images": ["guess31.webp","guess32.webp","guess33.webp"]},
    {"date": "2025-12-06", "time": "00:00", "content": "🔥 GUESS W1044G1 Men’s Watch\n💵 Now only $149.99 (was $280)\n⚡ Limited stock: only 46 pieces available!\n\nBold design, premium stainless steel, and signature GUESS style.\n\n👉 Buy now: https://shoppeboom.com/product/brand/guess", "images": ["guess41.webp","guess42.webp","guess43.webp"]},

]

# ====== FUNCTION TO SEND POSTS ======
def send_post(post):
    try:
        if "images" in post and post["images"]:
            # If multiple images, send as album
            if len(post["images"]) > 1:
                media_group = []
                for idx, img_file in enumerate(post["images"]):
                    if os.path.exists(img_file):
                        if idx == 0:
                            media_group.append(InputMediaPhoto(open(img_file, "rb"), caption=post["content"]))
                        else:
                            media_group.append(InputMediaPhoto(open(img_file, "rb")))
                if media_group:
                    bot.send_media_group(chat_id=CHANNEL_ID, media=media_group)
            else:
                # Single image
                img_file = post["images"][0]
                if os.path.exists(img_file):
                    with open(img_file, "rb") as photo:
                        bot.send_photo(chat_id=CHANNEL_ID, photo=photo, caption=post["content"])
                else:
                    bot.send_message(chat_id=CHANNEL_ID, text=post["content"])
        else:
            # Text only
            bot.send_message(chat_id=CHANNEL_ID, text=post["content"])

        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Posted: {post['content']}")
    except Exception as e:
        print(f"Failed to post {post['content']}: {e}")

# ====== IMMEDIATE POSTS IF BOT STARTS LATE ======
now = datetime.now(TIMEZONE)
for post in posts:
    hour, minute = map(int, post["time"].split(":"))
    post_time = TIMEZONE.localize(datetime(now.year, now.month, now.day, hour, minute))
    if now >= post_time and now <= post_time + timedelta(minutes=5):
        send_post(post)  # post immediately if missed within last 5 minutes

# ====== SCHEDULE JOBS ======
for post in posts:
    hour, minute = map(int, post["time"].split(":"))
    scheduler.add_job(send_post, 'cron', hour=hour, minute=minute, args=[post], timezone=TIMEZONE,
                      misfire_grace_time=300)  # 5 minutes grace time

# ====== START BOT ======
print("Bot is running and will post messages automatically...")
scheduler.start()