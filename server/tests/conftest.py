"""pytest shared fixtures."""
import pytest
from hotdesk import create_app, db


@pytest.fixture
def app(tmp_path):
    """Create a testing instance of the app."""
    db_path = tmp_path / "data-test.sqlite"

    app = create_app({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///" + str(db_path)
        })

    with app.app_context():
        db.create_all()

    return app


@pytest.fixture
def client(app):
    """Create a test client."""
    return app.test_client()
