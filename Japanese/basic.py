"""MIT License"""

"""Copyright (c) 2026 [TeamJapanese](https://github.com/TeamJapanese)"""

"""Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:"""

"""The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software."""

"""THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""


import os
import random
import asyncio
from datetime import datetime
from pyrogram import Client, filters
from pyrogram.types import Message
from pymongo import MongoClient
from datetime import datetime, timedelta
import random
import asyncio, pytz, time, psutil, platform
from pyrogram.enums import ParseMode
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
from Japanese.database import add_user

from Japanese.database import get_groups_count, get_users_count, get_all_user_ids, get_all_group_ids
from Japanese.utils.helpers import generate_challenge_image, generate_reward
from Japanese.utils.constants import WORDS_POOL, CHALLENGE_INTERVAL


LOG_CHAT_ID = -1002519094633  # Your log group ID
BOT_START_TIME = time.time()
TEAM_LINK = "https://t.me/TeamJapaneseOfficial"
BOT_LINK = "https://t.me/JapaneseXRankBot"
BOT_USERNAME = "JapaneseXRankBot"



OWNER_ID = 7208410467  # 

@Client.on_message(filters.command("s") & filters.user(OWNER_ID))
async def stats_handler(client, msg):
    users = get_users_count()
    groups = get_groups_count()

    text = f"""
━━━━━━━━━━━━━━━━━━━
📊 **ᴅᴧᴛᴧʙᴧꜱᴇ sᴛᴧᴛs**

👤 **ᴜsᴇʀs:** `{users}`
👥 **ɢʀᴏᴜᴘs:** `{groups}`

