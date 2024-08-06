
import os
from dotenv import load_dotenv
import json
import requests


load_dotenv()

EDEN_API_KEY = os.getenv("EDEN_API")


class Bot:
    def __init__(self) -> None:
        self._history = []
    
    def chat(self, prompt):
        headers = {"Authorization": f"Bearer {EDEN_API_KEY}"}

        url = "https://api.edenai.run/v2/text/chat"
        payload = {
            "providers": "openai/gpt-4o",
            "text": prompt,
            "chatbot_global_action": """You are a teacher assistant that is quite funny and can help out with programming tasks.
            Don't give out the full answer, instead ask a question back. Your name is RO BÅT.
    .   """,
            "previous_history": self._history,
            "temperature": 0.5,
            "max_tokens": 500,
        }

        response = requests.post(url, json=payload, headers=headers)
        # print(response.json())
        answer = json.loads(response.text)['openai/gpt-4o']['generated_text']
        
        self._history.append({"role": "user", "message": prompt})
        self._history.append({"role": "assistant", "message": answer})

        return answer

