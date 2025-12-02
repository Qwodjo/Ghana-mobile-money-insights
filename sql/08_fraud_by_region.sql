-- Project Question: Which regions show higher fraud risk in mobile money usage?
-- This query shows, for each region: total transactions, fraudulent transactions,
-- and fraud rate as a percentage.

SELECT
    region,
    COUNT(*) AS tx_count,
    SUM(CASE WHEN isfraud THEN 1 ELSE 0 END) AS fraud_count,
    100.0 * SUM(CASE WHEN isfraud THEN 1 ELSE 0 END) / COUNT(*) AS fraud_rate_pct
FROM mobile_money_transactions
GROUP BY region
ORDER BY fraud_rate_pct DESC;