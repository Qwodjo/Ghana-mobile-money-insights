-- Project Question: How does mobile money usage by gender vary across regions?
-- This query shows, for each region and gender: number of transactions,
-- total transaction amount, and average transaction size.

SELECT
    region,
    gender,
    COUNT(*)    AS tx_count,
    SUM(amount) AS total_amount,
    AVG(amount) AS avg_amount
FROM mobile_money_transactions
GROUP BY region, gender
ORDER BY region, tx_count DESC;