"""Airflow DAG: clean raw mobile money CSV and upload cleaned CSV to S3.

This DAG intentionally does NOT touch your existing Postgres database.
It only:
1. Runs src.clean_data.run_cleaning() to regenerate the cleaned CSV file.
2. Uploads that cleaned CSV to an S3 bucket using boto3.

The project root is mounted into the Airflow container at /opt/airflow/project
(via docker-compose.yml), so we can import src.* modules and access data/.
"""

from datetime import datetime
import os
import sys

import boto3
from airflow import DAG
from airflow.operators.python import PythonOperator

# Inside the Airflow container, your project root is mounted here
PROJECT_ROOT = "/opt/airflow/project"
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# Import your existing cleaning function from src/clean_data.py
from src.clean_data import run_cleaning

# Path to the cleaned CSV inside the container (same relative path as on host)
CLEANED_CSV_PATH = os.path.join(
    PROJECT_ROOT,
    "data",
    "mobile_money_transactions_cleaned.csv",
)

# TODO: change this to your real bucket name (must already exist in AWS)
BUCKET_NAME = "ghana-mm-data-qwodjo-1234"  # e.g. "ghana-mm-data-qwodjo-1234"
# Optional folder/key prefix inside the bucket
KEY_PREFIX = "raw/"


def upload_cleaned_csv_to_s3(**context):
    """Upload the cleaned CSV to S3 using boto3.

    This function expects AWS credentials and region to be available
    as environment variables in the Airflow container:
    - AWS_ACCESS_KEY_ID
    - AWS_SECRET_ACCESS_KEY
    - AWS_DEFAULT_REGION
    """

    if not os.path.exists(CLEANED_CSV_PATH):
        raise FileNotFoundError(f"Cleaned CSV not found at {CLEANED_CSV_PATH}")

    s3_client = boto3.client("s3")
    key = os.path.join(KEY_PREFIX, os.path.basename(CLEANED_CSV_PATH))

    # This uploads the local file CLEANED_CSV_PATH to s3://BUCKET_NAME/key
    s3_client.upload_file(CLEANED_CSV_PATH, BUCKET_NAME, key)


default_args = {
    "owner": "airflow",
    "depends_on_past": False,
}

with DAG(
    dag_id="mobile_money_clean_to_s3",
    default_args=default_args,
    start_date=datetime(2023, 1, 1),
    schedule_interval=None,  # Run manually; change to "@daily" later if you want
    catchup=False,
) as dag:

    clean_data_task = PythonOperator(
        task_id="clean_data_task",
        python_callable=run_cleaning,
    )

    upload_to_s3_task = PythonOperator(
        task_id="upload_to_s3_task",
        python_callable=upload_cleaned_csv_to_s3,
        provide_context=True,
    )

    # Ensure cleaning runs before upload
    clean_data_task >> upload_to_s3_task
