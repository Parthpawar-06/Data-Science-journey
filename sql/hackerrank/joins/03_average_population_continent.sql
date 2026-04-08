-- Problem: Average Population of Each Continent
-- Platform: HackerRank | Difficulty: Easy
-- Link: https://www.hackerrank.com/challenges/average-population-of-each-continent/problem
--
-- Task: For each continent, find average city population rounded down.
-- Combines JOIN (day 3) + GROUP BY + FLOOR (day 2) — key milestone.

SELECT CONTINENT ,FLOOR(AVG(CITY.POPULATION))
FROM COUNTRY 
JOIN CITY ON COUNTRY.CODE = CITY.COUNTRYCODE
GROUP BY CONTINENT;
