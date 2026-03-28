from flask import Flask
from src.Config.db import init_db
from src.routes import register_routes
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)

    # inicializando DB
    init_db(app)

    # registro das rotas
    register_routes(app)

    return app

app = create_app()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)