🧠 **ᴛᴏᴛᴧʟ:** `{users + groups}`
━━━━━━━━━━━━━━━━━━━
⚡ **ᴘᴏᴡᴇʀᴇᴅ ʙʏ:** [ᴛᴇᴧᴍ ᴊᴧᴘᴧɴᴇsᴇ]({TEAM_LINK})
"""
    await msg.reply_text(text)





async def send_broadcast_message(client, message, chat_id):
    try:
        # Peer resolve karo
        if str(chat_id).startswith("-100"):
            await client.get_chat(chat_id)
        else:
            await client.get_users(chat_id)

        await message.forward(chat_id)
        return True

    except Exception as e:
        print(f"[BROADCAST ERROR] {chat_id} | {type(e).__name__}: {e}")
        return False




# ==================== BROADCAST USERS ====================








# ==================== BROADCAST USERS ====================

@Client.on_message(filters.command("bu") & filters.user(OWNER_ID))
async def broadcast_users(client, msg):
    if not msg.reply_to_message:
        return await msg.reply_text(
            "❌ Please reply to a message to use /bu."
        )

    user_ids = list(get_all_user_ids())
    print(f"[BU DEBUG] Total users: {len(user_ids)}")
    print(f"[BU DEBUG] Sample IDs: {user_ids[:5]}")

    sent, failed = 0, 0
    total = len(user_ids)

    status = await msg.reply_text(
        f"━━━━━━━━━━━━━━━━━━━\n"
        f"📢 ᴜsᴇʀ ʙʀᴏᴀᴅᴄᴀsᴛ sᴛᴀʀᴛᴇᴅ\n\n"
        f"👤 ᴛᴏᴛᴀʟ ᴜsᴇʀs: {total}\n"
        f"━━━━━━━━━━━━━━━━━━━"
    )

    for user_id in user_ids:
        if await send_broadcast_message(
            client, msg.reply_to_message, user_id
        ):
            sent += 1
        else:
            failed += 1

        await asyncio.sleep(0.1)

    await status.edit_text(
        f"━━━━━━━━━━━━━━━━━━━\n"
        f"📢 ᴜsᴇʀ ʙʀᴏᴀᴅᴄᴀsᴛ sᴛᴀᴛᴜs\n\n"
        f"👤 ᴜsᴇʀs sᴇɴᴛ: {sent}\n"
        f"❌ ғᴀɪʟᴇᴅ / ʀᴇᴍᴏᴠᴇᴅ: {failed}\n\n"
        f"🧠 ᴛᴏᴛᴀʟ: {total}\n"
        f"━━━━━━━━━━━━━━━━━━━\n"
        f"⚡ **ᴘᴏᴡᴇʀᴇᴅ ʙʏ:** "
        f"[ᴛᴇᴧᴍ ᴊᴧᴘᴧɴᴇsᴇ]({TEAM_LINK})"
    )


# ==================== BROADCAST GROUPS ====================

@Client.on_message(filters.command("bg") & filters.user(OWNER_ID))
async def broadcast_groups(client, msg):
    if not msg.reply_to_message:
        return await msg.reply_text(
            "❌ Please reply to a message to use /bg."
        )

    group_ids = list(get_all_group_ids())
    print(f"[BG DEBUG] Total groups: {len(group_ids)}")
    print(f"[BG DEBUG] Sample IDs: {group_ids[:5]}")

    sent, failed = 0, 0
    total = len(group_ids)

    status = await msg.reply_text(
        f"━━━━━━━━━━━━━━━━━━━\n"
        f"📢 ɢʀᴏᴜᴘ ʙʀᴏᴀᴅᴄᴀsᴛ sᴛᴀʀᴛᴇᴅ\n\n"
        f"👥 ᴛᴏᴛᴀʟ ɢʀᴏᴜᴘs: {total}\n"
        f"━━━━━━━━━━━━━━━━━━━"
    )

    for group_id in group_ids:
        if await send_broadcast_message(
            client, msg.reply_to_message, group_id
        ):
            sent += 1
        else:
            failed += 1

        await asyncio.sleep(0.1)

    await status.edit_text(
        f"━━━━━━━━━━━━━━━━━━━\n"
        f"📢 ɢʀᴏᴜᴘ ʙʀᴏᴀᴅᴄᴀsᴛ sᴛᴀᴛᴜs\n\n"
        f"👥 ɢʀᴏᴜᴘs sᴇɴᴛ: {sent}\n"
        f"❌ ғᴀɪʟᴇᴅ / ʀᴇᴍᴏᴠᴇᴅ: {failed}\n\n"
        f"🧠 ᴛᴏᴛᴀʟ: {total}\n"
        f"━━━━━━━━━━━━━━━━━━━\n"
        f"⚡ **ᴘᴏᴡᴇʀᴇᴅ ʙʏ:** "
        f"[ᴛᴇᴧᴍ ᴊᴧᴘᴧɴᴇsᴇ]({TEAM_LINK})"
    )


# ==================== BROADCAST ALL ====================

@Client.on_message(filters.command("b") & filters.user(OWNER_ID))
async def broadcast_all(client, msg):
    if not msg.reply_to_message:
        return await msg.reply_text(
            "❌ Please reply to a message to use /b."
        )

    user_ids = list(get_all_user_ids())
    group_ids = list(get_all_group_ids())

    print(
        f"[B DEBUG] Users: {len(user_ids)} | "
        f"Groups: {len(group_ids)}"
    )
    print(f"[B DEBUG] Sample users: {user_ids[:5]}")
    print(f"[B DEBUG] Sample groups: {group_ids[:5]}")

    sent, failed = 0, 0
    total = len(user_ids) + len(group_ids)

    status = await msg.reply_text(
        f"━━━━━━━━━━━━━━━━━━━\n"
        f"📢 ʙʀᴏᴀᴅᴄᴀsᴛ ᴀʟʟ sᴛᴀʀᴛᴇᴅ\n\n"
        f"👤 ᴜsᴇʀs: {len(user_ids)}\n"
        f"👥 ɢʀᴏᴜᴘs: {len(group_ids)}\n"
        f"🧠 ᴛᴏᴛᴀʟ: {total}\n"
        f"━━━━━━━━━━━━━━━━━━━"
    )

    for chat_id in user_ids + group_ids:
        if await send_broadcast_message(
            client, msg.reply_to_message, chat_id
        ):
            sent += 1
        else:
            failed += 1

        await asyncio.sleep(0.1)

    await status.edit_text(
        f"━━━━━━━━━━━━━━━━━━━\n"
        f"📢 ʙʀᴏᴀᴅᴄᴀsᴛ ᴀʟʟ sᴛᴀᴛᴜs\n\n"
        f"👤 ᴜsᴇʀs + ɢʀᴏᴜᴘs sᴇɴᴛ: {sent}\n"
        f"❌ ғᴀɪʟᴇᴅ / ʀᴇᴍᴏᴠᴇᴅ: {failed}\n\n"
        f"🧠 ᴛᴏᴛᴀʟ: {total}\n"
        f"━━━━━━━━━━━━━━━━━━━\n"
        f"⚡ **ᴘᴏᴡᴇʀᴇᴅ ʙʏ:** "
        f"[ᴛᴇᴧᴍ ᴊᴧᴘᴧɴᴇsᴇ]({TEAM_LINK})"
    )






            

















# -------------------- DATABASE SETUP -------------------- #

MONGO_URL = os.environ.get("MONGO_URL")
if not MONGO_URL:
    raise RuntimeError("MONGO_URL not set")

mongo_client = MongoClient(MONGO_URL)
db = mongo_client["TeamJapanese"]

users_col = db["users"]
groups_col = db["groups"]

# Active challenges (in-memory)
active_challenges = {}
CHALLENGE_DURATION = 60 # 10 minutes per challenge

# -------------------- GROUP REGISTER -------------------- #

@Client.on_message(filters.new_chat_members)
async def on_bot_added(client: Client, message: Message):
    for member in message.new_chat_members:
        if member.is_self:
            groups_col.update_one(
                {"group_id": message.chat.id},
                {"$set": {
                    "group_id": message.chat.id,
                    "title": message.chat.title,
                    "added_at": datetime.utcnow()
                }},
                upsert=True
            )
            await message.reply_text(
                "ᴛʜᴧɴᴋs ғᴏʀ ᴧᴅᴅɪɴɢ **[ᴊᴧᴘᴧɴᴇsᴇ x ʀᴧɴᴋɪɴɢ ʙᴏᴛ](https://t.me/JapaneseXRankBot)** — ʟᴇᴛ ᴛʜᴇ ᴄʜᴧʟʟᴇɴɢᴇs ʙᴇɢɪɴ! ⚡\n\n"
                "ᴧᴜᴛᴏᴍᴧᴛᴇᴅ ᴛʏᴘɪɴɢ ᴄʜᴧʟʟᴇɴɢᴇs ᴡɪʟʟ ɴᴏᴡ ʀᴜɴ ᴧᴛ ʀᴇɢᴜʟᴧʀ ɪɴᴛᴇʀᴠᴧʟs.\n\n"
                "ᴘᴧʀᴛɪᴄɪᴘᴧɴᴛs ᴄᴧɴ ᴄᴏᴍᴘᴇᴛᴇ ɪɴ ʀᴇᴧʟ-ᴛɪᴍᴇ, ᴇᴧʀɴ ᴘᴏɪɴᴛs, ᴧɴᴅ ᴧᴘᴘᴇᴧʀ ᴏɴ ᴛʜᴇ ɢʟᴏʙᴧʟ ʀᴧɴᴋɪɴɢs.\n\n"
                "ᴘʀᴇᴘᴧʀᴇ ʏᴏᴜʀ ғɪɴɢᴇʀs — sᴘᴇᴇᴅ ᴧɴᴅ ᴧᴄᴄᴜʀᴧᴄʏ ᴅᴇᴄɪᴅᴇ ᴛʜᴇ ᴡɪɴɴᴇʀ."
            )

# -------------------- CHALLENGE SYSTEM -------------------- #


async def challenge_loop(client: Client):
    await asyncio.sleep(10)  # bot start hone ke 10 sec baad

    while True:
        print("🎮 sending challenge...")
        await send_challenge(client)
        await asyncio.sleep(CHALLENGE_INTERVAL)  # 30 min


async def send_challenge(client: Client):
    now = datetime.utcnow()
    groups = list(groups_col.find())

    for group in groups:
        group_id = group.get("group_id")
        if not group_id:
            continue

        # 🔥 CLEAR EXPIRED CHALLENGE
        old = active_challenges.get(group_id)
        if old and now > old["end_time"]:
            active_challenges.pop(group_id, None)

        # ⛔ Still active → skip
        if group_id in active_challenges:
            continue

        word = random.choice(WORDS_POOL)
        reward = generate_reward()

        active_challenges[group_id] = {
            "word": word.lower(),
            "reward": reward,
            "end_time": now + timedelta(seconds=CHALLENGE_DURATION)
        }

        image = generate_challenge_image(word)

        try:
            await client.send_photo(
                chat_id=group_id,
                photo=image,
                caption=(
                    "🏆 **[ᴊᴧᴘᴧɴᴇsᴇ x ʀᴧɴᴋɪɴɢ](https://t.me/JapaneseXRankBot)**\n\n"
                    "ᴛʏᴘᴇ ᴛʜᴇ ᴇxᴧᴄᴛ ᴡᴏʀᴅ sʜᴏᴡɴ ɪɴ ᴛʜᴇ ɪᴍᴧɢᴇ.\n"
                    "ғɪʀsᴛ ᴄᴏʀʀᴇᴄᴛ ᴧɴsᴡᴇʀ ᴡɪɴs!\n\n"
                    f"🎁 ʀᴇᴡᴧʀᴅ: **{reward} ᴄᴏɪɴs & ᴘᴏɪɴᴛs**"
                )
            )
        except Exception as e:
            print(f"[CHALLENGE ERROR] {group_id} -> {e}")
            active_challenges.pop(group_id, None)














@Client.on_message(filters.text & filters.group)
async def answer_handler(client: Client, message: Message):
    group_id = message.chat.id
    challenge = active_challenges.get(group_id)

    if not challenge:
        return

    # ⏱ TIME OVER
    if datetime.utcnow() > challenge["end_time"]:
        active_challenges.pop(group_id, None)
        await message.reply_text("❌ **Time’s Up!** Next round coming soon.")
        return

    # ✅ CORRECT ANSWER
    if message.text.lower().strip() == challenge["word"]:
        reward = challenge["reward"]

        users_col.update_one(
            {"user_id": message.from_user.id},
            {
                "$setOnInsert": {
                    "user_id": message.from_user.id,
                    "name": message.from_user.first_name
                },
                "$inc": {
                    "points": reward,
                    "coins": reward
                }
            },
            upsert=True
        )

        await message.reply_text(
            f"🎉 **ᴡɪɴɴᴇʀ!**\n\n"
            f"{message.from_user.first_name} ᴛʏᴘᴇᴅ ᴄᴏʀʀᴇᴄᴛʟʏ!\n"
            f"+{reward} ᴘᴏɪɴᴛs ᴧᴅᴅᴇᴅ 🏆"
        )
        
        active_challenges.pop(group_id, None)


# -------------------- BOT COMMANDS -------------------- #


# ==================== START COMMAND ====================

@Client.on_message(filters.command("start"))
async def start_cmd(client, message):

    # ==================== USER REGISTRATION ====================

    from Japanese.database import add_user

    user = message.from_user

    if user:
        try:
            add_user(user.id, user.first_name)
            print(f"[START DEBUG] User registered: {user.id}")
        except Exception as e:
            print(f"[START ERROR] User registration failed: {e}")

    # ==================== BOT & USER MENTIONS ====================

    bot_user = await client.get_me()
    bot_username = bot_user.username or "username"

    bot_mention = f"[{bot_user.first_name}](https://t.me/{bot_username})"

    if not user:
        return await message.reply_text(
            "❌ Unable to identify your Telegram account."
        )

    user_link = f"[{user.first_name}](tg://user?id={user.id})"
    username = f"@{user.username}" if user.username else "None"

    # ==================== TIME (IST) ====================

    ist = pytz.timezone("Asia/Kolkata")
    current_time = datetime.now(ist).strftime("%d-%m-%Y | %I:%M:%S %p")

    # ==================== MAIN START TEXT ====================

    reply_text = (
        f"✨👋 **ᴡᴇʟᴄᴏᴍᴇ, {user_link}!** 👋✨\n\n"
        f"🏆 **ɪ ᴀᴍ {bot_mention}** — ᴀ ʀᴇᴀʟ-ᴛɪᴍᴇ ᴛʏᴘɪɴɢ & ʀᴀɴᴋɪɴɢ ʙᴏᴛ ⚡\n\n"
        "⌨️ ᴛʏᴘᴇ ғᴀsᴛ • ᴇᴀʀɴ ᴘᴏɪɴᴛs • ᴄʟɪᴍʙ ᴛʜᴇ ʟᴇᴀᴅᴇʀʙᴏᴀʀᴅ\n"
        "⏱️ ᴀᴜᴛᴏᴍᴀᴛᴇᴅ ᴄʜᴀʟʟᴇɴɢᴇs ʀᴜɴ ʀᴇɢᴜʟᴀʀʟʏ ɪɴ ɢʀᴏᴜᴘs\n\n"
        "🏷️ ᴏғғɪᴄɪᴀʟ ᴄʜᴀɴɴᴇʟ: "
        "[ᴛᴇᴀᴍ ᴊᴀᴘᴀɴᴇsᴇ](https://t.me/TeamJapaneseOfficial)"
    )

    # ==================== START BUTTONS ====================

    buttons = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                "ᴅᴇᴠᴇʟᴏᴘᴇʀ",
                url="https://t.me/sxndeep_shxrmx"
            )
        ],
        [
            InlineKeyboardButton(
                "ᴛᴇᴀᴍ ᴊᴀᴘᴀɴᴇsᴇ",
                url="https://t.me/TeamJapaneseOfficial"
            )
        ]
    ])

    # ==================== SEND START MESSAGE ====================

    await message.reply_photo(
        photo="img/ranking.png",
        caption=reply_text,
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=buttons
    )

    # ==================== USER LOG TEXT ====================

    log_text = (
        f"🔔 **ɴᴇᴡ ᴜsᴇʀ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ!** 🔔\n\n"
        f"👤 **ɴᴀᴍᴇ:** {user_link}\n"
        f"🏷 **ᴜsᴇʀɴᴀᴍᴇ:** {username}\n"
        f"🆔 **ᴜsᴇʀ ɪᴅ:** `{user.id}`\n"
        f"🕒 **ᴛɪᴍᴇ (ɪsᴛ):** `{current_time}`\n"
        f"🔗 **ᴘᴇʀᴍᴀɴᴇɴᴛ ʟɪɴᴋ:** "
        f"[ᴛᴀᴘ ʜᴇʀᴇ](tg://user?id={user.id})\n\n"
        f"⚡ **ᴀᴄᴛɪᴏɴ:** `/start` ᴇxᴇᴄᴜᴛᴇᴅ\n"
        f"💬 **sᴛᴀᴛᴜs:** ᴜsᴇʀ ʜᴀs sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ 🚀\n"
        f"⚡ **ᴘᴏᴡᴇʀᴇᴅ ʙʏ:** "
        "[ᴛᴇᴀᴍ ᴊᴀᴘᴀɴᴇsᴇ](https://t.me/TeamJapaneseOfficial)"
    )

    # ==================== LOG BUTTONS ====================

    log_buttons = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                "👤 ᴠɪᴇᴡ ᴘʀᴏꜰɪʟᴇ",
                url=f"tg://user?id={user.id}"
            )
        ]
    ])

    # ==================== SEND LOG TO LOG GROUP ====================

    try:
        await client.send_message(
            chat_id=-1002519094633,
            text=log_text,
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=log_buttons,
            disable_web_page_preview=True
        )
    except Exception as e:
        print(f"[START LOG ERROR] Failed to send user log: {e}")




@Client.on_message(filters.command("repo"))
async def repo_handler(client: Client, message: Message):
    repo_text = f"""
