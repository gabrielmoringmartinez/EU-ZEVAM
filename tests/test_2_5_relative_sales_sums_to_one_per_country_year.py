# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

import os
import pandas as pd
import pytest

INPUT_DIR = "inputs"
FILENAME = "1_1_new_registrations_by_fuel_type_1970_2050_clusters.csv"

def test_relative_sales_sums_to_one_per_country_year():
    """
    Verify that 'relative sales' values sum to 1.00 per country and year in the input CSV.

    This test reads the specified file and checks that for each combination of 'time' (year)
    and 'geo country', the sum of the 'relative sales' column is approximately 1.00 (within ±0.01).

    It also asserts that required columns are present and handles missing or non-numeric values
    by excluding them from the sum calculation.

    Raises:
        AssertionError: If any country-year group’s relative sales sum differs from 1.00 by more than 0.01,
                        or if required columns are missing.
    """
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
