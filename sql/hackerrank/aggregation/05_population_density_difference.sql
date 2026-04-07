-- Problem: Population Density Difference
-- Platform: HackerRank | Difficulty: Easy
-- Link: https://www.hackerrank.com/challenges/population-density-difference/problem
--
-- Task: Find difference between highest and lowest population in CITY table.

SELECT MAX(POPULATION)-MIN(POPULATION)
FROM CITY;
