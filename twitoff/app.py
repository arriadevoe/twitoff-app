from decouple import config
from flask import Flask, render_template
from .models import DB, Users, Tweets

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL') # loads from .env, later a postgres url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # eliminates warnings
    app.config['ENV']=config('ENV')
    DB.init_app(app)

    @app.route('/')
    def root():
        users = Users.query.all()
        return render_template('base.html', title='Home', users=users)

    # Replaces authentication (login,etc) temporarily
    @app.route('/reset')
    def reset():
        DB.drop_all()
        DB.create_all()
        return render_template('base.html', title='DB Reset!', users=[])

    return app