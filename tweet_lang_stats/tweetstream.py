import time
import re
from langdetect import detect

# Twitter API for python
import tweepy
from tweepy import OAuthHandler
# import secret codes to access Twitter API
from tweet_lang_stats.twitter_pwd import access_token, access_token_secret, consumer_key, consumer_secret

# language detection


class TweetStream:

    def __init__(self):
        # set_up Twitter API
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    def get_user_tweets(self, screen_name, max_num_twts=50):
        """ Given an account id,
            method retrieves a specified maximum number of tweets written or retweeted by account owner.
            It returns them in a list.
            Args:
                * screen_name: string. Id that identifies the twitter account
                * max_num_twts: integer. Maximum number of tweets to be retrieved for each account
            Returns:
                * list_tweets: list including info of all retrieved tweets in JSON format"""
        list_tweets = []
        timeline = tweepy.Cursor(self.api.user_timeline, id=screen_name,
                                 count=200, include_rts=False).items(max_num_twts)
        while True:
            try:
                tw = next(timeline)
                list_tweets.append((tw._json['user']['screen_name'],
                                    tw.text, tw.lang, tw.created_at))
            except tweepy.TweepError as e:
                if '401' in str(e):
                    print(e)
                    time.sleep(2)
                    break
                elif '404' in str(e):
                    print(e)
                    time.sleep(2)
                    break
                else:
                    time.sleep(60 * 15)
                    continue
            except StopIteration:
                break
        return list_tweets


if __name__ == "__main__":
    twstream = TweetStream()
    tweets = twstream.get_user_tweets("@wagensberg")
