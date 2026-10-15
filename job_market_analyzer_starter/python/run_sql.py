
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "data" / "job_market.db"

queries = {
    "Total jobs": """
        SELECT COUNT(*) AS total_jobs
        FROM jobs;
    """,
    "Jobs by location": """
        SELECT location, COUNT(*) AS total_jobs
        FROM jobs
        GROUP BY location
        ORDER BY total_jobs DESC;
    """,
    "Top job titles": """
        SELECT job_title, COUNT(*) AS total_jobs
        FROM jobs
        GROUP BY job_title
        ORDER BY total_jobs DESC
        LIMIT 10;
    """,
    "Average salary": """
        SELECT ROUND(AVG(salary_min_lpa), 2),
               ROUND(AVG(salary_max_lpa), 2)
        FROM jobs;
    """
}

with sqlite3.connect(DB_PATH) as conn:
    for title, query in queries.items():
        print(f"\n--- {title} ---")
        for row in conn.execute(query):
            print(row)
