from LxmlSoup import LxmlSoup
import requests
import os
from rules import parser_rules

#from chat_gpt_sender import send_to_chat_gpt

# Читаем файл txt в список
with open('web.txt', 'r', encoding='utf-8', errors='replace') as f:
    urls = [url.strip() for url in f.readlines()]

# Создаем папку для парсерных файлов
parser_folder = 'parser_files'
if not os.path.exists(parser_folder):
    os.makedirs(parser_folder)
    
for i, url in enumerate(urls):
    try:
        response = requests.get(url, verify=False)
        response.raise_for_status() 
    except requests.RequestException as e:
        print(f"Ошибка парсинга URL: {e}")
        continue
    print(f"Парсинг завершен {url}")

    html = response.text
    soup = LxmlSoup(html)  # создаём экземпляр класса LxmlSoup
    product = parser_rules(soup)
    
    with open(f'{parser_folder}/output_{i+1}.txt', 'w', encoding='utf-8', errors='replace') as f:
        for element in product:
            text = element.text().strip() 
            url = element.get("href")
            f.write(f"{text},{url}\n")

    # Отправляем текст в Chat GPT
    #answer = send_to_chat_gpt(text)
    #print(f"ответ: {answer}")