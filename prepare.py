import os
from PIL import Image

def compress_image(file_path, quality=75):
    """
    Compresses an image and saves it to the same file path.

    :param file_path: The file path of the image to compress
    :param quality: The quality of compression (default is 75)
    """
    image = Image.open(file_path)
    image.save(file_path, 'JPEG', quality=quality, optimize=True)

def compress_images_in_folder(folder_path, file_type="JPEG", quality=75):
    """
    Compresses all images in a folder and its subdirectories.

    :param folder_path: The path of the folder to search for images
    :param file_type: The file type of the images to compress (default is JPEG)
    :param quality: The quality of compression (default is 75)
    """
    for root, _, files in os.walk(folder_path):
        for f in files:
            if f.endswith(file_type):
                file_path = os.path.join(root, f)
                compress_image(file_path, quality)
                print(f"Compressed {file_path} to {quality}%")

compress_images_in_folder('arctus/static/assets')
