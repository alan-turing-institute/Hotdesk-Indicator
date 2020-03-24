"""Flask RESTful API for hotdesk indicators."""
from collections import defaultdict
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


def default_desk_status():
    """Produce the default desk status entry."""
    status = {
        "status": "free",
        "name": None,
        "until": None
        }
    return status


desk_status = defaultdict(default_desk_status)


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

if __name__ == '__main__':
    app.run(debug=True)
