import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print('tell me something : ')
    audio = r.listen(source, timeout = 10)

    try: 
        text = r.recognize_google(audio)
        print('You said:{}'.format(text))
        if str is bytes: 
            result = u"{}".format(text).encode("utf-8")
        else: 
            result = "{}".format(text)
# stores the speech into a text file and creates the file called speechtotextfromvoice.txt
        with open("speechtotextfromvoice.txt","a") as f:
            f.write(result)
    except:
        print('Sorry could not recognize your voice')