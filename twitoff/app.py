from flask import Flask, render_template
from .models import DB, Users, Tweets

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # eliminates warnings
    app.config['ENV']='debug' # more verbose error handling, don't deploy this!
    DB.init_app(app)

    @app.route('/')
    def root():
        users = Users.query.all()
        return render_template('base.html', title='Home', users=users)

    return app