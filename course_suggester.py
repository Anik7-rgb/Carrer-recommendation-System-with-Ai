course_db = {
    "python": ["Python for Everybody – Coursera", "Learn Python – Codecademy"],
    "sql": ["Intro to SQL – Khan Academy", "SQL Basics – DataCamp"],
    "machine learning": ["ML Crash Course – Google", "ML A-Z – Udemy"],
    "html": ["HTML & CSS – FreeCodeCamp"],
    "flask": ["Flask Mega-Tutorial – Miguel Grinberg"]
}

def recommend_courses(skills):
    recommended = []
    for skill, courses in course_db.items():
        if skill not in skills:
            for course in courses:
                recommended.append((skill.title(), course))
    return recommended[:5]  # limit output
