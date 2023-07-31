import re
from utils import format_image
from services import extract_text


def get_servid(img):

    fmtd_img = format_image(img)

    get_text = extract_text(fmtd_img)

    print(get_text)