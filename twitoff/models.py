from flask_sqlalchemy import SQLAlchemy 

DB = SQLAlchemy()

# Class name = table name being created
class User(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    name = DB.Column(DB.String(20), nullable=False)

class Tweet(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    # Many SQLALchemy datatypes available
    text = DB.Column(DB.Unicode(280), nullable=False) # Allows for emojis