━━━━━━━━━━━━━━━━━━━
**[𝑱𝒂𝒑𝒂𝒏𝒆𝒔𝒆 𝑿 𝑹𝒂𝒏𝒌𝒊𝒏𝒈]({BOT_LINK})**
**ʀᴇᴘᴏꜱɪᴛᴏʀʏ:** ᴏᴘᴇɴ-sᴏᴜʀᴄᴇ
**ꜱᴛᴀᴛᴜꜱ:** ᴀᴄᴛɪᴠᴇʟʏ ᴍᴀɪɴᴛᴀɪɴᴇᴅ
**ꜱᴄᴏᴘᴇ:** ᴘʀᴏᴅᴜᴄᴛɪᴏɴ-ʀᴇᴀᴅʏ ᴄᴏᴅᴇʙᴀꜱᴇ
**ᴅᴏᴄᴜᴍᴇɴᴛᴀᴛɪᴏɴ:** ᴄʟᴇᴀʀ & ᴡᴇʟʟ sᴛʀᴜᴄᴛᴜʀᴇᴅ
━━━━━━━━━━━━━━━━━━━
**ᴍᴀɪɴᴛᴀɪɴᴇʀ:** [ᴛᴇᴧᴍ ᴊᴧᴘᴧɴᴇsᴇ]({TEAM_LINK})
"""

    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton(
            "ᴠɪᴇᴡ ɢɪᴛʜᴜʙ ʀᴇᴘᴏꜱɪᴛᴏʀʏ",
            url="https://github.com/TeamJapanese/Japanese-X-Ranking"
        )]
    ])

    await message.reply_text(
        repo_text,
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=buttons,
        disable_web_page_preview=True
    )




@Client.on_message(filters.command("groups") & filters.user(OWNER_ID))
async def groups_handler(client: Client, message: Message):
    groups = list(groups_col.find())

    if not groups:
        return await message.reply_text("❌ No groups registered yet.")

    text = "━━━━━━━━━━━━━━━━━━━\n"
    text += "👥 **ʀᴇɢɪsᴛᴇʀᴇᴅ ɢʀᴏᴜᴘs**\n\n"

    for i, group in enumerate(groups[:20], start=1):  # show first 20
        title = group.get("title", "Unknown Group")
        group_id = group.get("group_id", "N/A")
        text += f"{i}. **{title}**\n"
        text += f"   🆔 `{group_id}`\n\n"

    if len(groups) > 20:
        text += f"➕ `{len(groups) - 20}` more groups not shown...\n\n"

    text += "━━━━━━━━━━━━━━━━━━━\n"
    text += f"📊 **ᴛᴏᴛᴀʟ ɢʀᴏᴜᴘs:** `{len(groups)}`\n"
    text += f"⚡ **ᴘᴏᴡᴇʀᴇᴅ ʙʏ:** [ᴛᴇᴀᴍ ᴊᴀᴘᴀɴᴇsᴇ]({TEAM_LINK})"

    await message.reply_text(
        text,
        parse_mode=ParseMode.MARKDOWN,
        disable_web_page_preview=True
    )







@Client.on_message(filters.command("alive"))
async def alive_cmd(client, message):
    ist = pytz.timezone("Asia/Kolkata")
    current_time = datetime.now(ist).strftime("%d-%m-%Y | %I:%M:%S %p")

    uptime_seconds = time.time() - BOT_START_TIME
    uptime_str = f"{int(uptime_seconds//3600)}h:{int((uptime_seconds%3600)//60)}m:{int(uptime_seconds%60)}s"
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    system = platform.system()
    release = platform.release()
    bot_user = await client.get_me()

    alive_text = (
        f"✨══════════✨\n"
        f"🤖 **ʙᴏᴛ:** [{bot_user.first_name}](https://t.me/{bot_user.username})\n"
        f"🕒 **ᴛɪᴍᴇ (ɪsᴛ):** `{current_time}`\n"
        f"⏱ **ᴜᴘᴛɪᴍᴇ:** `{uptime_str}`\n"
        f"💻 **sʏsᴛᴇᴍ:** `{system} {release}`\n"
        f"⚙️ **ᴄᴘᴜ:** `{cpu}%` | **ʀᴀᴍ:** `{ram}%` | **ᴅɪsᴋ:** `{disk}%`\n"
        f"🏷️ ᴄʜᴀɴɴᴇʟ: [ᴛᴇᴀᴍ ᴊᴀᴘᴀɴᴇsᴇ](https://t.me/TeamJapaneseOfficial)\n"
        f"✨══════════✨"
    )

    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("⚡ ᴅᴇᴠᴇʟᴏᴘᴇʀ", url="https://t.me/sxndeep_shxrmx")],
        [InlineKeyboardButton("📢 ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ", url="https://t.me/TeamJapaneseOfficial")]
    ])

    await message.reply_text(alive_text, parse_mode=ParseMode.MARKDOWN, reply_markup=buttons, disable_web_page_preview=True)


@Client.on_message(filters.command("ping"))
async def ping_cmd(client, message):
    start_time = time.time()
    m = await message.reply_text("⚡ ᴄʜᴇᴄᴋɪɴɢ ʙᴏᴛ sʏsᴛᴇᴍ ᴀɴᴅ ᴘɪɴɢ...")
    await asyncio.sleep(0.3)
    end_time = time.time()
    
    ping_ms = (end_time - start_time) * 1000
    uptime_seconds = time.time() - BOT_START_TIME
    uptime_str = f"{int(uptime_seconds//3600)}h:{int((uptime_seconds%3600)//60)}m:{int(uptime_seconds%60)}s"
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    ist = pytz.timezone("Asia/Kolkata")
    ping_time = datetime.now(ist).strftime("%I:%M:%S %p")
    bot_user = await client.get_me()

    ping_text = (
        f"✨══════════✨\n"
        f"🏓 **ᴘɪɴɢ:** `{ping_ms:.2f} ms`\n"
        f"⏱ **ᴜᴘᴛɪᴍᴇ:** `{uptime_str}`\n"
        f"🕒 **ᴛɪᴍᴇ (ɪsᴛ):** `{ping_time}`\n"
        f"⚙️ **ᴄᴘᴜ:** `{cpu}%` | **ʀᴀᴍ:** `{ram}%` | **ᴅɪsᴋ:** `{disk}%`\n"
        f"🤖 **ʙᴏᴛ:** [{bot_user.first_name}](https://t.me/{bot_user.username})\n"
        f"🏷️ ᴄʜᴀɴɴᴇʟ: [ᴛᴇᴀᴍ ᴊᴀᴘᴀɴᴇsᴇ](https://t.me/TeamJapaneseOfficial)\n"
        f"✨══════════✨"
    )

    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("⚡ ᴅᴇᴠᴇʟᴏᴘᴇʀ", url="https://t.me/sxndeep_shxrmx")],
        [InlineKeyboardButton("📢 ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ", url="https://t.me/TeamJapaneseOfficial")]
    ])

    await m.edit_text(ping_text, parse_mode=ParseMode.MARKDOWN, reply_markup=buttons)



@Client.on_message(filters.command("help") & filters.private)
async def help_command(client: Client, message: Message):
    await message.reply_text(
        f"""
