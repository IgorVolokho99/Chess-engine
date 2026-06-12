from flask import Flask

from src.myapp.config import DevelopmentConfig
from src.myapp.container import bootstrap
from src.myapp.presentation.flask_app.blueprints.auth.views import auth_bp


def create_app(config_object: type = DevelopmentConfig) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_object)

    container = bootstrap(
        database_url=app.config["DATABASE_URL"]
    )

    app.extensions["use_cases"] = container.use_cases

    app.register_blueprint(auth_bp)

    return app
