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

from Japanese.database import add_user, add_points
from Japanese.database import update_user, update_group_user, add_group_user
from datetime import datetime

# Active challenges per group
active_challenges = {}

@Client.on_message(filters.group & filters.text)
async def handle_game_answer(client: Client, message: Message):
    group_id = message.chat.id
    user = message.from_user

    if group_id not in active_challenges:
        return

    challenge = active_challenges[group_id]
    correct_word = challenge["word"]

    if message.text.lower().strip() != correct_word:
        return

    # Winner found
    reward = challenge["reward"]

    add_user(user.id, user.first_name)
    add_group_user(group_id, user.id, user.first_name)
    add_points(user.id, reward, reward)
    update_user(user.id, points=reward, coins=reward)
    update_group_user(group_id, user.id, points=reward, coins=reward)

    del active_challenges[group_id]

    await message.reply_text(
        f"🎉 {user.first_name} typed correctly!\n\n"
        f"Word: `{correct_word}`\n"
        f"Reward: `{reward}` coins & points"
    )
