from ..desk import update_display
import argparse
from inky import InkyPHAT
import requests

COLOUR = "red"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--desk-id", "-i", type=str, required=True,
        help="Desk unique identifier"
        )
    parser.add_argument(
        "--url", "-u", type=str, default="http://127.0.0.1:5000",
        help="URL of the REST API, from where statuses are obtained"
        )

    clargs = parser.parse_args()

    inky_display = InkyPHAT(COLOUR)

    status = requests.get("/".join([clargs.url, clargs.desk_id])).json()

    update_display(inky_display, status["status"], clargs.desk_id,
                   name=status["name"], until=status["until"])
