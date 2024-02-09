from PIL import Image


def resize_image(file_path: str, new_width: int,
                 optimize: bool = True, quality: int = 80):

    image = Image.open(file_path)
    new_height = (new_width * image.height) // image.width
    image.resize((new_height, new_height))
    image.save(file_path, 'png', optimize=True, quality=80)
    image.close()
