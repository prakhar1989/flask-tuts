from flask import Blueprint, render_template

mod = Blueprint('admin', __name__, url_prefix='/admin')

# route handles for /admin and /admin/page
@mod.route('/', defaults={'page': 'index'})
@mod.route('/<page>')
def show(page):
  return render_template('admin/index.html', page=page)
