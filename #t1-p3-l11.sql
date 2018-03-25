# Term 1 - Part 3 - Lesson 11
# notes

SELECT SUM(num) nums, SUM(letter) letters
FROM (
  SELECT name, CASE
  WHEN LEFT(UPPER(name), 1) IN ('0','1','2','3','4','5','6','7','8','9') THEN 1
  ELSE 0
  END AS num, CASE
  WHEN LEFT(UPPER(name), 1) IN ('0','1','2','3','4','5','6','7','8','9') THEN 0
  ELSE 1
  END AS letter
  FROM accounts) t1;


SELECT
  primary_poc,
  STRPOS(primary_poc, ' ') AS ws_pos,
  LEFT(primary_poc, STRPOS(primary_poc, ' ') - 1) AS first_name,
  RIGHT(primary_poc, LENGTH(primary_poc) - STRPOS(primary_poc, ' ')) AS last_name
FROM accounts;


WITH table_1 AS (
  SELECT
    primary_poc,
    STRPOS(primary_poc, ' ') AS ws_pos,
    LEFT(primary_poc, STRPOS(primary_poc, ' ') - 1) AS first_name,
    RIGHT(primary_poc, LENGTH(primary_poc) - STRPOS(primary_poc, ' ')) AS last_name,
    name AS company
  FROM accounts
)
SELECT first_name, last_name, CONCAT(first_name, '.', last_name, '@', REPLACE(company, ' ', ''), '.com')
FROM table_1
