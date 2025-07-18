import os
import pandas as pd
import pytest

INPUT_DIR = "inputs"
REFERENCE_FILE = os.path.join(INPUT_DIR, "0_country_clusters.csv")

FILES_TO_CHECK = {
    "1_2_A_2_new_registrations...": "1_2_A_2_new_registrations_data_passenger_cars_eu_countries_1970_2021.csv",
    "2_1_A_1_age_resolved_data...": "2_1_A_1_age_resolved_data_passenger_car_stock_fleet_eu_countries_2021.csv",
    "2_2_A_1_stock_year": "2_2_A_1_stock_year.csv"
}


def load_countries_from_file(file_path: str, column_name: str = "geo country") -> set:
    df = pd.read_csv(file_path, delimiter=';', decimal=',')
    return set(df[column_name].dropna().str.strip().unique())


def test_countries_exist_in_reference():
    reference_countries = load_countries_from_file(REFERENCE_FILE)

    for label, filename in FILES_TO_CHECK.items():
        path = os.path.join(INPUT_DIR, filename)
        countries = load_countries_from_file(path)

        unknown = countries - reference_countries
        assert not unknown, (
            f"The following countries in '{filename}' are not listed in '0_country_clusters.csv':\n"
            + "\n".join(f"- {country}" for country in sorted(unknown))
        )


def test_all_files_have_consistent_country_coverage():
    country_sets = {}
    for label, filename in FILES_TO_CHECK.items():
        path = os.path.join(INPUT_DIR, filename)
        country_sets[label] = load_countries_from_file(path)

    all_countries = set.union(*country_sets.values())
    inconsistencies = []

    for country in sorted(all_countries):
        present_in = [label for label, countries in country_sets.items() if country in countries]
        if len(present_in) != len(FILES_TO_CHECK):
            missing_from = set(FILES_TO_CHECK.keys()) - set(present_in)
            inconsistencies.append(
                f"- {country} is missing in: {', '.join(sorted(missing_from))}"
            )

    assert not inconsistencies, (
        "Some countries are not present in all 3 input files:\n" + "\n".join(inconsistencies)
    )