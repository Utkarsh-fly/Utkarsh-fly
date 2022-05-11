import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser

engine=pyttsx3.init('sapi5')

voices = engine.getProperty("voices")
print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def jarvisvoice(audio):
    engine.say(audio)
    engine.runAndWait()

   # jarvisvoice("hello utkarsh sahu nice to meet you. I am Your virtual asistance.")

def wish():
    h=int(datetime.datetime.now().hour)
    print("----->",h)
    if(h>=0 and h<12):
            jarvisvoice("Good Morning utkarsh :)")
    elif h>=12 and h<18:
        jarvisvoice("Good AfterNoon :)")
    else:
        jarvisvoice("Good Evening utkarsh,:)")


def takecommand():
    r =sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening Utkarsh.........")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognizing.........")
        query= r.reconize_google(audio,language='en-in')
        print("Query",query)

    except Exception as e:
            print(e)
            print("Say that again please...")
            return "None"
    return query

    wish()

    status=True
    while status:
        query=takecommand().lower()

        if "what is" in query or "who is" in query:
            jarvisvoice("Searching in Wikipedia....please wait")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=4)
            print(results)
            jarvisvoice("According to wikipedia...")
            jarvisvoice(results)
        elif "open google" in query:
            webbrowser.open("google.com")
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open gmail" in query:
            webbrowser.open("gmail.com")


