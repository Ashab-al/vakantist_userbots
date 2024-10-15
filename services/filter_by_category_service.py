import re
import logging
import datetime
from services.read_db_service import ReadDB
from services.send_api_request_service import ApiRequest
from services.create_links_service import Link
import services
# Настройка логирования
logging.basicConfig(filename='logfile_err.log', level=logging.ERROR, format='%(asctime)s %(message)s')

class FilterByCategory:
    @staticmethod
    def general_filter(message):
        for word_exceptons in ReadDB.get_general_exceptions('db/db_word.json'):
            if re.search(rf"{word_exceptons}", message.lower()):
                return False
        return True
   
    @staticmethod
    async def run_filterint_all_category(message_text, username, platform_id):
        if f"@{username}" != "@None" and f"@{username}" not in ReadDB.get_username_exceptions('db/db_word.json') and FilterByCategory.general_filter(message=message_text):
            db = ReadDB.get_all('db/db_word.json')
            categories = { 
                "smm": "SMM",
                "assistant": "Ассистент",
                "grafdesign": "Дизайн",
                "copirate": "Копирайт",
                "site":"Сайты",
                "target": "Таргет",
                "tehspec": "Тех-спец",
                "getcourse": "GetCourse"
            }
            for category in list(categories.keys()):
                await FilterByCategory.filtering_messages_by_category(category_name=categories[category], message=message_text,
                                                    keywords=db[category]["keyword"], exceptons=db[category]["exception"],
                                                    username_customer=username, platform_id=platform_id)
            return True
    
    @staticmethod
    async def filtering_messages_by_category(category_name, message: str, keywords: list, exceptons: list, \
                                        username_customer, platform_id):
        for word_ex in exceptons:
            try:
                if re.search(rf"{word_ex}", message.lower()):
                    return False
            except AttributeError as e:
                current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                logging.error(f"Time: {current_time} - Error method filtering_messages_by_category, expection word {word_ex}: Errors: {e}")

        for word_key in keywords: 
            try:
                if re.search(rf"{word_key}", message.lower()):
                    await ApiRequest.send_message_api(message, category_name, username=username_customer, platform_id=platform_id)
                    return True
                 
            except AttributeError as e:
                current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                logging.error(f"Time: {current_time} - Error method filtering_messages_by_category,  key word {word_key}: Errors: {e}")
        return False