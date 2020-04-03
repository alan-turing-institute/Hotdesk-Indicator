"""App module."""
from config import configs
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

bootstrap = Bootstrap()
db = SQLAlchemy()


def create_app(config_name):
    """Create Flask App instance."""
    app = Flask(__name__)
    # app.config.from_object(configs[config_name])
    app.config.from_object(configs["default"])

    bootstrap.init_app(app)
    db.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .api import api_blueprint
    app.register_blueprint(api_blueprint)

    return app
