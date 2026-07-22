import speech_recognition as sr
from config import AUDIO_FILE


def speech_to_text():

    recognizer = sr.Recognizer()

    with sr.AudioFile(AUDIO_FILE) as source:

        audio = recognizer.record(source)

    try:

        text = recognizer.recognize_google(audio)

        return text

    except sr.UnknownValueError:

        return ""

    except Exception as e:

        print(e)

        return ""