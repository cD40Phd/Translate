# Перевод текста с помощью Google Translate API в Python
# https://dev-gang.ru/article/perevod-teksta-s-pomosczu-google-translate-api-v-python-ahgm88wx1k/ 

from googletrans import Translator
import datetime

translator = Translator()
data_log = datetime.date.today()

# Перевод текстовых документов
f = open('text.txt', 'r')  # 'test.txt'
if f.mode == 'r':                                       # находится ли файл в режиме «чтения», используя свойство mode:
    contents = f.read()
#print(contents)
file_translate = Translator()
result = translator.translate(contents, dest='ru')
print(result.text)
with open('C:\\Users\\Dmitry\\Documents\\MEGA\\MEGAsync\\Translate\\Python_translate.txt', 'a+', encoding='utf8') as f:
    f.write(data_log.strftime('%d-%m-%Y') + '\n' + result.text + '\1\n\r') # добавляем перевод в файл на рабочем столе
    