import os
from telegram import Bot

TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN', '')
CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID', '')

def send_telegram_message(text):
    if not TOKEN or not CHAT_ID:
        print("Telegram token or chat ID not set")
        return
    bot = Bot(token=TOKEN)
    bot.send_message(chat_id=CHAT_ID, text=text)
