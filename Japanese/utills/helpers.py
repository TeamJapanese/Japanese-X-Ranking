"""MIT License"""

"""Copyright (c) 2026 [TeamJapanese](https://github.com/TeamJapanese)"""

"""Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:"""

"""The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software."""

"""THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""


from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import os
import random
from Japanese.utils.constants import (
    REWARD_MIN,
    REWARD_MAX,
)

# ===== BASE DIR =====
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ===== IMAGE FOLDER =====
IMG_DIR = os.path.join(BASE_DIR, "..", "..", "img")

# ===== FONT =====
FONT_PATH = os.path.join(BASE_DIR, "..", "..", "font", "Roboto-Regular.ttf")

# ===== WORD LIST =====
WORDS_POOL = [
    "WIN", "RUN", "GO", "TRY", "DO",
    "UP", "NOW", "MOVE", "PLAY", "FAST",
    "REAL", "TRUE", "SAFE", "NEXT",
    "POWER", "SMILE", "PEACE", "TRUST", "LIGHT",
    "HEART", "FOCUS", "BRAVE", "CALM", "LEVEL",
    "START", "RISE", "BUILD", "LEARN", "GROW",
    "BOOST", "ENERGY", "CONTROL",
    "SUCCESS", "RESPECT", "FUTURE", "PROGRESS",
    "VICTORY", "ACHIEVE", "BELIEVE", "BALANCE",
    "CONFIDENT", "COURAGE", "STABILITY",
    "POWERFUL", "MOTIVATE",
    "DISCIPLINE", "PATIENCE", "DETERMINED",
    "CONSISTENT", "FOCUSEDMIND",
    "SELFCONTROL", "PERFORMANCE",
    "TRANSFORM", "DEDICATION",
    "ACHIEVEMENT", "COMMITMENT",
    "DOMINATE", "UNSTOPPABLE", "LEGENDARY",
    "CHAMPION", "MASTER", "ELITE",
    "MAXIMUM", "UPGRADE"
]

def generate_challenge_image(word: str = None) -> BytesIO:
    if word is None:
        word = random.choice(WORDS_POOL)

    # ===== RANDOM BACKGROUND IMAGE =====
    images = [
        f for f in os.listdir(IMG_DIR)
        if f.startswith("japanese") and f.endswith(".png")
    ]

    if not images:
        raise FileNotFoundError("No japanese*.png images found in img folder.")

    BASE_IMAGE = os.path.join(IMG_DIR, random.choice(images))

    img = Image.open(BASE_IMAGE).convert("RGBA")
    draw = ImageDraw.Draw(img)
    W, H = img.size

    # ===== LOAD FONT =====
    font_size = 80
    try:
        if os.path.exists(FONT_PATH):
            font = ImageFont.truetype(FONT_PATH, font_size)
        else:
            raise OSError
    except OSError:
        font = ImageFont.load_default()
        print("⚠️ WARNING: Custom font missing, using default font")

    # ===== TEXT SIZE =====
    bbox = font.getbbox(word)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    x = (W - tw) // 2
    y = (H - th) // 2

    # ===== DRAW TEXT =====
    draw.text((x + 3, y + 3), word, font=font, fill=(0, 0, 0, 180))
    draw.text(
        (x, y),
        word,
        font=font,
        fill=(255, 255, 255, 255),
        stroke_width=5,
        stroke_fill=(0, 0, 0),
    )

    # ===== OUTPUT =====
    output = BytesIO()
    output.name = "challenge.png"
    img.save(output, format="PNG")
    output.seek(0)
    return output


def generate_reward() -> int:
    return random.randint(REWARD_MIN, REWARD_MAX)
