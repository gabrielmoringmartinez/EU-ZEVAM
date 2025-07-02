# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

import pandas as pd

from src.load_data_and_prepare_inputs.dimension_names import *


def replace_powertrain_share_registrations_with_country(registrations, country, plot_params):
    """
    Modifies the powertrain-specific share of vehicle registrations for a specified country from a given year onward.
    This function replaces the relative sales and registration values for all countries with the values from the
    selected country starting from a specified year.

    Parameters:
        - registrations (pd.DataFrame): A DataFrame containing registration data by year, powertrain, and country.
        - country (str): The name of the country whose powertrain-specific registration shares will be used to
          replace those for all other countries from the specified year onward.
        - plot_params (dict): A dictionary containing plotting and analysis parameters, including:
          - `year_to_modify_registrations_label` (int): The year from which the registrations for all countries
            will be replaced by the values from the selected country.

    Returns:
        - pd.DataFrame: A modified copy of the `registrations` DataFrame, where the powertrain registration shares
          and relative sales for all countries have been replaced by those of the specified country from the given
          year onward.
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
