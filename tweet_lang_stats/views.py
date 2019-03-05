from flask import render_template, request, url_for

from tweet_lang_stats import app, db

from .tweetstream import TweetStream
from .models import Tweet, User, Language

tweets = []


def store_tweets(username):
    tweets = []
    streamer = TweetStream()
    tweets.extend(streamer.get_user_tweets(username))
    return tweets


@app.route('/')
def index():
    return render_template('index.html', ppr="Alten", uur="Engie")


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        username = request.form["username"]
        tweets = store_tweets(username)
        app.logger.debug('storing tweets from {}'.format(username))

        new_user = tweets[0][0]
        user_exists = User.query.filter_by(username=new_user).first()

        if user_exists:
            for tw in tweets:
                tweet_exists = Tweet.query.filter_by(text=tw[1]).first()
                if not tweet_exists:
                    lang_exists = Language.query.filter_by(lang=tw[2]).first()
                    if lang_exists:
                        tweet = Tweet(text=tw[1], date=tw[3], user_id=user_exists.id, lang_id=lang_exists.id)
                    else:
                        new_lang = Language(lang=tw[2])
                        tweet = Tweet(text=tw[1], date=tw[3], user_id=user_exists.id, language=new_lang)
                    db.session.add(tweet)
                else:
                    continue
        else:
            user = User(username=new_user)
            for tw in tweets:
                lang_exists = Language.query.filter_by(lang=tw[2]).first()
                if lang_exists:
                    tweet = Tweet(text=tw[1], date=tw[3], user=user, lang_id=lang_exists.id)
                else:
                    new_lang = Language(lang=tw[2])
                    tweet = Tweet(text=tw[1], date=tw[3], user=user, language=new_lang)
                db.session.add(tweet)

    return render_template('add.html')


@app.errorhandler(404)
def page_not_found():
    return render_template('404.html'), 404
