import requests
import json

class HuggingChat:
    def __init__(self):
        self._BASE:str="https://huggingface.co/chat/conversation/"
        self._ID:str=self._get_id()
        self.json={
            "inputs": "",
            "parameters": {
                "temperature": 0.9,
                "top_p": 0.95,
                "repetition_penalty": 1.2,
                "top_k": 50,
                "truncate": 1024,
                "watermark": False,
                "max_new_tokens": 1024,
                "stop": ["<|endoftext|>"],
                "return_full_text": False
            },
            "stream": False,
            "options": {
                "use_cache": False
            }
        }
        self._session=requests.Session()
    
    def _get_id(self):
        resp=requests.post(self._BASE).content
        return json.loads(resp)["conversationId"]

    def ask(self,prompt):
        self.json["inputs"]=prompt
        return self._session.post(self._BASE+self._ID,json=self.json).text

chat=HuggingChat()
print(chat.ask("Hello"))
        
