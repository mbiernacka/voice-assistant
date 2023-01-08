import pyttsx3
import speech_recognition as sr
from questions import *
from questions import get_team
import sys

engine = pyttsx3.init()
engine.setProperty('rate', 170)
recognizer = sr.Recognizer()
recognizer.dynamic_energy_threshold = False


def cmd():

    while True:
        team = None
        with sr.Microphone() as source:
            print('Clearing...')
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            print('Waiting for the team name...')
            recordedAudio = recognizer.listen(source, 60, 10)
            try:
                team = recognizer.recognize_google(recordedAudio, language='pl_PL')
            except sr.UnknownValueError:
                print('nie rozumiem')
            except sr.RequestError as e:
                print('error:', e)
            path = get_team(team)
            if path[0] is None:
                print('Nie rozumiem')
                engine.say('Nie rozumiem')
                engine.runAndWait()
            else:
                while True:
                    print('Clearing...')
                    recognizer.adjust_for_ambient_noise(source, duration=0.5)
                    print('Waiting for statistics...')
                    recordedAudio = recognizer.listen(source, 60, 10)
                    try:
                        command = recognizer.recognize_google(recordedAudio, language='pl_PL')
                        if command is None:
                            print('Nie posiadam takiej informacji.')
                            engine.say('Nie posiadam takiej informacji.')
                            engine.runAndWait()
                            break
                        elif command.lower() == 'zmień drużynę':
                            engine.say('Wybierz inną drużynę.')
                            engine.runAndWait()
                            break
                        else:
                            answer = get_answer(command, path[0], path[1])
                            engine.say(answer)
                            engine.runAndWait()
                    except sr.UnknownValueError:
                        print('nie rozumiem')
                    except sr.RequestError as e:
                        print('error:', e)


while True:
    cmd()
