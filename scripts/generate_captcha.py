import os
import random
import string
from captcha.image import ImageCaptcha

NUM_CAPTCHAS = 100
CAPTCHA_LENGTH = 6
IMAGE_WIDTH = 300
IMAGE_HEIGHT = 100
OUTPUT_DIR = "../data/raw"
CHARACTER_SET = string.ascii_uppercase

os.makedirs(OUTPUT_DIR, exist_ok=True)
image_generator = ImageCaptcha(width=IMAGE_WIDTH, height=IMAGE_HEIGHT)

for i in range(NUM_CAPTCHAS):
    text = ''.join(random.choices(CHARACTER_SET, k=CAPTCHA_LENGTH))
    image = image_generator.generate_image(text)
    image.save(f"{OUTPUT_DIR}/{text}.png")

print(f"Generated {NUM_CAPTCHAS} CAPTCHAs")