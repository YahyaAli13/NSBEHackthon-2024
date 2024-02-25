import speech_recognition as sr
import cohere
import pyttsx3
import random

#Initialize the Cohere client with the API key
co = cohere.Client('8MYY4YXA4Ci1ne6MPRSCEHUgX1POwIpV6rLmMj2N')

#Initialize text-to-speech engine and set it to a female voice
tts_engine = pyttsx3.init()
voices = tts_engine.getProperty('voices')
female_voice_index = 1  
tts_engine.setProperty('voice', voices[female_voice_index].id)

def speak(text):
    """Convert text to speech."""
    tts_engine.say(text)
    tts_engine.runAndWait()

def audio_to_text():
    """Convert spoken audio from the user into text, with retries for unclear input."""
    r = sr.Recognizer()
    while True:  #Loop until a successful recognition
        with sr.Microphone() as source:
            print("Please speak now...")
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio)
                print("You said: " + text)
                return text
            except sr.UnknownValueError:
                speak("Sorry, I couldn't understand that. Can you please repeat?")
            except sr.RequestError as e:
                speak("Sorry, I'm having trouble with my connection. Please try again.")
                print(f"Could not request results; {e}")
                break  #Exit the loop if there's a connection issue

def assess_urgency(condition):
    """Assess the urgency based on the patient's condition."""
    urgency_scale = {
        "bleeding": 5,
        "severe pain": 5,
        "high fever": 4,
        "fever": 3,
        "cough": 2,
        "ache":2,
        "headache": 1
    }
    for key, value in urgency_scale.items():
        if key in condition.lower():
            return value
    return 1  #Default to least urgent if condition not recognized

def main():
    names = ["Alice", "Bob", "Charlie", "Diana", "Ethan", "Fiona", "George", "Hannah", "Ivan", "Julia"]
    ages = ["20", "25", "30", "35", "40", "45", "50", "55", "60", "65"]
    feelings_questions = [
        "How are you feeling today?",
        "Is there anything in particular that's bothering you?",
        "Can you describe how you feel right now?",
        "Are you feeling well today?",
        "What's been on your mind regarding your health?"
    ]

    #Select a random name, age, and feelings question
    name = random.choice(names)
    age = random.choice(ages)
    feelings_question = random.choice(feelings_questions)

    speak(f"Hello {name}, are you {age} years old?")
    audio_to_text()  #Just to acknowledge, no need to process the response

    speak(feelings_question)
    audio_to_text()  #Acknowledge feelings, no need to process response

    speak("What's bothering you today?")
    condition = audio_to_text()
    urgency_level = assess_urgency(condition)

    if urgency_level == 5:
        speak("Please go right inside to the nurse's room for immediate care.")
    elif urgency_level == 4:
        speak("Your condition seems to require prompt attention. Your wait time will be short.")
    else:
        speak("Please have a seat in the waiting room. We will take care of you as soon as possible.")

if __name__ == "__main__":
    main()
