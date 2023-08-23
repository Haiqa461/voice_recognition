# # import speech_recognition as sr
# # import pyttsx3
# # import nltk
# # import random
# # import string
# # import warnings
# # from sklearn.feature_extraction.text import TfidfVectorizer
# # from sklearn.metrics.pairwise import cosine_similarity

# # # Download NLTK data
# # nltk.download('punkt')
# # nltk.download('wordnet')

# # # Disable warnings
# # warnings.filterwarnings('ignore')

# # # Initialize NLTK chatbot
# # pairs = [
# #     # Define your chatbot's responses here
# #     ("hi", ["Hello!", "Hi there!"]),
# #     ("how are you", ["I'm just a bot, but I'm here to help!", "I'm good, thank you."]),
# #     # Add more pairs
# # ]

# # bot = nltk.chat.util.Chat(pairs, nltk.chat.util.reflections)

# # # Initialize speech recognition
# # recognizer = sr.Recognizer()

# # # Initialize text-to-speech engine
# # engine = pyttsx3.init()

# # # Open and read the chatbot data file
# # # ... (your chatbot data file reading goes here)

# # # Preprocessing
# # # ... (your LemTokens, LemNormalize functions go here)

# # # Greetings function
# # # ... (your Greetings function goes here)

# # # Vectorization and response generation
# # # ... (your Response function goes here)

# # # Main loop
# # if __name__ == "__main__":
# #     flag = True
# #     print("This is Udemy ChatBOT for answering your questions... ")
# #     while flag:
# #         try:
# #             # Capture voice input
# #             with sr.Microphone() as mic:
# #                 print("Say something...")
# #                 recognizer.adjust_for_ambient_noise(mic, duration=0.1)
# #                 audio = recognizer.listen(mic)
# #                 user_input = recognizer.recognize_google(audio)
                
# #                 # Process voice input
# #                 user_input = user_input.lower()
# #                 if user_input == "bye":
# #                     flag = False
# #                     print("Chatbot: Goodbye!")
# #                 else:
# #                     if Greetings(user_input) is not None:
# #                         print("Chatbot: " + Greetings(user_input))
# #                     else:
# #                         print("You:", user_input)
# #                         print("Chatbot:", end=' ')
# #                         print(Response(user_input))
# #                         sentence_tokens.remove(user_input)
                        
# #                         # Convert chatbot response to speech and play
# #                         engine.say(Response(user_input))
# #                         engine.runAndWait()
                
# #         except sr.UnknownValueError:
# #             print("Sorry, I couldn't understand that. Could you please repeat?")
# #         except sr.RequestError as e:
# #             print(f"Error with the request: {e}")


# import speech_recognition as sr
# import pyttsx3
# import nltk
# import random
# import string
# import warnings
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity

# # Download NLTK data
# nltk.download('punkt')
# nltk.download('wordnet')

# # Disable warnings
# warnings.filterwarnings('ignore')

# # Initialize NLTK chatbot
# pairs = [
#     # Define your chatbot's responses here
#     ("hi", ["Hello!", "Hi there!"]),
#     ("how are you", ["I'm just a bot, but I'm here to help!", "I'm good, thank you."]),
#     # Add more pairs
# ]

# bot = nltk.chat.util.Chat(pairs, nltk.chat.util.reflections)

# # Initialize speech recognition
# recognizer = sr.Recognizer()

# # Initialize text-to-speech engine
# engine = pyttsx3.init()

# # Preprocessing
# Lemmer = nltk.stem.WordNetLemmatizer()

# def LemTokens(tokens):
#     return [Lemmer.lemmatize(token) for token in tokens]

# Remove_Punctuation_from_Dictionary = dict((ord(punctuation), None) for punctuation in string.punctuation)

# def LemNormalize(text):
#     return LemTokens(nltk.word_tokenize(text.lower().translate(Remove_Punctuation_from_Dictionary)))

