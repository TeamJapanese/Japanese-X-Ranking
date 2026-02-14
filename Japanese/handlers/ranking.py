from pyrogram import Client, filters
from pyrogram.types import Message

from Japanese.database import get_top_users, get_user_rank, add_user

# -------------------- /ranking -------------------- #

@Client.on_message(filters.command("ranking"))
async def ranking_cmd(client: Client, message: Message):
    user = message.from_user
    add_user(user.id, user.first_name)

    rank, data = get_user_rank(user.id)

    if not data:
        await message.reply_text("You have no points yet. Start playing!")
        return

    await message.reply_text(
        f"Your Ranking Status\n\n"
        f"Name: {data['name']}\n"
        f"Rank: #{rank}\n"
        f"Points: {data['points']}\n"
        f"Coins: {data['coins']}"
    )

# -------------------- /topgame -------------------- #

@Client.on_message(filters.command("topgame"))
async def topgame_cmd(client: Client, message: Message):
    top_users = get_top_users(10)

    if not top_users:
        await message.reply_text("No rankings yet.")
        return

    text = "Global Top Players\n\n"

    for i, user in enumerate(top_users, start=1):
        text += (
            f"{i}. {user['name']} — "
            f"{user['points']} points\n"
        )

    await message.reply_text(text)
