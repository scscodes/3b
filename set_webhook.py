# set_webhook.py

import requests
import config

TOKEN = config.TELEGRAM_BOT_TOKEN
WEBHOOK_URL = f'https://ourselves-holders--romance.trycloudflare.com/{TOKEN}'  # Replace with your ngrok URL

def set_webhook():
    url = f'https://api.telegram.org/bot{TOKEN}/setWebhook'
    response = requests.post(url, data={'url': WEBHOOK_URL})
    print(response.text)

if __name__ == '__main__':
    set_webhook()
