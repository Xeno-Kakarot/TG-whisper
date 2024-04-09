import asyncio
import json
import logging
import os
import sys
import time
from random import choice

import telegram
import telegram.ext as tg
from pyrogram import Client, errors
from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.constants import ParseMode
from telegram.ext import Application, ApplicationBuilder
from telethon import TelegramClient, events
from telethon.sessions import MemorySession

# <=======================================================================================================>

# <================================================= NECESSARY ======================================================>
StartTime = time.time()

loop = asyncio.get_event_loop()
# <=======================================================================================================>

# <================================================= LOGGER ======================================================>
# Initialize the logger
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    handlers=[logging.FileHandler("Logs.txt"), logging.StreamHandler()],
    level=logging.INFO,
)
# Set the log levels for specific libraries
logging.getLogger("apscheduler").setLevel(logging.ERROR)
logging.getLogger("telethon").setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("pyrate_limiter").setLevel(logging.ERROR)

# Define the logger for this module
LOGGER = logging.getLogger(__name__)
# <=======================================================================================================>

# <================================================ SYS =======================================================>
# Check Python version
if sys.version_info < (3, 6):
    LOGGER.error(
        "You MUST have a Python version of at least 3.6! Multiple features depend on this. Bot quitting."
    )
    sys.exit(1)
# <=======================================================================================================>

# <================================================ ENV VARIABLES =======================================================>
# Determine whether the bot is running in an environment with environment variables or not
ENV = bool(os.environ.get("ENV", False))

if ENV:
    # Read configuration from environment variables
    API_ID = int(os.environ.get("API_ID", None))
    API_HASH = os.environ.get("API_HASH", None)
    MONGO_DB_URI = os.environ.get("MONGO_DB_URI")
    TOKEN = os.environ.get("TOKEN", None)




API_ID = Config.API_ID   
API_HASH = Config.API_HASH
MONGO_DB_URI = Config.MONGO_DB_URI
TOKEN = Config.TOKEN



dispatcher = Application.builder().token(TOKEN).build()
function = dispatcher.add_handler



# Get bot information
print("[INFO]: Getting Bot Info...")
BOT_ID = dispatcher.bot.id
BOT_NAME = dispatcher.bot.first_name
BOT_USERNAME = dispatcher.bot.username
# <=======================================================================================================>

# <================================================== CONVERT LISTS =====================================================>
