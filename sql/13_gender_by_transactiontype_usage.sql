-- Project Question: How does mobile money usage by gender differ across transaction types?
-- This query shows, for each transaction type and gender: number of transactions,
-- total transaction amount, and average transaction size.

SELECT
    transactiontype,
    gender,
    COUNT(*)    AS tx_count,
    SUM(amount) AS total_amount,
    AVG(amount) AS avg_amount
FROM mobile_money_transactions
GROUP BY transactiontype, gender
ORDER BY transactiontype, tx_count DESC;