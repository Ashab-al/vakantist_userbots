from pyrogram import Client, filters
import asyncio
import gspread
from google.oauth2.service_account import Credentials
import logging
import re
import os
import json
import requests
import datetime
import random

from dotenv import load_dotenv

from services.google_sheet_service import GSheet
from services.save_to_json_service import SaveFile
from services.create_json_wordlists_service import DataWord
from services.read_db_service import ReadDB
from services.filter_by_category_service import FilterByCategory
from services.send_api_request_service import ApiRequest

# https://my.telegram.org/apps


# Настройка логирования
logging.basicConfig(filename='logfile_err.log', level=logging.ERROR, format='%(asctime)s %(message)s')

#юзербот
load_dotenv()

api_id = os.getenv('USERBOT_1_API_ID') 
api_hash = os.getenv('USERBOT_1_API_HASH')
chat_id = os.getenv('CHAT_ID') 
app = Client("my_account", api_id=api_id, api_hash=api_hash, 
             device_model="Linux 5.15.0", system_version="Ubuntu 20.04.6 LTS")


@app.on_message(filters.text & filters.regex(r"\bОбновить ключевые слова\b"))
def message_text(client, message):
    app.send_message(chat_id=int(chat_id), text="Обновление ключевых слов - 0%")

    SaveFile(DataWord.parsing_data(GSheet.get_column_data(list_name="Фильтр")), 
             'db/db_word.json').save_file()

    app.send_message(chat_id=int(chat_id), text="Обновление ключевых слов - 100%")

@app.on_message(filters.text & ~filters.user("infobizaa_bot") & filters.channel)   
async def message_from_channel(client, message): 
    await FilterByCategory.run_filterint_all_category(
            message_text=message.text, 
            username=message.chat.username,
            platform_id=f"{random.randint(1, 999999) + random.randint(1, 999999)}"
        )

@app.on_message(filters.text)
async def message_from_chat(client, message):
    try:
        username = message.from_user.username if message.from_user.username is not None else "None"
    except Exception as e:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        logging.error(f"Time: {current_time} - Error method message_from_chat : {e}")
    
    await FilterByCategory.run_filterint_all_category(
            message_text=message.text, 
            username=username,
            platform_id=message.from_user.id
        )


app.run()
