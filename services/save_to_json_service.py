import json
import os

class SaveFile:
    def __init__(self, data, file_path):
        self.data = data
        self.file_path = file_path

    def save_file(self):
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(self.data, file, indent=4, ensure_ascii=False)