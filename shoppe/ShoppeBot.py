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
    {"date":"2025-12-22","time":"17:00","content":"✨ Marc Jacobs Baker Gold Green Watch ✨ Elegant, stylish, and perfect for any outfit. ⌚💎 👉 Shop Now: https://watchesofusa.com/products/marc-jacobs-mbm3245-baker-gold-green-dial-ladies-watch?variant=42924362498102&utm_source=AWIN&utm_medium=AWIN&source=aw&utm_id=2091833_&utm_campaign=affiliate&aw_affid=2091833&awc=116479_1765456231_ba5a14d69dc7b3b4c301a6def7b241d0 Explore more: https://shoppeboom.com/product/brand/marc-jacobs","images":["22b1.webp","22b2.webp"]},

    {"date":"2025-12-23","time":"02:00","content":"✨ Hugo Boss Center Court Lux Men's Watch ✨ Sophisticated, bold, and perfect for any outfit. ⌚💎 👉 Shop Now: https://watchesofusa.com/products/hugo-boss-1514027-center-court-lux-mens-watch?variant=42924361187382&utm_source=AWIN&utm_medium=AWIN&source=aw&utm_id=2091833_&utm_campaign=affiliate&aw_affid=2091833&awc=116479_1765456384_b6f732a7900b38825425cbe6aa9dda66 Explore more: https://shoppeboom.com/product/brand/hugo-boss","images":["23a1.webp","23a2.webp","23a3.webp"]},
    {"date":"2025-12-23","time":"17:00","content":"✨ Hugo Boss Taper Chronograph Men's Watch ✨ Sleek, powerful, and perfect for any outfit. ⌚💎 👉 Shop Now: https://watchesofusa.com/products/hugo-boss-1514087-taper-chronograph-men-s-watch?variant=42924361515062&utm_source=AWIN&utm_medium=AWIN&source=aw&utm_id=2091833_&utm_campaign=affiliate&aw_affid=2091833&awc=116479_1765456466_7aa0ce5710e479828d0aab2c2e1f32a5 Explore more: https://shoppeboom.com/product/brand/hugo-boss","images":["23b1.webp","23b2.webp"]},

    {"date":"2025-12-24","time":"02:00","content":"✨ Hugo Boss Center Court Bronze Dial Men's Watch ✨ Elegant, refined, and perfect for any outfit. ⌚💎 👉 Shop Now: https://watchesofusa.com/products/hugo-boss-1514024-center-court-bronze-dial-mens-watch?variant=42924361089078&utm_source=AWIN&utm_medium=AWIN&source=aw&utm_id=2091833_&utm_campaign=affiliate&aw_affid=2091833&awc=116479_1765456718_c4ad504eb19a7436f5b6dafbecbe6671 Explore more: https://shoppeboom.com/product/brand/hugo-boss","images":["24a1.webp","24a2.webp","24a3.webp"]},
    {"date":"2025-12-24","time":"11:00","content":"✨ CHIKO Abigail Pointy Toe Wedge Knee High Boots ✨ Chic, bold, and perfect for any outfit. 👢💎 👉 Shop Now: https://www.chikoshoes.com/shop/chiko-abigail-pointy-toe-wedge-knee-high-boots/?aw_affid=2091833&awc=24111_1765456834_9516e63a087f1f6f9e64fd94c79138b3 Explore more: https://shoppeboom.com/product/brand/chiko","images":["24b1.jpg","24b2.jpg","24b3.jpg"]},
    {"date":"2025-12-24","time":"19:00","content":"✨ CHIKO Icess Pointy Toe Kitten Heels Knee High Boots ✨ Elegant, chic, and perfect for any outfit. 👢💎 👉 Shop Now: https://www.chikoshoes.com/shop/chiko-icess-pointy-toe-kitten-heels-knee-high-boots/?aw_affid=2091833&awc=24111_1765457056_c5c77a73d61074860cc2e3744c1172cb Explore more: https://shoppeboom.com/product/brand/chiko","images":["24c1.jpg","24c2.jpg","24c3.jpg"]},

    {"date":"2025-12-25","time":"11:00","content":"👠 CHIKO Christy Leather Loafers — Elegant style + all-day comfort!\n\nDiscover the beautiful CHIKO Christy Square Toe Block Heels Loafers Shoes. Premium leather & a comfy 2cm block heel.\n\nShop now:\n👉 ShoppeBoom: https://shoppeboom.com/main-slug/women\n👉 Partner Link: https://www.chikoshoes.com/shop/chiko-christy-square-toe-block-heels-loafers-shoes/?aw_affid=2091833&awc=24111_1766395762_6d6c3cbf7ff427325dd64d32c9eec3f0","images":["25a2.jpg","25a1.jpg"]},
    {"date":"2025-12-25","time":"23:59","content":"👠 CHIKO Cinnamon T-Strap Heels — Elegant, comfy & premium leather! Featuring a soft leather upper, leather lining, and a comfy 2cm block heel.\n\nShop now:\n👉 ShoppeBoom: https://shoppeboom.com/main-slug/women\n👉 Partner Link: https://www.chikoshoes.com/shop/chiko-cinnamon-square-toe-block-heels-t-strap-shoes/?aw_affid=2091833","images":["25b1.jpg","25b2.jpg"]},

    {"date":"2025-12-26","time":"11:00","content":"👠 CHIKO Ciannait Mary Jane Heels — soft leather & suede with a comfy 1cm block heel! Elegant, lightweight, and perfect for daily wear.\n\nShop now:\n👉 ShoppeBoom: https://shoppeboom.com/main-slug/women\n👉 Partner Link: https://www.chikoshoes.com/shop/chiko-ciannait-round-toe-block-heels-mary-jane-shoes/?aw_affid=2091833","images":["26a1.jpg","26a2.jpg"]},
    {"date":"2025-12-26","time":"17:30","content":"👠 CHIKO Cilicia Loafers — stylish leather & suede with a comfy 1cm block heel! Elegant, soft, and perfect for everyday wear.\n\nShop now:\n👉 ShoppeBoom: https://shoppeboom.com/main-slug/women\n👉 Partner Link: https://www.chikoshoes.com/shop/chiko-cilicia-square-toe-block-heels-loafers-shoes/?aw_affid=2091833","images":["26b1.jpg","26b2.jpg"]},

    {"date":"2025-12-27","time":"11:00","content":"⌚ Burberry Pioneer Ladies Watch — Elegant 20mm gold dial & gold ion-plated design. Perfect for a sophisticated look!\n\nShop now:\n👉 ShoppeBoom: https://shoppeboom.com/product/brand/burberry\n👉 Partner Link: https://watchesofusa.com/products/burberry-bu9509-pioneer-gold-dial-gold-ion-plated-ladies-watch?variant=42924316622902&utm_source=AWIN&utm_medium=AWIN&source=aw&utm_id=2091833_&utm_campaign=affiliate&aw_affid=2091833&awc=116479_1766396814_b07df738e2ae9de6bff8d70921af26d0","images":["27a1.webp","27a2.webp"]},
    {"date":"2025-12-27","time":"23:59","content":"⌚ Burberry The City Navy Blue Chronograph Men’s Watch — sleek design, precise chronograph, and a sophisticated look for every occasion!\n\nShop now:\n👉 ShoppeBoom: https://shoppeboom.com/product/brand/burberry\n👉 Partner Link: https://watchesofusa.com/products/burberry-the-city-navy-blue-chronograph-mens-watch?utm_source=AWIN&utm_medium=AWIN&source=aw&utm_id=2091833_&utm_campaign=affiliate&aw_affid=2091833","images":["27b2.webp","27b1.webp"]},

    {"date":"2025-12-28","time":"00:10","content":"👢 CHIKO Christina Stiletto Boots — sleek square toe & elegant heels for day-to-night style!\n\nShop now:\n👉 ChikoShoes: https://www.chikoshoes.com/shop/chiko-christina-square-toe-stiletto-boots/?aw_affid=2091833&awc=24111_1765449852_08bf985f3e4c443d17231f36f774edb3\n👉 More styles: https://shoppeboom.com/","images":["15b1.jpg","15b2.jpg","15b3.jpg"]},
    {"date":"2025-12-28","time":"11:00","content":"👠 CHIKO Chumani Loafers — chic square toe & comfy block heels for work or night out!\n\nShop now:\n👉 ChikoShoes: https://www.chikoshoes.com/shop/chiko-chumani-square-toe-block-heels-loafers-shoes/?aw_affid=2091833&awc=24111_1765449536_a7692c1d539dfab28c3039e09f20d408\n👉 More styles: https://shoppeboom.com/","images":["15a1.jpg","15a2.jpg","15a3.jpg"]},
    
    {"date":"2025-12-29","time":"11:00","content":"⌚ Burberry Classic Round Ladies Watch — timeless elegance for everyday sophistication! \n\nShop now:\n👉 ShoppeBoom: https://shoppeboom.com/product/brand/burberry\n👉 Partner Link: https://watchesofusa.com/products/burberry-bu10113-classic-round-ladies-watch?variant=42928882057270&utm_source=AWIN&utm_medium=AWIN&source=aw&utm_id=2091833_&utm_campaign=affiliate&aw_affid=2091833&awc=116479_1766397253_9432732989ba45b26ea813b0f6256d73","images":["29a2.webp","29a1.webp"]},
    {"date":"2025-12-29","time":"19:00","content":"⌚ Burberry Classic Swiss Made Two Tone Women’s Watch — refined design and quality craftsmanship for timeless elegance!\n\nShop now:\n👉 ShoppeBoom: https://shoppeboom.com/product/brand/burberry\n👉 Partner Link: https://watchesofusa.com/products/burberry-bu10118-classic-swiss-made-two-tone-womens-watch?variant=42924314427446&utm_source=AWIN&utm_medium=AWIN&source=aw&utm_id=2091833_&utm_campaign=affiliate&aw_affid=2091833&awc=116479_1766397366_ff8396c252847f1cb43c7eb6b12edcb7","images":["29b1.webp","29b2.webp"]},
    
    {"date":"2025-12-30","time":"11:59","content":"⌚ Emporio Armani Chronograph Two-Tone Men’s Watch — sleek design with premium quality for a sophisticated look!\n\nShop now:\n👉 ShoppeBoom: https://shoppeboom.com/product/brand/emporio-armani\n👉 Partner Link: https://watchesofusa.com/products/emporio-armani-ar11511-chronograph-two-tone-mens-watch?variant=42924327206966&utm_source=AWIN&utm_medium=AWIN&source=aw&utm_id=2091833_&utm_campaign=affiliate&aw_affid=2091833&awc=116479_1766397974_6dfd6246a272813c6e0550367e074478","images":["30a1.webp","30a2.webp"]},
    {"date":"2025-12-30","time":"20:30","content":"⌚ Emporio Armani Men’s Watch — sleek, stylish, and perfect for every occasion!\n\nShop now:\n👉 ShoppeBoom: https://shoppeboom.com/product/brand/emporio-armani\n👉 Partner Link: https://watchesofusa.com/products/emporio-armani-ar11340-mens-watch?variant=42924326289462&utm_source=AWIN&utm_medium=AWIN&source=aw&utm_id=2091833_&utm_campaign=affiliate&aw_affid=2091833&awc=116479_1766398072_4258afb81cbf9280ccb5c07d9e5ccb96","images":["30b2.webp","30b1.webp"]},
   
    {"date":"2025-12-31","time":"11:00","content":"⌚ Emporio Armani Men’s Diver Watch — bold, stylish, and perfect for adventure or everyday wear!\n\nShop now:\n👉 ShoppeBoom: https://shoppeboom.com/product/brand/emporio-armani\n👉 Partner Link: https://watchesofusa.com/products/emporio-armani-ar11338-mens-diver-watch?variant=42924326191158&utm_source=AWIN&utm_medium=AWIN&source=aw&utm_id=2091833_&utm_campaign=affiliate&aw_affid=2091833&awc=116479_1766398692_1eec90240f7e7116fd3a261bcb68a617","images":["31a1.webp","31a2.webp"]},
    {"date":"2025-12-31","time":"23:59","content":"⌚ Gucci Grip Quartz Unisex Watch — modern, stylish, and perfect for any outfit!\n\nShop now:\n👉 ShoppeBoom: https://shoppeboom.com/product/brand/gucci\n👉 Partner Link: https://watchesofusa.com/products/gucci-ya157412-grip-quartz-unisex-watch?variant=42924345360438&utm_source=AWIN&utm_medium=AWIN&source=aw&utm_id=2091833_&utm_campaign=affiliate&aw_affid=2091833&awc=116479_1766398789_5ae9141107f44ce5ff5de92744663","images":["31b1.webp","31b2.webp","31b3.webp"]},

    {"date":"2026-01-01","time":"13:59","content":"⌚ Gucci G-Timeless Unisex Watch — modern, stylish, and perfect for any outfit!\n\nShop now:\n👉 ShoppeBoom: https://shoppeboom.com/product/brand/gucci\n👉 Partner Link: https://watchesofusa.com/products/gucci-ya1264084-g-timeless-unisex-watch?variant=42924334874678&utm_source=AWIN&utm_medium=AWIN&source=aw&utm_id=2091833_&utm_campaign=affiliate&aw_affid=2091833&awc=116479_1766399206_a5e1d99e5ca100a322cf2b09acd51930","images":["1a1.webp","1a2.webp"]},
    {"date":"2026-01-01","time":"23:59","content":"⌚ Gucci Black Snake Dial Men’s Watch — bold, modern, and perfect for stylish everyday wear!\n\nShop now:\n👉 ShoppeBoom: https://shoppeboom.com/product/brand/gucci\n👉 Partner Link: https://watchesofusa.com/products/gucci-ya136218-black-snake-dial-mens-watch?variant=42924338151478&utm_source=AWIN&utm_medium=AWIN&source=aw&utm_id=2091833_&utm_campaign=affiliate&aw_affid=2091833&awc=116479_1766399340_c54fc0795583d1a004ac1be578c05054","images":["1b1.webp","1b2.webp","1b3.webp"]},

    {"date":"2026-01-02","time":"13:59","content":"⌚ Gucci Disney X Grip Unisex Watch 35mm — fun, stylish, and perfect for any outfit!\n\nShop now:\n👉 ShoppeBoom: https://shoppeboom.com/product/brand/gucci\n👉 Partner Link: https://watchesofusa.com/products/gucci-ya157420-disney-x-gucci-grip-unisex-watch-35mm?variant=42924346212406&utm_source=AWIN&utm_medium=AWIN&source=aw&utm_id=2091833_&utm_campaign=affiliate&aw_affid=2091833&awc=116479_1766399438_9a0fcb2c79e2fed4370d04683b1e7198","images":["2a1.webp","2a2.webp"]},
    {"date":"2026-01-02","time":"23:59","content":"⌚ Gucci Interlocking-G Black Dial Brown Leather Ladies Watch — stylish, sophisticated, and perfect for any outfit!\n\nShop now:\n👉 ShoppeBoom: https://shoppeboom.com/product/brand/gucci\n👉 Partner Link: https://watchesofusa.com/products/gucci-ya133304-interlocking-g-black-dial-brown-leather-ladies-watch?variant=42924336742454&utm_source=AWIN&utm_medium=AWIN&source=aw&utm_id=2091833_&utm_campaign=affiliate&aw_affid=2091833&awc=116479_1766399515_0c3b77630c74e999ea453db8e958bd26","images":["2b1.webp","2b2.webp"]},
    
    {"date":"2026-01-03","time":"01:59","content":"⌚ Tommy Hilfiger Men’s Watch — classic, stylish, and perfect for everyday or office wear!\n\nShop now:\n👉 ShoppeBoom: https://shoppeboom.com/product/brand/tommy-hilfiger\n👉 Partner Link: https://watchesofusa.com/products/tommy-hilfiger-1791790-mens-watch?variant=42924377767990&utm_source=AWIN&utm_medium=AWIN&source=aw&utm_id=2091833_&utm_campaign=affiliate&aw_affid=2091833&awc=116479_1766399930_3af4c56c654d5345762b009aedfcddfc","images":["3a1.webp","3a2.webp"]},
    {"date":"2026-01-03","time":"17:59","content":"⌚ Tommy Hilfiger Women’s Watch — classic, stylish, and perfect for everyday or office wear!\n\nShop now:\n👉 ShoppeBoom: https://shoppeboom.com/product/brand/tommy-hilfiger\n👉 Partner Link: https://watchesofusa.com/products/tommy-hilfiger-1781809-womens-watch?variant=42924375146550&utm_source=AWIN&utm_medium=AWIN&source=aw&utm_id=2091833_&utm_campaign=affiliate&aw_affid=2091833&awc=116479_1766400000_1a6151751c2e43d37111f920fd218373","images":["3b1.webp","3b2.webp"]},

    {"date":"2026-01-04","time":"23:59","content":"⌚ Tommy Hilfiger Chronograph Landon Men's Watch — classic, stylish, and perfect for everyday or office wear!\n\nShop now:\n👉 ShoppeBoom: https://shoppeboom.com/product/brand/tommy-hilfiger\n👉 Partner Link: https://watchesofusa.com/products/tommy-hilfiger-1791529-chronograph-landon-mens-watch?variant=42924376752182&utm_source=AWIN&utm_medium=AWIN&source=aw&utm_id=2091833_&utm_campaign=affiliate&aw_affid=2091833&awc=116479_1766400116_8c594d2e49e539ac630b8a661317a4fc","images":["4a1.webp"]},
    {"date":"2026-01-04","time":"13:59","content":"⌚ Tommy Hilfiger Blue Dial Blue Silicone Men's Watch — sporty, stylish, and perfect for everyday wear!\n\nShop now:\n👉 ShoppeBoom: https://shoppeboom.com/product/brand/tommy-hilfiger\n👉 Partner Link: https://watchesofusa.com/products/tommy-hilfiger-1791204-blue-dial-blue-silicone-mens-watch?variant=42924376064054&utm_source=AWIN&utm_medium=AWIN&source=aw&utm_id=2091833_&utm_campaign=affiliate&aw_affid=2091833&awc=116479_1766400183_adaf173beee2ae23e1ba0bf8d6d7382f","images":["4b1.webp","4b2.webp"]},

    {"date":"2026-01-05","time":"23:59","content":"👠 CHIKO Chroma Round Toe Wedge Oxfords Shoes — stylish, comfortable, and perfect for elevating any outfit!\n\nShop now:\n👉 ShoppeBoom: https://shoppeboom.com/product/brand/chiko\n👉 Partner Link: https://www.chikoshoes.com/shop/chiko-chroma-round-toe-wedge-oxfords-shoes/?aw_affid=2091833&awc=24111_1766403499_daaf96bb851ea74ec3dabd31000a6a73","images":["5a1.jpg","5a2.jpg"]},
    {"date":"2026-01-05","time":"23:59","content":"👠 CHIKO Clapton Round Toe Block Heels Oxfords Shoes — stylish, comfortable, and perfect for elevating any outfit!\n\nShop now:\n👉 ShoppeBoom: https://shoppeboom.com/product/brand/chiko\n👉 Partner Link: https://www.chikoshoes.com/shop/chiko-clapton-round-toe-block-heels-oxfords-shoes/?aw_affid=2091833&awc=24111_1766403580_e2f6a7aafee2050bcf14973066f3592b","images":["5b1.jpg","5b2.jpg"]},

    {"date":"2026-01-06","time":"23:59","content":"👠 CHIKO Cisneros Round Toe Flatforms Loafers Shoes — stylish, comfortable, and perfect for elevating any outfit!\n\nShop now:\n👉 Partner Link: https://www.chikoshoes.com/shop/chiko-cisneros-round-toe-flatforms-loafers-shoes/?aw_affid=2091833&awc=24111_1766403661_ec4a60f84cf7730585e9bad14eccee99\n👉 ShoppeBoom: https://shoppeboom.com/product/brand/chiko","images":["6a1.jpg","6a2.jpg"]},
    {"date":"2026-01-06","time":"23:59","content":"👠 CHIKO Clarissa Square Toe Block Heels Loafers Shoes — stylish, comfortable, and perfect for elevating any outfit!\n\nShop now:\n👉 Partner Link: https://www.chikoshoes.com/shop/chiko-clarissa-square-toe-block-heels-loafers-shoes/?aw_affid=2091833&awc=24111_1766403758_83c97babd659a590f3599de1093accaa\n👉 ShoppeBoom: https://shoppeboom.com/product/brand/chiko","images":["6b1.jpg","6b2.jpg"]},

    {"date":"2026-01-07","time":"23:59","content":"👠 CHIKO Cinzia Pointy Toe Wedge Pumps Shoes — stylish, comfortable, and perfect for elevating any outfit!\n\nShop now:\n👉 Partner Link: https://www.chikoshoes.com/shop/chiko-cinzia-pointy-toe-wedge-pumps-shoes/?aw_affid=2091833&awc=24111_1766403832_5f9319b5d351272036b463003f55a46d\n👉 ShoppeBoom: https://shoppeboom.com/product/brand/chiko","images":["7a1.jpg","7a2.jpg","7a3.jpg"]},
    {"date":"2026-01-07","time":"23:59","content":"👢 CHIKO Christabel Square Toe Block Heels Ankle Boots — stylish, comfortable, and perfect for elevating any outfit!\n\nShop now:\n👉 Partner Link: https://www.chikoshoes.com/shop/chiko-christabel-square-toe-block-heels-ankle-boots/?aw_affid=2091833&awc=24111_1766403928_0c38fdaef0f3e87aa3ab7595869a357b\n👉 ShoppeBoom: https://shoppeboom.com/product/brand/chiko","images":["7b1.jpg","7b2.jpg","7b3.jpg"]},
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