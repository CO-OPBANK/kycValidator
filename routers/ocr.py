import base64
from io import BytesIO
import numpy as np
from fastapi import APIRouter, UploadFile, File
from PIL import Image

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
