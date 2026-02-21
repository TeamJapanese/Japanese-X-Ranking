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
