-- Project Question: Are there differences in fraud exposure between genders?
-- This query shows, for each gender: total transactions, fraudulent transactions,
-- and fraud rate as a percentage.

SELECT
    gender,
    COUNT(*) AS tx_count,
    SUM(CASE WHEN isfraud THEN 1 ELSE 0 END) AS fraud_count,
    100.0 * SUM(CASE WHEN isfraud THEN 1 ELSE 0 END) / COUNT(*) AS fraud_rate_pct
FROM mobile_money_transactions
GROUP BY gender
ORDER BY fraud_rate_pct DESC;