import os
import pandas as pd

INPUT_DIR = "inputs"

# Define files and their grouping columns
GROUPED_FILES = {
    "0_country_clusters.csv": ["geo country"],
    "1_1_new_registrations_by_fuel_type_1970_2050_clusters.csv": ["geo country", "powertrain"],
    "1_2_A_2_new_registrations_data_passenger_cars_eu_countries_1970_2021.csv": ["geo country", "powertrain"],
    "2_1_A_1_age_resolved_data_passenger_car_stock_fleet_eu_countries_2021.csv": ["geo country", "powertrain"],
}


def test_each_country_or_country_powertrain_has_consistent_row_counts():
    for filename, group_cols in GROUPED_FILES.items():
        path = os.path.join(INPUT_DIR, filename)
        df = pd.read_csv(path, delimiter=';', decimal=',')

        # Only drop NA from columns that exist
        available_group_cols = [col for col in group_cols if col in df.columns]
        df = df.dropna(subset=available_group_cols)

        # Group and count rows
        group_sizes = df.groupby(available_group_cols).size()

        # Check if group sizes are consistent
        unique_sizes = group_sizes.unique()
        if len(unique_sizes) > 1:
            most_common = group_sizes.mode().iloc[0]
            inconsistent = group_sizes[group_sizes != most_common]
            summary = "\n".join(f"{idx}: {size} rows" for idx, size in inconsistent.items())
            raise AssertionError(
                f"Inconsistent number of rows per {available_group_cols} in {filename}.\n"
                f"Expected consistent group size (e.g., per year or per fuel type): {most_common}\n"
                f"Inconsistent groups:\n{summary}"
            )