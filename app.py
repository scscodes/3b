# app.py

from flask import Flask, request
from threading import Thread
from db import init_db
from handlers import handle_update
from scheduler import start_scheduler
import config

app = Flask(__name__)

TOKEN = config.BOT_TOKEN

# Webhook route
@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    update = request.get_json()
    if update and 'message' in update:
        handle_update(update['message'])
    return 'ok'

if __name__ == '__main__':
    init_db()
    # Start the reminder scheduler in a separate thread
    Thread(target=start_scheduler).start()
    # Run the Flask app
    app.run(host='0.0.0.0', port=5000)
