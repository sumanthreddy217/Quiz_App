# 🌟 Quiz App

This is a **personal full-stack quiz application project** built to practice and showcase modern web development skills.  
It combines a Python Flask backend with a React.js frontend, connected by a REST API.

The app allows:
✅ Users to choose from multiple quizzes, attend them, and get their score instantly  
✅ Admins to easily add or edit quizzes and questions through a built-in admin panel

---

## 🚀 **Live Demo**
👉 [**Click here to see the live quiz app**](https://your-frontend-link.vercel.app)

---

## ✏ **Project Overview & How it Works**
- **Admin Panel:** Powered by Flask‑Admin, where the quiz creator can add new quizzes and questions.  
- **Backend API:** Exposes `/api/quizzes` endpoint, serving quiz data as JSON to the frontend.
- **Frontend:** React.js app that fetches quizzes, displays them in a clean card layout, and lets users select answers.
- **User Flow:**  
  1️⃣ See list of available quizzes →  
  2️⃣ Choose a quiz →  
  3️⃣ Answer questions →  
  4️⃣ Submit →  
  ✅ See your score instantly.

All quiz data is dynamic and driven from the database, so you can add new quizzes anytime without changing frontend code.

---

## 📦 **Folder Structure**

quiz-app/
├── backend/ ← Flask backend
│ ├── server.py ← Main Flask application
│ ├── models/ ← Database models: Quiz, Question, User
│ │ ├── quiz.py
│ │ ├── user.py
│ │ └── ...
│ ├── quiz.db ← SQLite database file
│ ├── requirements.txt ← Python dependencies
│ └── config/ ← (Optional) Config files if used
│ ├── config.py
│ └── database.py
│
└── frontend/ ← React frontend
├── src/
│ ├── App.js ← Main app component
│ ├── Quiz.js ← Quiz list & quiz page component
│ ├── App.css ← Custom styles
│ └── index.js
├── public/
│ └── index.html
├── package.json ← npm dependencies
├── README.md ← Frontend README if separate
└── ...

---

## 🛠 **Languages & Frameworks Used**
- **Python**: Flask, Flask‑Admin, Flask‑Login
- **JavaScript**: React.js, Axios
- **HTML & CSS**: Bootstrap 5 for responsive design, plus custom CSS

---

## 🌱 **Main Features**
- Dynamic quiz creation and editing through admin panel
- Multiple quizzes: users can pick any quiz to attend
- Displays each quiz’s questions and options fetched live from backend
- Instant score calculation after submission
- Clean, responsive card-based design
- Fully driven by backend database: quizzes can be updated anytime without frontend changes

---

✅ This project was built as a personal portfolio app to learn and practice **full‑stack development**, including REST APIs, admin tools, and modern frontend design.

