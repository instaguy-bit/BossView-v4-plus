import time
from bossview_app.telegram_notifier import send_telegram_message

def run_bossview_monitor():
    # Placeholder for your trading logic
    print("🧠 BossView AI scanning market...")
    # Send a startup test alert
    send_telegram_message("🚨 BossView Level 4+ bot started and running!")
    while True:
        print("📡 Bot running... market scan cycle")
        time.sleep(60)
