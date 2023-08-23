# # I typed a command in terminal name "pip3 install speechrecognition"
# #  then I used a library "pip3 install pyttsx3" and "________________ pyaudio"

# import speech_recognition
# import pyttsx3
# import pyaudio
# import string

# Recognizer = speech_recognition.Recognizer()
# # What you exactly saying in the microphone.
# while True:
#     try:
#         with speech_recognition.Microphone() as mic:
#             Recognizer.adjust_for_ambient_noise(mic, duration=0.2)
#             audio = Recognizer.listen(mic)
#             text = Recognizer.recognize_bing(audio)
#             text= text.lower()

#             print(f"Recognized {text}")

#     except speech_recognition.UnknownValueError():
#         Recognizer= speech_recognition.Recognizer()
#         continue

import speech_recognition
import pyttsx3
import pyaudio

Recognizer = speech_recognition.Recognizer()

# What you are exactly saying into the microphone.
while True:
    try:
        with speech_recognition.Microphone() as mic:
            Recognizer.adjust_for_ambient_noise(mic, duration=0.1)
            audio = Recognizer.listen(mic)
            text = Recognizer.recognize_google(audio)
            text = text.lower()

            print(f"Recognized: {text}")

    except speech_recognition.UnknownValueError:
        continue

# import speech_recognition as 

# Recognizer = sr.Recognizer()

# # Your Bing API key
# bing_api_key = "YOUR_BING_API_KEY"

# # What you are saying into the microphone
# while True:
#     try:
#         with sr.Microphone() as mic:
#             Recognizer.adjust_for_ambient_noise(mic, duration=0.2)
#             audio = Recognizer.listen(mic)
#             text = Recognizer.recognize_bing(audio, key=bing_api_key)
#             text = text.lower()

#             print(f"Recognized: {text}")

#     except sr.UnknownValueError:
#         continue
