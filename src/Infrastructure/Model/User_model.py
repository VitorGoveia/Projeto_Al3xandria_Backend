from src.Config.db import db 

class UserModel(db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    celular = db.Column(db.String(14), nullable=False)
    senha = db.Column(db.String(16), nullable=False)
    status = db.Column(db.String(10), nullable=False, default='Ativo')

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "password": self.senha,
            "phone": self.celular,
        }