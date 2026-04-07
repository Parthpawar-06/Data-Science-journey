-- Problem: Average Population
-- Platform: HackerRank | Difficulty: Easy
-- Link: https://www.hackerrank.com/challenges/average-population/problem
--
-- Task: Find the average population for all cities, rounded down to nearest integer.
-- Note: FLOOR() rounds down, not ROUND() which rounds to nearest.
SELECT FLOOR(AVG(POPULATION))
FROM CITY;

