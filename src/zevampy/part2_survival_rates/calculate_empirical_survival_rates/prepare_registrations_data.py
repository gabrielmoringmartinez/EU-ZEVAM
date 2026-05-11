"""Prepare registration data for empirical survival-rate estimation."""

# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

import pandas as pd
from zevampy.load_data_and_prepare_inputs.dimension_names import age_dim, country_dim, time_dim, \
    stock_year_empirical_csp_data_dim
from zevampy.part2_survival_rates.calculate_empirical_survival_rates.filter_vehicle_age import filter_vehicle_age


def prepare_registrations_data(registrations, stock_year):
    """
    Prepare registration data for survival-rate estimation.

    This function merges registration data with stock-year information, calculates vehicle ages, and filters the dataset
    to retain only valid vehicle-age ranges.

    Parameters:
        registrations (pandas.DataFrame):
            DataFrame containing historical vehicle registration data.

        stock_year (pandas.DataFrame):
            DataFrame containing stock-year information for each country.

    Returns:
        pandas.DataFrame:
            Registration data with calculated vehicle ages and filtered vehicle-age ranges.
    """
    # Merge to get stock year, calculate vehicle age, and filter
    registrations = pd.merge(registrations, stock_year, on=country_dim, how='left')
    # Calculates the vehicle age in a certain stock year based on the new registrations year
    registrations[age_dim] = registrations[stock_year_empirical_csp_data_dim] - registrations[time_dim] + 1
    # Keeps only values between 1 and 45
    registrations = filter_vehicle_age(registrations)
    return registrations
