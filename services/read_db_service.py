import json

class ReadDB:
    @staticmethod
    def get_all(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    
    @staticmethod
    def get_general_exceptions(file_path):
        return ReadDB.get_all(file_path)["general_filter"]["exception"]
    
    @staticmethod
    def get_username_exceptions(file_path):
        return ReadDB.get_all(file_path)["username"]["exception"]