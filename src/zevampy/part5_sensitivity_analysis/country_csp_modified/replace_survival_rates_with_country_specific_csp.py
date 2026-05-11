"""Replace CSP curves with country-specific survival-rate distributions."""

# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

import pandas as pd

from zevampy.load_data_and_prepare_inputs.dimension_names import *


def replace_survival_rates_with_country_specific_csp(survival_rates, country_label):
    """
    Replace CSP values with country-specific survival-rate curves.

    This function applies the fitted cumulative survival probability (CSP) curves from a selected country to all
    countries in the dataset.

    Parameters:
        survival_rates (pandas.DataFrame):
            DataFrame containing fitted survival-rate values.

        country_label (str):
            Country whose CSP curves are applied to all countries.

    Returns:
        pandas.DataFrame:
            DataFrame containing updated survival-rate values.
    """
    # Selecting rows for the specific country label
    country_data = survival_rates[survival_rates[country_dim] == country_label]
    # Selecting survival rates for the specified country
    country_survival_rates = country_data[[age_dim, survival_rate_weibull_dim, survival_rate_weibull_gaussian_dim,
                                           distribution_dim]]
    # Merge survival rates of the specified country with the original DataFrame for all countries
    survival_rates_updated = pd.merge(survival_rates, country_survival_rates, on=age_dim, suffixes=(f'_{country_label}', ''))
    # Drop redundant columns
    survival_rates_updated.drop(columns=[f'{survival_rate_weibull_dim}_{country_label}',
                                        f'{survival_rate_weibull_gaussian_dim}_{country_label}',
                                        f'{distribution_dim}_{country_label}'], inplace=True)
    return survival_rates_updated

