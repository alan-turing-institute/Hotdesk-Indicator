"""Main app views."""
from . import main
from .forms import BookingForm
from .. import db
from ..models import Booking, Desk
from datetime import datetime
from flask import render_template, redirect, url_for, flash


@main.route('/')
def index():
    """Index route."""
    return render_template('index.html')


@main.route('/book', methods=['GET', 'POST'])
def book():
    """Desk booking route."""
    form = BookingForm()
    if form.validate_on_submit():
        # Determine the begining and end of the booking as datetime objects
        date = form.date.data
        from_when = datetime.combine(date, form.from_when.data.time())
        until_when = datetime.combine(date, form.until_when.data.time())

        # Create a Booking objet
        booking = Booking(
            name=form.name.data,
            desk_id=form.desk.data,
            from_when=from_when,
            until_when=until_when
            )
        # Ensure the booking does not overlap with existing bookings
        bookings = Booking.query.filter_by(desk_id=form.desk.data).all()
        if any((booking.overlap(other) for other in bookings)):
            flash("Your request overlaps with an existing booking.")
            return render_template('book.html', form=form)
        else:
            db.session.add(booking)
            db.session.commit()
            flash('Your desk is booked!')
            return redirect(url_for('main.bookings'))
    return render_template('book.html', form=form)


@main.route('/bookings')
def bookings():
    """Route to show all bookings."""
    bookings = Booking.query.all()
    return render_template('bookings.html', bookings=bookings)


@main.route('/desks')
def desks():
    """Route to show all desks and their current status."""
    desks = Desk.query.all()
    return render_template('desks.html', desks=desks)
