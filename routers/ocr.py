import base64
from io import BytesIO
import numpy as np
from fastapi import APIRouter, UploadFile, File
from PIL import Image

from models import get_natid
from models import get_psprt
from models import get_servid

router = APIRouter(
    prefix="/ocr/extract",
    tags=["ocr"],
)


@router.post("/idno")
async def process_ocr(file: UploadFile = File(...)):
    file_bytes = file.file.read()
    image = np.frombuffer(file_bytes, np.uint8)
    return get_natid(image)


@router.post("/psprt")
async def process_ocr(file: UploadFile = File(...)):
    file_bytes = file.file.read()
    image = np.frombuffer(file_bytes, np.uint8)
    return get_psprt(image)


@router.post("/servid")
async def process_ocr(file: UploadFile = File(...)):
    file_bytes = file.file.read()
    image = np.frombuffer(file_bytes, np.uint8)
    return get_servid(image)
