import pyttsx3
import speech_recognition as sr
from questions import *
from questions import get_team

engine = pyttsx3.init()
# voices = engine.getProperty('voice')
# engine.setProperty('voice', voices[1])
recognizer = sr.Recognizer()
recognizer.dynamic_energy_threshold = False

def cmd():

    team = None
    while True:
        with sr.Microphone() as source:
            print('Clearing...')
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            print('Listening...')
            recordedAudio = recognizer.listen(source, 10)

            try:
                team = recognizer.recognize_google(recordedAudio, language='pl_PL')
            except Exception as ex:
                print(ex)
            path = get_team(team)
            print("path " + str(path))
            if path is None:
                engine.say('Nie rozumiem')
                break

            try:
                recordedAudio = recognizer.listen(source, 10)
                command = recognizer.recognize_google(recordedAudio, language='pl_PL')
            except Exception as ex:
                print(ex)

            answer = get_answer(command, path)
            engine.say(answer)
            engine.runAndWait()


while True:
    cmd()
# import speech_recognition as sr
# r = sr.Recognizer()
# with sr.Microphone() as source:
#    audio = r.listen(source)
#
# print("Google Speech Recognition thinks you said " + r.recognize_google(audio, language="pl"))
