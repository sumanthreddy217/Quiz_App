import React, { useEffect, useState } from 'react';
import axios from 'axios';

function QuizList({ onSelectQuiz }) {
  const [quizzes, setQuizzes] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:5000/api/quizzes')
      .then(res => setQuizzes(res.data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div className="container mt-4">
      <h2 className="mb-4 text-center">📝 Choose a Quiz</h2>
      <div className="row">
        {quizzes.map((qz) => (
          <div key={qz.id} className="col-md-4 mb-4">
            <div
              className="card h-100 shadow-sm"
              style={{ cursor: 'pointer' }}
              onClick={() => onSelectQuiz(qz)}
            >
              <div className="card-body text-center">
                <h5 className="card-title">{qz.title}</h5>
                <p className="card-text">Total Questions: {qz.questions.length}</p>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default QuizList;
