import React, { useEffect, useState } from 'react';
import axios from 'axios';

function Quiz() {
  const [quizzes, setQuizzes] = useState([]);         // all quizzes
  const [selectedQuiz, setSelectedQuiz] = useState(null); // chosen quiz
  const [answers, setAnswers] = useState({});
  const [submitted, setSubmitted] = useState(false);
  const [score, setScore] = useState(0);

  useEffect(() => {
    axios.get('https://quiz-app-deq3.onrender.com/api/quizzes')
      .then(res => {
        console.log(res.data);
        setQuizzes(res.data);
      })
      .catch(err => console.error(err));
  }, []);

  const handleChange = (qId, ansIdx) => {
    setAnswers({ ...answers, [qId]: ansIdx });
  };

  const handleSubmit = () => {
    let s = 0;
    selectedQuiz.questions.forEach(q => {
      if (parseInt(answers[q.id]) === q.answer) s++;
    });
    setScore(s);
    setSubmitted(true);
  };

  // Step 4: if user didn't pick quiz yet → show list of quizzes
  if (!selectedQuiz) {
  return (
    <div className="container mt-4 ">
      <h2 className="mb-4 text-center">Choose a Quiz</h2>
      <div className="row">
        {quizzes.map((qz) => (
          <div key={qz.id} className="col-md-4 mb-4">
            <div className="card h-100 shadow-sm">
              <div className="card-body d-flex flex-column justify-content-between">
                <h5 className="card-title text-center">{qz.title}</h5>
                {/* optional: add description or number of questions */}
                <p className="card-text text-center">
                  Total Questions: {qz.questions.length}
                </p>
                <div className="d-grid">
                  <button 
                    className="btn btn-primary mt-auto"
                    onClick={() => setSelectedQuiz(qz)}
                  >
                    Start Quiz
                  </button>
                </div>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}


  // Step 5: if user picked quiz → show its questions
  return (
    <div className="container mt-4">
      <h2 className="mb-4 text-center">{selectedQuiz.title}</h2>
      {selectedQuiz.questions.map((q, idx) => (
        <div key={q.id} className="card mb-3 p-3">
          <p><strong>{idx + 1}. {q.question}</strong></p>
          {q.options.map((opt, i) => (
            <div className="form-check" key={i}>
              <input
                className="form-check-input"
                type="radio"
                name={`q${q.id}`}
                value={i}
                onChange={() => handleChange(q.id, i)}
                disabled={submitted}
              />
              <label className="form-check-label">{opt}</label>
            </div>
          ))}
        </div>
      ))}
      {!submitted && <button className="btn btn-primary" onClick={handleSubmit}>Submit</button>}
      {submitted && <p className="mt-3 alert alert-success">Your Score: {score} / {selectedQuiz.questions.length}</p>}
    </div>
  );
}

export default Quiz;
