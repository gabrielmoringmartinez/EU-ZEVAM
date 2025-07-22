import os
import pandas as pd
from collections import defaultdict

INPUT_DIR = "inputs"
dimension_columns = {"geo country", "powertrain", "cluster", "year", "time"}  # add more as needed

def list_dimensions_and_unique_values():
    """
       Scan CSV input files to identify and report unique values for key dimension columns.

       This function searches all CSV files in the 'inputs' directory and extracts unique values
       from specified dimension columns (e.g., "geo country", "powertrain", "cluster", "time").
       It prints the unique values found per file and a combined list across all files for each dimension.

       Notes:
           - CSV files are read with semicolon (';') delimiter and comma (',') decimal notation.
           - Files that cannot be read will print a warning message but do not halt execution.

       Returns:
           None: Outputs are printed directly to the console.
       """
    files = [f for f in os.listdir(INPUT_DIR) if f.endswith(".csv")]
    dimension_values = defaultdict(lambda: defaultdict(set))

    for file in files:
        path = os.path.join(INPUT_DIR, file)
        try:
            df = pd.read_csv(path, delimiter=';', decimal=',')
            for col in df.columns:
                col_clean = col.strip()
                if col_clean in dimension_columns:
                    unique_vals = df[col].dropna().astype(str).str.strip().unique()
                    dimension_values[col_clean][file] = set(unique_vals)
        except Exception as e:
            print(f"⚠️ Could not read {file}: {e}")

    for dim, sources in dimension_values.items():
        print(f"\n=== Dimension: {dim} ===")
        all_values = set()
        for file, values in sources.items():
            print(f"From {file}: {sorted(values)}")
            all_values |= values
        print(f"Combined ({len(all_values)} unique): {sorted(all_values)}")

def test_list_dimensions_and_unique_values():
    """
       Test wrapper to run `list_dimensions_and_unique_values()` function.

       This test ensures that the dimension listing function executes without errors.
       It does not perform assertions but can help verify data consistency during development.

       Returns:
           None
       """
    list_dimensions_and_unique_values()