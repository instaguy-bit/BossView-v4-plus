from flask import Flask
import threading
import os
from bossview_app.core import run_bossview_monitor

app = Flask(__name__)

@app.route('/')
def index():
    return "✅ BossView Level 4+ is LIVE and scanning markets..."

def start_background():
    thread = threading.Thread(target=run_bossview_monitor)
    thread.daemon = True
    thread.start()

if __name__ == '__main__':
    start_background()
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
