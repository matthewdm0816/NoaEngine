from flask import Flask, render_template, request, jsonify, url_for
from config import Config, Prompts

import json
import pretty_errors

if Config.llm_type == 'azure_gpt3_5':
    from llm_az import ChatGPT3_5
    endpoint, key = open('azgpt.key').readlines()
    theLLM = ChatGPT3_5(endpoint.strip(), key.strip())
    print('Welcome to Azure GPT-3.5!')
    theLLM.messages[0]['content'] = Prompts.system
    #print(theLLM.forward('Hello World'))
else:
    raise Exception('Not implemented yet.')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', config=Config)

@app.route('/command', methods=['POST'])
def command():
    user_input = request.json.get('command')
    # 处理命令，返回响应
    #response = f"{Config.dm_name}收到了命令：{user_input}"
    response = theLLM.forward(user_input)
    return jsonify({'response': response})

@app.route('/load_conversation', methods=['GET'])
def load_conversation():
    with open('conversation.json', 'r') as file:
        conversation = json.load(file)
    return jsonify(conversation)

if __name__ == "__main__":
    app.run(debug=True)
