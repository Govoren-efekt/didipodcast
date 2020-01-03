from gtts import gTTS
import os

# mytext = "Talk to me. Quick round fox jump over the lazy dog. This is a very long sentence."
# language ='en'
# output = gTTS(text=mytext, lang=language, slow=False)
# output.save("lastoutput.mp3")
#os.system("start lastoutput.mp3")


# open the text file created by speechtotext.py 
with open("translated.txt") as file:
	t = gTTS(file.read(), "fr")
# save the speech into an mp3 format
t.save("texttospeech.mp3")

import subprocess
audio_file = "/Users/svetlanavidenova/hellodidi/texttospeech.mp3"

return_code = subprocess.call(["afplay", audio_file])