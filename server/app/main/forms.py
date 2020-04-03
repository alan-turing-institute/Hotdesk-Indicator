"""Main app forms."""
import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateTimeField, SelectField
from wtforms.validators import DataRequired


desks = [
    ('REG-07', 'REG-07'),
    ('REG-42', 'REG-42'),
]


class BookingForm(FlaskForm):
    """Desk booking form."""

    name = StringField('Name', validators=[DataRequired()])
    desk = SelectField('Desk', choices=desks, validators=[DataRequired()])
    from_when = DateTimeField('From when', format="%H:%M",
                              default=datetime.datetime.now(),
                              validators=[DataRequired()])
    until_when = DateTimeField('Until when', format="%H:%M",
                               default=datetime.datetime.now(),
                               validators=[DataRequired()])
    submit = SubmitField('Submit')
