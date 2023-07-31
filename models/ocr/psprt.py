from PIL import Image
import pytesseract
import cv2
import re
import numpy as np
import json
import csv
from io import StringIO


def psprt_recognizer(img, lang="eng"):
    """Process a PIL image."""
    # tmp_image = np.array(img)
    #
    # gray_img = get_grayscale(tmp_image)
    #
    # thresh = threshold(gray_img)
    #
    # noisy_img = remove_noise(thresh)
    #
    # new_image = Image.fromarray(noisy_img)
    #
    # custom_config = r'-l eng --oem 3 --psm 6'
    # extracted = pytesseract.image_to_string(img, config=custom_config)
    #

    # print(extracted)

    d = pytesseract.image_to_data(img)
    print(d)
    tsv_data = csv.DictReader(StringIO(d), delimiter='\t')
    d = [row for row in tsv_data]

    print("New Data")
    print(d)

    digit_pattern = '[A4]{1}(\d+)'
    
    extracted_text = []
    
    for row in d:
        print(float(row['conf']))
        match = re.search(digit_pattern, row['text'])
        print("Match")
        print(row['text'])
        print(match)
        if match:
            extracted_text.append("A" + match.group(1))
        # if int(float(row['conf'])) > 60:

    if isinstance(extracted_text, list):
        # extracted_text = extracted_text[-1]
        extracted_text = extracted_text[0]

    print(extracted_text)

    if not extracted_text:
        return {"status": "error", "message": "Kindly retry"}
    
    return {"status": "success", "message": "" .join(extracted_text)}