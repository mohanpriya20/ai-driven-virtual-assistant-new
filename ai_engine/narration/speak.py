from gtts import gTTS
import os

def speak(text):
    tts = gTTS(text)
    tts.save("output.mp3")
    os.system("start output.mp3")