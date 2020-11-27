from io import BytesIO
from PIL import Image
from PIL import Image as PILImage
from PIL import ImageDraw, ImageEnhance, ImageFilter, ImageFont, ImageOps, ImageSequence, UnidentifiedImageError

class PILManip:
    @staticmethod
    def pil_image(image: bytes) -> Image:
        if image.__sizeof__() > 10 * (2 ** 20):
            raise ValueError("Exceeds 10MB")
        try:
            io = BytesIO(image)
            io.seek(0)
            return Image.open(io)
        except UnidentifiedImageError:
            raise ValueError("Unable to use Image")

    @staticmethod
    def pil_image_save(img: Image) -> BytesIO:
        image_bytes = BytesIO()
        img.save(image_bytes, format="png")
        image_bytes.seek(0)
        return image_bytes

def invert(img: bytes):
    img = PILManip.pil_image(img)
    im = img.resize((400, 400), 1)
    inverted = ImageOps.invert(im)
    return PILManip.pil_image_save(inverted)

def red(img: bytes):
    img = PILManip.pil_image(img)
    im = img.resize((400, 400), 1)
    red = Image.new("RGBA", (400, 400), color=(255, 0, 0, 120))
    im.paste(red, mask=red)
    return PILManip.pil_image_save(im)

# img = Image.open("./TERM_010.png")
# red(img)
