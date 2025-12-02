-- Project Question (detail): Which age groups send larger amounts on average?
-- This query focuses only on the average transaction amount per age group,
-- which supports insights on value, not just volume.

SELECT
    age_group,
    AVG(amount) AS avg_amount
FROM mobile_money_transactions
GROUP BY age_group
ORDER BY avg_amount DESC;