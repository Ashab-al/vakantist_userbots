import re

class Link:
    @staticmethod
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