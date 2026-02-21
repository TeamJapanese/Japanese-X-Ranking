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
