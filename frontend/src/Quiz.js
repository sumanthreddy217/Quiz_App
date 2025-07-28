import React, { useEffect, useState } from 'react';

function Quiz({ quiz, onBack }) {
  const [answers, setAnswers] = useState({});
  const [submitted, setSubmitted] = useState(false);
  const [score, setScore] = useState(0);

  // save quiz id to localStorage
  useEffect(() => {
    if (quiz) {
      localStorage.setItem('selectedQuizId', quiz.id);
    }

    // handle back button
    const handleBack = (e) => {
      e.preventDefault();
      onBack(); // go back to quizzes list
    };
    window.history.pushState(null, '', window.location.href);
    window.addEventListener('popstate', handleBack);
    return () => window.removeEventListener('popstate', handleBack);
  }, [quiz, onBack]);

  const handleChange = (qId, ansIdx) => {
    setAnswers({ ...answers, [qId]: ansIdx });
  };

  const handleSubmit = () => {
    let s = 0;
    quiz.questions.forEach(q => {
      if (parseInt(answers[q.id]) === q.answer) s++;
    });
    setScore(s);
    setSubmitted(true);
    localStorage.removeItem('selectedQuizId'); // remove after submit
  };

  const allAnswered = quiz.questions.every(q => answers[q.id] !== undefined);

  return (
    <div className="container mt-4">
      <h2 className="mb-4 text-center">{quiz.title}</h2>
      {quiz.questions.map((q, idx) => (
        <div key={q.id} className="card mb-3 p-3">
          <p><strong>{idx + 1}. {q.question}</strong></p>
          {q.options.map((opt, i) => {
            const isCorrect = submitted && i === q.answer;
            return (
              <div key={i} className={`form-check ${isCorrect ? 'bg-success text-white rounded' : ''}`}>
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
            );
          })}
        </div>
      ))}
      {!submitted && (
        <button
          className="btn btn-primary mb-4"
          onClick={handleSubmit}
          disabled={!allAnswered}
        >
          Submit
        </button>
      )}
      {submitted && (
        <p className="alert alert-success">Your Score: {score} / {quiz.questions.length}</p>
      )}
    </div>
  );
}

export default Quiz;
