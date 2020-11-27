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
    img = img.resize((400, 400), 1)
    if img.mode == "RGBA":
        r,g,b,a = img.split()
        rgb_img = Image.merge("RGB", (r,g,b))
        inverted = ImageOps.invert(rgb_img)
        r2,g2,b2 = inverted.split()
        final = Image.merge('RGBA', (r2,g2,b2,a))
    else:
        im = img.resize((400, 400), 1)
        final = ImageOps.invert(im)
    return save_image(final)

def red(img: bytes):
    img = bytes2image(img)
    im = img.resize((400, 400), 1)
    w, h = im.size
    red = Image.new("RGBA", (w, h), color=(255, 0, 0, 120))
    im.paste(red, mask=red)
    return save_image(im)

# img = Image.open("./TERM_010.png")
# red(img)
