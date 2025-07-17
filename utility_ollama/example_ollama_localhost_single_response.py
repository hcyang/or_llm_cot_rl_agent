
import os

import requests
import json

# REFERENCE: https://github.com/ollama/ollama
# REFERENCE: https://github.com/ollama/ollama/blob/main/docs/api.md

headers = {
    'Content-Type': 'application/json'
}

url_generate = 'http://localhost:11434/api/generate'
payload_prompt = {
    'model': 'llama3.2',
    # 'messages': messages,
    'prompt': 'What is water made of? Respond using JSON',
    "stream": False
}

message = {
    'role': 'user',
    'content': 'What is water made of?'
}
messages = [
    message,
]

response_generate = requests.post(url_generate, headers=headers, data=json.dumps(payload_prompt))
print(response_generate.content)

if response_generate.status_code == 200:
    print('SUCCESS:', json.loads(response_generate.content))
    # print('SUCCESS:', response_generate.status_code)
else:
    print('ERROR:', response_generate.status_code)
