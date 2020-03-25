"""Flask RESTful API for hotdesk indicators."""
from collections import defaultdict
import datetime
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_restful import Resource, Api
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateTimeField, SelectField
from wtforms.validators import DataRequired

# Initial Flask app and extensions
app = Flask(__name__)
app.config['SECRET_KEY'] = 'xh)9l8;{P-us_&h>@q{u'
api = Api(app)
bootstrap = Bootstrap(app)


# Construct desk status dictionary
def default_desk_status():
    """Produce the default desk status entry."""
    status = {
        "status": "free",
        "name": None,
        "until": None
        }
    return status


desk_status = defaultdict(default_desk_status)
desk_status['REG-42'] = {
    "status": "taken",
    "name": "Kaiser Söze",
    "until": None
    }
desk_status['REG-07'] = {
    "status": "free",
    "name": "Kaiser Söze",
    "until": "14:00"
    }


# Desk status RESTful API
class DeskStatus(Resource):
    """Desk status RESTful resource."""

    def get(self, desk_id):
        """
        Handle a get request to the DeskStatus resource.

        This returns the current status of a desk.

        :arg str desk_id: The unique identifier of the desk whose status should
            be returned.

        :returns: The status of desk `desk_id`.
        :rtype: dict
        """
        return desk_status[desk_id]


api.add_resource(DeskStatus, '/<string:desk_id>')

# Forms
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


# Routes
@app.route('/')
def index():
    """Index route."""
    return render_template('index.html')


@app.route('/book', methods=['GET', 'POST'])
def book():
    """Desk booking route."""
    form = BookingForm()
    if form.validate_on_submit():
        name = form.name.data
        desk = form.desk.data
        from_when = form.from_when.data
        until_when = form.until_when.data
        print(name, desk, from_when, until_when)
        return render_template('index.html')
    return render_template('book.html', form=form)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
