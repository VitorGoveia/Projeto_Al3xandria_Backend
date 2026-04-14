from src.Application.Service.game_service import GameService
from flask import request, jsonify, make_response


class GameController:
    @staticmethod
    def get_slug_name(name):
        return GameService.get_slug_name(name)
    

    @staticmethod
    def get_game_by_slug_name(slug_name):
        return GameService.get_game_by_slug_name(slug_name)


    @staticmethod
    def register_game():
        data = request.get_json()
        jogo = GameService.register_game(data)
        return make_response(jsonify({
            "mensagem": "Jogo salvo com sucesso",
            "usuarios": jogo
        }), 200)
    
    @staticmethod
    def register_user_game():
        data = request.get_json()
        user_data = data["user_data"]
        game_data = data["game_data"]

        return GameService.register_user_game(user_data, game_data)

