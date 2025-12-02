-- Project Question: Which age groups are the heaviest users of mobile money?
-- This query shows, for each age group: number of transactions, total amount,
-- and average transaction size.

SELECT
    age_group,
    COUNT(*)    AS tx_count,
    SUM(amount) AS total_amount,
    AVG(amount) AS avg_amount
FROM mobile_money_transactions
GROUP BY age_group
ORDER BY tx_count DESC;