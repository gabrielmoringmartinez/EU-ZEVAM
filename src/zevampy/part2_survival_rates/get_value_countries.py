"""Retrieve survival-rate values for a selected country."""

# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

from zevampy.load_data_and_prepare_inputs.dimension_names import country_dim, survival_rate_dim


def get_value_countries(survival_rates, country_name):
    """
    Retrieve survival rates for a specific country.

    Parameters:
        survival_rates (pandas.DataFrame):
            DataFrame containing survival-rate data.

        country_name (str):
            Name of the country for which survival rates are retrieved.

    Returns:
        pandas.Series:
            Survival-rate values for the selected country.
    """
    values_country = survival_rates[survival_rates[country_dim] == country_name]
    survival_rates_country = values_country[survival_rate_dim]
    return survival_rates_country
