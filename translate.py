from googletrans import Translator

text = open('speechtotextfromvoice.txt').read()
print(text)

#text = "Please translate this text to French."
destination_language = {
    # 'Spanish' : 'es',
    # 'Bulgarian' : 'bg',
    # 'Russian' : 'ru',
    'French' : 'fr' 
}

translator = Translator()
for key, value in destination_language.items():
    print(translator.translate(text,dest=value).text)
with open("translated.txt","a") as f:
    f.write(translator.translate(text,dest=value).text)
