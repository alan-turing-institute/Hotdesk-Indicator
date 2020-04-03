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
$ FLASK_APP=hotdesk.py FLASK_CONFIG=<config> flask shell
...
>>> db.create_all()
>>> exit()
```

To run the app,

```
$ FLASK_APP=hotdesk.py FLASK_CONFIG=<config> flask run
```
