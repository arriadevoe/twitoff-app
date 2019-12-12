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
