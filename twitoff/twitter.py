"""Retrieve tweets, embeddings, and persists in the database."""
import tweepy, basilica
from decouple import config
from .models import DB, Tweets, Users

# Authenticates connection with Twitter
TWITTER_AUTH = tweepy.OAuthHandler(config('TWITTER_CONSUMER_KEY'), config('TWITTER_CONSUMER_SECRET'))

TWITTER_AUTH.set_access_token(config('TWITTER_ACCESS_TOKEN'),config('TWITTER_ACCESS_TOKEN_SECRET'))

TWITTER = tweepy.API(TWITTER_AUTH)

BASILICA = basilica.Connection(config('BASILICA_KEY'))

# Useful functions
# Came from playing with API on a python shell
def add_or_update_user(screen_name):
    """
    Add or updates a user and their Tweets.
    Throws error if user doesn't exist, is private, or duplicate.
    """
    try: # will try to execute
        twitter_user = TWITTER.get_user(screen_name)
        db_user = (Users.query.get(twitter_user.id) or Users(id=twitter_user.id, name=screen_name)) # checks if exists in DB
        DB.session.add(db_user)

        tweets = twitter_user.timeline(
            count=200, 
            exclude_replies=True, 
            include_rts=True, 
            since_id=db_user.newest_tweet_id
        )

        if tweets:
            db_user.newest_tweet_id = tweets[0].id

        for tweet in tweets:
            embedding = BASILICA.embed_sentence(tweet, model='twitter')
            db_tweet = Tweets(id=tweet.id, text=tweet.text, embedding=embedding)
            DB.session.add(db_tweet)
        
        # DB.session.commit()
    except: # if it encounters error, goes here
        pass
    else: # always executes?
        pass