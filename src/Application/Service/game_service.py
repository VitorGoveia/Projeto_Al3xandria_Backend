import requests
from src.Config.db import db

from src.Infrastructure.Model.User_model import UserModel

from src.Infrastructure.Model.Game_model import GameModel
from src.Domain.Game import GameDomain

from src.Domain.UserGame import UserGameDomain
from src.Infrastructure.Model.UserGame_model import UserGameModel

key = 'e18914f7d42442ed93ccb77333915330'

class GameService:
    @staticmethod
    def get_slug_name(name):
        url = f'https://api.rawg.io/api/games?search={name}&key={key}&exclude_additions=true&parent_platforms=1,2,3,7,9,11&page_size=40'

        possible_matches = []
        results = requests.get(url).json()["results"]

        for item in results:
            if item["metacritic"] or item["added"] > 100:
                possible_matches.append({
                    "slug_name": item["slug"],
                    "name": item["name"],
                    "capa": item["background_image"]
                })
        
        return possible_matches
    
    @staticmethod
    def get_game_by_slug_name(slug_name):
        chosed_game = slug_name
        url = f'https://api.rawg.io/api/games/{chosed_game}?key={key}'
        response = requests.get(url).json()

        return {
            "nome": response["name"],
            "imagem": response["background_image"],
            "slug_name": response["slug"],
            "meta_score": response["metacritic"],
            "url_meta_score": response["metacritic_url"],
            "release_date": response["released"],
            "website": response["website"],
            "description": response["description_raw"],
            "rawg_id": response["id"]
        }

    @staticmethod
    def register_game(data):
        rawg_id = data["rawg_id"]
        game = GameModel.query.filter_by(rawg_id=rawg_id).first()
        if not game:
            new_game = GameDomain(rawg_id=rawg_id, nome=data["nome"], imagem=data["imagem"], slug_name=data["slug_name"], meta_score=data["meta_score"], url_meta_score=data["url_meta_score"], release_date=data["release_date"], website=data["website"], description=data["description"])

            game_register = GameModel(nome=new_game.nome, imagem=new_game.imagem, slug_name=new_game.slug_name, meta_score=new_game.meta_score, url_meta_score=new_game.url_meta_score, release_date=new_game.release_date, website=new_game.website, description=new_game.description, rawg_id=new_game.rawg_id)

            db.session.add(game_register)
            db.session.commit()
            return game_register.to_dict()
            
        else:
            return game.to_dict()
        
    @staticmethod
    def register_user_game(user_data, data):
        user_id = user_data["user_id"]
        user_rate = user_data["user_rate"] or 0
        user = UserModel.query.get(user_id)
        if not user:
            return {"Erro": "Usuário não encontrado", "code": 404}
        
        game = GameService.register_game(data)
        existing_relation = UserGameModel.query.filter_by(
            user_id=user_id,
            game_id=data["rawg_id"]
        ).first()

        if existing_relation:
            return {"Erro": "Jogo já está na sua biblioteca", "code": 400}
        
        user_game_object = {
            "user_id": user_id,
            "game_id": data["rawg_id"],
            "user_rate": user_rate
        }
        
        new_user_game = UserGameDomain(
            user_id, user_game_object["game_id"], user_rate
        )
        print(f"OBJETO:  {new_user_game}")

        new_user_game_bd = UserGameModel(
            user_id=new_user_game.user_id,
            game_id=new_user_game.game_id,
            user_rate=new_user_game.user_rate,
            status="library"
        )

        db.session.add(new_user_game_bd)
        db.session.commit()
        return new_user_game_bd