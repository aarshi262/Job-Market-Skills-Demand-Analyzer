-- MySQL 8+ starter queries
-- Import data/processed/jobs_clean.csv into a table named jobs_clean.
-- Import data/processed/job_skills.csv into a table named job_skills.
-- The demo data is synthetic; do not describe these outputs as real market findings.

-- 1. Number of postings by role
SELECT job_title, COUNT(*) AS posting_count
FROM jobs_clean
GROUP BY job_title
ORDER BY posting_count DESC;

-- 2. Most frequently mentioned skills
SELECT skill, COUNT(DISTINCT job_id) AS jobs_mentioning_skill
FROM job_skills
GROUP BY skill
ORDER BY jobs_mentioning_skill DESC;

-- 3. Demand by location
SELECT location, COUNT(*) AS posting_count
FROM jobs_clean
GROUP BY location
ORDER BY posting_count DESC;

-- 4. Salary summary by role (only disclosed salaries)
SELECT job_title,
       COUNT(salary_mid_lpa) AS salary_records,
       ROUND(AVG(salary_mid_lpa), 2) AS average_salary_lpa,
       ROUND(MIN(salary_mid_lpa), 2) AS min_salary_lpa,
       ROUND(MAX(salary_mid_lpa), 2) AS max_salary_lpa
FROM jobs_clean
WHERE salary_mid_lpa IS NOT NULL
GROUP BY job_title
ORDER BY average_salary_lpa DESC;

-- 5. Postings by month
SELECT posted_month, COUNT(*) AS posting_count
FROM jobs_clean
GROUP BY posted_month
ORDER BY posted_month;

-- 6. Experience level x skill
SELECT experience_level, skill, COUNT(DISTINCT job_id) AS job_count
FROM job_skills
GROUP BY experience_level, skill
ORDER BY experience_level, job_count DESC;
