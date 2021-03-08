import pyttsx3
import speech_recognition as sr
from Wikipedia import Wikipedia
from base import greet, introduction, current_time
import webbrowser as web
import re
import pywhatkit
import os
import Calculator
import pyjokes
import pywintypes
from win10toast import ToastNotifier

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def is_url(url):
    regex = r"([A-Za-z]*\.[a-z])\w+"
    url = re.search(regex, url)
    return url


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def open_url(url, web):
    if is_url(url):
        speak("Opening " + url)
        web.open(url)


def init():
    # speak(greet("Ashik"))
    # speak("Hey, It's me Jarvis. How may I help you?")
    toast = ToastNotifier()
    toast.show_toast("Jarvis", "Hey, I am ready for your help.", duration=5)
    os.chdir(r"C:\MyData\Python\AI\Jarvis")


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print("User said: " + command)
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
            else:
                command = 'wait'
    except:
        command = 'wait'
    return command


if __name__ == "__main__":
    init()
    while True:
        query = take_command()
        if 'who is' in query:
            speak("Searching Wikipedia..")
            speak(Wikipedia(query).data)
        elif 'search on youtube about' in query:
            query = query.replace('search on youtube about', '')
            speak("Opening youtube with search results")
            # web.register('chrome', None, web.BackgroundBrowser(chrome_path))
            # web = web.get('chrome')
            web.open('https://youtube.com/results?search_query={}'.format(query.strip().replace(' ', '+')))

        elif 'search' in query:
            query = query.replace('search', '')
            result = pywhatkit.search(query)
            print(result)
            speak(result)
        elif 'in chrome' in query:
            web.register('chrome', None, web.BackgroundBrowser(chrome_path))
            web = web.get('chrome')
            query = query.replace('open', '')
            query = query.replace('in chrome', '')
            open_url(query, web)

        elif 'open' in query:
            query = query.replace("open", "")
            query = query.strip()
            print(query)
            if is_url(query):
                speak("Opening " + query)
                web.open(query)
            else:
                query = query.replace(" ", "")
                if os.system(query):
                    speak("Opened " + query)
        elif 'play' in query:
            query = query.replace("play", "")
            pywhatkit.playonyt(query)
        elif 'calculate' in query:
            query = query.replace("calculate", "")
            result = Calculator.calculate(query)
            print(result)
            speak(result)
        elif 'current time' in query:
            speak("It's " + current_time())
        elif 'introduce yourself' in query or 'who are you' in query or 'who you are' in query:
            speak(introduction())
        elif 'joke' in query:
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)
        elif 'exit' in query or 'quit' in query or 'close your self' in query or 'close yourself' in query:
            speak("Good Bye, Ashik")
            quit()
        elif 'wait' in query:
            pass
