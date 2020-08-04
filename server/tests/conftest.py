"""pytest shared fixtures."""
from datetime import datetime, time, timedelta
from hotdesk import create_app, db
from hotdesk.models import Desk, Booking
import pytest


@pytest.fixture(scope="session")
def today():
    """Today's date."""
    return datetime.now().date()


@pytest.fixture(scope="session")
def yesterday():
    """Yesterday's date."""
    return datetime.now().date() - timedelta(days=1)


@pytest.fixture
def app(tmp_path, yesterday):
    """Create a testing instance of the app."""
    db_path = tmp_path / "data-test.sqlite"

    app = create_app({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///" + str(db_path),
        "WTF_CSRF_ENABLED": False
        })

    with app.app_context():
        db.create_all()
        populate_database(db, yesterday)

    return app


@pytest.fixture
def client(app):
    """Create a test client."""
    return app.test_client()


def populate_database(db, date):
    """Add some entries to the database for testing."""
    desks = []
    desks.append(Desk(name="DESK-01"))
    desks.append(Desk(name="DESK-02"))
    desks.append(Desk(name="DESK-03"))

    bookings = []
    bookings.append(Booking(
        name="Harry Lime",
        from_when=datetime.combine(date, time(9, 0)),
        until_when=datetime.combine(date, time(17, 0)),
        desk=desks[0]
        ))
    bookings.append(Booking(
        name="Kaiser Söze",
        from_when=datetime.combine(date, time(9, 0)),
        until_when=datetime.combine(date, time(12, 0)),
        desk=desks[1]
        ))
    bookings.append(Booking(
        name="Sam Spade",
        from_when=datetime.combine(date, time(13, 0)),
        until_when=datetime.combine(date, time(16, 0)),
        desk=desks[1]
        ))

    db.session.add_all(desks+bookings)
    db.session.commit()
