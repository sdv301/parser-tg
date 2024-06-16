from openai import OpenAI

client = OpenAI(api_key='sk-proj-svRGS9g6MxTgMA5L1UizT3BlbkFJXKXfXJ9bycvkpn9uvmKV')

def gpt(text):
        response = client.chat.completions.create(
        model = 'gpt-3.5-turbo',                            #Модель можно выбрать на свой вкус
        messages = [
            {"role": "system", "content" : "You are a bot assistant imitating a real person."},        #Тут задаётся личность нейросети. Натсраивается по своему усмотрению (на английском языке) 
            {'role': 'user', 'content': f'{text}'}, 
            {'role': 'assistant','content': f'{con} {con2}' }                                    #Запрос от пользователя, который и обрабатывает нейросеть
        ],
        temperature = 0.5                    #Количество вольности нейросети от 0 до 1. Чем больше, тем больше выразительности и воды
        )

        english_text = response.choices[0].message.content
    
        return english_text