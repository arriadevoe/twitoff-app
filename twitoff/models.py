from flask_sqlalchemy import SQLAlchemy 

DB = SQLAlchemy()

# Class name = table name being created
class Users(DB.Model):
    id = DB.Column(DB.BigInteger, primary_key=True)
    name = DB.Column(DB.String(20), nullable=False)
    newest_tweet_id = DB.Column(DB.BigInteger) # keeps track of most recent tweet

    # define a representation for style
    def __repr__(self):
        return f'<User {self.name}'

class Tweets(DB.Model):
    id = DB.Column(DB.BigInteger, primary_key=True)
    # Many SQLALchemy datatypes available
    text = DB.Column(DB.Unicode(300), nullable=False) # Allows for emojis
    embedding = DB.Column(DB.PickleType, nullable=False) 
    user_id = DB.Column(DB.Integer, DB.ForeignKey('users.id'), nullable=False)
    user = DB.relationship("Users", backref=DB.backref('tweets', lazy=True))

    def __repr__(self):
        return f'<Tweet {self.text}'