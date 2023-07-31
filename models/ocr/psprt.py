import re
from utils import format_image
from services import extract_text


def psprt_recognizer(img, lang="eng"):

    fmtd_img = format_image(img)

    get_text = extract_text(fmtd_img)

    print(get_text)

    digit_pattern = '[A4]{1}(\d+)'

    extracted_text = []

    for row in get_text:
        print(row)
        match = re.search(digit_pattern, row)
        if match:
            extracted_text.append("A" + match.group(1))

    if isinstance(extracted_text, list):
        extracted_text = extracted_text[0]

    print(extracted_text)

    if not extracted_text:
        return {"status": "error", "message": "Kindly retry"}
    
    return {"status": "success", "message": "" .join(extracted_text)}