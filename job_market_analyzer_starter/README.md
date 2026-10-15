# Job Market & Skills Demand Analyzer

**Stack:** Python, Pandas, MySQL, Power BI  
**Level:** Beginner

## Important data note
`data/job_postings_demo.csv` is a **synthetic practice dataset** created to help you learn the workflow. It is not a record of actual vacancies and must not be used to claim real-world job-market findings in a resume or interview.

For a portfolio version with real evidence, replace it with a public dataset whose source, collection date, license, and limitations you document. One project/dataset reference to evaluate is the public GitHub repository below; inspect its README and dataset provenance before reuse:
- https://github.com/powaromkar931-netizen/India_Tech_Job_Market_Analysis
- Alternative project reference: https://github.com/vaishnavivahile/Data-Analyst-Job-Market-Analysis

Do not copy another person's completed project or claim their findings as your own. Use only the dataset you can lawfully access and cite its original source.

## Business questions
1. Which job titles appear most frequently?
2. Which skills are mentioned in the most postings?
3. Which locations have the most listings in the dataset?
4. What salary ranges are disclosed, and how many records include salary?
5. How does posting volume vary by month?
6. Which skills appear across experience levels?

## Folder structure
- `data/job_postings_demo.csv` — synthetic practice data
- `python/analyze_jobs.py` — cleaning and exploratory analysis
- `sql/analysis_queries.sql` — SQL practice queries
- `data/processed/` — generated CSV outputs (created after running Python)

## Step 1 — Python setup
Install Python 3.10+ and run:
```bash
python -m pip install pandas
python python/analyze_jobs.py
```
The script creates `data/processed/jobs_clean.csv` and `data/processed/job_skills.csv`.

## Step 2 — SQL
Create a MySQL database and import the two processed CSVs into tables named `jobs_clean` and `job_skills`. Use the queries in `sql/analysis_queries.sql`.

Suggested `jobs_clean` columns:
`job_id, job_title, company, location, experience_level, work_mode, posted_date, salary_min_lpa, salary_max_lpa, job_url, salary_mid_lpa, posted_month`

Suggested `job_skills` columns:
`job_id, job_title, location, experience_level, salary_mid_lpa, skills, skill`

## Step 3 — Power BI dashboard
Use **Get Data → Text/CSV** to import `jobs_clean.csv` and `job_skills.csv`.

Build one report page with:
- KPI cards: total postings, number of roles, locations, salary disclosure %
- Bar chart: top 10 skills by jobs mentioning skill
- Bar chart: postings by job title
- Column chart: postings by location
- Line chart: postings by month
- Slicers: experience level, location, work mode

Useful measures (adjust table names to your model):
```DAX
Total Postings = DISTINCTCOUNT(jobs_clean[job_id])

Roles Count = DISTINCTCOUNT(jobs_clean[job_title])

Locations Count = DISTINCTCOUNT(jobs_clean[location])

Salary Disclosure % =
DIVIDE(
    COUNT(jobs_clean[salary_mid_lpa]),
    DISTINCTCOUNT(jobs_clean[job_id]),
    0
)
```
For skill demand, use `job_skills` and count distinct `job_id` per skill. Create a relationship between `jobs_clean[job_id]` and `job_skills[job_id]` if needed; avoid double-counting postings after expanding skills.

## Step 4 — Interpretation
For each chart, write 1–2 sentences answering:
- What do I observe?
- What might it mean for a job seeker?
- What are the limits of this dataset?

Do not assume that a skill causes higher salary just because the two appear together. Salary data may be missing or unrepresentative.

## Resume bullet — use only after completing with real sourced data
**Job Market & Skills Demand Analyzer | Python, SQL, Power BI**
- Cleaned and analyzed public job-posting data using Python and Pandas, documenting missing values and duplicate handling.
- Used SQL to summarize role demand, skill frequency, location patterns, and disclosed salary ranges.
- Built an interactive Power BI dashboard with KPI cards, skill-demand charts, role/location breakdowns, and filters.
- Documented data source, collection period, key findings, and limitations.

Replace generic wording with your actual dataset size and verified findings. Never invent metrics.

## GitHub checklist
- Add the dataset's original source and license/terms.
- Include your cleaning and SQL scripts.
- Add a screenshot of your own Power BI dashboard.
- Add 3–5 findings supported by your own analysis.
- Explain missing salary data and any other limitations.
- Do not upload private, restricted, or personally identifiable data.

## Interview explanation
"I built a Job Market & Skills Demand Analyzer to understand which skills appear most often in data-related job postings. I used Python and Pandas to inspect missing values, standardize fields, remove duplicate job IDs, and split skill lists into a separate analysis table. I then used SQL to compare skills, job titles, locations, and disclosed salary ranges. Finally, I created a Power BI dashboard with filters so users can explore the data. I also documented the source and limitations, especially missing salary information. The results describe the dataset I analyzed and should not automatically be generalized to the entire job market."

## Beginner concepts to learn
- Rows, columns, data types
- Missing values and duplicates
- `value_counts()`, `groupby()`, `explode()`
- SQL `SELECT`, `GROUP BY`, `COUNT`, `AVG`, `ORDER BY`
- Power BI visuals, slicers, relationships, basic DAX
