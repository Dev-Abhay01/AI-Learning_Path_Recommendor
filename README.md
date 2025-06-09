---

# 🎓 AI-Powered Learning Path Recommender

A smart, modern web application that recommends the *best online courses* tailored to a user's *skills, goals, and experience level*. This project simulates an AI-based recommendation engine that pulls courses from multiple platforms, matches them intelligently, and presents them in a beautiful, user-friendly interface.

---

## 🚀 Features

- 🧠 *AI-Curated Results* — Course matching based on skill, level, and goal
- 🌗 *Dark Mode* with localStorage memory
- 🧾 *User Input Form* with animated labels and real-time validation
- 📊 *Course Cards* with:
  - Title, platform, match score, progress bar
  - Platform icons, tags, badges (e.g. 🔥 Popular, 💡 Trending)
  - Description with *Read more* toggle
- 📚 *Multi-source Integration* (Coursera, YouTube, Google, edX, Khan Academy, etc.)
- 🎯 *Smart Tips Section* with learning advice
- ✨ *Visual Enhancements*:
  - Gradient animation
  - Floating hero icons
  - Responsive layout
  - Scroll-based reveal animations
- 📤 *Extras*:
  - Share page link 📎
  - Download recommendations as PDF 🖨

---

## 📂 Folder Structure

project/ │ ├── static/ │   └── platform_thumbs/       # Platform logos and default icon │ ├── templates/ │   ├── index.html             # Input form with animation and hero │   ├── result.html            # Final result UI with recommendations │   └── course_card.html       # Each course UI block (included dynamically) │ ├── course_fetcher.py          # Course mock fetchers + platform logic ├── app.py                     # Flask application logic └── README.md                  # Project documentation

---

## 🛠 Tech Stack

| Frontend                | Backend       | Data Handling        |
|------------------------|---------------|----------------------|
| HTML, CSS, JavaScript  | Python (Flask)| BeautifulSoup, mock  |
| ScrollReveal.js        | Jinja2 Templating | Random module |

---

## 🔧 Setup Instructions

```bash
git clone https://github.com/yourusername/ai-learning-recommender.git
cd ai-learning-recommender
pip install -r requirements.txt
python app.py

Then open http://localhost:5000 in your browser.

> ✅ Python 3.7+ recommended




---

✨ How It Works

1. User enters:

Name (for personalization)

A skill/topic (e.g., Python, Marketing)

Their experience level (Beginner, Intermediate, Advanced)

A goal (e.g., Become a developer)



2. Backend:

Builds a dynamic search query

Pulls course suggestions from multiple platforms

Assigns a match score

Displays the top 12–15 results visually with UI cards



3. User can:

Explore each course

Expand the description

Copy the page link or download the recommendation

---

✅ Final Year Project Highlights

💼 Industry-Ready Frontend

⚙ Functional Flask Backend

📚 Multi-platform education aggregator

🤖 AI-simulated logic

🧠 Modern UX Design

🧾 No database required



---

📌 Customization Ideas

🔍 Add autocomplete using JS + typeahead.js

📦 Store actual course JSON from real APIs

🔐 Add user login & profile with Flask-Login

🧾 Export final plan via pdfkit or WeasyPrint

🎓 Display AI-picked badges (🧠, 🆓, 📺)



---

📄 License

This project is licensed under the MIT License.


---

👨‍💻 Created By

Abhay (Dev-Abhay) — Final Year CSE Student
Guided by OpenAI ChatGPT
College Project 2025

---
