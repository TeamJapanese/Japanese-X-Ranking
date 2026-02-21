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
