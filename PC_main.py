from PC_fun import di
import pyaudio
import pyttsx3
import pyautogui
import speech_recognition as sr
import datetime


engine=pyttsx3.init('dummy')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning again Sir")

    elif hour>=12 and hour<18:
        speak("Good Afternoon again Sir")   

    else:
        speak("Good Evening again Sir")
    
    
def takeCommand():

    while True:
        r=sr.Recognizer()

        with sr.Microphone() as source:
            print('listening...')
            r.pause_threshold=1
            r.energy_threshold=2000
            audio=r.listen(source)
        
        try:
            print("Recognizing....")
            query = r.recognize_google(audio,language='en-in')
           
            print(f"User said: {query}\n")
            return query
        except Exception as e:
            print("Say That again please...")

    

if __name__ == "__main__":
    c=1
    wishMe()
    
    speak("This is  your personal assistant  how can I help you:")
    while(c):
        
        query=takeCommand()
        query=query.lower()
        #print(query)
    
        for x in di:
            if x in query:
                di[x]()
        a=input("Press E to exit or C to continue:").lower()
        if 'e'==a:
            c=0
        elif'c' ==a:
            wishMe()
            speak("How can I help you:")
            c=1

           
