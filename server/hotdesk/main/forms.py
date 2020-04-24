"""Main app forms."""
from ..models import Desk
from datetime import datetime, timedelta
from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField, DateField, DateTimeField,
                     SelectField)
from wtforms.validators import DataRequired


def current_date():
    """Return the current date."""
    return datetime.now().date()


def current_time():
    """Return the current time."""
    return datetime.now()


def next_hour():
    """Return the current time plus one hour."""
    return datetime.now() + timedelta(hours=1)


class BookingForm(FlaskForm):
    """Desk booking form."""

    name = StringField('Name', validators=[DataRequired()])
    desk = SelectField('Desk', coerce=int, validators=[DataRequired()])
    date = DateField('Date', default=current_date,
                     validators=[DataRequired()])
    from_when = DateTimeField('From when', format="%H:%M",
                              default=current_time,
                              validators=[DataRequired()])
    until_when = DateTimeField('Until when', format="%H:%M",
                               default=next_hour,
                               validators=[DataRequired()])
    submit = SubmitField('Submit')

    def __init__(self):
        """Construct a :class:`BookingForm`."""
        super().__init__()

        # Get desk names from table
        self.desk.choices = [(desk.id, desk.name) for desk in Desk.query.all()]
