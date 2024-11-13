# handlers.py

import time
import json
from utils import send_message, parse_duration
from db import get_db_connection
import random

def handle_update(message):
    json_str = json.dumps(message, indent=2)
    print(json_str)
    message_id = message['message_id']
    chat_id = message['chat']['id']
    text = message.get('text', '')
    if text.startswith('/pin '):
        handle_pin(chat_id, message, message_id)
    elif text == '/ping':
        handle_ping(chat_id)
    elif text.startswith('/remindme'):
        handle_remindme(chat_id, message, message_id)
    elif text == '/flip':
        handle_flips(chat_id)
    else:
        send_message(chat_id, "I'm sorry, I didn't understand that command.")

def handle_flips(chat_id):
    flip_variations = [
        "(╯°□°）╯︵ ┻━┻",
        "(ノಠ益ಠ)ノ彡┻━┻",
        "(╯‵Д′)╯彡┻━┻",
        "(╯°Д°）╯︵ /(.□ . \\)",
        "┻━┻ ︵ヽ(`Д´)ﾉ︵ ┻━┻"
    ]
    flip_message = random.choice(flip_variations)
    send_message(chat_id, flip_message)


def handle_ping(chat_id):
    send_message(chat_id, 'Pong!')

def handle_pin(chat_id, message, message_id):
    user_id = message['from']['id']
    text = message.get('text', '')
    pin_message = text.partition(' ')[2].strip()

    if not pin_message:
        send_message(chat_id, 'Usage: /pin <message>', message_id)
        return

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO pins (user_id, chat_id, message) VALUES (?, ?, ?)',
        (user_id, chat_id, pin_message)
    )
    conn.commit()
    conn.close()

    send_message(chat_id, 'Message pinned!', message_id)

def handle_remindme(chat_id, message, message_id):
    user_id = message['from']['id']
    text = message.get('text', '')
    parts = text.split(' ', 2)

    if len(parts) < 3:
        send_message(chat_id, 'Usage: /remindme <duration> <message>', message_id)
        return

    duration_str = parts[1]
    reminder_text = parts[2]
    duration_seconds = parse_duration(duration_str)

    if duration_seconds is None:
        send_message(chat_id, 'Invalid duration format. Use "10s", "5m", "2h", etc.', message_id)
        return

    remind_at = int(time.time()) + duration_seconds

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO reminders (user_id, chat_id, message, remind_at) VALUES (?, ?, ?, ?)',
        (user_id, chat_id, reminder_text, remind_at)
    )
    conn.commit()
    conn.close()

    send_message(chat_id, f'Reminder set for {duration_str} from now!', message_id)
