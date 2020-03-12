from inky import InkyPHAT
from PIL import Image, ImageFont, ImageDraw
from font_source_sans_pro import SourceSansPro

BLACK = InkyPHAT.BLACK
WHITE = InkyPHAT.WHITE
RED = InkyPHAT.RED


def text_box(draw, coordinates, text, font, alert=False):
    if alert:
        box_colour = RED
        outline_colour = BLACK
        text_colour = WHITE
    else:
        box_colour = WHITE
        outline_colour = BLACK
        text_colour = BLACK

    # Draw text box
    draw.rectangle(coordinates, fill=box_colour, width=1,
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


def update_display(inky_display, status, desk_id, name=None, until=None):
    image = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
    draw = ImageDraw.Draw(image)

    status_font = ImageFont.truetype(SourceSansPro, 32)
    info_font = ImageFont.truetype(SourceSansPro, 24)

    # Status box
    if status == "taken":
        alert = True
    elif status == "free":
        alert = False
    text_box(draw, (0, 0, 106, 52), status.upper(), status_font, alert=alert)

    # ID box
    text_box(draw, (inky_display.width-106, 0, inky_display.width-1, 52),
             desk_id, status_font)

    # Information box
    if status == "taken":
        info = name
    elif status == "free":
        if until is None:
            info = ""
        else:
            info = f"Free until: {until}"
    if info is None:
        info = ""
    text_box(draw, (0, 53, inky_display.width-1, inky_display.height-1),
             info, info_font)

    # Send image to buffer
    inky_display.set_image(image)
    # Display image
    inky_display.show()
