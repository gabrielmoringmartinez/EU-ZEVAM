# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

import pandas as pd
from src.load_data_and_prepare_inputs.dimension_names import age_dim, country_dim, time_dim, \
    stock_year_empirical_csp_data_dim
from src.part2_survival_rates.calculate_empirical_survival_rates.filter_vehicle_age import filter_vehicle_age


def prepare_registrations_data(registrations, stock_year):
    """
        Merges registration data with stock year information, calculates vehicle age (age_dim), and filters the result.

        Args:
            registrations (pd.DataFrame): DataFrame containing vehicle registration data with 'year' and country_dim.
            stock_year (pd.DataFrame): DataFrame containing stock_year_dim information for each country_dim.

        Returns:
            pd.DataFrame: A DataFrame with added age_dim column, filtered to include only relevant ages.
        """
    # Merge to get stock year, calculate vehicle age, and filter
    registrations = pd.merge(registrations, stock_year, on=country_dim, how='left')
    # Calculates the vehicle age in a certain stock year based on the new registrations year
    registrations[age_dim] = registrations[stock_year_empirical_csp_data_dim] - registrations[time_dim] + 1
    # Keeps only values between 1 and 45
    registrations = filter_vehicle_age(registrations)
    return registrations
