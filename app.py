import os

from flask import Flask
from flask_smorest import Api
from flask_migrate import Migrate
from flask_cors import CORS

from db import db
import models

from resources.business import blp as BusinessBlueprint

from dotenv import load_dotenv


def create_app():
    app = Flask(__name__)
    CORS(app)
    load_dotenv()

    app.config["PROGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Business Registration API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "/https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MOFICATIONS"] = False
    db.init_app(app)
    migrate = Migrate(app, db)
    api = Api(app)


    api.register_blueprint(BusinessBlueprint)

    return app
