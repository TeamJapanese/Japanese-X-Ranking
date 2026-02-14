import threading
import asyncio
import time
from pyrogram import Client
from Japanese.basic import send_challenge  # Import the async challenge function

# -------------------- Scheduler Class -------------------- #
class ChallengeScheduler:
    """
    Runs ranking challenges periodically in all registered groups.
    Uses a background thread to schedule async tasks safely.
    """

    def __init__(self, bot: Client, interval: int = 1800):  # Default: 30 minutes
        self.bot = bot
        self.interval = interval
        self.running = False
        self.thread = threading.Thread(target=self._run)
        self.thread.daemon = True  # Daemon thread will exit when main program exits

    def start(self):
        """Start the scheduler."""
        if not self.running:
            self.running = True
            self.thread.start()
            print("[Scheduler] Challenge scheduler started.")

    def stop(self):
        """Stop the scheduler."""
        self.running = False
        print("[Scheduler] Challenge scheduler stopped.")

    def _run(self):
        """
        Main loop for the scheduler.
        Runs the async send_challenge() using the bot's event loop.
        """
        while self.running:
            try:
                print("[Scheduler] Sending new challenge to all active groups...")
                # Schedule the async send_challenge task safely
                asyncio.run_coroutine_threadsafe(send_challenge(self.bot), self.bot.loop)
            except Exception as e:
                print(f"[Scheduler] Error: {e}")
            time.sleep(self.interval)
