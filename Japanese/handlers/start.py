from pyrogram import Client, filters
from pyrogram.types import Message

from Japanese.database import add_user, add_group

@Client.on_message(filters.command("start"))
async def start_cmd(client: Client, message: Message):
    if message.chat.type == "private":
        add_user(message.from_user.id, message.from_user.first_name)

        await message.reply_text(
            "Welcome to Japanese X Ranking Bot.\n\n"
            "Join a group and start playing typing challenges.\n"
            "Use /ranking to see your points."
        )

@Client.on_message(filters.new_chat_members)
async def bot_added(client: Client, message: Message):
    if message.new_chat_members:
        add_group(message.chat.id, message.chat.title)
