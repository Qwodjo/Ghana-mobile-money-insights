-- Project Question: What does the overall mobile money activity in this dataset look like?
-- This query gives high-level context: number of transactions, time period,
-- how many regions / age groups / genders / transaction types, and total/average amount.

SELECT
    COUNT(*)                         AS total_transactions,
    COUNT(DISTINCT region)           AS distinct_regions,
    COUNT(DISTINCT age_group)        AS distinct_age_groups,
    COUNT(DISTINCT gender)           AS distinct_genders,
    COUNT(DISTINCT transactiontype)  AS distinct_transaction_types,
    MIN("timestamp")                   AS min_timestamp,
    MAX("timestamp")                   AS max_timestamp,
    SUM(amount)                      AS total_amount,
    AVG(amount)                      AS avg_amount
FROM mobile_money_transactions;