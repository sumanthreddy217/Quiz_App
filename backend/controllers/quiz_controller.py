from models.quiz import Quiz, Question
from config.database import db
from flask import jsonify, request

def get_quizzes():
    quizzes = Quiz.query.all()
    return jsonify([{'id': q.id, 'title': q.title} for q in quizzes])

def get_quiz(quiz_id):
    quiz = Quiz.query.get_or_404(quiz_id)
    return jsonify({
        'id': quiz.id,
        'title': quiz.title,
        'questions': [
            {
                'id': q.id,
                'question': q.question,
                'options': q.options
            }
            for q in quiz.questions
        ]
    })

def create_quiz():
    data = request.get_json()
    quiz = Quiz(title=data['title'])
    db.session.add(quiz)
    db.session.commit()
    for q in data['questions']:
        question = Question(
            question=q['question'],
            options=q['options'],
            answer=q['answer'],
            quiz_id=quiz.id
        )
        db.session.add(question)
    db.session.commit()
    return jsonify({'message': 'Quiz created!'}), 201
