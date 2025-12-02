-- Project Question: Which mobile money services (transaction types) are used the most,
-- and which generate the highest value?
-- This query shows, for each transaction type: number of transactions,
-- total amount, and average transaction size.

SELECT
    transactiontype               AS transaction_type,
    COUNT(*)                      AS tx_count,
    SUM(amount)                   AS total_amount,
    AVG(amount)                   AS avg_amount
FROM mobile_money_transactions
GROUP BY transactiontype
ORDER BY tx_count DESC;