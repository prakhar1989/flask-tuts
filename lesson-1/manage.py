from flask.ext.script import Manager, Server, Shell
from hello import app
from hello import db

# (optional) - include models if you want to!
import hello.models as models

def _make_context():
  """ context for passing into to the shell command """
  return dict(app=app, db=db, models=models)

# set manager
manager = Manager(app)

# add commands
manager.add_command("runserver", Server())
manager.add_command("shell", Shell(make_context = _make_context))

if __name__ == "__main__":
  manager.run()
