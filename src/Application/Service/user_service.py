# Aqui seria para cirar o usuario e já colocar a informação dele no banco de dados

from src.Config.db import db
from src.Infrastructure.Model.User_model import UserModel
from src.Domain.User import UserDomain


class UserService:
    @staticmethod
    def create_user(nome, email, senha, celular):
        new_user = UserDomain(nome, email, senha, celular)
        user = UserModel(nome=new_user.nome, email=new_user.email,
                         senha=new_user.senha, celular=new_user.celular)
        user.to_dict()
        db.session.add(user)
        db.session.commit()
        return user

    def get_user(user_id):
        user = UserModel.query.get(user_id)
        if not user:
            return {"Erro": "Usuário não encontrado"}
        return user

    @staticmethod
    def update_user(user_id, data):
        user = UserModel.query.get(user_id)
        if not user:
            return None

        user.nome = data.get("nome", user.nome)
        user.email = data.get("email", user.email)
        user.celular = data.get("celular", user.celular)
        user.senha = data.get("senha", user.senha)
        user.status = data.get("status", user.status)

        db.session.commit()
        return user

    @staticmethod
    def delete_user(user_id):
        user = UserModel.query.get(user_id)
        if not user:
            return False

        user.status = "Inativo"

        db.session.commit()
        return True

    @staticmethod
    def _validar_dados_obrigatorios(data, campos_obrigatorios):
        campos_faltantes = [
            campo for campo in campos_obrigatorios if campo not in data]
        if campos_faltantes:
            return False, {"erro": f"Campos obrigatórios faltando: {campos_faltantes}"}, 400
        return True, None, None

    @staticmethod
    def login_user(**credentials):
        try:
            campos_obrigatorios = ["email", "password"]
            valido, erro, status = UserService._validar_dados_obrigatorios(
                credentials, campos_obrigatorios)
            if not valido:
                return erro, status

            user = UserModel.query.filter_by(
                email=credentials["email"]).first()

            if not user:
                return {"erro": "Email ou senha inválidos"}, 401

            if user.status != "Ativo":
                return {"erro": "Usuário inativo/não existe."}, 403

            return user, 200

        except Exception as e:
            raise e
