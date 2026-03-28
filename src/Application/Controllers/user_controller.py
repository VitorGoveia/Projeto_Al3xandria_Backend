from flask import request, jsonify, make_response
from src.Application.Service.user_service import UserService
from src.Infrastructure.Model.User_model import UserModel

class UserController:
    @staticmethod
    def register_user():
        """Cadastra o Usúario no DB"""
        data = request.get_json()

        dados_obrigatorios = ["nome", "email", "senha", "celular"]
        info_faltantes = dados_obrigatorios[:]
        for item in data:
            if item in dados_obrigatorios:
                info_faltantes.remove(item)
        
        if info_faltantes:
            return make_response(jsonify({"erro": f"Estão faltando os seguintes campos: {info_faltantes}"}), 400)
        
        if len(data) > len(dados_obrigatorios):
            return make_response(jsonify({"erro": f"Há campos à mais que o necessário, são necessários apenas os campos {dados_obrigatorios}"}), 400)
        
        if not '@' in data["email"] or not '.com' in data["email"]:
            return make_response(jsonify({"erro": "E-mail inválido"})), 400
        
        try:
            if int(data["celular"]) < 13:
                return make_response(jsonify({"erro": "Numero de celular invalido. Formato: 5511912345678"})), 400
            
        except:
            return make_response(jsonify({"erro": "Celular invalido. Por favor, insira somente caracteres numericos"})), 400

        user = UserService.create_user(data["nome"], data["email"], data["senha"], data["celular"])
        return make_response(jsonify({
            "mensagem": "User salvo com sucesso",
            "usuarios": user.to_dict()
        }), 200)    

    def get_users(user_id):
        "Busca todos os usuarios no DB"
        user = UserService.get_user(user_id)
        return {
            "Id": user.id,
            "Nome": user.nome,
            "E-mail": user.email,
            "Celular": user.celular,
            "Status": user.status
        }
      
    def update_user(user_id):
        data = request.get_json()
        update_user = UserService.update_user(user_id, data)

        if not update_user:
            return make_response(jsonify({"erro":"Usuário não encontrado!!!"}), 404)

        return jsonify ({
        "mensagem": "Usuário atualizado com sucesso!!!",
        "usuario": update_user.to_dict()
        })   
    
    def delete_user(user_id):
        sucess = UserService.delete_user(user_id)

        if not sucess:
            return make_response(jsonify({"erro":"Usuário não encontrado"}), 404)
        return jsonify({"mensagem": "Usuário inativado com sucesso!!!"})
 