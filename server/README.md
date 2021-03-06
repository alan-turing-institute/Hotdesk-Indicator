# Hotdesk Indicator Server

## Installation

Install the Flask applications requirements using pip,

```
$ pip install -r requirement.txt
```

Configurations are described in [config.py](./config.py).

**Important:** In production the `SECRET_KEY` environment variable must be set
to a secret string of suitable length. Otherwise the "default" key, publicly
displayed, in [config.py](config.py) will be used.

To initiate the database use a Flask shell session with the appropriate
configuration,

```
$ FLASK_APP="hotdesk:create_app('<config>')" flask shell
...
>>> db.create_all()
>>> exit()
```

To run the app,

```
$ FLASK_APP="hotdesk:create_app('<config>')" flask run
```

If no configuration is specified, the "development" configuration will be used.
For example,

```
$ FLASK_APP=hotdesk flask run
```
