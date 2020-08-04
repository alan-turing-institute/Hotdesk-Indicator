"""Model (databate table) definitions."""
from . import db
import datetime


class Desk(db.Model):
    """Desk model."""

    __tablename__ = 'desks'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(6), unique=True)
    # One to many relationship to bookings
    bookings = db.relationship('Booking', backref='desk', lazy='dynamic')

    def is_booked(self):
        """Find if a desk is currently booked."""
        if any((booking.is_active() for booking in self.bookings)):
            return True
        else:
            return False

    def active_booking(self):
        """Return the active booking for this desk if there is one."""
        for booking in self.bookings:
            if booking.is_active():
                return booking

        return None


class Booking(db.Model):
    """Booking model."""

    __tablename__ = 'bookings'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=False)
    from_when = db.Column(db.DateTime, unique=False)
    until_when = db.Column(db.DateTime, unique=False)
    desk_id = db.Column(db.Integer, db.ForeignKey('desks.id'))

    def is_active(self):
        """Find if a booking is currently active."""
        current_time = datetime.datetime.now()
        active = (
            current_time >= self.from_when and current_time < self.until_when
            )
        return active

    def overlap(self, other):
        """
        Test if two bookings overlap.

        :arg other: The booking to test against.
        :type other: :class:`Booking`

        :returns: `True` if the two bookings conflict, `False` otherwise.
        :rtype: bool
        """
        # If other begins after self beings, but also begins before self ends
        if self.from_when <= other.from_when:
            if other.from_when < self.until_when:
                return True

        # Vice versa
        if other.from_when <= self.from_when:
            if self.from_when < other.until_when:
                return True

        return False
