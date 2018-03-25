# Term 1 - Part 3 - Lesson 10
# notes

SELECT reg_name, MAX(total_amt) total_amt
FROM(
  SELECT sales_reps.name rep_name, region.name reg_name, SUM(orders.total_amt_usd) total_amt
  FROM sales_reps
  JOIN accounts
  ON sales_reps.id = accounts.sales_rep_id
  JOIN orders
  ON accounts.id = orders.account_id
  JOIN region
  ON region.id = sales_reps.region_id
  GROUP BY 1,2
  ORDER BY 3 DESC
) t1
GROUP BY 1