📌 **ᴄᴏᴍᴍᴧɴᴅ ɢᴜɪᴅᴇ**

🚀 /start 
↳ ʙᴇɢɪɴ ʏᴏᴜʀ ᴊᴏᴜʀɴᴇʏ ᴡɪᴛʜ ᴊᴧᴘᴧɴᴇsᴇ x ʀᴧɴᴋɪɴɢ  
↳ ɢᴇᴛ ᴀɴ ᴏᴠᴇʀᴠɪᴇᴡ ᴏғ ᴛʜᴇ ɢᴧᴍᴇ ᴀɴᴅ ғᴇᴧᴛᴜʀᴇs  

⚡ /ping
↳ ᴄʜᴇᴄᴋ ʙᴏᴛ ʀᴇsᴘᴏɴsᴇ sᴘᴇᴇᴅ ᴀɴᴅ ʟᴧᴛᴇɴᴄʏ  

🧬 /alive 
↳ ᴄᴏɴғɪʀᴍ ᴛʜᴧᴛ ᴛʜᴇ ʙᴏᴛ ɪs ᴏɴʟɪɴᴇ ᴀɴᴅ sᴍᴏᴏᴛʜʟʏ ʀᴜɴɴɪɴɢ  

📊 /stats
↳ ᴠɪᴇᴡ ᴅᴧᴛᴧʙᴧsᴇ sᴛᴧᴛɪsᴛɪᴄs (ᴜsᴇʀs & ɢʀᴏᴜᴘs)  

