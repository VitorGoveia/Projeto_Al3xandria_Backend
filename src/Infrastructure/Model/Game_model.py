from src.Config.db import db 

class GameModel(db.Model):
    __tablename__ = 'games'

    rawg_id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    imagem = db.Column(db.String(500), nullable=False)
    slug_name = db.Column(db.String(100), nullable=False)
    meta_score = db.Column(db.Integer, nullable=True)
    url_meta_score = db.Column(db.String(500), nullable=True)
    release_date = db.Column(db.String(15), nullable=True)
    website = db.Column(db.String(500), nullable=True)
    description = db.Column(db.String(50000), nullable=True)

    def to_dict(self):
        return {
            "nome": self.nome,
            "imagem": self.imagem,
            "slug_name": self.slug_name,
            "meta_score": self.meta_score,
            "url_meta_score": self.url_meta_score,
            "release_date": self.release_date,
            "website": self.website,
            "description": self.description,
            "rawg_id": self.rawg_id
        }