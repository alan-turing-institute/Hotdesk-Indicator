"""RESTful API resources."""
from . import api
from collections import defaultdict
from flask_restful import Resource


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


api.add_resource(DeskStatus, '/api/get/<string:desk_id>')
