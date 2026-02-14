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
