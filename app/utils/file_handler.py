import os
import shutil
from fastapi import UploadFile

def save_image(image: UploadFile, folder: str = "images") -> str:
    os.makedirs(folder, exist_ok=True)

    file_path = os.path.join(folder, image.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)

    return image.filename