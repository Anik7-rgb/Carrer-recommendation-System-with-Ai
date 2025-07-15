import requests
from bs4 import BeautifulSoup

def get_jobs_for_role(role, max_results=5):
    query = role.replace(" ", "+")
    url = f"https://www.indeed.com/jobs?q={query}&l="
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        job_cards = soup.find_all('a', class_='tapItem', limit=max_results)

        jobs = []
        for job in job_cards:
            title = job.find("h2").text.strip() if job.find("h2") else "No Title"
            link = "https://www.indeed.com" + job["href"]
            jobs.append((title, link))

        return jobs
    except Exception as e:
        return [("Error fetching jobs", "#")]