🏆 /topgame 
↳ sᴇᴇ ᴛʜᴇ ɢʟᴏʙᴧʟ ᴛᴏᴘ ʀᴧɴᴋᴇᴅ ᴘʟᴧʏᴇʀ  
↳ ғɪɴᴅ ᴏᴜᴛ ᴡʜᴏ ᴅᴏᴍɪɴᴧᴛᴇs ᴛʜᴇ ʟᴇᴧᴅᴇʀʙᴏᴧʀᴅ  

📈 /ranking 
↳ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴄᴜʀʀᴇɴᴛ ᴘᴏɪɴᴛs ᴀɴᴅ ʀᴧɴᴋ  
↳ ᴛʀᴧᴄᴋ ʏᴏᴜʀ ᴘʀᴏɢʀᴇss  

👥 /groups 
↳ ᴠɪᴇᴡ ᴀʟʟ ʀᴇɢɪsᴛᴇʀᴇᴅ ɢʀᴏᴜᴘs  
↳ ᴛᴧᴘ ᴀɴʏ ɢʀᴏᴜᴘ ɴᴧᴍᴇ ᴛᴏ ᴏᴘᴇɴ ɪᴛ  

━━━━━━━━━━━━━━━━━━━
⚡ **ᴘᴏᴡᴇʀᴇᴅ ʙʏ:** [ᴛᴇᴧᴍ ᴊᴧᴘᴧɴᴇsᴇ]({TEAM_LINK})
""",
        disable_web_page_preview=True
    )






@Client.on_message(filters.command("topgame"))
async def topgame_command(client: Client, message: Message):
    top_players = list(
        users_col.find({}, {"_id": 0, "user_id": 1, "name": 1, "points": 1})
        .sort("points", -1)
        .limit(10)
    )

    if not top_players:
        return await message.reply_text("❌ No rankings available yet!")

    leaderboard = "🏆 **ᴛᴏᴘ 10 ɢʟᴏʙᴀʟ ᴘʟᴀʏᴇʀs** 🏆\n\n"
    medals = ["🥇", "🥈", "🥉"]

    for idx, user in enumerate(top_players, start=1):
        medal = medals[idx - 1] if idx <= 3 else f"`#{idx}`"
        uid = user.get("user_id")
        name = user.get("name", "Unknown")
        points = user.get("points", 0)

        # 👤 Mention player
        mention = f"[{name}](tg://user?id={uid})" if uid else name

        leaderboard += (
            f"{medal} {mention}\n"
            f"   ⭐ Points: `{points}`\n\n"
        )

    leaderboard += "━━━━━━━━━━━━━━━━━━━\n"
    leaderboard += f"⚡⚡ **ᴘᴏᴡᴇʀᴇᴅ ʙʏ:** [ᴛᴇᴧᴍ ᴊᴧᴘᴧɴᴇsᴇ]({TEAM_LINK})"

    await message.reply_text(
        leaderboard,
        disable_web_page_preview=True
    )












@Client.on_message(filters.command("ranking"))
async def ranking_command(client: Client, message: Message):
    user_id = message.from_user.id

    # 🔹 Fetch all players sorted by points
    players = list(
        users_col.find({}, {"_id": 0, "user_id": 1, "name": 1, "points": 1})
        .sort("points", -1)
    )

    if not players:
        return await message.reply_text("❌ No rankings available yet!")

    total_players = len(players)

    # 🔹 Find current user's data & rank
    current_user = None
    rank = None
    for idx, user in enumerate(players, start=1):
        if user.get("user_id") == user_id:
            current_user = user
            rank = idx
            break

    if not current_user:
        return await message.reply_text("❌ You haven't played any games yet!")

    points = current_user.get("points", 0)

    # 🔹 Progress bar (relative to top player)
    top_points = players[0]["points"]
    bar_length = 10
    filled = int((points / top_points) * bar_length) if top_points > 0 else 0
    progress_bar = "█" * filled + "░" * (bar_length - filled)

    # 🔹 Player list (all players with mentions)
    player_list = ""
    for idx, user in enumerate(players, start=1):
        uid = user.get("user_id")
        name = user.get("name", "Unknown")
        mention = f"[{name}](tg://user?id={uid})" if uid else name
        player_list += f"`#{idx}` {mention} — ⭐ `{user.get('points', 0)}`\n"

    ranking_text = (
        f"🏅 **ʏᴏᴜʀ ʀᴀɴᴋɪɴɢ** 🏅\n\n"
        f"👤 **Name:** {current_user.get('name')}\n"
        f"⭐ **Points:** `{points}`\n"
        f"🏆 **Rank:** `#{rank}` of `{total_players}` players\n\n"
        f"📈 **Progress:** `{progress_bar}`\n\n"
        f"━━━━━━━━━━━━━━━━━━━\n"
        f"👥 **ᴀʟʟ ᴘʟᴀʏᴇʀs**\n"
        f"{player_list}"
        f"━━━━━━━━━━━━━━━━━━━\n"
        f"⚡⚡ **ᴘᴏᴡᴇʀᴇᴅ ʙʏ:** [ᴛᴇᴧᴍ ᴊᴧᴘᴧɴᴇsᴇ]({TEAM_LINK})"
    )

    await message.reply_text(
        ranking_text,
        disable_web_page_preview=True
    )


# -------------------- ANSWER HANDLER -------------------- #

@Client.on_message(
    filters.group
    & (filters.text | filters.caption)
    & ~filters.command(["topgame", "ranking", "start", "help", "ping", "alive"])
)
async def answer_handler(client: Client, message: Message):
    group_id = message.chat.id
    challenge = active_challenges.get(group_id)

    if not challenge:
        return

    user_text = message.text or message.caption
    if not user_text:
        return

    if user_text.lower().strip() == challenge["word"]:
        reward = challenge["reward"]

        users_col.update_one(
            {"user_id": message.from_user.id},
            {
                "$setOnInsert": {
                    "user_id": message.from_user.id,
                    "name": message.from_user.first_name
                },
                "$inc": {
                    "points": reward,
                    "coins": reward
                }
            },
            upsert=True
        )

        await message.reply_text(
            f"🎉 **ᴡɪɴɴᴇʀ!**\n\n"
            f"{message.from_user.first_name} ᴛʏᴘᴇᴅ ᴄᴏʀʀᴇᴄᴛʟʏ!\n"
            f"+{reward} ᴘᴏɪɴᴛs ᴧᴅᴅᴇᴅ 🏆"
        )

        active_challenges.pop(group_id, None)
