-- Problem: Revising the Select Query II
-- Platform: HackerRank
-- Difficulty: Easy
-- Link: https://www.hackerrank.com/challenges/revising-the-select-query-2/problem
--
-- Task: Query the NAME of all American cities with population > 120000.

SELECT NAME
FROM CITY
WHERE POPULATION > 120000
AND COUNTRYCODE = 'USA';
