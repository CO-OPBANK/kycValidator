from PIL import Image
import pytesseract
import cv2
import re
import numpy as np
import json
import csv
from io import StringIO

from utils import get_grayscale
from utils import remove_noise
from utils import threshold

def natid_recognizer(img, lang="eng"):
    """Process a PIL image."""
    
    tmp_image = np.array(img)
    
    gray_img = get_grayscale(tmp_image)

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