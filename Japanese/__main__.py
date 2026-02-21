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
import logging
import threading
import time
import requests

from flask import Flask
from flask_restful import Resource, Api

from pyrogram import Client, idle
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid
from Japanese.basic import challenge_loop

# -------------------- Logging -------------------- #
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# -------------------- Pyrogram Client -------------------- #
Japanese = Client(
    "JapaneseXRanking",
    api_id=int(os.environ.get("API_ID")),
    api_hash=os.environ.get("API_HASH"),
    bot_token=os.environ.get("BOT_TOKEN"),
    plugins={"root": "Japanese"},
    workers=100
)

# -------------------- Flask -------------------- #
app = Flask(__name__)
api = Api(app)

class Greeting(Resource):
    def get(self):
        return {"message": "Japanese X Ranking is Up & Running!"}

api.add_resource(Greeting, '/')

def run_flask():
    port = int(os.environ.get("PORT", 8080))
    logging.info(f"[Flask] Running server on port {port}")
    app.run(host="0.0.0.0", port=port)

def keep_alive():
    url = os.environ.get("PING_URL", "https://your-render-url.onrender.com").strip()
    while True:
        try:
            logging.info(f"[KeepAlive] Pinging {url}")
            requests.get(url, timeout=10)
        except Exception as e:
            logging.warning(f"[KeepAlive] Failed to ping: {e}")
        time.sleep(600)  # Ping every 10 minutes


# -------------------- Start Threads -------------------- #
threading.Thread(target=run_flask, daemon=True).start()
threading.Thread(target=keep_alive, daemon=True).start()

# -------------------- MAIN -------------------- #
if __name__ == "__main__":
    try:
        logging.info("🚀 Starting bot...")
        Japanese.start()

        # 🔥 START GAME LOOP
        Japanese.loop.create_task(challenge_loop(Japanese))

        logging.info(f"🤖 Bot running as @{Japanese.me.username}")
        idle()

    except (ApiIdInvalid, ApiIdPublishedFlood):
        logging.error("❌ Invalid API ID / HASH")
    except AccessTokenInvalid:
        logging.error("❌ Invalid BOT TOKEN")
    finally:
        Japanese.stop()
        logging.info("🛑 Bot stopped")
