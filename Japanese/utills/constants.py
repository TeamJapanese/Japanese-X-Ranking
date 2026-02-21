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
