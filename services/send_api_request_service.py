import requests
import datetime
import logging
from services.create_links_service import Link
# Настройка логирования
logging.basicConfig(filename='logfile_err.log', level=logging.ERROR, format='%(asctime)s %(message)s')

class ApiRequest:
    @staticmethod
    async def send_message_api(message, category_name, username, platform_id):
        links_from_message = await Link.extract_links_and_mentions(text=message, regular=r'http\S+|www\S+', method=1)
        username_from_message = await Link.extract_links_and_mentions(text=message, regular=r'@\w+', method=1)
        
        message_false = await Link.extract_links_and_mentions(text=message, regular=r'http\S+|www\S+', method=2)
        message_false = await Link.extract_links_and_mentions(text=message_false, regular=r'@\w+', method=2)

        ApiRequest.api_request({
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
    
    @staticmethod
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
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            logging.error(f"Time: {current_time} - Error method api_request Errors: {e}")