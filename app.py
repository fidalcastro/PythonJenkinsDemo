from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/greet', methods=['GET'])
def greet():
    args = request.args
    name = args.get('name')

    return f'Hello, {name}!'
