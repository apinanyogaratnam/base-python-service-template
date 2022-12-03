from flasgger import Swagger
from flask import Flask
from flask_restful import Api

from api.controllers import HealthCheck, Home


def create_app():
    app = Flask(__name__)
    api = Api(app)
    swagger = Swagger(app)

    app.config["SWAGGER"] = {
        "title": "Python Flask API",
    }

    # Initialize Config
    app.config.from_pyfile("../../config.py")

    # Register Resources
    api.add_resource(HealthCheck, "/healthcheck")
    api.add_resource(Home, "/")

    return app
