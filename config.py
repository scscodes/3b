# config.py

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the bot token
BOT_TOKEN = os.getenv('BOT_TOKEN')
DB_NAME = os.getenv('DB_NAME')
WEBHOOK_URL = os.getenv('WEBHOOK_URL')