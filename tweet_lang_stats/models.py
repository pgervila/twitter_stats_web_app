from tweet_lang_stats import db


class Language(db.Model):
    __tablename__ = 'languages'
    id = db.Column(db.Integer, primary_key=True)
    lang = db.Column(db.String(64), unique=True)
    tweet = db.relationship('Tweet', backref='language', uselist=False)

    def __repr__(self):
        return '<Language {}>'.format(self.lang)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    tweets = db.relationship('Tweet', backref='user', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Tweet(db.Model):
    __tablename__ = 'tweets'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200), unique=False, index=True)
    date = db.Column(db.Date)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    lang_id = db.Column(db.Integer, db.ForeignKey('languages.id'), nullable=False)

    def __repr__(self):
        return '<Tweet {}>'.format(self.text)
