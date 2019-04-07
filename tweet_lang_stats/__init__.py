from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from logging import DEBUG

import logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.logger.setLevel(DEBUG)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://postgres:Arnau3.1@localhost/TwitterLangs"
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)

from . import models
from . import views


