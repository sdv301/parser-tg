from LxmlSoup import LxmlSoup
import requests
import logging
import re

# Читаем файл txt в список
with open('web.txt', 'r', encoding='utf-8', errors='replace') as f:
    urls = [url.strip() for url in f.readlines()]

for url in urls:
    try:
        response = requests.get(url)
        response.raise_for_status() 
        logging.info(f"Парсим этот URL: {url}")
    except requests.RequestException as e:
        logging.error(f"Ошибка парсинга URL: {e}")
        continue

html = response.text
soup = LxmlSoup(html)  # создаём экземпляр класса LxmlSoup

links = soup.find_all('a') + soup.find_all('b') + soup.find_all('li') + soup.find_all('p') + soup.find_all('span') + soup.find_all('string')

with open('output.txt', 'a', encoding='utf-8', errors='replace') as f:
    for link in links:
        name =link.text().strip()  
        f.write(f"{name}\n")
    print(f"Парсинг завершен {url}")
       