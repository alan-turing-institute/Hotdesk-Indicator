"""RESTful API subapp."""
from flask import Blueprint
from flask_restful import Api

api_blueprint = Blueprint("api", __name__)
api = Api(api_blueprint)

from . import resources  # noqa: E402

__all__ = ["api", "api_blueprint", "resources"]
