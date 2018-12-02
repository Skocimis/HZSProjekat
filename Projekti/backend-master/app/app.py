from flask import Flask
from flask_cors import CORS

from view import main_view


def create_app(debug=False):
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(main_view.teams)
    app.debug = debug

    return app


if __name__ == "__main__":
    app = create_app(debug=True)
    app.run(host='0.0.0.0')
