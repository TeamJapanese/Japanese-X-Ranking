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
CHALLENGE_INTERVAL = 300 # 5 minutes
# CHALLENGE_INTERVAL = 60 # 1 minutes

WORDS_POOL = [
    # 🔹 Very short (3–4 letters) – ultra fast rounds
    "Win", "Run", "Go", "Try", "Do",
    "Up", "Now", "Move", "Play", "Fast",
    "Real", "True", "Safe", "Next",
    "Rise", "Aim", "Act", "Lead",
    "Hope", "Step", "Dash", "Jump",

    # 🔹 Short (5–6 letters) – balanced speed
    "Power", "Smile", "Peace", "Trust", "Light",
    "Heart", "Focus", "Brave", "Calm", "Level",
    "Start", "Build", "Learn", "Grow", "Boost",
    "Energy", "Control", "Create", "Vision",
    "Winner", "Spirit", "Leader", "Impact",
    "Charge", "Dream", "Drive", "Skill",
    "Strong", "Bright", "Talent",

    # 🔹 Medium (7–8 letters) – skill based
    "Success", "Respect", "Future", "Progress",
    "Victory", "Achieve", "Believe", "Balance",
    "Courage", "Stability", "Powerful", "Motivate",
    "Journey", "Freedom", "Mindset", "Purpose",
    "Results", "Winning", "Upgrade", "Advance",
    "Stronger", "Creator", "Builder",

    # 🔹 Long (9–12 letters) – high difficulty rounds
    "Discipline", "Patience", "Determined",
    "Consistent", "Focusedmind",
    "Selfcontrol", "Performance",
    "Transform", "Dedication",
    "Achievement", "Commitment",
    "Confidence", "Persistence",
    "Productivity", "Excellence",
    "Improvement",

    # 🔹 Hard English words
    "Perseverance", "Magnificent", "Extraordinary",
    "Unbreakable", "Relentless", "Determination",
    "Unbelievable", "Revolutionary",
    "Unpredictable", "Spectacular",
    "Reinforcement", "Masterpiece",
    "Transformation", "Intelligence",
    "Responsibility", "Professional",
    "Acceleration", "Configuration",
    "Implementation", "Optimization",
    "Communication", "Development",
    "Architecture", "Engineering",

    # 🔹 Japanese cultural / traditional words (Romaji)
    "Samurai", "Bushido", "Shogun",
    "Ronin", "Katana", "Shuriken",
    "Sakura", "Kimono", "Origami",
    "Ikigai", "Dojo", "Ninja",
    "Kaizen", "Sensei", "Torii",
    "Tatami", "Kendo", "Uchiwa",
    "Yokai", "Hikari", "Takumi",
    "Kizuna", "Shinobi",

    # 🔹 Indian cultural / common words (non-religious)
    "Namaste", "Bazaar", "Chai",
    "Masala", "Rickshaw", "Dhaba",
    "Jugaad", "Pakka", "Desi",
    "Swadeshi", "Bandhan", "Utsav",
    "Adda", "Dost", "Biryani",
    "Chutney", "Tandoori", "Papad",
    "Lassi", "Chaat",

    # 🔹 Bonus motivational words
    "Dominate", "Unstoppable", "Legendary",
    "Champion", "Master", "Elite",
    "Maximum", "Upgrade",
    "Supreme", "Invincible",
    "Greatness", "Overpower",
    "Trailblazer"
]

# ================= REWARDS =================
REWARD_MIN = 10
REWARD_MAX = 50

# ================= SERVER =================
PING_INTERVAL = 300
