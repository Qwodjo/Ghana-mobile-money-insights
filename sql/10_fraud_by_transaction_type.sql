-- Project Question: Which mobile money services (transaction types) carry higher fraud risk?
-- This query shows, for each transaction type: total transactions, fraudulent transactions,
-- and fraud rate as a percentage.

SELECT
    transactiontype               AS transaction_type,
    COUNT(*)                      AS tx_count,
    SUM(CASE WHEN isfraud THEN 1 ELSE 0 END) AS fraud_count,
    100.0 * SUM(CASE WHEN isfraud THEN 1 ELSE 0 END) / COUNT(*) AS fraud_rate_pct
FROM mobile_money_transactions
GROUP BY transactiontype
ORDER BY fraud_rate_pct DESC;