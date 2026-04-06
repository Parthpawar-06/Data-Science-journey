-- Problem: Revising the Select Query I
-- Platform: HackerRank
-- Difficulty: Easy
-- Link: https://www.hackerrank.com/challenges/revising-the-select-query/problem
--
-- Task: Query all columns for all American cities in CITY table
-- with population larger than 100000. CountryCode = 'USA'.

SELECT *
FROM CITY
WHERE POPULATION > 100000
  AND COUNTRYCODE = 'USA';
