import uuid
from flask import Flask, render_template
from .models import DB, User, Tweet

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_db.sqlite'
    DB.init_app(app)

    @app.route('/')
    def index():
        # You can add any HTML/CSS to this
        # We can also add a test user like so:
        # rand_name = str(uuid.uuid4)
        # rand_user = User(name=rand_name)
        # DB.session.add(rand_u)
        # DB.session.commit()
        return f'Index page'

    @app.route('/hello')
    def hello():
        return render_template('base.html', title='Hello Page')
    
    return app