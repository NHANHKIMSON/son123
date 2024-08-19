from gtts import gTTS
import os

tts = gTTS(text="Hello world", lang='en')
tts.save("output.mp3")
os.system("afplay output.mp3")