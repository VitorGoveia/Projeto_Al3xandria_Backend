from flask import Flask
from src.Config.db import init_db
from src.routes import register_routes
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from src.Infrastructure.Auth.jwt_callbacks import register_jwt_callbacks
from datetime import timedelta, timezone
import os

def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": "*"}})

    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY", "30f081e5-461d-46f6-a318-b5d48f9552ac")
    app.config["JWT_ALGORITHM"] = "HS256"
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
    
    BRASILIA_TZ = timezone(timedelta(hours=-3))
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
    
    jwt = JWTManager(app)

    register_jwt_callbacks(jwt)

    # inicializando DB
    init_db(app)

    # registro das rotas
    register_routes(app)

    return app

app = create_app()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)