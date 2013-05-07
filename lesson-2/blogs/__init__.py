from flask import Flask, url_for

app = Flask(__name__)

from blogs.admin.views import mod as adminModule
from blogs.posts.views import mod as postsModule
app.register_blueprint(adminModule)
app.register_blueprint(postsModule)

@app.route('/')
def index():
    return "<a href='%s'>Admin Section</a> | \
            <a href='%s'>Posts Section</a>" % (url_for('admin.show'),
                                               url_for('posts.show'))
