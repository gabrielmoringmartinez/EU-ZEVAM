import os
import pandas as pd
import pytest

INPUT_DIR = "inputs"
FILENAME = "1_1_new_registrations_by_fuel_type_1970_2050_clusters.csv"

def test_relative_sales_sums_to_one_per_country_year():
    path = os.path.join(INPUT_DIR, FILENAME)
    df = pd.read_csv(path, delimiter=';', decimal=',')

    required_cols = {"time", "geo country", "relative sales"}
    missing = required_cols - set(df.columns)
    assert not missing, f"Missing columns in {FILENAME}: {missing}"

    df["relative sales"] = pd.to_numeric(df["relative sales"], errors="coerce")
    df = df.dropna(subset=["relative sales", "time", "geo country"])

    grouped = df.groupby(["time", "geo country"])["relative sales"].sum().round(2)
    invalid = grouped[grouped != 1.00]

    if not invalid.empty:
        details = "\n".join(
            f"{country} in {year}: sum = {value}"
            for (year, country), value in invalid.items()
        )
        raise AssertionError(
            f"In file '{FILENAME}', relative sales do not sum to 1.00 (±0.01) "
            f"for the following year-country combinations:\n{details}"
        )
