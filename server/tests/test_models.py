"""Test SQLAlchemy models."""
from hotdesk import db
from hotdesk.models import Desk
import pytest


class TestDesks():
    """Test the Desk model."""

    @pytest.mark.parametrize("desk_name", ["DESK-01", "DESK-02", "DESK-03"])
    def test_existing(self, app, desk_name):
        """Ensure the desks initialised in the app fixture are present."""
        with app.app_context():
            desk = Desk.query.filter_by(name=desk_name).all()
            assert len(desk) == 1
            assert desk[0].name == desk_name

    def test_size(self, app):
        """Ensure only the initialised desks are present."""
        with app.app_context():
            desks = Desk.query.all()
            assert len(desks) == 3

    def test_add(self, app):
        """Test adding a new desk."""
        with app.app_context():
            desk = Desk(name="TEST_DESK")
            db.session.add(desk)
            db.session.commit()

            desks = Desk.query.all()
            assert len(desks) == 4

            new_desk = Desk.query.filter_by(name="TEST_DESK").first()
            assert new_desk.name == "TEST_DESK"

    def test_remove(self, app):
        """Test removing a desk."""
        with app.app_context():
            desk = Desk(name="TEST_DESK")
            db.session.add(desk)
            db.session.commit()

            desks = Desk.query.all()
            assert len(desks) == 4

            db.session.delete(desk)

            new_desk = Desk.query.filter_by(name="TEST_DESK").first()
            assert new_desk is None
            desks = Desk.query.all()
            assert len(desks) == 3
