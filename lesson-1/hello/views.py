# views go here
from hello import app
from hello.models.person import Person
from flask import render_template

@app.route('/')
def hello():
  return render_template("index.html")

@app.route('/test')
def test():
  return "i am the test route"

@app.route('/person')
def person():
  p1 = Person.query.first()
  return "name = %s, age= %s" % (p1.first_name + " " + p1.last_name, p1.age)
