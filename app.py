from flask import Flask, render_template, request
import markdown
from markupsafe import Markup
from hydra import ask
from engine import process_voice
from speaker import speak 

app = Flask(__name__)

# Stores the current conversation
conversation = []


@app.route("/", methods=["GET", "POST"])
def home():

    global conversation

    if request.method == "POST":

        question = request.form.get("question", "").strip()

        # Voice input
        if question == "__VOICE__":

            result = process_voice()

            conversation.append({
                "user": result["question"] if result["question"] else "🎙 Voice Input",
                "bot": result["answer"]
            })

        # Typed input
        elif question:

            raw_answer = ask(question)

            #Speak the answer 
            #speak(raw_answer)

            answer = Markup(
                markdown.markdown(raw_answer)
            )

            conversation.append({
                "user": question,
                "bot": answer
            })

    return render_template(
        "index.html",
        conversation=conversation
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )