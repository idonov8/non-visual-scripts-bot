import os
from dotenv import load_dotenv
load_dotenv()

# Getting mode, so we could define run function for local and Heroku setup
MODE = os.getenv("MODE")
BOT_TOKEN = os.getenv("BOT_TOKEN")