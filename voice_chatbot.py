import speech_recognition as sr
import pyttsx3
import nltk
from nltk.chat.util import Chat, reflections

# Initialize NLTK chatbot
pairs = [
    # Define your chatbot's responses here
    ("hi", ["Hello!", "Hi there!"]),
    ("how are you", ["I'm just a bot, but I'm here to help!", "I'm good, thank you."]),
    # Add more pairs
]

bot = Chat(pairs, reflections)

# Initialize speech recognition
recognizer = sr.Recognizer()

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Main loop
while True:
    try:
        # Capture voice input
        with sr.Microphone() as mic:
            print("Say something...")
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)
            user_input = recognizer.recognize_google(audio)

            # Process user input using the chatbot
            response = bot.respond(user_input)
            print("Chatbot:", response)

            # Convert chatbot response to speech and play
            engine.say(response)
            engine.runAndWait()

    except sr.UnknownValueError:
        print("Sorry, I couldn't understand that. Could you please repeat?")
    except sr.RequestError as e:
        print(f"Error with the request: {e}")
