from flasgger import Swagger
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from src.db import Base
from src.db import engine
from src.models.mail_black_list import MailBlackList  # noqa
from src.routes import black_list_routes


def config_app(flask_app):
    flask_app.config["DEBUG"] = True
    flask_app.config["PROPAGATE_EXCEPTIONS"] = True
    flask_app.config["PRESERVE_CONTEXT_ON_EXCEPTION"] = False
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


app = Flask(__name__)
app.register_blueprint(black_list_routes.blueprint)
Swagger(app)
config_app(app)
CORS(app)
JWTManager(app)
Base.metadata.create_all(engine)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
