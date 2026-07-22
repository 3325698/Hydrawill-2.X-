import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("🎤 Speak now...")
    recognizer.adjust_for_ambient_noise(source, duration=1)

    audio = recognizer.listen(source)

try:
    text = recognizer.recognize_google(audio)
    print("\nYou said:", text)

except sr.UnknownValueError:
    print("Sorry, I couldn't understand you.")

except sr.RequestError:
    print("Internet connection error.")
