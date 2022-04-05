import speech_recognition as sr
import pyttsx3
import wikipedia
import pywhatkit

listener = sr.Recognizer()
player = pyttsx3.init()


def listen():
    with sr.Microphone() as input_speech:
        print('I am ready, pls start speaking ....')
        voice_content = listener.listen(input_speech)
        text_command = listener.recognize_google(voice_content)
        text_command = text_command.lower()
        print(text_command)

        return text_command


def speak(text):
    player.say(text)
    player.runAndWait()


def run_voice_bot():
    command = listen()
    if "mimi" in command:
        command = command.replace("mimi", "")
        if "what is" in command:
            command = command.replace("what is", "")
            info = wikipedia.summary(command, 5)
            speak(info)
        elif "who is" in command:
            command = command.replace("who", "")
            info = wikipedia.summary(command, 5)
            speak(info)
        elif "where is" in command:
            command = command.replace("where is", "")
            info = wikipedia.summary(command, 5)
            speak(info)
        elif "how" in command:
            command = command.replace("how", "")
            info = wikipedia.summary(command, 5)
            speak(info)
        elif "play" in command:
            command = command.replace("play", "")
            pywhatkit.playonyt(command)
        else:
            speak("I am unable to find what you are looking for")


run_voice_bot()
