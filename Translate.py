
from googletrans import Translator
import datetime
import re
import os

translator = Translator()
data_log = datetime.date.today()
print(os.getcwd())
# Перевод текстовых документов
f = open('text.txt', 'r')  # 'test.txt'
if f.mode == 'r':                                       # находится ли файл в режиме «чтения», используя свойство mode:
    contents = f.read()
contents = re.sub(r"\n{1,}","\n",contents)              # удаляем пустые строки

file_translate = Translator()
result = translator.translate(contents, dest='ru')
print('---------------------------------------------------------------------------------------------------------------')
print(result.text)
with open('C:\\Users\\Dmitry\\Documents\\MEGA\\MEGAsync\\Translate\\Python_translate.txt', 'a+', encoding='utf8') as f:
    f.write(data_log.strftime('%d-%m-%Y') + '\n' + result.text + '\1\n\r') # добавляем перевод в файл на рабочем столе

with open('C:\\Users\\Dmitry\\Documents\\MEGA\\MEGAsync\\Translate\\Original_translate.txt', 'a+', encoding='utf8') as f:
    f.write(data_log.strftime('%d-%m-%Y') + '\n' + contents + '\1\n\r') # добавляем перевод в файл на рабочем столе
