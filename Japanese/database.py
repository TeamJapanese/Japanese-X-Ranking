
import os
from pymongo import MongoClient

# -------------------- DB SETUP -------------------- #

MONGO_URL = os.environ.get("MONGO_URL")

if not MONGO_URL:
    raise RuntimeError("MONGO_URL environment variable is not set")

mongo = MongoClient(MONGO_URL)
db = mongo["TeamJapanese"]

users_col = db["users"]
groups_col = db["groups"]
group_users_col = db["group_users"]


# -------------------- USERS -------------------- #

def add_user(user_id: int, name: str):
    users_col.update_one(
        {"user_id": user_id},
        {
            "$set": {"name": name},
            "$setOnInsert": {
                "user_id": user_id,
                "points": 0,
                "coins": 0
            }
        },
        upsert=True
    )


def update_user(user_id: int, points: int = 0, coins: int = 0):
    users_col.update_one(
        {"user_id": user_id},
        {
            "$inc": {
                "points": points,
                "coins": coins
            }
        },
        upsert=True
    )


def add_points(user_id: int, points: int = 0, coins: int = 0):
    update_user(user_id, points, coins)


def get_user(user_id: int):
    return users_col.find_one({"user_id": user_id})


def get_top_users(limit: int = 10):
    return list(
        users_col.find({"user_id": {"$exists": True}})
        .sort("points", -1)
        .limit(limit)
    )


def get_user_rank(user_id: int):
    users = list(
        users_col.find({"user_id": {"$exists": True}})
        .sort("points", -1)
    )

    for i, user in enumerate(users, start=1):
        if user.get("user_id") == user_id:
            return i, user

    return None, None


# -------------------- GROUPS -------------------- #

def add_group(group_id: int, title: str):
    groups_col.update_one(
        {"group_id": group_id},
        {
            "$set": {"title": title},
            "$setOnInsert": {"group_id": group_id}
        },
        upsert=True
    )


def get_group(group_id: int):
    return groups_col.find_one({"group_id": group_id})


# -------------------- GROUP USERS -------------------- #

def add_group_user(
    group_id: int,
    user_id: int,
    name: str
):
    group_users_col.update_one(
        {"group_id": group_id, "user_id": user_id},
        {
            "$set": {"name": name},
            "$setOnInsert": {
                "group_id": group_id,
                "user_id": user_id,
                "points": 0,
                "coins": 0
            }
        },
        upsert=True
    )


def update_group_user(
    group_id: int,
    user_id: int,
    points: int = 0,
    coins: int = 0
):
    group_users_col.update_one(
        {"group_id": group_id, "user_id": user_id},
        {
            "$inc": {
                "points": points,
                "coins": coins
            }
        },
        upsert=True
    )


def get_group_top_users(group_id: int, limit: int = 10):
    return list(
        group_users_col.find({"group_id": group_id})
        .sort("points", -1)
        .limit(limit)
    )


def get_group_user_rank(group_id: int, user_id: int):
    users = list(
        group_users_col.find({"group_id": group_id})
        .sort("points", -1)
    )

    for i, user in enumerate(users, start=1):
        if user.get("user_id") == user_id:
            return i, user

    return None, None


# -------------------- BROADCAST HELPERS -------------------- #

def _to_telegram_id(value, allow_negative=False):
    """Return a numeric Telegram ID, or None for invalid values."""

    if isinstance(value, bool):
        return None

    if isinstance(value, int):
        if value > 0 or (allow_negative and value < 0):
            return value
        return None

    if isinstance(value, str):
        value = value.strip()

        if value.isdigit():
            result = int(value)
            return result if result > 0 else None

        if allow_negative and value.startswith("-"):
            digits = value[1:]
            if digits.isdigit() and int(digits) > 0:
                return -int(digits)

    # MongoDB ObjectId is NOT a Telegram chat ID.
    return None


def get_all_user_ids():
    user_ids = set()

    for user in users_col.find(
        {},
        {"_id": 1, "user_id": 1}
    ):
        # Prefer the actual Telegram user_id field.
        user_id = _to_telegram_id(user.get("user_id"))

        # Legacy support only when _id itself is numeric.
        if user_id is None:
            user_id = _to_telegram_id(user.get("_id"))

        if user_id is not None:
            user_ids.add(user_id)

    return list(user_ids)


def get_all_group_ids():
    group_ids = set()

    for group in groups_col.find(
        {},
        {"_id": 1, "group_id": 1}
    ):
        # Prefer the actual Telegram group_id field.
        group_id = _to_telegram_id(
            group.get("group_id"),
            allow_negative=True
        )

        # Legacy support only when _id itself is numeric.
        if group_id is None:
            group_id = _to_telegram_id(
                group.get("_id"),
                allow_negative=True
            )

        if group_id is not None:
            group_ids.add(group_id)

    return list(group_ids)


# Compatibility helpers for existing code.
def get_all_users():
    return users_col.find({}, {"_id": 1, "user_id": 1})


def get_all_groups():
    return groups_col.find({}, {"_id": 1, "group_id": 1})


# -------------------- COUNTS -------------------- #

def total_users():
    return users_col.count_documents({})


def total_groups():
    return groups_col.count_documents({})


def get_users_count():
    return total_users()


def get_groups_count():
    return total_groups()
