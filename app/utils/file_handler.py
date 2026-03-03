import os

def save_file(file_bytes: bytes, filename: str, folder: str = "images") -> str:
    os.makedirs(folder, exist_ok=True)

    file_path = os.path.join(folder, filename)

    with open(file_path, "wb") as f:
        f.write(file_bytes)

    return filename