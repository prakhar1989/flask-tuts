from flask import Blueprint, render_template

mod = Blueprint('posts', __name__, url_prefix='/posts')

# route handles for /posts and /posts/page
@mod.route('/', defaults={'page': 'index'})
@mod.route('/<page>')
def show(page):
  return render_template('posts/index.html', page=page)
