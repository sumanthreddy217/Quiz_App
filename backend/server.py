from flask import Flask
from flask_login import LoginManager
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_admin import BaseView, expose
from config.config import Config
from config.database import db
from models.user import User
from models.quiz import Quiz, Question
from routes.quiz_routes import quiz_routes
from flask import redirect, url_for, request
from flask_login import current_user
from wtforms import TextAreaField
from flask_admin.form import rules
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
app.config.from_object(Config)
db.init_app(app)

# Login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Flask-Admin secure views
class SecureModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated
    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('login', next=request.url))


class QuestionModelView(SecureModelView):
    form_overrides = dict(options=TextAreaField)
    form_columns = ['question', 'options', 'answer', 'quiz_id']
    
    def on_model_change(self, form, model, is_created):
        raw = form.options.data
        # Remove brackets if any and split by comma
        if raw.startswith('[') and raw.endswith(']'):
            raw = raw[1:-1]
        model.options = [x.strip().strip('"').strip("'") for x in raw.split(',')]


class LogoutView(BaseView):
    @expose('/')
    def index(self):
        logout_user()
        return redirect(url_for('login'))

# admin setup
admin = Admin(app, name='Quiz Admin Panel', template_mode='bootstrap3')
admin.add_view(LogoutView(name='Logout', endpoint='logout'))
admin.add_view(SecureModelView(Quiz, db.session))
admin.add_view(QuestionModelView(Question, db.session))

# Register blueprint
app.register_blueprint(quiz_routes)

@app.route('/')
def index():
    return "Quiz App Backend Running!"

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
