import React, { useEffect, useState } from 'react';
import QuizList from './QuizList';
import Quiz from './Quiz';
import axios from 'axios';

function App() {
  const [selectedQuiz, setSelectedQuiz] = useState(null);

  useEffect(() => {
    const savedId = localStorage.getItem('selectedQuizId');
    if (savedId) {
      axios.get('http://127.0.0.1:5000/api/quizzes')
        .then(res => {
          const found = res.data.find(q => q.id === parseInt(savedId));
          if (found) setSelectedQuiz(found);
        });
    }
  }, []);

  return (
    <div>
      {!selectedQuiz && <QuizList onSelectQuiz={setSelectedQuiz} />}
      {selectedQuiz && <Quiz quiz={selectedQuiz} onBack={() => setSelectedQuiz(null)} />}
    </div>
  );
}

export default App;
