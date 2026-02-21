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
