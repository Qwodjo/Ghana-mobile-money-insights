-- Project Question: Which age groups are more exposed to fraud in mobile money?
-- This query shows, for each age group: total transactions, fraudulent transactions,
-- and fraud rate as a percentage.

SELECT
    age_group,
    COUNT(*) AS tx_count,
    SUM(CASE WHEN "isFraud" = 1 THEN 1 ELSE 0 END) AS fraud_count,
    100.0 * SUM(CASE WHEN "isFraud" = 1 THEN 1 ELSE 0 END) / COUNT(*) AS fraud_rate_pct
FROM mobile_money_transactions
GROUP BY age_group
ORDER BY fraud_rate_pct DESC;