-- Problem: The Blunder
-- Platform: HackerRank | Difficulty: Easy
-- Link: https://www.hackerrank.com/challenges/the-blunder/problem
--
-- Task: Samantha calculates average salary but accidentally
-- removes all zeros from salary values. Find the difference
-- between actual average and miscalculated average, rounded up.

SELECT CEIL((AVG(SALARY)) - (AVG(REPLACE(SALARY, '0', '')))) AS AVG_SALARY
FROM EMPLOYEES;
