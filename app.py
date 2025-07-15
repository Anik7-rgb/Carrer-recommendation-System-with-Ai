from ml_predictor import predict_top_roles
from job_scraper import get_jobs_for_role
from course_suggester import recommend_courses

from flask import Flask, request, render_template
from resume_parser import extract_skills_from_text, extract_text_from_pdf
from recommender import recommend_roles
import os
import requests

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# ✅ Only 1 ai_answer_query function here
def ai_answer_query(query, extracted_skills):
    prompt = f"""The user has these skills: {', '.join(extracted_skills)}.
Their query is: "{query}".
Give a short, helpful career suggestion."""

    try:
        response = requests.post(
            "http://localhost:1234/v1/chat/completions",
            json={
                "model": "mistral-7b-instruct-v0.1",  # Match LM Studio model name
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.7,
                "max_tokens": 250
            },
            timeout=15
        )
        result = response.json()
        return result['choices'][0]['message']['content'].strip()
    except requests.exceptions.RequestException as e:
        return f"Error connecting to LM Studio: {e}"
    except KeyError:
        return "Error: Invalid response format from LM Studio"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    file = request.files['resume_file']
    filename = file.filename
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    custom_query = request.form.get('custom_query', '').lower().strip()

    resume_text = extract_text_from_pdf(filepath)
    extracted_skills = extract_skills_from_text(resume_text)

    if custom_query and any(word in custom_query for word in ["role", "job", "career", "position", "field", "recommend"]):
        job_query = custom_query
    else:
        top_roles = predict_top_roles(extracted_skills)
        job_query = top_roles[0][0] if top_roles else "Software Developer"

    jobs = get_jobs_for_role(job_query)
    courses = recommend_courses(extracted_skills)
    top_roles = predict_top_roles(extracted_skills)

    ai_response = ""
    if custom_query:
        ai_response = ai_answer_query(custom_query, extracted_skills)

    return render_template(
        'index.html',
        filename=filename,
        skills=extracted_skills,
        top_roles=top_roles,
        jobs=jobs,
        courses=courses,
        custom_query=custom_query,
        job_query=job_query,
        ai_response=ai_response
    )

if __name__ == '__main__':
    app.run(debug=True)
