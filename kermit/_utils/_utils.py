from typing import Union
from pathlib import Path
from PIL import Image
from io import BytesIO
import base64
import requests
import re


def encode_image(image_path_or_pil: Union[Path, Image], encoding: str = "utf-8") -> str:
    """encode image from file or PIL.Image into base64"""
    if isinstance(image_path_or_pil, Image.Image):
        buffer = BytesIO()
        image_path_or_pil.save(buffer, format="JPEG")
        bytes_data = buffer.getvalue()
    else:
        if not image_path_or_pil.exists():
            raise FileNotFoundError(f"{image_path_or_pil} not exists")
        with open(str(image_path_or_pil), "rb") as image_file:
            bytes_data = image_file.read()
    return base64.b64encode(bytes_data).decode(encoding)


def decode_image(img_url_or_b64: str) -> Image:
    """decode image from url or base64 into PIL.Image"""
    if img_url_or_b64.startswith("http"):
        # image http(s) url

        resp = requests.get(img_url_or_b64)
        img = Image.open(BytesIO(resp.content))
    else:
        # image b64_json
        b64_data = re.sub("^data:image/.+;base64,", "", img_url_or_b64)
        img_data = BytesIO(base64.b64decode(b64_data))
        img = Image.open(img_data)
    return img
