"""Functions for manipulating the hotdesk indicators display."""
from inky import InkyPHAT
from PIL import Image, ImageFont, ImageDraw
from font_source_sans_pro import SourceSansPro

BLACK = InkyPHAT.BLACK
WHITE = InkyPHAT.WHITE
RED = InkyPHAT.RED


def text_box(draw, coordinates, text, font, alert=False):
    """
    Write a text box to an image.

    :arg draw: Draw object for the PIL image to be written to the display.
    :type draw: :class:`PIL.ImageDraw.Draw`
    :arg coordinates: A tuple defining the bounds of the text box, in the
        format (top left x coordinate, top left y coordinate, bottom right x
        coordinate, bottom right y coordinate).
    :type coordinates: tuple(int, int, int, int)
    :arg font: Font to use.
    :type font: :class:`PIL.ImageFont.FreeTypeFont`
    :arg bool alert: If `True` the background of the text box is rendered in
        colour. Default is `False`.
    """
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
    """
    Update the indicators display according to its status.

    :arg inky_display: Display to update.
    :type inky_display: :class:`inky.InkypHAT`
    :arg str status: Desk status, one of 'taken' or 'free'.
    :arg str desk_id: Desk unique identifier.
    :arg str name: Name of the person who has booked the desk. Only used when
        status is 'taken'. Default is `None`.
    :arg str until: Time when the desk will no longer be free. Only used when
        status is 'free'. Default is `None`.
    """
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
