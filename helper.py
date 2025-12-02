import os
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from PIL import Image

DOWNLOADS = "downloads"
THUMBS = "thumbs"

os.makedirs(DOWNLOADS, exist_ok=True)
os.makedirs(THUMBS, exist_ok=True)

def get_metadata(file_path):
    parser = createParser(file_path)
    metadata = extractMetadata(parser)
    return metadata.exportDictionary() if metadata else {}

def save_thumbnail(image_bytes, user_id):
    path = os.path.join(THUMBS, f"{user_id}.jpg")
    with open(path, "wb") as f:
        f.write(image_bytes)
    return path
