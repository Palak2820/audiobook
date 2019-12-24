from gtts import gTTS

import os

f=open('a.txt.txt')

x=f.read()

language ='en'

audio=gTTS(text=x,lang=language,slow= 'false')


audio.save("a.wav")


os.system("a.wav")