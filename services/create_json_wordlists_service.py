class DataWord:
    @staticmethod
    def parsing_data(data_sheet):
        keyword_smm = [item['Ключевые слова SMM'] for item in filter(lambda item: item["Ключевые слова SMM"] != 0 and item["Ключевые слова SMM"] != '', data_sheet)]
        exceptions_smm = [item['Слова исключения SMM'] for item in filter(lambda item: item["Слова исключения SMM"] != 0 and item["Слова исключения SMM"] != '', data_sheet)]
        keyword_assistant = [item['Ключевые слова Ассистент'] for item in filter(lambda item: item["Ключевые слова Ассистент"] != 0 and item["Ключевые слова Ассистент"] != '', data_sheet)]
        exceptions_assistant = [item['Слова исключения Ассистент'] for item in filter(lambda item: item["Слова исключения Ассистент"] != 0 and item["Слова исключения Ассистент"] != '', data_sheet)]
        keyword_grafdesign = [item['Ключевые слова Графический дизайн'] for item in filter(lambda item: item["Ключевые слова Графический дизайн"] != 0 and item["Ключевые слова Графический дизайн"] != '', data_sheet)]
        exceptions_grafdesign = [item['Слова исключения Графический дизайн'] for item in filter(lambda item: item["Слова исключения Графический дизайн"] != 0 and item["Слова исключения Графический дизайн"] != '', data_sheet)]
        keyword_copirate = [item['Ключевые слова Копирайт'] for item in filter(lambda item: item["Ключевые слова Копирайт"] != 0 and item["Ключевые слова Копирайт"] != '', data_sheet)]
        exceptions_copirate = [item['Слова исключения Копирайт'] for item in filter(lambda item: item["Слова исключения Копирайт"] != 0 and item["Слова исключения Копирайт"] != '', data_sheet)]
        keyword_site = [item['Ключевые слова Сайты'] for item in filter(lambda item: item["Ключевые слова Сайты"] != 0 and item["Ключевые слова Сайты"] != '', data_sheet)]
        exceptions_site = [item['Слова исключения Сайты'] for item in filter(lambda item: item["Слова исключения Сайты"] != 0 and item["Слова исключения Сайты"] != '', data_sheet)]
        keyword_target = [item['Ключевые слова Таргет'] for item in filter(lambda item: item["Ключевые слова Таргет"] != 0 and item["Ключевые слова Таргет"] != '', data_sheet)]
        exceptions_target = [item['Слова исключения Таргет'] for item in filter(lambda item: item["Слова исключения Таргет"] != 0 and item["Слова исключения Таргет"] != '', data_sheet)]
        keyword_tehspec = [item['Ключевые слова Тех-спец'] for item in filter(lambda item: item["Ключевые слова Тех-спец"] != 0 and item["Ключевые слова Тех-спец"] != '', data_sheet)]
        exceptions_tehspec = [item['Слова исключения Тех-спец'] for item in filter(lambda item: item["Слова исключения Тех-спец"] != 0 and item["Слова исключения Тех-спец"] != '', data_sheet)]
        keyword_getcourse = [item['Ключевые слова getcourse'] for item in filter(lambda item: item["Ключевые слова getcourse"] != 0 and item["Ключевые слова getcourse"] != '', data_sheet)]
        exceptions_getcourse = [item['Слова исключения getcourse'] for item in filter(lambda item: item["Слова исключения getcourse"] != 0 and item["Слова исключения getcourse"] != '', data_sheet)]
        exceptions_username = [item['Исключения отправители'] for item in filter(lambda item: item["Исключения отправители"] != 0 and item["Исключения отправители"] != '', data_sheet)]
        general_filter_exceptions = [item['Общий фильр'] for item in filter(lambda item: item["Общий фильр"] != 0 and item["Общий фильр"] != '', data_sheet)]

        return {
            "smm": {"keyword": keyword_smm, "exception": exceptions_smm},
            "assistant": {"keyword": keyword_assistant, "exception": exceptions_assistant},
            "grafdesign": {"keyword": keyword_grafdesign, "exception": exceptions_grafdesign},
            "copirate": {"keyword": keyword_copirate, "exception": exceptions_copirate},
            "site": {"keyword": keyword_site, "exception": exceptions_site},
            "target": {"keyword": keyword_target, "exception": exceptions_target},
            "tehspec": {"keyword": keyword_tehspec, "exception": exceptions_tehspec},
            "getcourse": {"keyword": keyword_getcourse, "exception": exceptions_getcourse},
            "username": {"exception": exceptions_username},
            "general_filter": {"exception": general_filter_exceptions}
        }
