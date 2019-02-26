from tweet_lang_stats import app, db

from flask_script import Manager, prompt_bool

manager = Manager(app)


@manager.command
def initdb():
    db.create_all()
    #db.session.add(User(username="@KRLS"))
    print("Initialized the database")


@manager.command
def dropdb():
    if prompt_bool("Are you sure you want to lose all the data stored in the database ?"):
        db.drop_all()
        print("Dropped the database")


if __name__ == "__main__":
    manager.run()
