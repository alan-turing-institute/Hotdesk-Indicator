import argparse
from PIL import Image, ImageFont, ImageDraw
from inky import InkyPHAT
from font_source_sans_pro import SourceSansPro

COLOUR = "red"


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


def update_display(inky_display, status, desk_id, name=None):
    image = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
    draw = ImageDraw.Draw(image)

    status_font = ImageFont.truetype(SourceSansPro, 32)
    name_font = ImageFont.truetype(SourceSansPro, 24)

    # Status box
    if status == "taken":
        box_colour = inky_display.RED
        outline_colour = inky_display.WHITE
        font_colour = inky_display.WHITE
    elif status == "free":
        box_colour = inky_display.WHITE
        outline_colour = inky_display.RED
        font_colour = inky_display.RED

    draw.rectangle([(0, 0), (106, 52)], fill=box_colour, width=2,
                   outline=outline_colour)

    status_text = status.upper()
    status_w, status_h = status_font.getsize(status_text)
    x = (106 - status_w) // 2
    y = (52 - status_h) // 2
    draw.text((x, y), status_text, fill=font_colour, font=status_font)

    # ID box
    box_colour = inky_display.WHITE
    outline_colour = inky_display.RED
    font_colour = inky_display.RED

    draw.rectangle([(inky_display.width-106, 0), (inky_display.width-1, 52)],
                   fill=box_colour, width=2, outline=outline_colour)

    id_w, id_h = status_font.getsize(desk_id)
    x = inky_display.width - 106 // 2
    x -= id_w // 2
    y = (52 - id_h) // 2
    draw.text((x, y), desk_id, fill=font_colour, font=status_font)

    # Name box
    draw.rectangle([(0, 53), (inky_display.width-1, inky_display.height-1)],
                   fill=inky_display.WHITE, width=2, outline=inky_display.RED)
    if status == "taken":
        assert name is not None
        name_w, name_h = name_font.getsize(name)
        x = (inky_display.width - name_w) // 2
        y = inky_display.height - 53 // 2
        y -= name_h // 2
        draw.text((x, y), name, fill=inky_display.RED, font=name_font)

    # Send image to buffer
    inky_display.set_image(image)
    # Display image
    inky_display.show()


if __name__ == "__main__":
    main()
