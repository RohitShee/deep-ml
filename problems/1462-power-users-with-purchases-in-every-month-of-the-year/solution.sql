-- your query
SELECT user_id 
FROM
(SELECT user_id, month(purchase_date) as purchase_month
FROM purchases
WHERE year(purchase_date)=2024
GROUP BY user_id, month(purchase_date)
HAVING count(*)>=2)
GROUP BY user_id 
HAVING count(*)=12;
