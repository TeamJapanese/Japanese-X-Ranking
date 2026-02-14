import os

# ================= BASE DIR =================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ================= IMAGE =================
# Background / heart image (1536x1024 recommended)
BASE_IMAGE_PATH = os.path.join(
    BASE_DIR, "..", "..", "img", "japanese.png"
)

# ================= FONT =================
# Bold & highly readable font
FONT_PATH = os.path.join(
    BASE_DIR, "..", "..", "font", "Roboto-Regular.ttf"
)

# ================= FONT SETTINGS =================
FONT_SIZE = 80         # Main font size (Telegram safe)
MIN_FONT_SIZE = 140      # Never go below this
STROKE_WIDTH = 5         # Outline thickness

# ================= CHALLENGE =================
CHALLENGE_INTERVAL = 900 # 15 minutes
# CHALLENGE_INTERVAL = 60 # 1 minutes

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

# ================= REWARDS =================
REWARD_MIN = 10
REWARD_MAX = 50

# ================= SERVER =================
PING_INTERVAL = 600
