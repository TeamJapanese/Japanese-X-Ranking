from datetime import datetime
from typing import List

class Group:
    def __init__(self, group_id: int, name: str, active_users: List[int] = None):
        self.group_id = group_id
        self.name = name
        self.active_users = active_users or []
        self.created_at = datetime.utcnow()

    def add_user(self, user_id: int):
        if user_id not in self.active_users:
            self.active_users.append(user_id)

    def remove_user(self, user_id: int):
        if user_id in self.active_users:
            self.active_users.remove(user_id)

    def to_dict(self):
        return {
            "group_id": self.group_id,
            "name": self.name,
            "active_users": self.active_users,
            "created_at": self.created_at
        }

    def __repr__(self):
        return f"<Group {self.name} | Users: {len(self.active_users)}>"
