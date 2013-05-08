from flask import Flask, render_template, jsonify, request
from flask.ext.sqlalchemy import SQLAlchemy
from flask.views import View, MethodView
from datetime import datetime
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///person.db'

db = SQLAlchemy(app)

# models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    age = db.Column(db.Integer)

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return '<user %r>' % self.name

# render template views
class RenderTemplateView(View):
    def __init__(self, template_name):
        self.template_name = template_name

    def dispatch_request(self):
        return render_template(self.template_name)


# render listviews
class ListView(View):
    def get_template_name(self):
        raise NotImplementedError()

    def render_template(self, context):
        return render_template(self.get_template_name(), **context)

    def dispatch_request(self):
        context = self.get_context()
        return self.render_template(context)


class UserListView(ListView):
    def get_template_name(self):
        return "users.html"

    def get_context(self):
        context = {'objects': User.query.all(), 'time': datetime.now()}
        return context

# api views
class UserAPI(MethodView):
    def get(self, user_id):
        if user_id is None:
            users = User.query.all()
            json_results = [{'name': u.name, 'age': u.age} for u in users]
        else:
            user = User.query.get_or_404(user_id)
            json_results = [{'name': user.name, 'age': user.age}]
        return jsonify(item=json_results)

    def post(self):
        user = User(request.form['name'], request.form['age'])
        db.session.add(user)
        db.session.commit()
        return jsonify(item = [{'status': 'new item added'}])

    def delete(self, user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return jsonify(item = [{'status': 'item deleted'}])

    def put(self, user_id):
        user = User.query.get_or_404(user_id)
        user.name = request.form['name']
        user.age = request.form['age']
        db.session.add(user)
        db.session.commit()
        return jsonify(item = [{'status': 'item deleted'}])

# urls for APIs
user_api_view = UserAPI.as_view('user_api')
app.add_url_rule('/users/', defaults={'user_id': None},
                 view_func = user_api_view, methods=["GET",])
app.add_url_rule('/users/', view_func = user_api_view, methods=["POST",])
app.add_url_rule('/users/<int:user_id>', view_func = user_api_view,
                 methods=["GET", "PUT", "DELETE"])

# urls for rendering simple templates
app.add_url_rule('/about', view_func = RenderTemplateView.as_view('about_page', template_name="about.html"))
app.add_url_rule('/', view_func = RenderTemplateView.as_view('index_page', template_name="index.html"))

# urls for list views
app.add_url_rule('/userlist/', view_func = UserListView.as_view('user_list'))

if __name__ == "__main__":
    app.run(debug=True)
