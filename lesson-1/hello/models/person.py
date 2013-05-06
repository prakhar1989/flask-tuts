from hello import db

class Person(db.Model):
  __tablename__ = "person"

  id = db.Column(db.Integer, primary_key=True)
  first_name = db.Column(db.String(80))
  last_name = db.Column(db.String(80))
  age = db.Column(db.Integer)

  def __init__(self, first_name, last_name, age):
    self.first_name = first_name
    self.last_name = last_name
    self.age = age

  def __repr__(self):
    return '<Person %r>' % (self.first_name + self.last_name)
