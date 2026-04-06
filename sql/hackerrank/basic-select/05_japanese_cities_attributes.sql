-- Problem: Japanese Cities Attributes
-- Platform: HackerRank
-- Difficulty: Easy
-- Link: https://www.hackerrank.com/challenges/japanese-cities-attributes/problem
--
-- Task: Query all attributes of every Japanese city.
-- CountryCode for Japan = 'JPN'.

SELECT *
FROM CITY
WHERE COUNTRYCODE = 'JPN';
