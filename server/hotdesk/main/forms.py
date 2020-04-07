"""Main app forms."""
from ..models import Desk
import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateTimeField, SelectField
from wtforms.validators import DataRequired


class BookingForm(FlaskForm):
    """Desk booking form."""

    name = StringField('Name', validators=[DataRequired()])
    desk = SelectField('Desk', coerce=int, validators=[DataRequired()])
    from_when = DateTimeField('From when', format="%H:%M",
                              default=datetime.datetime.now(),
                              validators=[DataRequired()])
    until_when = DateTimeField('Until when', format="%H:%M",
                               default=datetime.datetime.now(),
                               validators=[DataRequired()])
    submit = SubmitField('Submit')

    def __init__(self):
        """Construct a :class:`BookingForm`."""
        super().__init__()

        # Get desk names from table
        self.desk.choices = [(desk.id, desk.name) for desk in Desk.query.all()]
