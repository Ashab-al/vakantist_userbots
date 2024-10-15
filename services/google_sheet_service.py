import gspread
from google.oauth2.service_account import Credentials

class GSheet:
    @staticmethod
    def sheet_open():
        creds = Credentials.from_service_account_file(filename='savvy-temple-380003-e855ebfc1557.json', 
                                                  scopes=['https://www.googleapis.com/auth/spreadsheets',
                                                          'https://www.googleapis.com/auth/drive']) 
        return gspread.authorize(creds)
   
    @staticmethod
    def get_column_data(list_name: str):
        return GSheet.sheet_open().open('Фриланс заказы | Асхаб').worksheet(list_name).get_all_records()