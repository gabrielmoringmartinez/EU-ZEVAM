# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

import pandas as pd

from zevampy.load_data_and_prepare_inputs.dimension_names import country_dim, time_dim


def preprocess_historical_registrations(historical_registrations, registrations_projected, reference_year,
                                        countries_to_keep, start_year, end_year):
    """
        Preprocesses the historical vehicle registration data by filtering, merging, and cleaning the data.
        Parameters:
        - historical_registrations (pd.DataFrame): DataFrame containing historical registration data.
        - countries_to_keep (list): List of countries to retain in the dataset.
        - reference_year (int): The reference year used to filter the historical data.
        Returns:
        - pd.DataFrame: The cleaned and processed historical registration data.
        """
    # Step 1: Remove data for the year 2022
    historical_registrations = historical_registrations[historical_registrations[time_dim] <= reference_year]
    common_cols = historical_registrations.columns.intersection(registrations_projected.columns)
    absolute_registrations = pd.concat([historical_registrations[common_cols], registrations_projected[common_cols]],
                                       ignore_index=True)
    absolute_registrations = absolute_registrations[absolute_registrations[country_dim].isin(countries_to_keep)]
    absolute_registrations = absolute_registrations[
        (absolute_registrations[time_dim] >= start_year) &
        (absolute_registrations[time_dim] <= end_year)
        ]
    return absolute_registrations
