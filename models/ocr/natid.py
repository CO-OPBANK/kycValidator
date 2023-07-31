import re
from utils import format_image
from services import extract_text


def get_natid(img):

    fmtd_img = format_image(img)
    get_text = extract_text(fmtd_img)

    digit_pattern = '<[B8O0a]{2}(\d+)'
    extracted_text = []

    for row in get_text:
        print(row)
        match = re.search(digit_pattern, row)
        if match:
            extracted_text.append(match.group(1))

    print(extracted_text)

    if not extracted_text:
        return {"status": "error", "message": "Kindly retry"}

    return {"status": "success", "message": "".join(extracted_text)}
