import os
import pandas as pd
import pytest

INPUT_DIR = "inputs"


def get_all_input_csv_files():
    """Return a list of all .csv files in the inputs folder."""
    return [
        f for f in os.listdir(INPUT_DIR)
        if f.endswith(".csv") and os.path.isfile(os.path.join(INPUT_DIR, f))
    ]


@pytest.mark.parametrize("filename", get_all_input_csv_files())
def test_no_missing_values_in_input_csv(filename):
    file_path = os.path.join(INPUT_DIR, filename)
    df = pd.read_csv(
        file_path,
        delimiter=';',
        decimal=',',
        keep_default_na=True,
        na_values=["", " ", "  ", "NA", "n/a", "null"]
    )
    # Check if any missing values exist
    assert not df.isnull().values.any(), f"Missing values found in: {filename}"

    # Optional: check that there are no partially filled rows
    partially_filled = df.notnull().any(axis=1) & df.isnull().any(axis=1)
    assert not partially_filled.any(), f"Partially filled rows found in: {filename}"
