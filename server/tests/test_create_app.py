"""Test the app factory."""
from hotdesk import create_app


def test_test_config(app):
    """Test the default app created by the app fixture."""
    assert app.config["TESTING"] is True
    assert "data-test.sqlite" in app.config["SQLALCHEMY_DATABASE_URI"]
    assert app.config["SECRET_KEY"] == "uxh)9l8;{P-us_&h>@q{u"


def test_env_var(tmp_path, monkeypatch):
    """
    Test creating an app using a configuration file.

    This includes testing overwriting the default variables.
    """
    config_path = tmp_path / "config.py"
    monkeypatch.setenv("FLASK_CONFIG", str(config_path))

    db_path = tmp_path / "data-test-env.sqlite"

    with open(config_path, "w") as config:
        config.writelines([
            "TESTING = True\n",
            f"SQLALCHEMY_DATABASE_URI = 'sqlite:///' + '{str(db_path)}'\n"
            ])

    app = create_app()

    assert app.config["TESTING"] is True
    assert "data-test-env.sqlite" in app.config["SQLALCHEMY_DATABASE_URI"]
    assert app.config["SECRET_KEY"] == "uxh)9l8;{P-us_&h>@q{u"
