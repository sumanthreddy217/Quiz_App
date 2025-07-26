from flask import Flask, redirect, url_for, request
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from config.config import Config
from config.database import db
from models.user import User
from models.quiz import Quiz, Question
from routes.quiz_routes import quiz_routes
from wtforms import TextAreaField
from flask_cors import CORS
from datetime import timedelta

app = Flask(__name__)
CORS(app)
app.config.from_object(Config)
db.init_app(app)

# Session config (optional, harmless to keep)
app.config['SESSION_PERMANENT'] = False
app.config['REMEMBER_COOKIE_DURATION'] = timedelta(hours=1)

# Open (unprotected) admin views
class OpenModelView(ModelView):
    pass

class QuestionModelView(OpenModelView):
    form_overrides = dict(options=TextAreaField)
    form_columns = ['question', 'options', 'answer', 'quiz_id']

    def on_model_change(self, form, model, is_created):
        raw = form.options.data
        if raw.startswith('[') and raw.endswith(']'):
            raw = raw[1:-1]
        model.options = [x.strip().strip('"').strip("'") for x in raw.split(',')]

# Admin setup
admin = Admin(app, name='Quiz Admin Panel', template_mode='bootstrap3')
admin.add_view(OpenModelView(Quiz, db.session))
admin.add_view(QuestionModelView(Question, db.session))

# Register blueprint
app.register_blueprint(quiz_routes)

@app.route('/')
def index():
    return "Quiz App Backend Running! (No login - Open admin panel)"

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
