from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    # You can add any HTML/CSS to this
    return f'Index page'

@app.route('/hello')
def hello():
    return 'Hello, World!'