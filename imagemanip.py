from io import BytesIO

from PIL import (
    Image,
    ImageOps,
    UnidentifiedImageError,
)


def bytes2image(image: bytes) -> Image.Image:
    if image.__sizeof__() > 10 * (2 ** 20):
        raise ValueError("Exceeds 10MB")
    try:
        io = BytesIO(image)
        io.seek(0)
        return Image.open(io)
    except UnidentifiedImageError:
        raise ValueError("Unable to use Image")


def image2bytes(img: Image.Image) -> BytesIO:
    image_bytes = BytesIO()
    img.save(image_bytes, format="png")  # type: ignore
    image_bytes.seek(0)
    return image_bytes


def invert(img_bytes: bytes):
    img: Image.Image = bytes2image(img_bytes).resize((400, 400), 1)
    img = img.convert("RGB")
    return image2bytes(ImageOps.invert(img))


def red(img_bytes: bytes):
    img = bytes2image(img_bytes)
    im = img.resize((400, 400), 1)
    w, h = im.size
    red = Image.new("RGBA", (w, h), color=(255, 0, 0, 120))
    im.paste(red, mask=red)
    return image2bytes(im)


def sad(img_bytes: bytes):
    img = bytes2image(img_bytes)
    im = img.resize((400, 400), 1)
    w, h = im.size
    raindrop = Image.open("assets/raindrops.png")
    raindrop = raindrop.convert("RGBA")
    darken = Image.new("RGBA", (w, h), color=(0, 0, 0, 100))
    im.paste(darken, mask=darken)
    im.paste(raindrop, mask=raindrop)
    return image2bytes(im)


def polaroid(img_bytes: bytes, fixed: bool = True):
    if fixed is True:
        w, h = (401, 401)
        img = bytes2image(img_bytes).resize((w, h), 1)
    else:
        img = bytes2image(img_bytes)
        w, h = img.size
    W, H = (w + 29, h + 29)
    blank = Image.new("RGBA", (W, H + 80), color=(255, 255, 255, 255))
    blank.paste(img, (round(round(W - w) / 2), round(round(H - h) / 2)))
    final = blank
    return image2bytes(final)
