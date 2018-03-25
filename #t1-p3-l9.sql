# Term 1 - Part 3 - Lesson 9
# notes

# join 2 tables
# categoriation based on calculations

SELECT a.name, SUM(total_amt_USD) total_spent,
CASE
WHEN SUM(total_amt_USD) > 200000 THEN 'top'
WHEN SUM(total_amt_USD) > 100000 THEN 'middle'
ELSE 'low' END AS customer_level
FROM orders o
JOIN accounts a
ON o.account_id = a.id
GROUP BY a.name
ORDER BY 2 DESC

# join 2 tables
# categoriation based on calculations
# with calculations restricted to dates > 31.12.2015

SELECT a.name, SUM(total_amt_usd) total_spent,
     CASE WHEN SUM(total_amt_usd) > 200000 THEN 'top'
     WHEN  SUM(total_amt_usd) > 100000 THEN 'middle'
     ELSE 'low' END AS customer_level
FROM orders o
JOIN accounts a
ON o.account_id = a.id
WHERE occurred_at > '2015-12-31'
GROUP BY 1
ORDER BY 2 DESC;
