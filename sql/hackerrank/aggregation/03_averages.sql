-- Problem: Revising Aggregations - Averages
-- Platform: HackerRank | Difficulty: Easy
-- Link: https://www.hackerrank.com/challenges/revising-aggregations-the-average-function/problem
--
-- Task: Find average population of all cities in California.
SELECT AVG(POPULATION)
FROM CITY
WHERE DISTRICT = 'California'
