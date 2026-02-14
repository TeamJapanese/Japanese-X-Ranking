
import os
from pymongo import MongoClient

# -------------------- DB SETUP -------------------- #

MONGO_URL = os.environ.get("MONGO_URL")
mongo = MongoClient(MONGO_URL)
db = mongo["JapaneseXRanking"]

users_col = db["users"]
groups_col = db["groups"]
group_users_col = db["group_users"]

# -------------------- USERS -------------------- #

def add_user(user_id: int, name: str):
    users_col.update_one(
        {"user_id": user_id},
        {"$setOnInsert": {
            "user_id": user_id,
            "name": name,
            "points": 0,
            "coins": 0
        }},
        upsert=True
    )

def update_user(user_id: int, points: int = 0, coins: int = 0):
    users_col.update_one(
        {"user_id": user_id},
        {"$inc": {
            "points": points,
            "coins": coins
        }},
        upsert=True
    )

def get_user(user_id: int):
    return users_col.find_one({"user_id": user_id})

def get_top_users(limit: int = 10):
    return list(users_col.find().sort("points", -1).limit(limit))

def get_user_rank(user_id: int):
    users = list(users_col.find().sort("points", -1))
    for i, user in enumerate(users, start=1):
        if user["user_id"] == user_id:
            return i, user
    return None, None

# -------------------- GROUPS -------------------- #

def add_group(group_id: int, title: str):
    groups_col.update_one(
        {"group_id": group_id},
        {"$setOnInsert": {
            "group_id": group_id,
            "title": title
        }},
        upsert=True
    )

def get_group(group_id: int):
    return groups_col.find_one({"group_id": group_id})

# -------------------- GROUP USERS -------------------- #

def add_group_user(group_id: int, user_id: int, name: str):
    group_users_col.update_one(
        {"group_id": group_id, "user_id": user_id},
        {"$setOnInsert": {
            "group_id": group_id,
            "user_id": user_id,
            "name": name,
            "points": 0,
            "coins": 0
        }},
        upsert=True
    )

def update_group_user(group_id: int, user_id: int, points: int = 0, coins: int = 0):
    group_users_col.update_one(
        {"group_id": group_id, "user_id": user_id},
        {"$inc": {
            "points": points,
            "coins": coins
        }},
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
        if user["user_id"] == user_id:
            return i, user
    return None, None



# -------------------- USERS -------------------- #

def add_user(user_id: int, name: str):
    users_col.update_one(
        {"user_id": user_id},
        {"$setOnInsert": {
            "user_id": user_id,
            "name": name,
            "points": 0,
            "coins": 0
        }},
        upsert=True
    )

def add_points(user_id: int, points: int = 0, coins: int = 0):
    users_col.update_one(
        {"user_id": user_id},
        {"$inc": {"points": points, "coins": coins}},
        upsert=True
    )

def get_user(user_id: int):
    return users_col.find_one({"user_id": user_id})


def total_users(users_col):
    return users_col.count_documents({})

def total_groups(groups_col):
    return groups_col.count_documents({})

def get_all_user_ids():
    return [u["user_id"] for u in users_col.find({}, {"user_id": 1})]

def get_all_group_ids():
    return [g["group_id"] for g in groups_col.find({}, {"group_id": 1})]
    
# Japanese/database/helpers.py

def get_users_count(users_col):
    return users_col.count_documents({})

def get_groups_count(groups_col):
    return groups_col.count_documents({})
