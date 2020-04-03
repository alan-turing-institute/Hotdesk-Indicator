"""App launching script."""
from app import create_app, db
from app.models import Desk, Booking
from flask_migrate import Migrate
import os

app = create_app(os.environ.get("FLASK_CONFIG") or "default")
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    """Create context for the `flask shell` session."""
    return dict(db=db, Desk=Desk, Booking=Booking)
