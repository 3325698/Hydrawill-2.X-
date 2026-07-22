from voice import record
from speech import speech_to_text
from hydra import ask
from speaker import speak


def process_voice():

    # Record the user's voice
    record()

    # Convert speech to text
    question = speech_to_text()

    if question == "":

        answer = "Sorry, I couldn't understand what you said."

        speak(answer)

        return {
            "question": "",
            "answer": answer
        }

    print(f"User: {question}")

    # Ask Gemini
    answer = ask(question)

    print(f"Hydra: {answer}")

    # Speak the answer
    speak(answer)

    return {
        "question": question,
        "answer": answer
    }
