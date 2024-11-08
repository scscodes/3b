# handlers.py

import time
from utils import send_message, parse_duration
from db import get_db_connection

def handle_update(message):
    chat_id = message['chat']['id']
    text = message.get('text', '')
    if text.startswith('/pin'):
        handle_pin(chat_id, message)
    elif text.startswith('/remindme'):
        handle_remindme(chat_id, message)
    else:
        send_message(chat_id, 'Unknown command.')

def handle_pin(chat_id, message):
    user_id = message['from']['id']
    text = message.get('text', '')
    pin_message = text.partition(' ')[2].strip()

    if not pin_message:
        send_message(chat_id, 'Usage: /pin <message>')
        return

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO pins (user_id, chat_id, message) VALUES (?, ?, ?)',
        (user_id, chat_id, pin_message)
    )
    conn.commit()
    conn.close()

    send_message(chat_id, 'Message pinned!')

def handle_remindme(chat_id, message):
    user_id = message['from']['id']
    text = message.get('text', '')
    parts = text.split(' ', 2)

    if len(parts) < 3:
        send_message(chat_id, 'Usage: /remindme <duration> <message>')
        return

    duration_str = parts[1]
    reminder_text = parts[2]
    duration_seconds = parse_duration(duration_str)

    if duration_seconds is None:
        send_message(chat_id, 'Invalid duration format. Use "10s", "5m", "2h", etc.')
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

    send_message(chat_id, f'Reminder set for {duration_str} from now!')