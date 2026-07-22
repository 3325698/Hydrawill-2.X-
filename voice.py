import sounddevice as sd
import soundfile as sf
import numpy as np
import time

from config import (
    SAMPLE_RATE,
    CHANNELS,
    AUDIO_FILE,
    SILENCE_TIMEOUT,
    MAX_RECORDING_TIME
)


def record():

    print("🎙 Listening...")

    recording = []

    silence_start = None

    start = time.time()

    def callback(indata, frames, t, status):

        nonlocal silence_start

        volume = np.linalg.norm(indata)

        recording.append(indata.copy())

        if volume < 0.01:

            if silence_start is None:

                silence_start = time.time()

        else:

            silence_start = None

    with sd.InputStream(
        samplerate=SAMPLE_RATE,
        channels=CHANNELS,
        callback=callback
    ):

        while True:

            elapsed = time.time() - start

            if elapsed >= MAX_RECORDING_TIME:
                print("⏹ Maximum recording time reached.")
                break

            if (
                silence_start is not None and
                time.time() - silence_start >= SILENCE_TIMEOUT
            ):
                print("🤫 Silence detected.")
                break

            time.sleep(0.1)

    audio = np.concatenate(recording)

    sf.write(
        AUDIO_FILE,
        audio,
        SAMPLE_RATE
    )

    print("✅ Recording saved.")