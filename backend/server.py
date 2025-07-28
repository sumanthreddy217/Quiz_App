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
    column_list = ['question', 'quiz', 'options', 'answer']
    form_columns = ['question', 'options', 'answer', 'quiz_id']
    column_labels = dict(
        question="Question Text",
        options="Options (comma separated)",
        answer="Correct Option Index",
        quiz_id="Quiz ID"
    )

    def on_model_change(self, form, model, is_created):
        raw = form.options.data
        if raw.startswith('[') and raw.endswith(']'):
            raw = raw[1:-1]
        model.options = [x.strip().strip('"').strip("'") for x in raw.split(',')]

# Admin setup
admin = Admin(app, name='📚 Admin Dashboard', template_mode='bootstrap4', base_template='admin/master.html')

@app.context_processor
def override_admin_css():
    return dict(admin_css='/static/admin.css')

admin.add_view(OpenModelView(Quiz, db.session, name='📝 Quizzes'))
admin.add_view(QuestionModelView(Question, db.session, name='❓ Questions'))

# Register blueprint
app.register_blueprint(quiz_routes)

@app.route('/')
def index():
    return "Quiz App Backend Running!"

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
