import argparse
from PIL import Image, ImageFont, ImageDraw
from inky import InkyPHAT
from font_source_sans_pro import SourceSansPro

COLOUR = "red"
BLACK = InkyPHAT.BLACK
WHITE = InkyPHAT.WHITE
RED = InkyPHAT.RED


def main():
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

    clargs = parser.parse_args()

    inky_display = InkyPHAT(COLOUR)

    update_display(inky_display, clargs.status, clargs.desk_id, clargs.name)


def text_box(draw, coordinates, text, font, alert=False):
    if alert:
        box_colour = RED
        outline_colour = WHITE
        text_colour = WHITE
    else:
        box_colour = WHITE
        outline_colour = RED
        text_colour = RED

    # Draw text box
    draw.rectangle(coordinates, fill=box_colour, width=2,
                   outline=outline_colour)

    # Get dimensions of text
    text_width, text_height = font.getsize(text)

    # Determine the top left coordinate of text
    x0, y0, x1, y1 = coordinates
    # x = x0 + (x1-x0)//2 - text_width//2
    x = (x0+x1)//2 - text_width//2
    # y = y0 + (y1-y0)//2 - text_height//2
    y = (y0+y1)//2 - text_height//2
    draw.text((x, y), text, fill=text_colour, font=font)


def update_display(inky_display, status, desk_id, name=None):
    image = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
    draw = ImageDraw.Draw(image)

    status_font = ImageFont.truetype(SourceSansPro, 32)
    name_font = ImageFont.truetype(SourceSansPro, 24)

    # Status box
    if status == "taken":
        alert = True
    elif status == "free":
        alert = False
    text_box(draw, (0, 0, 106, 52), status.upper(), status_font, alert=alert)

    # ID box
    text_box(draw, (inky_display.width-106, 0, inky_display.width-1, 52),
             desk_id, status_font)

    # Name box
    text_box(draw, (0, 53, inky_display.width-1, inky_display.height-1),
             name, name_font)

    # Send image to buffer
    inky_display.set_image(image)
    # Display image
    inky_display.show()


if __name__ == "__main__":
    main()
