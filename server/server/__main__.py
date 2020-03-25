"""Flask RESTful API for hotdesk indicators."""
from collections import defaultdict
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
bootstrap = Bootstrap(app)


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


@app.route('/')
def index():
    """Index route."""
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
