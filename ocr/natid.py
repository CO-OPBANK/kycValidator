from PIL import Image
import pytesseract
import cv2
import re
import numpy as np
import json
import csv
from io import StringIO

def get_grayscale(img):
    tmp_image = np.array(img)
    return cv2.cvtColor(tmp_image, cv2.COLOR_BGR2GRAY)

# noise removal
def remove_noise(img):
    tmp_image = np.array(img)
    return cv2.medianBlur(tmp_image,5)

def threshold(img):
    return cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

def natid_recognizer(img, lang="eng"):
    """Process a PIL image."""
    gray_img = get_grayscale(img)

    thresh = threshold(gray_img)

    noisy_img = remove_noise(thresh)

    new_image = Image.fromarray(noisy_img)

    custom_config = r'-l eng --oem 3 --psm 6'
    extracted = pytesseract.image_to_string(img, config=custom_config)

    d = pytesseract.image_to_data(img)
    print(d)
    tsv_data = csv.DictReader(StringIO(d), delimiter='\t')
    d = [row for row in tsv_data]

    digit_pattern = '<[B8O0]{2}(\d+)'
    
    extracted_text = []
    
    for row in d:
        if int(float(row['conf'])) > 60:
            match = re.search(digit_pattern, row['text'])
            if match:
                extracted_text.append(match.group(1))
    
    if not extracted_text:
        return {"status": "error", "message": "Kindly retry"}
    
    return {"status": "success", "message": "" .join(extracted_text)}