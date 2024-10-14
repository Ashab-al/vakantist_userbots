from pyrogram import Client, filters
import asyncio
import gspread
from google.oauth2.service_account import Credentials
import logging
import re
import os
import json
import requests
# https://my.telegram.org/apps

KEYWORD_SMM = []
EXCEPTONS_SMM = []

KEYWORD_ASSISTANT = []
EXCEPTONS_ASSISTANT= []

KEYWORD_GRAFDESIGN = []
EXCEPTONS_GRAFDESIGN = []

KEYWORD_COPIRATE = []
EXCEPTONS_COPIRATE = []

KEYWORD_SITE = []
EXCEPTONS_SITE = []

KEYWORD_TARGET = []
EXCEPTONS_TARGET = []

KEYWORD_TEHSPEC = []
EXCEPTONS_TEHSPEC = []

KEYWORD_GETCOURSE = []
EXCEPTONS_GETCOURSE = []

EXCEPTONS_USERNAME = []

#Общие ключевые слова
GENERAL_FILTER_EXCEPTONS = []

def sheet_open():
    creds = Credentials.from_service_account_file(filename='savvy-temple-380003-e855ebfc1557.json', 
                                                  scopes=['https://www.googleapis.com/auth/spreadsheets',
                                                          'https://www.googleapis.com/auth/drive']) 
    return gspread.authorize(creds)

def get_column_data(list_name: str):
    return sheet_open().open('Фриланс заказы | Асхаб').worksheet(list_name).get_all_records()

#юзербот
api_id = "14784408"
api_hash = "82bc0317e29988a8afb596880a99793e"
chat_id = "-1001786162328"
app = Client("my_account", api_id=api_id, api_hash=api_hash)

