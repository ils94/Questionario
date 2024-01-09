import base64
from PIL import Image
from io import BytesIO


def is_valid_image(base64_string):
    try:
        decoded_data = base64.b64decode(base64_string)
        image = Image.open(BytesIO(decoded_data))
        image.verify()
        return True
    except:
        return False
