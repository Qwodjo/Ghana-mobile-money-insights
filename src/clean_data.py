import os
from datetime import datetime, timedelta

import numpy as np
import pandas as pd


RAW_CSV_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "mobile_money_transactions.csv")
CLEAN_CSV_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "mobile_money_transactions_cleaned.csv")


def run_cleaning():
    """Clean and enrich the raw mobile money dataset.

    This is a script version of the logic in `notebooks/data_cleaning.ipynb`.
    It reads the raw CSV, performs cleaning and enrichment, and writes
    `mobile_money_transactions_cleaned.csv` into the `data/` folder.
    """

    # 1. Load raw CSV
    csv = pd.read_csv(RAW_CSV_PATH)

    # 2. Remove duplicates and rows with any missing values
    csv_cleaned = csv.drop_duplicates()
    csv_cleaned = csv_cleaned.dropna()

    # 3. Drop the 'step' column if present
    if "step" in csv_cleaned.columns:
        csv_cleaned = csv_cleaned.drop(columns=["step"])

    # 4. Add country column
    csv_cleaned["country"] = "Ghana"

    # 5. Add gender with realistic percentages
    gender_probs = [0.55, 0.45]
    csv_cleaned["gender"] = np.random.choice(["M", "F"], size=len(csv_cleaned), p=gender_probs)

    # 6. Add timestamp (date + time) for each transaction
    start_datetime = datetime(2023, 1, 1, 0, 0, 0)
    end_datetime = datetime(2025, 1, 31, 23, 59, 59)
    total_seconds = int((end_datetime - start_datetime).total_seconds())
    random_seconds = np.random.randint(0, total_seconds, size=len(csv_cleaned))
    csv_cleaned["timestamp"] = [
        start_datetime + timedelta(seconds=int(sec)) for sec in random_seconds
    ]

    # 7. Adjust hour distribution (more activity during the day)
    hours = np.arange(24)
    hour_probs = np.array([
        0.005, 0.005, 0.005, 0.005, 0.005, 0.005,  # 0–5
        0.04, 0.04, 0.04, 0.04,                     # 6–9
        0.07, 0.07, 0.07, 0.07, 0.07, 0.07, 0.07,   # 10–16
        0.05, 0.05, 0.05, 0.05, 0.05,               # 17–21
        0.01, 0.01                                  # 22–23
    ])
    hour_probs = hour_probs / hour_probs.sum()
    random_hours = np.random.choice(hours, size=len(csv_cleaned), p=hour_probs)
    csv_cleaned["timestamp"] = pd.to_datetime(csv_cleaned["timestamp"]).dt.normalize() + pd.to_timedelta(
        random_hours, unit="h"
    )

    # Drop original time/h column if present
    if "time/h" in csv_cleaned.columns:
        csv_cleaned = csv_cleaned.drop(columns=["time/h"])

    # 8. Assign Ghana regions with realistic shares
    ghana_regions = [
        "Greater Accra",
        "Ashanti",
        "Eastern",
        "Central",
        "Western",
        "Bono",
        "Bono East",
        "Volta",
        "Northern",
        "Upper East",
        "Upper West",
        "Ahafo",
        "North East",
        "Savannah",
        "Western North",
        "Oti",
    ]
    region_probs = [
        0.22,
        0.19,
        0.09,
        0.08,
        0.07,
        0.04,
        0.04,
        0.06,
        0.06,
        0.04,
        0.03,
        0.03,
        0.02,
        0.02,
        0.02,
        0.02,
    ]
    region_probs = np.array(region_probs) / np.sum(region_probs)
    csv_cleaned["region"] = np.random.choice(ghana_regions, size=len(csv_cleaned), p=region_probs)

    # 9. Add age_group using realistic distribution
    age_groups = ["18-24", "25-34", "35-44", "45-54", "55-64", "65+"]
    age_probs = [0.22, 0.30, 0.22, 0.13, 0.08, 0.05]
    age_probs = np.array(age_probs) / np.sum(age_probs)
    csv_cleaned["age_group"] = np.random.choice(age_groups, size=len(csv_cleaned), p=age_probs)

    # 10. Basic variation: noise on amounts
    np.random.seed(42)
    amount_std = csv_cleaned["amount"].std()
    if amount_std <= 0:
        amount_std = csv_cleaned["amount"].max() * 0.3
    noise = np.random.normal(loc=0, scale=amount_std * 0.4, size=len(csv_cleaned))
    csv_cleaned["amount"] = (csv_cleaned["amount"] + noise).clip(lower=1)

    # 11. More activity in Greater Accra and Ashanti
    high_activity_regions = ["Greater Accra", "Ashanti"]
    mask = csv_cleaned["region"].isin(high_activity_regions)
    extra = csv_cleaned[mask].sample(int(mask.sum() * 0.5), replace=True, random_state=42)
    csv_cleaned = pd.concat([csv_cleaned, extra], ignore_index=True)

    # 12. Skew amounts by age group
    def adjust_amount_by_age_group(row: pd.Series) -> float:
        if row["age_group"] in ["18-24", "25-34"]:
            factor = np.random.uniform(0.6, 0.9)
        elif row["age_group"] in ["35-44", "45-54"]:
            factor = np.random.uniform(1.1, 1.7)
        else:
            factor = np.random.uniform(0.8, 1.3)
        return row["amount"] * factor

    csv_cleaned["amount"] = csv_cleaned.apply(adjust_amount_by_age_group, axis=1)

    # 13. Slightly imbalanced gender
    csv_cleaned["gender"] = np.where(np.random.rand(len(csv_cleaned)) < 0.6, "M", "F")

    # 14. Save cleaned dataset
    csv_cleaned.to_csv(CLEAN_CSV_PATH, index=False)

    print(f"Cleaned dataset saved to {CLEAN_CSV_PATH}")


if __name__ == "__main__":
    run_cleaning()
