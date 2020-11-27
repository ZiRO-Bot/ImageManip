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
    img = bytes2image(img).resize((400, 400), 1)
    img = img.convert("RGB")
    return save_image(ImageOps.invert(img))

def red(img: bytes):
    img = bytes2image(img)
    im = img.resize((400, 400), 1)
    w, h = im.size
    red = Image.new("RGBA", (w, h), color=(255, 0, 0, 120))
    im.paste(red, mask=red)
    return save_image(im)

def polaroid(img: bytes, fixed: bool=True):
    if fixed is True:
        w, h = (401, 401)
        img = bytes2image(img).resize((w, h), 1)
    else:
        img = bytes2image(img)
        w, h = img.size
    W, H = (w+29, h+29)
    blank = Image.new("RGBA", (W, H+80), color=(255,255,255,255))
    blank.paste(img, (round(round(W-w)/2),round(round(H-h)/2)))
    final = blank
    return save_image(final)

# img = Image.open("./TERM_010.png")
# red(img)
