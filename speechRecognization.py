import speech_recognition as sr
import pyttsx3 as pt
import pywhatkit as pk

listening = sr.Recognizer()
engine = pt.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
def hear():
    cmd = ''
    try:
        with sr.Microphone() as mic:
            print('listening......')
            voice = listening.listen(mic)
            cmd = listening.recognize_google(voice)
            cmd = cmd.lower()
            if 'bhishma' in cmd:
                cmd = cmd.repalce('bhishma', " ")
                print(cmd)
    except:
        pass
    return cmd
def run():
    cmd = hear()
    print(cmd)
    if 'play' in cmd:
        song = cmd.replace('play', '')
        speak('playing' + song)
        pk.playonyt('playing.....' + song)

run()