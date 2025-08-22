import sys, re, os
from gigachat import GigaChat
from gigachat.models import Chat, Messages, MessagesRole
import gigachat.context
import credentials


giga = GigaChat(
    credentials=credentials.api_key
)

i = 1
while i:
    question = input("Спросите у GigaChat (0 для выхода из программы): ")
    if question == "0":
        break
    response = giga.chat(question)
    print("Ответ модели:")
    print(response.choices[0].message.content)
    print("-----------------------------------------------------------------")