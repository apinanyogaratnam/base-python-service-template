from flask_restful import Resource
import os
from api.types import BaseAPI


class Home(Resource):
    def __init__(self: "Home", base_api: BaseAPI) -> None:
        self.base_api = base_api

    def get(self: "Home") -> dict:
        return {"status": "OK", "pid": os.getpid(), "test": self.base_api.test}
