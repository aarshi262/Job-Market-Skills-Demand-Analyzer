
-- 1. Total job postings
SELECT COUNT(*) AS total_jobs
FROM jobs;

-- 2. Jobs by location
SELECT location, COUNT(*) AS total_jobs
FROM jobs
GROUP BY location
ORDER BY total_jobs DESC;

-- 3. Most common job titles
SELECT job_title, COUNT(*) AS total_jobs
FROM jobs
GROUP BY job_title
ORDER BY total_jobs DESC
LIMIT 10;

-- 4. Average salary range
SELECT
    ROUND(AVG(salary_min_lpa), 2) AS average_min_salary,
    ROUND(AVG(salary_max_lpa), 2) AS average_max_salary
FROM jobs;
