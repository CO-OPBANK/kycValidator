import re
from utils import format_image
from services import extract_text


def get_natid(img):

    fmtd_img = format_image(img)
    get_text = extract_text(fmtd_img)

    digit_pattern = '<[B8O0a]{2}(\d+)'
    extracted_idno = []

    for row in get_text:
        match = re.search(digit_pattern, row)
        if match:
            extracted_idno.append(match.group(1))

    print(extracted_idno)

    if not extracted_idno:
        return {"status": "error", "message": "Kindly retry"}

    serial_pattern = 'KYA(\d+)'
    extracted_serial = []

    for row in get_text:
        match = re.search(serial_pattern, row)
        if match:
            extracted_serial.append(match.group(1))

    print(extracted_serial)

    if not extracted_serial:
        return {"status": "error", "message": "Kindly retry"}

    return {"status": "success", "id_no": "" .join(extracted_idno), "serial_no": "" .join(extracted_serial)}
