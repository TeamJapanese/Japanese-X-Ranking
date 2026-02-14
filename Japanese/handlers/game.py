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
