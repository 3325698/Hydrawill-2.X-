import edge_tts
import asyncio
import tempfile
import os
import threading
import re
import subprocess


def _clean(text):

    text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)
    text = re.sub(r"\*(.*?)\*", r"\1", text)

    text = text.replace("#", "")
    text = text.replace("•", "")
    text = text.replace("```", "")

    return text.strip()


async def _generate_voice(text, filename):

    voice = "en-IN-NeerjaNeural"

    communicate = edge_tts.Communicate(
        text,
        voice
    )

    await communicate.save(filename)


def _speak(text):

    text = _clean(text)

    temp = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".mp3"
    )

    filename = temp.name
    temp.close()

    asyncio.run(
        _generate_voice(
            text,
            filename
        )
    )

    # Windows audio playback
    subprocess.run(
        [
            "powershell",
            "-c",
            f"(New-Object Media.SoundPlayer '{filename}').PlaySync();"
        ]
    )

    os.remove(filename)


def speak(text):

    threading.Thread(
        target=_speak,
        args=(text,),
        daemon=True
    ).start()