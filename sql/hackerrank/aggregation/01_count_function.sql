-- Problem: Revising Aggregations - The Count Function
-- Platform: HackerRank | Difficulty: Easy
-- Link: https://www.hackerrank.com/challenges/revising-aggregations-the-count-function/problem
--
-- Task: Count the number of cities in CITY table where population > 100000.

SELECT COUNT(NAME)
FROM CITY 
WHERE POPULATION>100000;
