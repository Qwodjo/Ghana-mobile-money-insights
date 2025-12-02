-- Project Question: What is the overall fraud rate in the dataset?
-- This query compares total fraudulent transactions to total transactions
-- and computes the fraud rate as a percentage.

SELECT
    COUNT(*) AS total_tx,
    SUM(CASE WHEN isfraud THEN 1 ELSE 0 END) AS fraud_tx,
    100.0 * SUM(CASE WHEN isfraud THEN 1 ELSE 0 END) / COUNT(*) AS fraud_rate_pct
FROM mobile_money_transactions;