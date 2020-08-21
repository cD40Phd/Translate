from googletrans import Translator
translator = Translator()

# print(googletrans.LANGUAGES) #Список поддерживаемых языков

intext = 'Commodities'

result = translator.translate(intext, dest='ru')
print(result.text)
