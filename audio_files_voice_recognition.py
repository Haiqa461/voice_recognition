import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# Path to the audio file
audio_file_path = "D:\Recording.wav"

# Load the audio file
with sr.AudioFile(audio_file_path) as source:
    audio = recognizer.record(source)  # Record the audio from the file

# Convert audio to text using Google Web Speech API
try:
    text = recognizer.recognize_google(audio)
    print(f"Recognized Text: {text}")
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print(f"Could not request results from Google Web Speech API; {e}")

