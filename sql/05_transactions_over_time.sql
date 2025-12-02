-- Project Question: How does mobile money usage evolve over time in the dataset?
-- This query aggregates transactions per day so we can see trends
-- (growth, peaks, or seasonality) over the analysis period.

SELECT
    DATE("timestamp") AS tx_date,
    COUNT(*)          AS tx_count,
    SUM(amount)       AS total_amount
FROM mobile_money_transactions
GROUP BY DATE("timestamp")
ORDER BY tx_date;