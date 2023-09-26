from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from api.controllers import HealthCheck, Home
from api.utils.base_api import BaseAPI


def create_app():
    app = Flask(__name__)
    api = Api(app)
    CORS(app)

    base_api = BaseAPI()

    # Initialize Config
    app.config.from_pyfile("../../config.py")

    # Register Resources
    api.add_resource(HealthCheck, "/healthcheck")
    api.add_resource(Home, "/", resource_class_kwargs={'base_api': base_api})

    return app
