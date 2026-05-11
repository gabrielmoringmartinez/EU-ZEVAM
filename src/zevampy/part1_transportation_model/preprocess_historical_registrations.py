"""Preprocess historical and projected vehicle registration datasets."""

# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

import pandas as pd

from zevampy.load_data_and_prepare_inputs.dimension_names import country_dim, time_dim


def preprocess_historical_registrations(historical_registrations, registrations_projected, reference_year,
                                        countries_to_keep, start_year, end_year):
    """
    Preprocess historical and projected vehicle registration data.

    The function filters historical registrations up to the specified reference year, combines them with projected
    registrations, filters the selected countries, and restricts the dataset to the specified simulation time range.

    Parameters:
        historical_registrations (pandas.DataFrame):
            DataFrame containing historical vehicle registration data.

        registrations_projected (pandas.DataFrame):
            DataFrame containing projected vehicle registrations.

        reference_year (int):
            Final historical year included before projected data begins.

        countries_to_keep (list[str]):
            Countries that should remain in the processed dataset.

        start_year (int):
            First year included in the processed dataset.

        end_year (int):
            Final year included in the processed dataset.

    Returns:
        pandas.DataFrame:
            Cleaned and combined registration dataset containing historical and projected registrations.
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