def update_keyword_exceptons():
    global KEYWORD_SMM, EXCEPTONS_SMM, KEYWORD_ASSISTANT, \
            EXCEPTONS_ASSISTANT, KEYWORD_GRAFDESIGN, \
            EXCEPTONS_GRAFDESIGN, KEYWORD_COPIRATE, EXCEPTONS_COPIRATE, KEYWORD_SITE, EXCEPTONS_SITE, \
            KEYWORD_TARGET, EXCEPTONS_TARGET, KEYWORD_TEHSPEC, EXCEPTONS_TEHSPEC, \
            EXCEPTONS_USERNAME, GENERAL_FILTER_EXCEPTONS, KEYWORD_GETCOURSE, EXCEPTONS_GETCOURSE
    
    print("Обновить ключевые слова Асхаб Алхазуров")

    result_get_data_sheet = get_column_data(list_name="Фильтр")

    KEYWORD_SMM = [item['Ключевые слова SMM'] for item in filter(lambda item: item["Ключевые слова SMM"] != 0 and item["Ключевые слова SMM"] != '', result_get_data_sheet)]
    EXCEPTONS_SMM = [item['Слова исключения SMM'] for item in filter(lambda item: item["Слова исключения SMM"] != 0 and item["Слова исключения SMM"] != '', result_get_data_sheet)]

    KEYWORD_ASSISTANT = [item['Ключевые слова Ассистент'] for item in filter(lambda item: item["Ключевые слова Ассистент"] != 0 and item["Ключевые слова Ассистент"] != '', result_get_data_sheet)]
    EXCEPTONS_ASSISTANT = [item['Слова исключения Ассистент'] for item in filter(lambda item: item["Слова исключения Ассистент"] != 0 and item["Слова исключения Ассистент"] != '', result_get_data_sheet)]

    KEYWORD_GRAFDESIGN = [item['Ключевые слова Графический дизайн'] for item in filter(lambda item: item["Ключевые слова Графический дизайн"] != 0 and item["Ключевые слова Графический дизайн"] != '', result_get_data_sheet)]
    EXCEPTONS_GRAFDESIGN = [item['Слова исключения Графический дизайн'] for item in filter(lambda item: item["Слова исключения Графический дизайн"] != 0 and item["Слова исключения Графический дизайн"] != '', result_get_data_sheet)]

    KEYWORD_COPIRATE = [item['Ключевые слова Копирайт'] for item in filter(lambda item: item["Ключевые слова Копирайт"] != 0 and item["Ключевые слова Копирайт"] != '', result_get_data_sheet)]
    EXCEPTONS_COPIRATE = [item['Слова исключения Копирайт'] for item in filter(lambda item: item["Слова исключения Копирайт"] != 0 and item["Слова исключения Копирайт"] != '', result_get_data_sheet)]

    KEYWORD_SITE = [item['Ключевые слова Сайты'] for item in filter(lambda item: item["Ключевые слова Сайты"] != 0 and item["Ключевые слова Сайты"] != '', result_get_data_sheet)]
    EXCEPTONS_SITE = [item['Слова исключения Сайты'] for item in filter(lambda item: item["Слова исключения Сайты"] != 0 and item["Слова исключения Сайты"] != '', result_get_data_sheet)]

    KEYWORD_TARGET = [item['Ключевые слова Таргет'] for item in filter(lambda item: item["Ключевые слова Таргет"] != 0 and item["Ключевые слова Таргет"] != '', result_get_data_sheet)]
    EXCEPTONS_TARGET = [item['Слова исключения Таргет'] for item in filter(lambda item: item["Слова исключения Таргет"] != 0 and item["Слова исключения Таргет"] != '', result_get_data_sheet)]

    KEYWORD_TEHSPEC = [item['Ключевые слова Тех-спец'] for item in filter(lambda item: item["Ключевые слова Тех-спец"] != 0 and item["Ключевые слова Тех-спец"] != '', result_get_data_sheet)]
    EXCEPTONS_TEHSPEC = [item['Слова исключения Тех-спец'] for item in filter(lambda item: item["Слова исключения Тех-спец"] != 0 and item["Слова исключения Тех-спец"] != '', result_get_data_sheet)]
    
    KEYWORD_GETCOURSE = [item['Ключевые слова getcourse'] for item in filter(lambda item: item["Ключевые слова getcourse"] != 0 and item["Ключевые слова getcourse"] != '', result_get_data_sheet)]
    EXCEPTONS_GETCOURSE = [item['Слова исключения getcourse'] for item in filter(lambda item: item["Слова исключения getcourse"] != 0 and item["Слова исключения getcourse"] != '', result_get_data_sheet)]
    
    EXCEPTONS_USERNAME = [item['Исключения отправители'] for item in filter(lambda item: item["Исключения отправители"] != 0 and item["Исключения отправители"] != '', result_get_data_sheet)]

    GENERAL_FILTER_EXCEPTONS = [item['Общий фильр'] for item in filter(lambda item: item["Общий фильр"] != 0 and item["Общий фильр"] != '', result_get_data_sheet)]

    app.send_message(chat_id=int(chat_id), text="Обновление ключевых слов - 100%")
    
    print(f"KEYWORD_SMM - {KEYWORD_SMM}\n\nEXCEPTONS_SMM - {EXCEPTONS_SMM}")
    print(f"KEYWORD_ASSISTANT - {KEYWORD_ASSISTANT}\n\nEXCEPTONS_ASSISTANT - {EXCEPTONS_ASSISTANT}")
    print(f"KEYWORD_GRAFDESIGN - {KEYWORD_GRAFDESIGN}\n\nEXCEPTONS_GRAFDESIGN - {EXCEPTONS_GRAFDESIGN}")
    print(f"KEYWORD_COPIRATE - {KEYWORD_COPIRATE}\n\nEXCEPTONS_COPIRATE - {EXCEPTONS_COPIRATE}")
    print(f"KEYWORD_SITE - {KEYWORD_SITE}\n\nEXCEPTONS_SITE - {EXCEPTONS_SITE}")
    print(f"KEYWORD_TARGET - {KEYWORD_TARGET}\n\nEXCEPTONS_TARGET - {EXCEPTONS_TARGET}")
    print(f"KEYWORD_TEHSPEC - {KEYWORD_TEHSPEC}\n\nEXCEPTONS_TEHSPEC - {EXCEPTONS_TEHSPEC}")
    print(f"EXCEPTONS_USERNAME - {EXCEPTONS_USERNAME}")
    print(GENERAL_FILTER_EXCEPTONS)


def general_filter(mes):
    global GENERAL_FILTER_EXCEPTONS

    for word_exceptons in GENERAL_FILTER_EXCEPTONS:
        if re.search(rf"{word_exceptons}", mes.lower()):
            return False
    return True

@app.on_message(filters.text & filters.regex(r"\bОбновить ключевые слова\b"))
def message_text(client, message):
    update_keyword_exceptons()

@app.on_message(filters.text & ~filters.user("infobizaa_bot") & filters.channel)   
async def message_from_channel(client, message): 
    await run_filterint_all_category(message_text=message.text, 
                                     username=message.chat.username,
                                     platform_id="123")

@app.on_message(filters.text & ~filters.user("infobizaa_bot"))
async def message_from_chat(client, message):
    await run_filterint_all_category(message_text=message.text, 
                                     username=message.from_user.username,
                                     platform_id=message.from_user.id)

