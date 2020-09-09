from googletrans import Translator
translator = Translator()

# print(googletrans.LANGUAGES) #Список поддерживаемых языков

# intext = 'Ellipsis'
t = " "
t = list(help(str))
intext = print(t)
# type(intext)  

result = translator.translate(intext, dest='ru')
print(result.text)
 