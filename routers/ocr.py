import base64
from io import BytesIO
import numpy as np
from fastapi import APIRouter, UploadFile, File
from PIL import Image
import tensorflow as tf
import json

from models import get_natid
from models import get_psprt
from models import get_servid
from models import get_krapin

router = APIRouter(
    prefix="/ocr/extract",
    tags=["ocr"],
)


@router.post("/idno")
async def process_ocr(img: dict):
    image_bytes = base64.b64decode(img["img"])
    image = np.frombuffer(image_bytes, np.uint8)
    return get_natid(image)


@router.post("/psprt")
async def process_ocr(img: dict):
    image_bytes = base64.b64decode(img["img"])
    image = np.frombuffer(image_bytes, np.uint8)
    return get_psprt(image)


@router.post("/servid")
async def process_ocr(img: dict):
    image_bytes = base64.b64decode(img["img"])
    image = np.frombuffer(image_bytes, np.uint8)
    return get_servid(image)


@router.post("/krapin")
def extract_data(img: dict):
    image = base64.b64decode(img["img"])
    return get_krapin(image)


# def load_model():
#     model = tf.keras.models.load_model('path/to/your/model')
#     return model
#
#
# face_model = load_model()


# def process_image(image_str):
#     # Convert the base64-encoded image to a numpy array
#     image = Image.open(BytesIO(base64.b64decode(image_str)))
#     image = np.array(image)
#
#     # Preprocess the image (resize, normalize, etc.) to match the model's input shape
#     # Modify the preprocessing based on the requirements of your face recognition model
#     image = tf.image.resize(image, [224, 224])
#     image = image / 255.0  # Normalize the image to values between 0 and 1
#
#     return image


# @router.post("/face_comparison")
# async def face_comparison(data: dict):
#     # print(data["data"][0])
#
#     # return data["data"]
#
#     image1_bytes = base64.b64decode(data["data"][0]["image1"])
#     image2_bytes = base64.b64decode(data["data"][1]["image2"])
#
#     image1 = tf.image.decode_image(image1_bytes)
#     image2 = tf.image.decode_image(image2_bytes)
#
#     features1 = tf.face.face_encodings(image1)
#     features2 = tf.face.face_encodings(image2)
#
#     comparison_results = tf.math.reduce_mean(tf.math.squared_difference(features1, features2))
#
#     compatibility_score = 100 - comparison_results
#
#     return {"compatibility_score": compatibility_score}
