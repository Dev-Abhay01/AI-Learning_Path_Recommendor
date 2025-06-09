from flask import Flask, render_template, request
from course_fetcher import fetch_courses
import random
import logging

app = Flask(__name__)

# Enable debug logs
logging.basicConfig(level=logging.INFO)

@app.route('/')
def home():
    # Send basic tag suggestions to enable client-side autocomplete (JS array)
    popular_tags = [
        "python", "web development", "machine learning", "data science",
        "cybersecurity", "ui ux design", "ai", "react", "cloud", "java",
        "flutter", "devops", "sql", "javascript", "node.js", "app development"
    ]
    return render_template("index.html", tag_suggestions=popular_tags)

@app.route('/recommend', methods=['POST'])
def recommend():
    user_name = request.form.get('name', 'Learner')
    skill = request.form.get('skill', '')
    level = request.form.get('level', '')
    goal = request.form.get('goal', '')

    query = f"{skill} {level} {goal}"
    logging.info(f"🧠 Querying for: {query}")

    try:
        all_courses = fetch_courses(query=query, max_results=30)
    except Exception as e:
        logging.error("Error fetching courses:", exc_info=e)
        all_courses = []

    for course in all_courses:
        course['score'] = round(random.uniform(81, 99), 2)
        course['level'] = level if not course.get('level') else course['level']
        course['mode'] = course.get('mode') or ("Video" if course.get('platform') in ['YouTube', 'Udemy'] else "Self-paced")
        course['type'] = course.get('type') or ("Free" if course.get('platform') in ['YouTube', 'Khan Academy'] else "Paid")

    sorted_courses = sorted(all_courses, key=lambda x: x['score'], reverse=True)
    max_courses = min(len(sorted_courses), random.randint(12, 15))
    recommendations = sorted_courses[:max_courses]
    fallback = len(recommendations) == 0

    tips = [
        "Choose courses that match your level and stick with one at a time for deep mastery.",
        "💡 Don’t just watch — practice what you learn to retain it better!",
        "📌 Explore 2–3 platforms before enrolling. Choose based on your pace, budget, and project needs.",
        "⭐ Take notes and create mini-projects to apply your knowledge.",
        "📚 Combine video learning with reading to reinforce understanding."
    ]

    return render_template(
        "result.html",
        user_name=user_name,
        recommendations=recommendations,
        fallback=fallback,
        tips=tips
    )

if __name__ == '__main__':
    app.run(debug=True)