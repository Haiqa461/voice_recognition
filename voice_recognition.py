# I typed a command in terminal name "pip3 install speechrecognition"
#  then I used a library "pip3 install pyttsx3" and "________________ pyaudio"

import speech_recognition
import pyttsx3
import pyaudio
import string

Recognizer = speech_recognition.Recognizer()
# What you exactly saying in the microphone.
while True:
    try:
        with speech_recognition.Microphone() as mic:
            Recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = Recognizer.listen(mic)
            text = Recognizer.recognize_bing(audio)
            text= text.lower()

            print(f"Recognized {text}")

    except speech_recognition.UnknownValueError():
        Recognizer= speech_recognition.Recognizer()
        continue