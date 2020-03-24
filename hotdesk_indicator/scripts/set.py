"""Set desk status 'offline'."""
from ..desk import update_display
import argparse
from inky import InkyPHAT

COLOUR = "red"


def main():
    """Set desk status 'offline'."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--status", "-s", type=str, required=True, choices=["taken", "free"],
        help="The status of the desk, either 'taken' or 'free'"
        )
    parser.add_argument(
        "--desk-id", "-i", type=str, required=True,
        help="A unique identifier for the desk (used for booking)"
        )
    parser.add_argument(
        "--name", "-n", type=str, required=False,
        help="The name of the person who has reserved the desk"
        )
    parser.add_argument(
        "--until", "-u", type=str, required=False,
        help="The time when a desk is free until"
        )

    clargs = parser.parse_args()

    inky_display = InkyPHAT(COLOUR)

    update_display(inky_display, clargs.status, clargs.desk_id, clargs.name,
                   clargs.until)


if __name__ == "__main__":
    main()
