from config.database import db

class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    # Add e.g. description
    # description = db.Column(db.String(255))
    questions = db.relationship('Question', backref='quiz', lazy=True)

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quizze = db.Column(db.String(120))
    question = db.Column(db.String(256), nullable=False)
    options = db.Column(db.PickleType, nullable=False)
    answer = db.Column(db.Integer, nullable=False)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable=False)