-- Problem: Top Earners
-- Platform: HackerRank | Difficulty: Medium
-- Link: https://www.hackerrank.com/challenges/earnings-of-employees/problem
--
-- Task: Find the maximum total earnings for all employees and the
-- total number of employees who have earned that maximum.
-- Total earnings = months * salary

SELECT (MONTHS*SALARY) AS EARNINGS ,COUNT(*)
FROM EMPLOYEE 
GROUP BY EARNINGS
ORDER BY EARNINGS DESC
LIMIT 1;
