"""App configuration."""
import os
import pathlib

base_dir = pathlib.Path(__file__).parent.absolute()


class Config(object):
    """App configuration base class."""

    SECRET_KEY = os.environ.get("SECRET_KEY") or "uxh)9l8;{P-us_&h>@q{u"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Development(Config):
    """Development configuration."""

    SQLALCHEMY_DATABASE_URI = "sqlite:///" + str(base_dir / "data.sqlite")


configs = {
    "development": Development,
    "default": Development
    }
