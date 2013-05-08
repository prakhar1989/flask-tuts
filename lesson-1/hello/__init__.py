# flask imports go here
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os

# declaring the app
app = Flask(__name__)

# get the base dir
base_dir = os.path.dirname(os.path.abspath(__file__))
app.config.from_pyfile(os.path.join(app.root_path, '../app.cfg'))

# create db
db = SQLAlchemy(app)

# importing views
import hello.views

# import models
from hello.models.person import Person
