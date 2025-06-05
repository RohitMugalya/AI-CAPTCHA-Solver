"""
Basic CAPTCHA Generator
Generates simple readable CAPTCHA images for training data
"""

import os
import random
import string
from captcha.image import ImageCaptcha

# Configuration
NUM_CAPTCHAS = 200              # Total CAPTCHAs to generate
CAPTCHA_LENGTH = 6               # Characters per CAPTCHA
IMAGE_WIDTH = 300                # Image width in pixels
IMAGE_HEIGHT = 100               # Image height in pixels
OUTPUT_DIR = "../data/raw"       # Output directory
CHARACTER_SET = string.ascii_uppercase  # Characters to use

def generate_simple_captchas():
    """Generate clean, readable CAPTCHA images"""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    image_generator = ImageCaptcha(width=IMAGE_WIDTH, height=IMAGE_HEIGHT)
    
    for i in range(NUM_CAPTCHAS):
        # Generate random text
        text = ''.join(random.choices(CHARACTER_SET, k=CAPTCHA_LENGTH))
        
        # Generate and save image
        image = image_generator.generate_image(text)
        image.save(f"{OUTPUT_DIR}/{text}.png")
        
        # Print progress every 100 CAPTCHAs
        if (i+1) % 100 == 0:
            print(f"Generated {i+1}/{NUM_CAPTCHAS}")

    print(f"\nSuccessfully generated {NUM_CAPTCHAS} clean CAPTCHAs in {OUTPUT_DIR}")

if __name__ == "__main__":
    generate_simple_captchas()