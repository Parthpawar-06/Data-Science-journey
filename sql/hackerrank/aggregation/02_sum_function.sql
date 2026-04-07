-- Problem: Revising Aggregations - The Sum Function
-- Platform: HackerRank | Difficulty: Easy
-- Link: https://www.hackerrank.com/challenges/revising-aggregations-sum/problem
--
-- Task: Find total population of all cities in California (district).
SELECT SUM(POPULATION)
FROM CITY
WHERE DISTRICT = "California";
