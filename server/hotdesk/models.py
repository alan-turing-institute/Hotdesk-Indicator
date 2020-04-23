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


class Booking(db.Model):
    """Booking model."""

    __tablename__ = 'bookings'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=False)
    from_when = db.Column(db.Time, unique=False)
    until_when = db.Column(db.Time, unique=False)
    desk_id = db.Column(db.Integer, db.ForeignKey('desks.id'))

    def is_active(self):
        """Find if a booking is currently active."""
        current_time = datetime.datetime.now().time()
        active = (
            current_time >= self.from_when and current_time < self.until_when
            )
        return active
