"""App module."""
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import os
import pathlib

bootstrap = Bootstrap()
db = SQLAlchemy()


def create_app(test_config=None):
    """Create Flask App instance."""
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY="uxh)9l8;{P-us_&h>@q{u",
        SQLALCHEMY_DATABASE_URI=(
            "sqlite:///" + os.path.join(app.instance_path, "data.sqlite")
            ),
        SQLALCHEMY_TRACK_MODIFICATIONS=False
        )

    pathlib.Path(app.instance_path).mkdir(exist_ok=True)

    if test_config:
        app.config.update(test_config)
    else:
        app.config.from_envvar("FLASK_CONFIG", silent=True)

    bootstrap.init_app(app)
    db.init_app(app)

    migrate = Migrate(app, db)  # noqa: F841

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .api import api_blueprint
    app.register_blueprint(api_blueprint)

    from .models import Desk, Booking
    @app.shell_context_processor
    def make_shell_context():
        """Create context for the `flask shell` session."""
        return dict(db=db, Desk=Desk, Booking=Booking)

    return app
