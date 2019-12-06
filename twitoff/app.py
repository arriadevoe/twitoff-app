from flask import Flask, render_template

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        # You can add any HTML/CSS to this
        return f'Index page'

    @app.route('/hello')
    def hello():
        return render_template('base.html', title='Hello Page')
    
    return app