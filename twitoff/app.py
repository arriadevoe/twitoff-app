from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        # You can add any HTML/CSS to this
        return f'Index page'

    @app.route('/hello')
    def hello():
        return 'Hello, World!'
    
    return app