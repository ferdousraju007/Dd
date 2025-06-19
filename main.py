# ✅ Telegram Signal Bot – Basic Version for 3-Min OTC Signals

import os
import logging
import random
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# --- Configure Logging ---
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# --- Your Configuration from Environment Variables ---
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
ADMIN_USER_ID = int(os.getenv("ADMIN_USER_ID"))

# --- Signal Generator Function (Demo Logic) ---
def generate_signal():
    pairs = ["EUR/USD", "GBP/USD", "AUD/USD"]
    directions = ["BUY", "SELL"]
    entry = f"1.{random.randint(1000, 9999)} – 1.{random.randint(1000, 9999)}"
    return {
        "pair": random.choice(pairs),
        "direction": random.choice(directions),
        "confidence": random.randint(80, 95),
        "entry": entry
    }

# --- Command Handler ---
def start(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    if user_id != ADMIN_USER_ID:
        update.message.reply_text("⛔ Access Denied. This bot is private.")
        return

    update.message.reply_text("🤖 Signal Bot activated! Sending your signal...")
    signal = generate_signal()

    msg = f"""
📢 SIGNAL ALERT
🕒 Time: {update.message.date.strftime('%I:%M %p')}
⏱️ Timeframe: 3-Min
💱 Pair: {signal['pair']}
📉 Signal: {signal['direction']}
🎯 Entry Zone: {signal['entry']}
📊 Confidence: {signal['confidence']}%
📍 Reason: EMA + RSI + S/R Alignment
"""
    update.message.reply_text(msg)

# --- Main Function ---
def main():
    updater = Updater(TELEGRAM_TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
