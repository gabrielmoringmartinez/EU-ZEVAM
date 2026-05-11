"""Replace registration shares with country-specific registration scenarios."""

# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

import pandas as pd

from zevampy.load_data_and_prepare_inputs.dimension_names import *


def replace_powertrain_share_registrations_with_country(registrations, country, plot_params):
    """
    Replace powertrain registration shares with values from one country.

    This function applies the selected country's powertrain-specific registration shares to all countries from a
    configured year onward.

    Parameters:
        registrations (pandas.DataFrame):
            Vehicle registration data by country, year, and powertrain.

        country (str):
            Country whose registration shares are used as replacement values.

        plot_params (dict):
            Dictionary containing sensitivity-analysis settings, including the year from which registrations are
            modified.

    Returns:
        pandas.DataFrame:
            Updated registration DataFrame containing modified powertrain shares and registration values.
    """
    year_country_replied = plot_params[year_to_modify_registrations_label]
    registrations = registrations.copy()
    # Selecting rows for the specific country label
    country_data = registrations[registrations[country_dim] == country]
    # Split the country data into before 2024 and from 2024 onwards
    country_data_before_2024 = country_data[country_data[time_dim] < year_country_replied]
    country_data_from_2024 = country_data[country_data[time_dim] >= year_country_replied]

    # Select survival rates for the specified country from 2024 onwards
    country_registrations_share_from_2024 = country_data_from_2024[[time_dim, powertrain_dim, relative_sales_dim,
                                                                    registrations_by_powertrain_dim]]

    # Merge survival rates from 2024 onwards with the original DataFrame for all countries
    registrations_merged = pd.merge(registrations, country_registrations_share_from_2024,
                                    on=[time_dim, powertrain_dim], suffixes=('', f'_{country}'), how='left')

    # Replace values from 2024 onwards
    registrations_merged.loc[registrations_merged[time_dim] >= year_country_replied, relative_sales_dim] = \
        registrations_merged[f'{relative_sales_dim}_{country}']
    registrations_merged.loc[registrations_merged[time_dim] >= year_country_replied, registrations_by_powertrain_dim] \
        = registrations_merged[f'{registrations_by_powertrain_dim}_{country}']

    # Drop the temporary columns
    registrations_merged.drop(columns=[f'{relative_sales_dim}_{country}',
                                       f'{registrations_by_powertrain_dim}_{country}'], inplace=True)
    registrations_merged[registrations_by_powertrain_dim] = registrations_merged[new_registrations_dim] *\
                                                            registrations_merged[relative_sales_dim]
    return registrations_merged
