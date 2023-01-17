import pyttsx3
import speech_recognition as sr
from questions import *
from questions import get_team

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
                if team == 'koniec':
                    exit(0)
                path = get_team(team)
                if path is None:
                    print('I don\'t understand...')
                    engine.runAndWait()
                else:
                    while True:
                        print('Clearing...')
                        recognizer.adjust_for_ambient_noise(source, duration=0.5)
                        print('Waiting for statistics...')
                        recordedAudio = recognizer.listen(source, 60, 10)
                        try:
                            command = recognizer.recognize_google(recordedAudio, language='pl_PL')
                            if command == 'koniec':
                                exit()
                            if command is None:
                                print('I don\'t have such information...')
                                engine.runAndWait()
                                break
                            elif command.lower() == 'zmień drużynę':
                                print("Choose different team...")
                                engine.runAndWait()
                                break
                            else:
                                answer = get_answer(command, path[0], path[1])
                                if answer is None:
                                    print('I don\'t have such information...')
                                else:
                                    print(answer)
                                    engine.say(answer)
                                    engine.runAndWait()
                        except sr.UnknownValueError:
                            print('nie rozumiem')
                        except sr.RequestError as e:
                            print('error:', e)
            except sr.UnknownValueError:
                print('I don\'t understand...')
            except sr.RequestError as e:
                print('error:', e)

if __name__ == '__main__':
    while True:
        cmd()
