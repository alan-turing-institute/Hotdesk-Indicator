"""App module."""
from config import configs
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

bootstrap = Bootstrap()
db = SQLAlchemy()


def create_app(config_name):
    """Create Flask App instance."""
    app = Flask(__name__)
    app.config.from_object(configs[config_name])

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
