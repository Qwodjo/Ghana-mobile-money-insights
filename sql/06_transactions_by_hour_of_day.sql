-- Project Question: At what time of day do customers use mobile money the most?
-- This query counts transactions by hour of day to reveal busy hours.

SELECT
    EXTRACT(HOUR FROM "timestamp") AS hour_of_day,
    COUNT(*)                        AS tx_count,
    SUM(amount)                     AS total_amount
FROM mobile_money_transactions
GROUP BY EXTRACT(HOUR FROM "timestamp")
ORDER BY hour_of_day;