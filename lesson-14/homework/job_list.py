import requests
import sqlite3
import csv
from bs4 import BeautifulSoup

database = "jobs.db"

def create_database():
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            company TEXT,
            location TEXT,
            description TEXT,
            application_link TEXT,
            UNIQUE(title, company, location)
        )
    """)
    conn.commit()
    conn.close()

def scrape_jobs():
    url = "https://realpython.github.io/fake-jobs"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    job_listings = []
    
    for job in soup.find_all("div", class_="card-content"):
        title = job.find("h2", class_="title").text.strip()
        company = job.find("h3", class_="company").text.strip()
        location = job.find("p", class_="location").text.strip()
        description = job.find("div", class_="description").text.strip()
        application_link = job.find("a")["href"]
        
        job_listings.append((title, company, location, description, application_link))
    
    return job_listings

def update_database(job_listings):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    for job in job_listings:
        cursor.execute("""
            INSERT INTO jobs (title, company, location, description, application_link)
            VALUES (?, ?, ?, ?, ?)
            ON CONFLICT(title, company, location) DO UPDATE SET
            description=excluded.description,
            application_link=excluded.application_link
        """, job)

    conn.commit()
    conn.close()

def filter_jobs(filter_type, filter_value):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    query = f"SELECT * FROM jobs WHERE {filter_type} = ?"
    cursor.execute(query, (filter_value,))
    results = cursor.fetchall()
    conn.close()
    return results

def export_to_csv(filter_type, filter_value):
    jobs = filter_jobs(filter_type, filter_value)
    if jobs:
        with open("filtered_jobs.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Title", "Company", "Location", "Description", "Application Link"])
            writer.writerows(jobs)
        print("Filtered jobs exported")
    else:
        print("No jobs found.")

if __name__ == "__main__":
    create_database()
    jobs = scrape_jobs()
    update_database(jobs)
    export_to_csv("company", "Example Company")
