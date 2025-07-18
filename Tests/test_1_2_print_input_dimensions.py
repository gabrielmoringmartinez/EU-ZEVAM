import os
import pandas as pd
from collections import defaultdict

INPUT_DIR = "inputs"
dimension_columns = {"geo country", "powertrain", "cluster", "year", "time"}  # add more as needed

def list_dimensions_and_unique_values():
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
    list_dimensions_and_unique_values()