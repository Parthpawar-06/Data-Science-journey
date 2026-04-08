-- Problem: African Cities
-- Platform: HackerRank | Difficulty: Easy
-- Link: https://www.hackerrank.com/challenges/african-cities/problem
--
-- Task: Return names of all cities in Africa continent.

SELECT CITY.NAME
FROM CITY 
JOIN COUNTRY ON CITY.COUNTRYCODE = COUNTRY.CODE
WHERE CONTINENT = 'Africa';
