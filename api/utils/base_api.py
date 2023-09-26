import os
from postgres_database_utils import create_connection, PostgresCredentials


class BaseAPI():
    def __init__(self) -> None:
        host = os.environ.get('DATABASE_HOST')
        name = os.environ.get('DATABASE_NAME')
        user = os.environ.get('DATABASE_USER')
        password = os.environ.get('DATABASE_PASSWORD')
        credentials = PostgresCredentials(host=host, database=name, user=user, password=password)
        self.connection = create_connection(credentials)
        self.test = "test"
