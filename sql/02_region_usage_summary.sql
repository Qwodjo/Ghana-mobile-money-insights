-- Project Question: Which regions drive the most mobile money usage and value?
-- This query shows, for each region: number of transactions, total amount,
-- and average transaction size.

SELECT
    region,
    COUNT(*)    AS tx_count,
    SUM(amount) AS total_amount,
    AVG(amount) AS avg_amount
FROM mobile_money_transactions
GROUP BY region
ORDER BY tx_count DESC;