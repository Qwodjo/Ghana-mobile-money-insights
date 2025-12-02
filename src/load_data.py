"""Load cleaned mobile money CSV into the PostgreSQL database.

This script:
1. Connects to the Ghana_momo database using `db_connection.get_connection()`.
2. Reads the cleaned CSV from `data/mobile_money_transactions_cleaned.csv`.
3. Inserts the data into the `mobile_money_transactions` table in batches.

Run this AFTER:
- The database `Ghana_momo` exists.
- The table `mobile_money_transactions` has been created using `sql/schema.sql`.
- Your `.env` file has the correct PGHOST/PGPORT/PGUSER/PGPASSWORD/PGDATABASE values.
"""

import math

import pandas as pd
from psycopg2.extras import execute_values

from db_connection import get_connection


# Relative path from the `src` folder to the cleaned CSV file
CSV_PATH = "../data/mobile_money_transactions_cleaned.csv"


def load_csv_batch(df_batch):
    """Insert one batch of rows from a DataFrame into the database.

    df_batch: a slice of the full DataFrame (few thousand rows at a time).
    We:
    - Turn each row into a Python tuple matching the table columns.
    - Use `execute_values` to insert many rows in a single SQL call
      (much faster than inserting one row at a time).
    """

    # 1. Open a new database connection
    conn = get_connection()
    cur = conn.cursor()

    # 2. Convert each DataFrame row into a tuple in the correct column order
    #    The order here MUST match the column list in the INSERT statement.
    rows = [
        (
            float(row["amount"]),        # amount of the transaction
            row["timestamp"],            # full timestamp (date + time)
            row["region"],               # Ghana region
            row["country"],              # country (Ghana)
            row["age_group"],            # age group label, e.g. '25-34'
            row["gender"],               # 'M' or 'F'
            row["transactionType"],      # type of transaction
            bool(row["isFraud"]),        # convert 0/1 to False/True if needed
        )
        for _, row in df_batch.iterrows()
    ]

    insert_sql = """
        INSERT INTO mobile_money_transactions (
            amount,
            timestamp,
            region,
            country,
            age_group,
            gender,
            transactionType,
            isFraud
        )
        VALUES %s
    """

    # 3. Insert all rows for this batch in one go
    execute_values(cur, insert_sql, rows)

    # 4. Save changes and close the connection
    conn.commit()
    cur.close()
    conn.close()


def main():
    """Main entry point: read the CSV and load it in batches."""

    print("Reading cleaned CSV from:", CSV_PATH)
    df = pd.read_csv(CSV_PATH)

    # Ensure the timestamp column is a proper datetime type
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    total_rows = len(df)
    batch_size = 5000  # number of rows to insert per batch
    num_batches = math.ceil(total_rows / batch_size)

    print(f"Total rows to load: {total_rows}")
    print(f"Batch size: {batch_size}, number of batches: {num_batches}")

    for i in range(num_batches):
        start = i * batch_size
        end = min((i + 1) * batch_size, total_rows)
        df_batch = df.iloc[start:end]
        print(f"Loading batch {i + 1}/{num_batches} (rows {start} to {end - 1})...")
        load_csv_batch(df_batch)

    print("All data loaded into mobile_money_transactions.")


if __name__ == "__main__":
    main()
