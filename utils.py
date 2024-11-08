# utils.py

import requests
import config

TOKEN = config.TELEGRAM_BOT_TOKEN

def send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    payload = {'chat_id': chat_id, 'text': text}
    requests.post(url, json=payload)

def parse_duration(duration_str):
    units = {'s': 1, 'm': 60, 'h': 3600}
    try:
        unit = duration_str[-1]
        amount = int(duration_str[:-1])
        return amount * units.get(unit, 0)
    except (ValueError, KeyError):
        return None
