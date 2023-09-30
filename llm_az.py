import requests
import json

class ChatGPT3_5:
    def __init__(self, endpoint, apiKey):
        self.endpoint = endpoint
        self.header = {
            "Content-Type": "application/json",
            "api-key": apiKey
        }
        self.messages = [{"role":"system","content":"You are a smart robot girl."}]
        self.body = {
            "messages": None,
            "max_tokens": 256,
            "temperature": 0.7,
            "top_p": 1,
            "frequency_penalty": 0,
            "presence_penalty": 0,
            "stop": None
        }
    
    def forward(self, x = 'Hello World'):
        self.body['messages'] = self.messages + [{"role":"user","content":x}]
        self.body['max_tokens'] = 3900 - len(x)
        if (self.body['max_tokens'] < 0):
            raise Exception('The input text is too long.')
        response = requests.post(self.endpoint, headers=self.header, data=json.dumps(self.body))
        return response.json()['choices'][0]['message']['content']

if __name__ == "__main__":
    fptxt = open('azgpt.key').readlines()
    endpoint = fptxt[0].strip()
    apiKey = fptxt[1].strip()
    chat = ChatGPT3_5(endpoint, apiKey)
    print(chat.forward('Hello World'))