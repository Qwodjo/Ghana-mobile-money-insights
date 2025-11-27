-- Schema definition for storing Ghana mobile money transactions in PostgreSQL
-- Main fact table for mobile money transactions
CREATE TABLE IF NOT EXISTS mobile_money_transactions (
    -- Surrogate primary key generated automatically
    transaction_id BIGSERIAL PRIMARY KEY,
    -- Optional: original id from the raw dataset (if present)
    raw_id BIGINT,
    -- Monetary amount of the transaction (in Ghana Cedi by default)
    amount NUMERIC(14, 2) NOT NULL,
    currency VARCHAR(10) DEFAULT 'GHS',
    -- Full timestamp (date + time + timezone)
    timestamp TIMESTAMPTZ NOT NULL,
    -- Convenience columns derived from `timestamp` for easier querying
    -- (we will populate these via an UPDATE after loading data)
    transaction_date DATE,
    transaction_hour SMALLINT,
    -- Geographic information
    region VARCHAR(50) NOT NULL,
    -- e.g. 'Greater Accra'
    country VARCHAR(50) NOT NULL DEFAULT 'Ghana',
    -- Demographic information
    age_group VARCHAR(10) NOT NULL,
    -- e.g. '18-24', '25-34'
    gender CHAR(1) NOT NULL CHECK (gender IN ('M', 'F')),
    -- Behaviour / risk information from the original dataset
    transactionType VARCHAR(50) NOT NULL,
    -- e.g. CASH_IN, TRANSFER, PAYMENT
    isFraud BOOLEAN NOT NULL,
    -- TRUE for fraud, FALSE otherwise
    -- When the row was loaded into the database
    created_at TIMESTAMPTZ DEFAULT NOW()
);
-- Index to speed up time-based queries (e.g. trends over time)
CREATE INDEX IF NOT EXISTS idx_mmt_timestamp ON mobile_money_transactions (timestamp);
-- Index to speed up regional aggregations (e.g. volume by region)
CREATE INDEX IF NOT EXISTS idx_mmt_region ON mobile_money_transactions (region);
-- Index to speed up age group aggregations
CREATE INDEX IF NOT EXISTS idx_mmt_age_group ON mobile_money_transactions (age_group);
-- Index to speed up gender-based analyses
CREATE INDEX IF NOT EXISTS idx_mmt_gender ON mobile_money_transactions (gender);
-- Index to speed up transaction type analysis
CREATE INDEX IF NOT EXISTS idx_mmt_transactionType ON mobile_money_transactions (transactionType);
-- Index to speed up fraud analysis
CREATE INDEX IF NOT EXISTS idx_mmt_isFraud ON mobile_money_transactions (isFraud);



SELECT * FROM mobile_money_transactions;
INSERT INTO mobile_money_transactions (raw_id, amount, currency, timestamp, transaction_date, transaction_hour, region, country, age_group, gender, transactionType, isFraud)
VALUES (123456, 150.75, 'GHS', '2024-06-15 14:30:00+00', '2024-06-15', 14, 'Greater Accra', 'Ghana', '25-34', 'M', 'TRANSFER', FALSE);