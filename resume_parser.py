# === resume_parser.py ===
import spacy
import re
import fitz  # PyMuPDF
# Load English tokenizer, POS tagger, parser
nlp = spacy.load("en_core_web_sm")

COMMON_SKILLS = ["python", "java", "c++", "html", "css", "javascript", "machine learning", "data analysis",
                 "sql", "communication", "leadership", "teamwork", "pandas", "numpy", "flask", "django"]

def extract_skills_from_text(text):
    text = text.lower()
    doc = nlp(text)
    found = set()
    for skill in COMMON_SKILLS:
        if skill in text:
            found.add(skill)
    return list(found)


def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text
