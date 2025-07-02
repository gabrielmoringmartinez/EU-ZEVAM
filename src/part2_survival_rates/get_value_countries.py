# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

from src.load_data_and_prepare_inputs.dimension_names import country_dim, survival_rate_dim


def get_value_countries(survival_rates, country_name):
    """
    Retrieves survival rates for a specified country.

    This function filters the `survival_rates` DataFrame to extract survival rate values corresponding
    to the specified country.

    Parameters:
        survival_rates (DataFrame): Contains survival rate data.
        country_name (str): The name or label of the country for which to retrieve survival rates.

    Returns:
        Series: Survival rates for the specified country.
    """
    values_country = survival_rates[survival_rates[country_dim] == country_name]
    survival_rates_country = values_country[survival_rate_dim]
    return survival_rates_country
