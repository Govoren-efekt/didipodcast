import speech_recognition as sr

r = sr.Recognizer()

# reads and accepts only .wav file from the current directory
with sr.AudioFile("daughter2.wav") as source:
    audio = r.record(source)
print(audio)
text = r.recognize_google(audio, language = 'en', show_all=False)
if str is bytes: 
     result = u"{}".format(text).encode("utf-8")
else: 
     result = "{}".format(text)
# stores the speech into a text file and creates the file called outputs.txt
with open("peechtotextfromwav.txt","a") as f:
     f.write(result)
# prints out as text what has been read vocally
print('You said:{}'.format(text))
