0. create repo and clone
1. pip install pipenv
2. pipenv shell
3. pipenv install flask
4. populate app script with boilerplating
5. FLASK_APP=twitoff:APP FLASK_ENV=development flask run 
6. FLASK_APP=twitoff:APP FLASK_ENV=development flask shell

### Steps to manually add users via shell
* from twitoff.models import *
* DB.drop_all(), drops all tables
* DB.create_all(), creates all tables, NEEDED
* u1 = Users(name = "something")
* t1 = Tweets(text = "some text")
* t2 = Tweets(text = "some other text")
* u1.tweets.append(t1)
* u1.tweets.append(t2)
* DB.session.add(u1)
* DB.session.commit()