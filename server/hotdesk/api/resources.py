"""RESTful API resources."""
from . import api
from ..models import Desk
from flask_restful import Resource


@api.resource('/api/desk_status/<string:desk_id>')
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
        desk = Desk.query.get_or_404(desk_id)
        if desk.is_booked():
            booked = True
            active_booking = desk.active_booking()
            until = active_booking.until_when.strftime("%H:%M")
            by = active_booking.name
        else:
            booked = False
            until = "n/a"
            by = "n/a"

        return {
            "name": desk.name,
            "booked": booked,
            "by": by,
            "until": until
            }
