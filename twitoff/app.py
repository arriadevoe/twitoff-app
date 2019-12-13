from decouple import config
from flask import Flask, render_template, request
from .models import DB, Users, Tweets
from .twitter import add_or_update_user

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL') # loads from .env, later a postgres url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # eliminates warnings
    app.config['ENV']=config('ENV')
    DB.init_app(app)

    @app.route('/') # GET by default
    def root():
        users = Users.query.all()
        return render_template('base.html', title='Home', users=users)

    # Replaces authentication (login,etc) temporarily
    @app.route('/reset')
    def reset():
        DB.drop_all()
        DB.create_all()
        return render_template('base.html', title='DB Reset!', users=[])

    @app.route('/user', methods=['POST'])
    @app.route('/user/<name>', methods=['GET'])
    def user(name=None, message=''):
        name = name or request.values['user_name']
        try:
            if request.method == 'POST':
                add_or_update_user(name)
                message = f"User {name} successfully added!"
            tweets = Users.query.filter(Users.name == name).one().tweets
        except Exception as e: # very basic, could be more specific plus others
            message = f"Error adding {name}: {e}"
            tweets = []
        return render_template('user.html', title=name, tweets=tweets, message=message)


    return app