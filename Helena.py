import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[2].id)
# print(voices)
engine.setProperty('voice', voices[3].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def greeting():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning")
    elif hour>12 and hour<=18:
        speak("Good afternoon")
    else:
        speak("Good Evening")
    
    speak("I am Helena. What can I do for you?")

def takeCommand():
    # It takes command from user using microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query

if __name__ == "__main__":
    greeting()
    while True:
        query = takeCommand().lower()

        if "wikipedia" in query:
            speak("Searching Wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to Wikipedia")
            speak(results)
            print(results)
        elif "exit" in query:
            exit(1)
        
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        
        elif "open facebook" in query:
            webbrowser.open("facebook.com")
        
        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")

        elif "play music" in query:
            music_dir = 'E:\\Fast NUCES\\1st Year\\1st Semester\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
        elif "the developer" in query:
            webbrowser.open("https://github.com/DaniyalIAhmed")
        else:
            speak("That functionality is not available yet. Please note that I am still under development. This support will last on May 30th, 2026")