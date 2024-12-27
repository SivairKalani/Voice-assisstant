import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os




engine = pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice' , voices[1].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takecommand():
    r=sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening.....")
        audio = r.listen(source)
    try:
        print("Wait for a few moments")
        query=r.recognize_google(audio,language="en-in")
        print("you said: ", query)
    except Exception as e :
        print(e)
        speak("Say that Again Please ")
        return None

if __name__ == "__main__":
    
    takecommand()

    while True :
      
        query = takecommand().lower()

        if"wikipedia" in query:
            speak("Searching in wikipedia")
            query=query.replace("wikipedia" ,"")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia ")
            speak(results)
            print(results)

        elif"open youtube" in query:
            speak("opening Boss")
            webbrowser.open("youtube.com")
        elif "open google" in query:
            speak("opening Boss")
            webbrowser.open("google.com")

        elif "open code"in query:
            speak("opening Boss")
            codepath = "C:\\Users\\Murali\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif "open chrome"in query:
            speak("opening Boss")
            chromepath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chromepath)
