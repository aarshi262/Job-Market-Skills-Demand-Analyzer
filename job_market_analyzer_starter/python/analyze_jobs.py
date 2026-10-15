"""
Job Market & Skills Demand Analyzer
IMPORTANT: job_postings_demo.csv contains synthetic DEMO data, not real vacancies.
Replace it with a properly sourced public dataset before publishing real market findings.
"""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "job_postings_demo.csv"
OUT = ROOT / "data" / "processed"
OUT.mkdir(exist_ok=True)

df = pd.read_csv(DATA)
print("Rows/columns:", df.shape)
print("\nMissing values:\n", df.isna().sum())
print("\nExact duplicate rows:", df.duplicated().sum())

# Clean text fields and remove duplicate job IDs
for col in ["job_title", "company", "location", "experience_level", "work_mode"]:
    df[col] = df[col].astype("string").str.strip()
df["posted_date"] = pd.to_datetime(df["posted_date"], errors="coerce")
df["salary_min_lpa"] = pd.to_numeric(df["salary_min_lpa"], errors="coerce")
df["salary_max_lpa"] = pd.to_numeric(df["salary_max_lpa"], errors="coerce")
df = df.drop_duplicates(subset=["job_id"])
df["salary_mid_lpa"] = df[["salary_min_lpa", "salary_max_lpa"]].mean(axis=1)
df["posted_month"] = df["posted_date"].dt.to_period("M").astype("string")

# Explode comma-separated skills into one skill per row
skills = (
    df[["job_id", "job_title", "location", "experience_level", "salary_mid_lpa", "skills"]]
    .dropna(subset=["skills"])
    .assign(skill=lambda x: x["skills"].str.split(","))
    .explode("skill")
)
skills["skill"] = skills["skill"].str.strip().str.title()
skills = skills[skills["skill"].ne("")]

# Export cleaned files for SQL and Power BI
df.to_csv(OUT / "jobs_clean.csv", index=False)
skills.to_csv(OUT / "job_skills.csv", index=False)

print("\nTop job titles:\n", df["job_title"].value_counts().head(10))
print("\nTop locations:\n", df["location"].value_counts().head(10))
print("\nTop skills:\n", skills["skill"].value_counts().head(10))
print("\nSalary coverage:", f'{df["salary_mid_lpa"].notna().mean():.1%}')
if df["salary_mid_lpa"].notna().any():
    print("Median disclosed salary midpoint (LPA):", round(df["salary_mid_lpa"].median(), 2))

print("\nExports created in data/processed/")
