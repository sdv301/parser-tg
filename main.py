from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import Message
from api_key import gpt

token = '7446126916:AAE3KK496DpAZHJl0Sph2vTIyE_yOVAK6rk'

bot = Bot(token)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')            #Обработка команды /start
async def start(message: Message):
    await message.answer('Привет, это чат-бот на основе модели gpt 3.5🔥\nПриступим!')


@dp.message_handler(content_types=types.ContentType.TEXT)        #Любой текст = запрос к chatgpt. 
async def mes(message: types.Message): 
    await message.answer('Генерируется ответ♻️')            #Даём понять пользователю, что бот работает
    await message.reply(gpt(message.text)) # type: ignore        Тут запрос принимается, отдаётся на обработку и выводится
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id + 1)        #Удаляем первое сообщение. Только для эстетики
    
if __name__ == '__main__':            #Запускаем проверку поступающих в бота сообщений.
    executor.start_polling(dp)



















# import requests

# class ChatGPTSender:
#     def __init__(self, api_key):
#         self.api_key = api_key

#     def send_text(self, text):
#         headers = {'Authorization': f'Bearer {self.api_key}'}
#         response = requests.post('https://api.chatgpt.com/v1/text', headers=headers, json={'text': text})
#         return response.json()

#     def get_answer(self, response):
#         return response['text']

# # Создаем экземпляр класса ChatGPTSender
# chat_gpt_sender = ChatGPTSender('YOUR_API_KEY')

# # Определяем функцию, которая будет отправлять текст в Chat GPT и возвращать ответ
# def send_to_chat_gpt(text):
#     response = chat_gpt_sender.send_text(text)
#     answer = chat_gpt_sender.get_answer(response)
#     return answer