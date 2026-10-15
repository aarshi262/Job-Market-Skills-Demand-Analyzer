
import sqlite3
import pandas as pd
from pathlib import Path

# Project ka main folder
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
DB_PATH = DATA_DIR / "job_market.db"

# CSV files read karo
jobs = pd.read_csv(DATA_DIR / "processed" / "jobs_clean.csv")
skills = pd.read_csv(DATA_DIR / "processed" / "job_skills.csv")

# SQLite database banao
with sqlite3.connect(DB_PATH) as conn:
    jobs.to_sql("jobs", conn, if_exists="replace", index=False)
    skills.to_sql("job_skills", conn, if_exists="replace", index=False)

    print("Database created successfully!")
    print("Jobs table rows:", len(jobs))
    print("Job skills rows:", len(skills))
    print("Jobs columns:", list(jobs.columns))
    print("Skills columns:", list(skills.columns))
