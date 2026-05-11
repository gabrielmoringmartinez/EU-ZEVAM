"""Calculate first-registration years from stock years and vehicle ages."""

# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

from zevampy.load_data_and_prepare_inputs.dimension_names import stock_year_dim, age_dim, time_dim


def calculate_year_of_first_registration(survival_rates):
    """
    Calculate the year of first vehicle registration.

    This function derives the first-registration year from the stock year and vehicle age.

    Parameters:
        survival_rates (pandas.DataFrame):
            DataFrame containing stock-year and vehicle-age data.

    Returns:
        pandas.DataFrame:
            Updated DataFrame containing calculated first-registration years.
    """
    survival_rates[time_dim] = survival_rates[stock_year_dim] - survival_rates[age_dim] + 1
    return survival_rates
