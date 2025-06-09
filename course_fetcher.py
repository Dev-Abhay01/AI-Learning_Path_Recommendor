# course_fetcher.py

import requests
from bs4 import BeautifulSoup
from urllib.parse import quote
import random

def clean_title(title):
    return title.strip().replace("\n", "").replace("  ", " ")

def fetch_youtube_courses(query, max_results=5):
    url = f"https://www.youtube.com/results?search_query={quote(query)}"
    return [{
        "title": f"YouTube: {query.title()} Tutorial #{i+1}",
        "platform": "YouTube",
        "link": url,
        "tags": ["Video", "Free"],
        "level": "Beginner",
        "score": round(random.uniform(85, 98), 2),
        "thumbnail": "https://img.youtube.com/vi/dQw4w9WgXcQ/0.jpg",
        "description": f"Watch and learn {query.lower()} with short, visual-based tutorials from top YouTube educators."
    } for i in range(max_results)]

def fetch_coursera_courses(query, max_results=3):
    try:
        url = f"https://www.coursera.org/search?query={quote(query)}"
        headers = {"User-Agent": "Mozilla/5.0"}
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, "html.parser")
        courses = soup.find_all("a", class_="css-1w8jli3", href=True)
        return [{
            "title": clean_title(c.text),
            "platform": "Coursera",
            "link": "https://www.coursera.org" + c["href"],
            "tags": ["Self-paced", "Paid", "Certificate"],
            "level": "Intermediate",
            "score": round(random.uniform(86, 98), 2),
            "thumbnail": "/static/platform_thumbs/coursera.png",
            "description": f"Coursera's {query.title()} course offers in-depth lectures from university-level instructors."
        } for c in courses[:max_results]]
    except:
        return []

def fetch_simplilearn_courses(query, max_results=4):
    return [{
        "title": f"Simplilearn Path: {query.title()} Developer",
        "platform": "Simplilearn",
        "link": "https://www.simplilearn.com/search?query=" + quote(query),
        "tags": ["Self-paced", "Paid", "Career Path"],
        "level": "Intermediate",
        "score": round(random.uniform(82, 97), 2),
        "thumbnail": "/static/platform_thumbs/simplilearn.png",
        "description": f"Learn {query.lower()} step-by-step with a structured career path from Simplilearn."
    } for _ in range(max_results)]

def fetch_google_courses(query, max_results=2):
    return [{
        "title": f"Google Digital Garage: {query.title()} Basics",
        "platform": "Google Digital Garage",
        "link": "https://learndigital.withgoogle.com/digitalgarage",
        "tags": ["Free", "Self-paced", "Certificate"],
        "level": "Beginner",
        "score": round(random.uniform(85, 97), 2),
        "thumbnail": "/static/platform_thumbs/google_digital_garage.png",
        "description": f"Google's course teaches the fundamentals of {query.lower()} in a practical and interactive way."
    } for _ in range(max_results)]

def fetch_khan_academy_courses(query, max_results=2):
    return [{
        "title": f"Khan Academy: Learn {query.title()} Basics",
        "platform": "Khan Academy",
        "link": "https://www.khanacademy.org",
        "tags": ["Free", "Self-paced"],
        "level": "Beginner",
        "score": round(random.uniform(85, 97), 2),
        "thumbnail": "/static/platform_thumbs/khan_academy.png",
        "description": f"Explore basic concepts of {query.lower()} through animations and practice exercises."
    } for _ in range(max_results)]

def fetch_great_learning_courses(query, max_results=2):
    return [{
        "title": f"Great Learning: Learn {query.title()} for Free",
        "platform": "Great Learning",
        "link": "https://www.mygreatlearning.com/academy",
        "tags": ["Free", "Self-paced", "Paid"],
        "level": "Beginner",
        "score": round(random.uniform(85, 97), 2),
        "thumbnail": "/static/platform_thumbs/great_learning.png",
        "description": f"Free {query.lower()} courses by Great Learning to help you get industry-ready skills."
    } for _ in range(max_results)]

def fetch_hubspot_courses(query, max_results=2):
    return [{
        "title": f"HubSpot Academy: {query.title()} Essentials",
        "platform": "HubSpot Academy",
        "link": "https://academy.hubspot.com/courses",
        "tags": ["Free", "Marketing", "Certificate"],
        "level": "Beginner",
        "score": round(random.uniform(85, 96), 2),
        "thumbnail": "/static/platform_thumbs/hubspot_academy.png",
        "description": f"Master the fundamentals of {query.lower()} for business and marketing from HubSpot experts."
    } for _ in range(max_results)]

def fetch_edx_courses(query, max_results=2):
    return [{
        "title": f"edX Online Course: {query.title()} Fundamentals",
        "platform": "edX",
        "link": "https://www.edx.org/search?q=" + quote(query),
        "tags": ["Free & Paid", "University", "Self-paced"],
        "level": "Intermediate",
        "score": round(random.uniform(84, 96), 2),
        "thumbnail": "/static/platform_thumbs/edx.png",
        "description": f"Join top university courses on edX to learn {query.lower()} from accredited educators."
    } for _ in range(max_results)]

def fetch_nptel_courses(query, max_results=2):
    return [{
        "title": f"NPTEL: {query.title()} Fundamentals",
        "platform": "NPTEL",
        "link": "https://nptel.ac.in/courses",
        "tags": ["Free", "Indian Govt", "Engineering", "Paid"],
        "level": "Intermediate",
        "score": round(random.uniform(83, 97), 2),
        "thumbnail": "/static/platform_thumbs/nptel.png",
        "description": f"NPTEL provides deep theoretical coverage of {query.lower()} curated by top IITs and IISc."
    } for _ in range(max_results)]

# Master fetch function
def fetch_courses(query, max_results=35):
    all_courses = []
    all_courses += fetch_youtube_courses(query, 5)
    all_courses += fetch_coursera_courses(query, 4)
    all_courses += fetch_simplilearn_courses(query, 4)
    all_courses += fetch_google_courses(query, 2)
    all_courses += fetch_khan_academy_courses(query, 2)
    all_courses += fetch_great_learning_courses(query, 2)
    all_courses += fetch_hubspot_courses(query, 2)
    all_courses += fetch_edx_courses(query, 2)
    all_courses += fetch_nptel_courses(query, 2)

    random.shuffle(all_courses)
    return all_courses[:max_results]