# # Greetings function
# Greeting_Input = ("hi", "hello", "whats up", "hey", "hi there", "hye", "salam")
# Greeting_Response = ("hi", "hey", "hello", "hi", "salam", "hi there", "whats up")

# def Greetings(scentences):
#     for word in scentences.split():
#         if word.lower() in Greeting_Input:
#             return random.choice(Greeting_Response)

# # Vectorization and response generation
# # ... (your Response function goes here)

# # Main loop
# if __name__ == "__main__":
#     flag = True
#     print("This is Udemy ChatBOT for answering your questions... ")
#     while flag:
#         try:
#             # Capture voice input
#             with sr.Microphone() as mic:
#                 print("Say something...")
#                 recognizer.adjust_for_ambient_noise(mic, duration=0.1)
#                 audio = recognizer.listen(mic)
#                 user_input = recognizer.recognize_google(audio)
                
#                 # Process voice input
#                 user_input = user_input.lower()
#                 if user_input == "bye":
#                     flag = False
#                     print("Chatbot: Goodbye!")
#                 else:
#                     if Greetings(user_input) is not None:
#                         print("Chatbot: " + Greetings(user_input))
#                     else:
#                         print("You:", user_input)
#                         print("Chatbot:", end=' ')
#                         print(Response(user_input))
#                         sentence_tokens.remove(user_input)
                        
#                         # Convert chatbot response to speech and play
#                         engine.say(Response(user_input))
#                         engine.runAndWait()
                
#         except sr.UnknownValueError:
#             print("Sorry, I couldn't understand that. Could you please repeat?")
#         except sr.RequestError as e:
#             print(f"Error with the request: {e}")


import speech_recognition as sr
import pyttsx3
import nltk
import random
import string
import warnings
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download NLTK data
nltk.download('punkt')
nltk.download('wordnet')

# Disable warnings
warnings.filterwarnings('ignore')

# Initialize NLTK chatbot
pairs = [
    # Define your chatbot's responses here
    ("hi", ["Hello!", "Hi there!"]),
    ("how are you", ["I'm just a bot, but I'm here to help!", "I'm good, thank you."]),
    # Add more pairs
]

bot = nltk.chat.util.Chat(pairs, nltk.chat.util.reflections)

# Initialize speech recognition
recognizer = sr.Recognizer()

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Preprocessing
Lemmer = nltk.stem.WordNetLemmatizer()

def LemTokens(tokens):
    return [Lemmer.lemmatize(token) for token in tokens]

Remove_Punctuation_from_Dictionary = dict((ord(punctuation), None) for punctuation in string.punctuation)

def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(Remove_Punctuation_from_Dictionary)))

# Greetings function
Greeting_Input = ("hi", "hello", "whats up", "hey", "hi there", "hye", "salam")
Greeting_Response = ("hi", "hey", "hello", "hi", "salam", "hi there", "whats up")

def Greetings(scentences):
    for word in scentences.split():
        if word.lower() in Greeting_Input:
            return random.choice(Greeting_Response)

# Vectorization and response generation
def Response(user_input):
    response = bot.respond(user_input)
    return response

# Main loop
if __name__ == "__main__":
    flag = True
    print("This is Udemy ChatBOT for answering your questions... ")
    while flag:
        try:
            # Capture voice input
            with sr.Microphone() as mic:
                print("Say something...")
                recognizer.adjust_for_ambient_noise(mic, duration=0.1)
                audio = recognizer.listen(mic)
                user_input = recognizer.recognize_google(audio)
                
                # Process voice input
                user_input = user_input.lower()
                if user_input == "bye":
                    flag = False
                    print("Chatbot: Goodbye!")
                else:
                    if Greetings(user_input) is not None:
                        print("Chatbot: " + Greetings(user_input))
                    else:
                        print("You:", user_input)
                        print("Chatbot:", end=' ')
                        print(Response(user_input))
                        
                        # Convert chatbot response to speech and play
                        engine.say(Response(user_input))
                        engine.runAndWait()
                
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand that. Could you please repeat?")
        except sr.RequestError as e:
            print(f"Error with the request: {e}")
