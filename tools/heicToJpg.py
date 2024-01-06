import os
from PIL import Image
import pyheif

def convert_heic_to_jpg(heic_path, jpg_path):
    heic_file = pyheif.read(heic_path)
    image = Image.frombytes(
        heic_file.mode, 
        heic_file.size, 
        heic_file.data,
        "raw",
        heic_file.mode,
        heic_file.stride,
    )
    
    image.save(jpg_path, "JPEG")

if __name__ == "__main__":
    heic_folder = "Images"
    jpg_folder = "JpgImages"

    for filename in os.listdir(heic_folder):
        if filename.endswith(".heic"):
            heic_path = os.path.join(heic_folder, filename)
            jpg_path = os.path.join(jpg_folder, os.path.splitext(filename)[0] + ".jpg")
            convert_heic_to_jpg(heic_path, jpg_path)