async def run_filterint_all_category(message_text, username, platform_id):
    global KEYWORD_SMM, EXCEPTONS_SMM, KEYWORD_ASSISTANT, \
            EXCEPTONS_ASSISTANT, KEYWORD_GRAFDESIGN, \
            EXCEPTONS_GRAFDESIGN, KEYWORD_COPIRATE, EXCEPTONS_COPIRATE, KEYWORD_SITE, EXCEPTONS_SITE, \
            KEYWORD_TARGET, EXCEPTONS_TARGET, KEYWORD_TEHSPEC, EXCEPTONS_TEHSPEC, \
            EXCEPTONS_USERNAME, KEYWORD_GETCOURSE, EXCEPTONS_GETCOURSE
    
    if f"@{username}" != "@None" and f"@{username}" not in EXCEPTONS_USERNAME and general_filter(mes=message_text):
        await filtering_messages_by_category(category_name='SMM', message=message_text,
                                                keywords=KEYWORD_SMM, exceptons=EXCEPTONS_SMM,
                                                username_customer=username, platform_id=platform_id)
        
        await filtering_messages_by_category(category_name='Ассистент', message=message_text,
                                                keywords=KEYWORD_ASSISTANT, exceptons=EXCEPTONS_ASSISTANT,
                                                username_customer=username, platform_id=platform_id)
        
        await filtering_messages_by_category(category_name='Дизайн', message=message_text,
                                                keywords=KEYWORD_GRAFDESIGN, exceptons=EXCEPTONS_GRAFDESIGN,
                                                username_customer=username, platform_id=platform_id)
        
        await filtering_messages_by_category(category_name='Копирайт', message=message_text,
                                                keywords=KEYWORD_COPIRATE, exceptons=EXCEPTONS_COPIRATE,
                                                username_customer=username, platform_id=platform_id)
        
        await filtering_messages_by_category(category_name='Сайты', message=message_text,
                                                keywords=KEYWORD_SITE, exceptons=EXCEPTONS_SITE,
                                                username_customer=username, platform_id=platform_id)
        
        await filtering_messages_by_category(category_name='Таргет', message=message_text,
                                                keywords=KEYWORD_TARGET, exceptons=EXCEPTONS_TARGET,
                                                username_customer=username, platform_id=platform_id)
        
        await filtering_messages_by_category(category_name='Тех-спец', message=message_text,
                                                keywords=KEYWORD_TEHSPEC, exceptons=EXCEPTONS_TEHSPEC,
                                                username_customer=username, platform_id=platform_id)
        
        await filtering_messages_by_category(category_name='GetCourse', message=message_text,
                                                keywords=KEYWORD_GETCOURSE, exceptons=EXCEPTONS_GETCOURSE,
                                                username_customer=username, platform_id=platform_id)
        return True
    else:
        return False
                           

async def filtering_messages_by_category(category_name, message: str, keywords: list, exceptons: list, \
                                        username_customer, platform_id):
        for word_ex in exceptons:
            try:
                if re.search(rf"{word_ex}", message.lower()):
                    return False
            except AttributeError as e:
                print(f"Функция filtering_messages_by_category. (exceptons) Слово исключение: {word_ex} Ошибка: {e}")
                await app.send_message(chat_id=int(chat_id), text=f"filtering_messages_by_category err: {e}")

        for word_key in keywords: 
            try:
                if re.search(rf"{word_key}", message.lower()):
                    await send_message_api(message, category_name, username=username_customer, platform_id=platform_id)
                    return True
                 
            except AttributeError as e:
                print(f"Функция filtering_messages_by_category. (keywords) ключевое слово: {word_key} Ошибка: {e}")
                await app.send_message(chat_id=int(chat_id), text=f"Функция filtering_messages_by_category. (keywords) ключевое слово: {word_key} Ошибка: {e}")
        return False

async def send_message_api(message, category_name, username, platform_id): 
    links_from_message = await extract_links_and_mentions(text=message, regular='http\S+|www\S+', method=1)
    username_from_message = await extract_links_and_mentions(text=message, regular='@\w+', method=1)
    
    message_false = await extract_links_and_mentions(text=message, regular='http\S+|www\S+', method=2)
    message_false = await extract_links_and_mentions(text=message_false, regular='@\w+', method=2)

    api_request({
        "params": {
            "category_title": category_name,
            "title": category_name,
            "contact_information": f"@{username}\n{links_from_message}\n{username_from_message}" ,
            "description": message_false,
            "platform_id": platform_id,
            "source": "tg_chat"
        },
        "url": "https://ashabal.ru/api/vacancies_create"
    })
    return True

async def extract_links_and_mentions(text, regular, method):
    if method == 1:
        links = re.findall(rf'{regular}', text)
        if len(links) > 0:
            text_links = ""
            for i, link in enumerate(links, start=1):
                text_links += f"{i}. {link} \n"
            return text_links  
        else:
            return ""
        
    elif method == 2:
        return re.sub(rf'{regular}', '', text)
    
    else:
        return False

def api_request(data):
    try:
        response = requests.post(data["url"], params=data["params"])
        if response.status_code == 201:
            return True 
        else:
            print(response)
            print(f"Выполнении запроса: {response.status_code}")
            print(f"Выполнении запроса: {response.text}")
            return False
    except Exception as e:
        print(f"Ошибка при выполнении запроса: {str(e)}")

app.run()
