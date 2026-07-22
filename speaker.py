from gtts import gTTS
from playsound import playsound
import os
import tempfile
import threading
import re


def _clean(text):

    import re 

    text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)
    text = re.sub(r"\*(.*?)\*", r"\1", text)

    text = text.replace("#", "")
    text = text.replace("•", "")
    text = text.replace("```", "")

    return text.strip() 


def _speak(text):

    text = _clean(text)

    tts = gTTS(
        text=text,
        lang="en",
        slow=False
    )

    temp = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".mp3"
    )

    temp.close()

    tts.save(temp.name)

    playsound(temp.name)

    os.remove(temp.name)


def speak(text):

    threading.Thread(
        target=_speak,
        args=(text,),
        daemon=True
    ).start()