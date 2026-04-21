from flask import jsonify, make_response
from src.Application.Controllers.user_controller import UserController
from src.Application.Controllers.game_controller import GameController

def register_routes(app):
    @app.route('/api', methods=['GET'])
    def health():
        return make_response(jsonify({
            "mensagem": "API - OK; Docker - Up - Al3xandria",
        }), 200)

    @app.route('/user', methods=['POST'])
    def route_register_user():
        return UserController.register_user()

    @app.route('/user/<int:user_id>', methods=['GET'])
    def route_get_users(user_id):
        return UserController.get_users(user_id)

    @app.route('/user/<int:user_id>', methods=['PUT'])
    def route_update_user(user_id):
        return UserController.update_user(user_id)
 
    @app.route('/user/<int:user_id>', methods=['DELETE'])
    def route_delete_user(user_id):
        return UserController.delete_user(user_id)
 
#Login
    @app.route('/login', methods=['POST'])
    def route_login_user():
        return UserController.login_user()
    
#CadastroJogo
    @app.route('/slug_game/<string:name>', methods=['GET'])
    def route_get_slug_name(name):
        return GameController.get_slug_name(name)
    
    @app.route('/game/<string:name>', methods=['GET'])
    def route_get_game_by_slug_name(name):
        return GameController.get_game_by_slug_name(name)
    
    @app.route('/game', methods=['POST'])
    def route_post_register_game():
        return GameController.register_game()
    
    @app.route('/usergame', methods=['POST'])
    def route_register_user_game():
        retorno = GameController.register_user_game()
        return retorno["msg"], retorno["erro"]
    
    @app.route('/usergame/<int:user_id>', methods=["GET"])
    def get_games_by_user(user_id):
        return GameController.get_games_by_user_id(user_id)