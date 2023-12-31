from flask import Flask, render_template, request, jsonify, url_for
from config import Config
import json
import pretty_errors

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html', config=Config)

@app.route('/command', methods=['POST'])
def command():
    user_input = request.json.get('command')
    # 处理命令，返回响应
    response = f"{Config.dm_name}收到了命令：{user_input}"
    return jsonify({'response': response})

@app.route('/load_conversation', methods=['GET'])
def load_conversation():
    with open('conversation.json', 'r') as file:
        conversation = json.load(file)
    return jsonify(conversation)

if __name__ == "__main__":
    app.run(debug=True)
