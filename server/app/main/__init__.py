"""Main subapp."""
from flask import Blueprint

main = Blueprint("main", __name__)

from . import views, forms  # noqa: E402

__all__ = ["main", "views", "forms"]
