# flask imports go here
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os

# declaring the app
app = Flask(__name__)

# app.root_path stores the root path of the application
app.config.from_pyfile(os.path.join(app.root_path, '../app.cfg'))

# create db
db = SQLAlchemy(app)

# importing views
import hello.views

# import models
from hello.models.person import Person
