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

# ===== IMAGE =====
BASE_IMAGE = os.path.join(BASE_DIR, "..", "..", "img", "japanese.png")

# ===== FONT =====
FONT_PATH = os.path.join(BASE_DIR, "..", "..", "font", "Roboto-Regular.ttf")

# ===== WORD LIST =====
WORDS_POOL = [
    # 🔹 Very short (3–4 letters) – ultra fast rounds
    "WIN", "RUN", "GO", "TRY", "DO",
    "UP", "NOW", "MOVE", "PLAY", "FAST",
    "REAL", "TRUE", "SAFE", "NEXT",

    # 🔹 Short (5–6 letters) – balanced speed
    "POWER", "SMILE", "PEACE", "TRUST", "LIGHT",
    "HEART", "FOCUS", "BRAVE", "CALM", "LEVEL",
    "START", "RISE", "BUILD", "LEARN", "GROW",
    "BOOST", "ENERGY", "CONTROL",

    # 🔹 Medium (7–8 letters) – skill based
    "SUCCESS", "RESPECT", "FUTURE", "PROGRESS",
    "VICTORY", "ACHIEVE", "BELIEVE", "BALANCE",
    "CONFIDENT", "COURAGE", "STABILITY",
    "POWERFUL", "MOTIVATE",

    # 🔹 Long (9–12 letters) – high difficulty rounds
    "DISCIPLINE", "PATIENCE", "DETERMINED",
    "CONSISTENT", "FOCUSEDMIND",
    "SELFCONTROL", "PERFORMANCE",
    "TRANSFORM", "DEDICATION",
    "ACHIEVEMENT", "COMMITMENT",

    # 🔹 Bonus motivational words (fun & rewarding)
    "DOMINATE", "UNSTOPPABLE", "LEGENDARY",
    "CHAMPION", "MASTER", "ELITE",
    "MAXIMUM", "UPGRADE"
]

def generate_challenge_image(word: str = None) -> BytesIO:
    if word is None:
        word = random.choice(WORDS_POOL)

    # ===== LOAD IMAGE =====
    if not os.path.exists(BASE_IMAGE):
        raise FileNotFoundError(f"Background image not found: {BASE_IMAGE}")
    img = Image.open(BASE_IMAGE).convert("RGBA")
    draw = ImageDraw.Draw(img)
    W, H = img.size

    # ===== LOAD FONT SAFELY =====
    font_size = 80
    try:
        if os.path.exists(FONT_PATH):
            font = ImageFont.truetype(FONT_PATH, font_size)
        else:
            raise OSError
    except OSError:
        font = ImageFont.load_default()
        print(f"⚠️ WARNING: Custom font missing, using default font")

    # ===== TEXT SIZE =====
    bbox = font.getbbox(word)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    x = (W - tw) // 2
    y = (H - th) // 2

    # ===== DRAW TEXT =====
    draw.text((x+3, y+3), word, font=font, fill=(0,0,0,180))
    draw.text(
        (x, y),
        word,
        font=font,
        fill=(255,255,255,255),
        stroke_width=5,
        stroke_fill=(0,0,0)
    )

    # ===== OUTPUT =====
    output = BytesIO()
    output.name = "challenge.png"
    img.save(output, format="PNG")
    output.seek(0)
    return output

def generate_reward() -> int:
    return random.randint(REWARD_MIN, REWARD_MAX)
