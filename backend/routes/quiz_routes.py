from flask import Blueprint, jsonify, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from models.quiz import Quiz
from models.user import User

quiz_routes = Blueprint('quiz_routes', __name__)

@quiz_routes.route('/api/quizzes', methods=['GET'])
def get_quizzes():
    quizzes = Quiz.query.all()
    result = []
    for quiz in quizzes:
        result.append({
            'id': quiz.id,
            'title': quiz.title,
            'questions': [
                {'id': q.id, 'question': q.question, 'options': q.options, 'answer': q.answer}
                for q in quiz.questions
            ]
        })
    return jsonify(result)

@quiz_routes.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page or url_for('admin.index'))
        else:
            flash('Invalid username or password')
    # return the HTML form (keep same)
    return '''... your HTML form ...'''

@quiz_routes.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
