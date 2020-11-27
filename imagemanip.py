from io import BytesIO
from PIL import Image
from PIL import Image as PILImage
from PIL import ImageDraw, ImageEnhance, ImageFilter, ImageFont, ImageOps, ImageSequence, UnidentifiedImageError

def bytes2image(image: bytes) -> Image:
    if image.__sizeof__() > 10 * (2 ** 20):
        raise ValueError("Exceeds 10MB")
    try:
        io = BytesIO(image)
        io.seek(0)
        return Image.open(io)
    except UnidentifiedImageError:
        raise ValueError("Unable to use Image")

def save_image(img: Image) -> BytesIO:
    image_bytes = BytesIO()
    img.save(image_bytes, format="png")
    image_bytes.seek(0)
    return image_bytes

def invert(img: bytes):
    img = bytes2image(img)
    im = img.resize((400, 400), 1)
    inverted = ImageOps.invert(im)
    return save_image(im)

def red(img: bytes):
    img = bytes2image(img)
    im = img.resize((400, 400), 1)
    red = Image.new("RGBA", (400, 400), color=(255, 0, 0, 120))
    im.paste(red, mask=red)
    return save_image(im)

# img = Image.open("./TERM_010.png")
# red(img)
