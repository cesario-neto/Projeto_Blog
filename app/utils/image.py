from django.conf import settings
from PIL import Image
from pathlib import Path


def resize_image(django_img: str, new_width: int,
                 optimize: bool = True, quality: int = 80):

    file_path = Path(settings.MEDIA_ROOT / django_img.name).resolve()

    img = Image.open(file_path)
    if img.width <= new_width:
        img.close()
        return

    new_height = (new_width * img.height) // img.width
    img.resize((new_height, new_height))
    img.save(file_path, 'png', optimize=optimize, quality=quality)
    return img
