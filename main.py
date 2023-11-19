import pyttsx3 as tts
import speech_recognition as sr

r = sr.Recognizer()
engine = tts.init()

def hear():
    
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    
    try:
        sen = r.recognize_google(audio)
        engine.say(sen)
        engine.runAndWait()
        print("You said" + sen)
    except :
        print("Hmm...Didn't catch that")
    
    if sen.find('exit'):
        return 0
    else:
        return 1
n = 1
while True:
    val = hear()
    if val:
        print("\nexiting")
        break




