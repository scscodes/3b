# scheduler.py

import time
from db import get_db_connection
from utils import send_message

def start_scheduler():
    while True:
        current_time = int(time.time())
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT id, chat_id, message FROM reminders WHERE remind_at <= ?', (current_time,))
        reminders_due = cursor.fetchall()

        for reminder in reminders_due:
            send_message(reminder['chat_id'], f'Reminder: {reminder["message"]}')
            cursor.execute('DELETE FROM reminders WHERE id = ?', (reminder['id'],))
            conn.commit()

        conn.close()
        time.sleep(30)  # Wait for 30 seconds before checking again
