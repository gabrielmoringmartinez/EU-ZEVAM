"""Calculate country-level shares of vehicle registrations."""
# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

from zevampy.load_data_and_prepare_inputs.dimension_names import time_dim, new_registrations_dim, share_dim, country_dim


def calculate_country_shares(data, year):
    """
    Calculate vehicle-registration shares for each country in a given year.

    The function filters the historical registration dataset for the
    specified year, computes the total number of registrations across all
    countries, and calculates the relative registration share of each
    country.

    Parameters:
        data (pandas.DataFrame):
            Historical registration dataset containing country-level
            registration values.

        year (int):
            Year for which the registration shares should be calculated.

    Returns:
        pandas.DataFrame:
            DataFrame containing country labels and their corresponding
            registration shares for the selected year.
    """
    # Step 1: Filter for the given year
    data_year = data[data[time_dim] == year].copy()
    # Step 2: Calculate the total registrations for the given year
    total_registrations_year = data_year[new_registrations_dim].sum()
    # Step 3: Calculate the share of each country
    data_year[share_dim] = data_year[new_registrations_dim] / total_registrations_year
    # Return the relevant columns
    return data_year[[country_dim, share_dim]]
