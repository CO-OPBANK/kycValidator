import base64
import io
import json
import logging
import sys
import uuid
from io import BytesIO
from typing import List

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from PIL import Image
from starlette.responses import Response

from ocr import natid_recognizer

# FastAPI
app = FastAPI(
    title="CO-OP Bank KYC Validator",
    description="""Visit port 8088/docs for the FastAPI documentation.""",
    version="0.0.1",
)

# Base64 Decoder
def base64_encode_img(img):
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    buffered.seek(0)
    img_byte = buffered.getvalue()
    encoded_img = "data:image/png;base64," + base64.b64encode(img_byte).decode()
    return encoded_img

@app.get("/")
async def root():
    return {"message": "CO-OP Bank KYC Validator"}

@app.post("/extract/idno")
def process_ocr(file: UploadFile = File(...)):
    file_bytes = file.file.read()
    image = Image.open(BytesIO(file_bytes))
    return natid_recognizer(image)

