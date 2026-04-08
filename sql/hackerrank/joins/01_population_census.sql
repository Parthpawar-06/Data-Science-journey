-- Problem: Population Census
-- Platform: HackerRank | Difficulty: Easy
-- Link: https://www.hackerrank.com/challenges/asian-population/problem
--
-- Task: Find total population of all cities in Asia continent.
-- Requires INNER JOIN between CITY and COUNTRY tables.
-- Join condition: CITY.CountryCode = COUNTRY.Code

SELECT SUM(CITY.POPULATION) AS TOTALPOPULATION 
FROM COUNTRY 
JOIN CITY ON COUNTRY.CODE = CITY.COUNTRYCODE
WHERE CONTINENT = 'ASIA';
