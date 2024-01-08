import os
import pytesseract

from dotenv import load_dotenv


def extract_text(img):
    load_dotenv()

    tess_config = os.getenv("TESS_CONFIG", "--psm 11 --oem 3")

    img_data = pytesseract.image_to_data(img, config=tess_config, output_type=pytesseract.Output.DATAFRAME)

    img_conf_text = img_data[["conf", "text"]]
    img_valid = img_conf_text[img_conf_text["text"].notnull()]
    img_words = img_valid[img_valid["text"].str.len() > 1]

    extracted_text = img_words["text"].to_list()
    print(extracted_text)

    return extracted_text
