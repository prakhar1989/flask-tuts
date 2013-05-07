from flask import Flask

app = Flask(__name__)

from blogs.admin.views import mod as adminModule
from blogs.posts.views import mod as postsModule
app.register_blueprint(adminModule)
app.register_blueprint(postsModule)

@app.route('/')
def index():
    return "<a href='/admin'>Admin Section</a> | \
            <a href='/posts'>Posts Section</a>"

