import requests
import json


class HuggingChat:

    def __init__(self):
        self._BASE: str = "https://huggingface.co/chat/conversation/"
        self._SETTINGS_URL: str = "https://huggingface.co/chat/settings/"
        self.settings_data = {
            "shareConversationsWithModelAuthors": False,
            "ethicsModalAcceptedAt": "",
            "ethicsModalAccepted": True,
            "activeModel": "OpenAssistant/oasst-sft-6-llama-30b-xor"
        }
        self.get_id_json = {"model": "OpenAssistant/oasst-sft-6-llama-30b-xor"}
        self.json = {
            "inputs": "hello",
            "parameters": {
                "temperature": 0.9,
                "truncate": 1000,
                "max_new_tokens": 1024,
                "stop": ["</s>"],
                "top_p": 0.95,
                "repetition_penalty": 1.2,
                "top_k": 50,
                "return_full_text": False
            },
            "stream": False,
            "options": {
                "id": "68e2cf66-88d9-4aa0-817c-a8a03040d531",
                "is_retry": False,
                "use_cache": False
            }
        }
        self._session = requests.Session()
        self._settings()
        self._ID: str = self._get_id()

    def _settings(self):
        return self._session.post(self._SETTINGS_URL,
                                  data=self.settings_data).content

    def _get_id(self):
        resp = self._session.post(self._BASE, json=self.get_id_json).content
        return json.loads(resp)["conversationId"]

    def ask(self, prompt):
        self.json["inputs"] = prompt
        return self._session.post(self._BASE + self._ID, json=self.json).text


chat = HuggingChat()
print(chat.ask("hello"))
