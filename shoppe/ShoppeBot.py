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
    {"date": "2025-12-05", "time": "21:00", "content": "✨ GUESS W0954L3 Women’s Watch\n💵 Only $189.99\n🌟 Stunning rose-gold tone with a luxurious crystal finish.\n\nPerfect for everyday elegance or a special gift.\n\n👉 Buy now: https://shoppeboom.com/product/brand/guess", "images": ["guess31.webp","guess32.webp","guess33.webp"]},
    {"date": "2025-12-06", "time": "00:00", "content": "🔥 GUESS W1044G1 Men’s Watch\n💵 Now only $149.99 (was $280)\n⚡ Limited stock: only 46 pieces available!\n\nBold design, premium stainless steel, and signature GUESS style.\n\n👉 Buy now: https://shoppeboom.com/product/brand/guess", "images": ["guess41.webp","guess42.webp","guess43.webp"]},

    {"date": "2025-12-06", "time": "11:00", "content": "🔥 NEW ARRIVAL ALERT! PROFESSIONAL STYLE, UNBEATABLE PRICE! 🔥\nLooking for that power suit that commands attention?\nWe've just dropped the stunning Alberto Nardoni Men's Blue Pinstripe Suit!\n\nThe Fit: Hybrid Fit – perfect mix of modern tailoring and classic comfort.\nThe Look: Elegant Navy Blue with a subtle, business-ready micro mini pinstripe. It's a full vested (3-piece) suit for a truly polished look!\nThe Price is RIGHT: Get this original brand suit for an incredible sale price: **$226.63 USD** (Approx.)\nTap below to grab yours before they sell out!\nhttps://shoppeboom.com/product/brand/alberto-nardoniase", "images": ["06a1.webp"]},
    {"date": "2025-12-06", "time": "17:00", "content": "✨ DESIGNER STYLE DROP! This Suit Changes Everything. ✨\n\nStop wearing plain suits! Grab this stunning, original **Men's Gray Plaid Suit** featuring a modern blue windowpane check. It’s the sharp, slim-fit look you need at an unbelievable price.\n\n* **Pattern:** Designer Grey & Blue Windowpane Plaid Check\n* **Fit:** Sharp Slim Fit with Peak Lapel\n* **Fabric:** Premium Wool Blend\n* **💰 SALE PRICE:** Only **$225.04 USD** (A fraction of designer retail!)\n\n**Click to step up your suit game before it sells out:**\nhttps://shoppeboom.com/product/brand/alberto-nardoniase", "images": ["06b2.webp"]},
    {"date": "2025-12-06", "time": "23:59", "content": "🚨 MEGA DEAL ALERT: 53% OFF Emporio Armani! 🚨\n\nCommand attention with the **Emporio Armani AR11348 Chronograph**. This is premium stainless steel craftsmanship and signature Armani style at an unmissable price.\n\n* **Brand:** 100% Original Emporio Armani\n* **Style:** Chronograph Men's Watch\n* **Original Price:** ~~$550.00~~\n* **💰 SALE PRICE:** Just **$259.99 USD** (Save $290—that's **53%** off!)\n\n**Click here to secure this luxury timepiece now:**\nhttps://shoppeboom.com/product/brand/emporio-armani", "images": ["07a1.webp", "07a2.webp"]},
    
    {"date": "2025-12-07", "time": "11:00", "content": "🔱 NEW DROP: The Diver Chronograph from Emporio Armani! 🔱\n\nGet the rugged, stylish look of a professional dive watch mixed with signature Armani luxury. This AR11361 chronograph is built for performance and priced for value.\n\n* **Style:** Diver Chronograph (High-Functionality)\n* **Brand:** 100% Original Emporio Armani\n* **Feature:** Bold, highly readable dial for active use\n* **💰 SALE PRICE:** Just **$289.99 USD** (Luxury Diver at an incredible price!)\n\n**Ready to upgrade your wrist? Shop the AR11361 Diver here:**\nhttps://shoppeboom.com/product/brand/emporio-armani", "images": ["07b1.webp", "07b2.webp", "07b3.webp"]},
    {"date": "2025-12-07", "time": "17:00", "content": "⚫️ ALL BLACK POWER! Emporio Armani Chronograph Drop. ⚫️\n\nMake a bold, sophisticated statement with the **AR11363 All Black Chronograph**. This stealth design is 100% original Armani luxury, now available at a sharp discount.\n\n* **Style:** All Black Chronograph (Sleek & Stealth)\n* **Original Price:** ~~$350.00~~\n* **💰 SALE PRICE:** Just **$259.99 USD** (Save 26% instantly!)\n\n**Tap to own the all-black look:**\nhttps://shoppeboom.com/product/brand/emporio-armani", "images": ["07c1.webp", "07c2.webp", "07c3.webp"]},
    {"date": "2025-12-07", "time": "21:00", "content": "💖 ELEGANCE ARRIVED: Emporio Armani Ladies Watch. 💖\n\nTreat yourself or someone special to the timeless style of the **AR11462 Ladies Watch**. Featuring a breathtaking White Mother of Pearl dial, this watch defines feminine luxury.\n\n* **Feature:** Exquisite White Mother of Pearl Dial\n* **Style:** Refined and classic ladies' timepiece\n* **Brand:** 100% Original Emporio Armani\n* **💰 SALE PRICE:** Just **$219.99 USD** (Luxury redefined and affordable!)\n\n**Tap below to add this Armani elegance to your collection:**\nhttps://shoppeboom.com/product/brand/emporio-armani", "images": ["07d1.webp", "07d2.webp", "07d3.webp"]},

    {"date": "2025-12-08", "time": "11:00", "content": "🔥 GUCCI DEAL! Save 34% on the G-Timeless Watch! 🔥\n\nOwn a piece of iconic luxury with the **Gucci YA1264084 G-Timeless Unisex Watch**. This unique, versatile timepiece is a stunning investment for any wardrobe.\n\n* **Brand:** 100% Original GUCCI\n* **Style:** G-Timeless Unisex Design\n* **Original Price:** ~~$1,010.00~~\n* **💰 SALE PRICE:** Just **$669.99 USD** (You save over **$340**!)\n\n**Secure your luxury Gucci watch now before this deal ends:**\nhttps://shoppeboom.com/product/brand/gucci", "images": ["08a1.webp", "08a2.webp", "08a3.webp"]},
    {"date": "2025-12-08", "time": "17:00", "content": "🔥 BLACK FRIDAY VIBES: 34% OFF Gucci G-Timeless! 🔥\n\nElevate your look instantly with the sleek **Gucci YA1264017 G-Timeless Men's Watch**. The iconic black dial with signature Gucci motifs makes this a timeless statement piece.\n\n* **Brand:** 100% Original GUCCI\n* **Style:** G-Timeless Black Dial\n* **Original Price:** ~~$960.00~~\n* **💰 SALE PRICE:** Just **$629.99 USD** (Save over **$330**!)\n\n**Click to claim this luxury timepiece at a massive discount:**\nhttps://shoppeboom.com/product/brand/gucci", "images": ["08c1.webp", "08c2.webp", "08c3.webp"]}, 
    {"date": "2025-12-08", "time": "23:59", "content": "✨ LUXURY CHRONOGRAPH DROP! Save 43% on Gucci! ✨\n\nExperience the pinnacle of precision and style with the **Gucci YA126268 G-Timeless Chronograph**. This is an original, high-end timepiece—nearly half off the retail price.\n\n* **Brand:** 100% Original GUCCI\n* **Style:** High-Performance Chronograph\n* **Original Price:** ~~$1,750.00~~\n* **💰 SALE PRICE:** Just **$989.99 USD** (Massive **43%** Savings!)\n\n**This flagship watch won't last—shop the deal now:**\nhttps://shoppeboom.com/product/brand/gucci", "images": ["08b1.webp", "08b2.webp", "08b3.webp"]},

    {"date": "2025-12-09", "time": "11:00", "content": "🚨 UNBOX THE UNUSUAL: 34% Off Gucci's UFO Red Dial! 🚨\n\nDare to stand out with the unique **Gucci YA1264023 G-Timeless Watch**. Featuring the iconic red dial and embroidered UFO motif, this watch is pure statement luxury at an unbeatable price.\n\n* **Brand:** 100% Original GUCCI\n* **Style:** Bold G-Timeless UFO Red Dial\n* **Original Price:** ~~$1,010.00~~\n* **💰 SALE PRICE:** Just **$669.99 USD** (Save over **$340**!)\n\n**Tap below to grab this collector's piece before it vanishes:**\nhttps://shoppeboom.com/product/brand/gucci", "images": ["09a1.webp", "09a2.webp", "09a3.webp"]},
    {"date": "2025-12-09", "time": "17:00", "content": "HALF PRICE GUCCI! 😱 Save 50% on G-Timeless Watch! 😱\n\nThis is a rare opportunity to own the luxury and style of the **Gucci YA1264079 G-Timeless Watch** for half the retail price. Classic design, massive savings.\n\n* **Brand:** 100% Original GUCCI\n* **Style:** Signature G-Timeless Design\n* **Original Price:** ~~$1,330.00~~\n* **💰 SALE PRICE:** Just **$659.99 USD** (That’s a full **50% OFF**!)\n\n**This deal is a limited time offer—shop the Gucci 50% off sale now:**\nhttps://shoppeboom.com/product/brand/gucci", "images": ["09b1.webp", "09b2.webp"]},
    
    {"date": "2025-12-10", "time": "01:00", "content": "✨ SPARKLING DEAL: 39% Off Guess Limelight Crystals! ✨\n\nAdd a touch of vibrant luxury to your look with the **Guess W0775L5 Pink Ladies Watch**. Featuring dazzling crystals and a feminine pink finish, it's the perfect accessory.\n\n* **Brand:** 100% Original Guess\n* **Feature:** Limelight Crystals and Pink Finish\n* **Original Price:** ~~$310.00~~\n* **💰 SALE PRICE:** Just **$189.99 USD** (Save 39% instantly!)\n\n**Click to claim this eye-catching timepiece:**\nhttps://shoppeboom.com/product/brand/guess", "images": ["10a1.webp", "10a2.webp"]},
    {"date": "2025-12-10", "time": "17:00", "content": "🚨 TREND ALERT: 30% OFF the Must-Have Guess Silicone Watch! 🚨\n\nPerfect for everyday wear, the **Guess W1025L4 Analogue Silicone Watch** combines effortless style with ultimate comfort. Get an original Guess piece at a great price.\n\n* **Feature:** Comfortable & Stylish Silicone Strap\n* **Style:** Modern Analogue Women's Watch\n* **Original Price:** ~~$200.00~~\n* **💰 SALE PRICE:** Just **$139.99 USD** (Save 30% instantly!)\n\n**Tap below to grab this comfortable, chic accessory:**\nhttps://shoppeboom.com/product/brand/guess", "images": ["10b1.webp", "10b2.webp"]},

    {"date": "2025-12-11", "time": "11:00", "content": "🚨 STEAL DEAL: 38% OFF Guess Women's Analogue Watch! 🚨\n\nUpgrade your accessory game with the stylish **Guess W0571L1 Quartz Watch**. This watch offers signature Guess design and quality at an unbeatable price.\n\n* **Brand:** 100% Original Guess\n* **Style:** Elegant Analogue Quartz Design\n* **Original Price:** ~~$210.00~~\n* **💰 SALE PRICE:** Just **$129.99 USD** (Save 38% instantly!)\n\n**Tap below to grab this stunning watch before it sells out:**\nhttps://shoppeboom.com/product/brand/guess", "images": ["11a1.webp", "11a2.webp"]}, 
    {"date": "2025-12-11", "time": "23:59", "content": "👔 HUGE SAVINGS! Get 37% OFF the Hugo Boss Energy Chrono! 👔\n\nCommand respect with the **Hugo Boss 1513970 Energy Chronograph**. This is original, sophisticated BOSS style at a massive discount—perfect for the modern professional.\n\n* **Brand:** 100% Original Hugo Boss\n* **Style:** High-Performance Chronograph\n* **Benefit:** **37% Discount** off the Regular Price!\n* **Value:** Premium design without the premium cost.\n\n**Tap below to grab this powerful timepiece now:**\nhttps://shoppeboom.com/product/brand/hugo-boss", "images": ["11b1.webp", "11b2.webp"]},

    {"date": "2025-12-12", "time": "11:00", "content": "👔 LIMITED DEAL: Save 27% on the Hugo Boss Associate Watch! 👔\n\nElevate your professional image with the sleek **Hugo Boss 1513975 Associate Watch**. Get sophisticated, 100% original BOSS style with an impressive **27% Discount** off the retail price.\n\n* **Brand:** 100% Original Hugo Boss\n* **Style:** Associate Series (Perfect for Business)\n* **Benefit:** **27% Discount** - Unbeatable Value!\n* **Value:** Make a powerful statement for less.\n\n**Tap below to secure this essential BOSS timepiece:**\nhttps://shoppeboom.com/product/brand/hugo-boss", "images": ["12a1.webp", "12a2.webp","12a3.webp"]},
    {"date": "2025-12-12", "time": "17:00", "content": "🚨 POWER DEAL: Huge 37% OFF the Hugo Boss Santiago Chrono! 🚨\n\nUpgrade your wristwear with the high-performance **Hugo Boss 1513936 Santiago Chronograph**. Get sophisticated, 100% original BOSS style with an immediate **37% Discount**!\n\n* **Brand:** 100% Original Hugo Boss\n* **Style:** Santiago Chronograph (Bold Design)\n* **Benefit:** **37% Discount** - Premium quality, exceptional savings.\n\n**Tap below to secure this essential BOSS timepiece:**\nhttps://shoppeboom.com/product/brand/hugo-boss", "images": ["12b1.webp", "12b2.webp","12b3.webp"]},

    {"date": "2025-12-13", "time": "01:00", "content": "⚫️ COMMAND ATTENTION: Hugo Boss Admiral Black Chronograph! ⚫️\n\nOwn the ultimate statement piece. The **Hugo Boss 1513966 Admiral Black Chronograph** delivers powerful, sophisticated design—now available at an exclusive discount.\n\n* **Brand:** 100% Original Hugo Boss\n* **Style:** Admiral Black Chronograph (Maximum Impact)\n* **Benefit:** **Exclusive Discount** Off Retail Price!\n* **Value:** Luxury Black-Out Style for Less.\n\n**Tap below to claim your original BOSS timepiece:**\nhttps://shoppeboom.com/product/brand/hugo-boss", "images": ["13a1.webp", "13a2.webp","13a3.webp"]},
    {"date": "2025-12-13", "time": "17:00", "content": "🇺🇸 CLASSIC AMERICAN STYLE: New Tommy Hilfiger Watch Drop! 🇺🇸\n\nInstantly upgrade your casual and professional look with the **Tommy Hilfiger 1791948 Multi Dial Watch**. Get that signature preppy style and quality craftsmanship today.\n\n* **Brand:** 100% Original Tommy Hilfiger\n* **Style:** Multi-Dial Quartz Men's Watch\n* **Feature:** Signature sporty yet refined look\n* **💰 SALE PRICE:** **[Insert Sale Price Here] USD** (Unbeatable Value!)\n\n**Tap below to grab this essential accessory:**\nhttps://shoppeboom.com/product/brand/tommy-hilfiger", "images": ["13b1.webp", "13b2.webp"]},

    {"date": "2025-12-14", "time": "21:00", "content": "✨ FRESH ARRIVAL: Tommy Hilfiger 1791790 Men's Watch! ✨\n\nElevate your casual sophistication with this essential timepiece from Tommy Hilfiger. Get that iconic American cool look with 100% original quality.\n\n* **Brand:** 100% Original Tommy Hilfiger\n* **Style:** Signature Men's Analogue Watch\n* **Feature:** Designed for effortless everyday style\n* **💰 SALE PRICE/DISCOUNT:** **[Insert Sale Price or Discount Here]** (Value you can't ignore!)\n\n**Tap below to grab your new Tommy Hilfiger watch:**\nhttps://shoppeboom.com/product/brand/tommy-hilfiger", "images": ["14a1.webp", "14a2.webp"]},
    {"date": "2025-12-14", "time": "00:00", "content": "🚨 HALF PRICE LUXURY! Save 48% on Tommy Hilfiger Gold Mesh! 🚨\n\nElevate your everyday style with the stunning **Tommy Hilfiger 1782302 Ladies Blake Watch**. Enjoy the elegant gold mesh design and a massive **48% Discount** off the retail price!\n\n* **Brand:** 100% Original Tommy Hilfiger\n* **Style:** Elegant Gold Mesh Strap\n* **Benefit:** HUGE **48% Discount** - Nearly half off!\n* **Feature:** Timeless and sophisticated look.\n\n**Tap below to claim this highly discounted luxury piece:**\nhttps://shoppeboom.com/product/brand/tommy-hilfiger", "images": ["14b1.webp", "14b2.webp", "14b3.webp"]},
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