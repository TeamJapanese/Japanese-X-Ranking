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

class User:
    def __init__(self, user_id: int, name: str, coins: int = 0, points: int = 0):
        self.user_id = user_id
        self.name = name
        self.coins = coins
        self.points = points
        self.joined_at = datetime.utcnow()

    def add_points(self, points: int):
        self.points += points

    def add_coins(self, coins: int):
        self.coins += coins

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "name": self.name,
            "coins": self.coins,
            "points": self.points,
            "joined_at": self.joined_at
        }

    def __repr__(self):
        return f"<User {self.name} | Points: {self.points} | Coins: {self.coins}>"
