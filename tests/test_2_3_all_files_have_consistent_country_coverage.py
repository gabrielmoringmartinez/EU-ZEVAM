# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

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
    """
       Load unique country names from a specified CSV file and column.

       Args:
           file_path (str): Path to the CSV input file.
           column_name (str): Name of the column containing country names (default "geo country").

       Returns:
           set: A set of unique country names (words) with spaces at the start and end removed.
       """
    df = pd.read_csv(file_path, delimiter=';', decimal=',')
    return set(df[column_name].dropna().str.strip().unique())


def test_countries_exist_in_reference():
    """
        Verify that all countries listed in specified input files exist in the reference country list.

        This test loads country names from each file in FILES_TO_CHECK and compares them against the
        official reference list of countries found in '0_country_clusters.csv'.

        If any country appears in an input file but not in the reference file, the test fails and
        reports which countries are unknown and in which files.

        Raises:
            AssertionError: If unknown countries are found in any of the input files.
        """
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
    """
        Check that the same set of countries is consistently present across all specified input files.

        This test ensures no country is missing from any of the input files listed in FILES_TO_CHECK.
        It identifies and reports any inconsistencies where countries appear in some files but not all.

        Raises:
            AssertionError: If any countries are missing from one or more input files.
        """
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
