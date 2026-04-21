from src.Config.db import db 
from datetime import datetime, timezone

class UserGameModel(db.Model):
    __tablename__ = 'user_games'
    
    user_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('games.rawg_id'), primary_key=True)

    added_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    status = db.Column(db.String(100), nullable=False)
    user_rate = db.Column(db.Integer, nullable=False, default=0)

    user = db.relationship("UserModel", backref="user_games")
    game = db.relationship("GameModel", backref="user_games")


    def to_dict(self):
        return {
            "user_id": self.user_id,
            "game_id": self.game_id,
            "added_at": self.added_at,
            "status": self.status,
            "user_rate": self.user_rate
        }