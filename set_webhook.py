# set_webhook.py
import os

import requests
import config
from dotenv import load_dotenv

load_dotenv()


TOKEN = os.getenv('BOT_TOKEN')
WEBHOOK = os.getenv('WEBHOOK_URL')
WEBHOOK_URL = f'{WEBHOOK}/{TOKEN}'  # Replace with your ngrok URL

def set_webhook():
    url = f'https://api.telegram.org/bot{TOKEN}/setWebhook'
    response = requests.post(url, data={'url': WEBHOOK_URL})
    print(response.text)

if __name__ == '__main__':
    set_webhook()
