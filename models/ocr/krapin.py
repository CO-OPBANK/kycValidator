import re
import pdf2image
from services import extract_text


def get_krapin(img):

    images = pdf2image.convert_from_bytes(img)
    image = images[0]

    get_text = extract_text(image)

    digit_pattern = 'A(?P<id>\d{9}[A-Z])'
    extracted_text = []

    for row in get_text:
        match = re.search(digit_pattern, row)
        if match:
            extracted_text.append("A" + match.group(1))

    print(extracted_text)

    if not extracted_text:
        return {"status": "error", "message": "Kindly retry"}

    return {"status": "success", "message": "" .join(extracted_text)}
