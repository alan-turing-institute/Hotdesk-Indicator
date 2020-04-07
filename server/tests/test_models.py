"""Test SQLAlchemy models."""
from datetime import time
from hotdesk import db
from hotdesk.models import Desk, Booking
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
            desk = Desk.query.filter_by(name="DESK-01").first()

            db.session.delete(desk)

            desk = Desk.query.filter_by(name="DESK-01").first()
            assert desk is None
            desks = Desk.query.all()
            assert len(desks) == 2


class TestBookings():
    """Test the bookings model."""

    @pytest.mark.parametrize(
        "name", ["Harry Lime", "Kaiser Söze", "Sam Spade"]
        )
    def test_existing(self, app, name):
        """Ensure the bookings initialised in the app fixture are present."""
        with app.app_context():
            booking = Booking.query.filter_by(name=name).all()
            assert len(booking) == 1
            booking = booking[0]
            assert booking.name == name

    def test_size(self, app):
        """Ensure only the initialised bookings are present."""
        with app.app_context():
            bookings = Booking.query.all()
            assert len(bookings) == 3

    def test_add(self, app):
        """Test adding a booking."""
        with app.app_context():
            desk = Desk.query.filter_by(name="DESK-03").first()
            booking = Booking(
                name="Richard Hannay",
                from_when=time(10, 30),
                until_when=time(14, 15),
                desk=desk
                )

            db.session.add(booking)
            db.session.commit()

            bookings = Booking.query.all()
            assert len(bookings) == 4

            new_booking = (
                Booking.query.filter_by(name="Richard Hannay").first()
                )
            assert new_booking.name == "Richard Hannay"
            assert new_booking.from_when == time(10, 30)
            assert new_booking.until_when == time(14, 15)
            assert new_booking.desk == desk
            assert new_booking.desk_id == desk.id

    def test_remove(self, app):
        """Test removing a booking."""
        with app.app_context():
            booking = Booking.query.filter_by(name="Kaiser Söze").first()

            db.session.delete(booking)

            booking = Booking.query.filter_by(name="Kaiser Söze").first()
            assert booking is None
            bookings = Booking.query.all()
            assert len(bookings) == 2
