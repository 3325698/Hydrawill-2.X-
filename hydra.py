import os
from dotenv import load_dotenv
import google.generativeai as genai

from config import MODEL_NAME

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(MODEL_NAME)

chat = model.start_chat(
    history=[
        {
            "role": "user",
            "parts": ["""
Your name is HydraWill 2.X.

You are a friendly AI assistant built for exhibitions.

Rules:

1. Keep answers short by default, i.e. of 3 lines maximum. 
2. Use numbered lists whenever suitable.
3. Explain in detail only when asked.
4. Be friendly and professional.
5. Encourage water conservation naturally when relevant.
6. Use simple English.
7. Remember the conversation until the program closes.
"""]
        },
        {
            "role": "model",
            "parts": [
                "Understood. I will follow these rules."
            ]
        }
    ]
)

def ask(question: str) -> str:
    """Send a question to Gemini and return the answer."""

    response = chat.send_message(question)

    return response.text