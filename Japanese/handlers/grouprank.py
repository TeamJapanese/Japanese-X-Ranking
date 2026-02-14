from pyrogram import Client, filters
from pyrogram.types import Message

from Japanese.database import get_group_top_users

@Client.on_message(filters.command("grouprank") & filters.group)
async def group_rank_cmd(client: Client, message: Message):
    group_id = message.chat.id
    top_users = get_group_top_users(group_id)

    if not top_users:
        await message.reply_text("No group rankings yet.")
        return

    text = "Group Leaderboard\n\n"

    for i, user in enumerate(top_users, start=1):
        text += (
            f"{i}. {user['name']} — "
            f"{user['points']} points\n"
        )

    await message.reply_text(text)
