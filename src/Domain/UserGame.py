class UserGameDomain:
    def __init__(self, user_id, game_id, user_rate=0, added_at=None, status="library"):
        self.user_id = user_id
        self.game_id = game_id
        self.added_at = added_at
        self.status = status
        self.user_rate = user_rate
    
    def to_dict(self):
        return {
            "user_id": self.user_id,
            "game_id": self.game_id,
            "added_at": self.added_at,
            "status": self.status,
            "user_rate": self.user_rate
        }