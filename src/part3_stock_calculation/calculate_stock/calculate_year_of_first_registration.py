# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

from src.load_data_and_prepare_inputs.dimension_names import stock_year_dim, age_dim, time_dim


def calculate_year_of_first_registration(survival_rates):
    """
        Calculates the year of first registration for each entry in the DataFrame based on stock year and vehicle age.

        Parameters:
            survival_rates (DataFrame): Data containing stock year and vehicle age.
        Returns:
            DataFrame: Updated DataFrame with calculated year of first registration.
        """
    survival_rates[time_dim] = survival_rates[stock_year_dim] - survival_rates[age_dim] + 1
    return survival_rates
