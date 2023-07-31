import base64
from io import BytesIO
import numpy as np
from fastapi import APIRouter, UploadFile, File
from PIL import Image

from models import natid_recognizer
from models import psprt_recognizer

router = APIRouter(
    prefix="/ocr/extract",
    tags=["ocr"],
)


@router.post("/idno")
async def process_ocr(file: UploadFile = File(...)):
    file_bytes = file.file.read()
    image = np.frombuffer(file_bytes, np.uint8)
    return natid_recognizer(image)


@router.post("/psprt")
async def process_ocr(file: UploadFile = File(...)):
    file_bytes = file.file.read()
    image = np.frombuffer(file_bytes, np.uint8)
    return psprt_recognizer(image)
