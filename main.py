import os

from api.views import create_app

app = create_app()

if __name__ == "__main__":
    host = os.environ.get("FLASK_RUN_HOST")
    port = os.environ.get("FLASK_RUN_PORT")
    debug = os.environ.get("FLASK_DEBUG")
    app.run(host, port, debug=bool(debug))
