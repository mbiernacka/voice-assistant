import pyttsx3
import speech_recognition as sr
from questions import *
from questions import get_team


def cmd():

    engine = pyttsx3.init()
    engine.setProperty('rate', 170)
    recognizer = sr.Recognizer()
    recognizer.dynamic_energy_threshold = False

    while True:
        with sr.Microphone() as source:
            print('Czyszczenie...')
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print('Podaj nazwę drużyny...')
            recordedAudio = recognizer.listen(source, 60, 10)
            try:
                team = recognizer.recognize_google(recordedAudio, language='pl_PL')
                if team == 'koniec':
                    exit(0)
                path = get_team(team)
                if path is None:
                    print('Nie rozumiem...')
                    engine.runAndWait()
                else:
                    print("\nDrużyna: " + path[1])
                    while True:
                        print('Czyszczenie...')
                        recognizer.adjust_for_ambient_noise(source, duration=1)
                        print('Podaj statystykę...')
                        recordedAudio = recognizer.listen(source, 60, 10)
                        try:
                            command = recognizer.recognize_google(recordedAudio, language='pl_PL')
                            if command == 'koniec':
                                exit()
                            if command is None:
                                print('Nie posiadam takiej informacji...')
                                engine.runAndWait()
                                break
                            elif command.lower() == 'zmień drużynę':
                                print("Wybierz inną drużynę...")
                                engine.runAndWait()
                                break
                            else:
                                answer = get_answer(command, path[0], path[1])
                                if answer is None:
                                    print('Nie posiadam takiej informacji...')
                                else:
                                    print(answer)
                                    engine.say(answer)
                                    engine.runAndWait()
                        except sr.UnknownValueError:
                            print('Nie rozumiem...')
                        except sr.RequestError as e:
                            print('error:', e)
            except sr.UnknownValueError:
                print('Nie rozumiem...')
            except sr.RequestError as e:
                print('error:', e)

if __name__ == '__main__':
    while True:
        cmd()
