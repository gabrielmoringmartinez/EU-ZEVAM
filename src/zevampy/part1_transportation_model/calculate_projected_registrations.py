"""Calculate projected vehicle registrations by country."""

# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

import pandas as pd
from zevampy.load_data_and_prepare_inputs.dimension_names import time_dim, new_registrations_dim, share_dim


def calculate_projected_registrations(country_registration_shares, registrations_projected):
    """
    Calculate projected vehicle registrations for each country.

    The function combines country-level registration shares with projected
    total vehicle registrations and estimates future registrations for each
    country by multiplying the projected totals by the corresponding
    country shares.

    Parameters:
        country_registration_shares (pandas.DataFrame):
            DataFrame containing the share of vehicle registrations for
            each country.

        registrations_projected (pandas.DataFrame):
            DataFrame containing projected total vehicle registrations for
            future years.

    Returns:
        pandas.DataFrame:
            DataFrame containing projected vehicle registrations for each
            country and year.
    """
    # Perform cross join between country shares and vehicle registrations by year
    projected_registrations = pd.merge(country_registration_shares,
                                       registrations_projected[[time_dim, new_registrations_dim]], how='cross')

    # Calculate projected registrations by multiplying share with total registrations
    projected_registrations[new_registrations_dim] = projected_registrations[new_registrations_dim] * \
                                                     projected_registrations[share_dim]

    # Drop the share_dim column as it is no longer needed
    projected_registrations = projected_registrations.drop(columns=[share_dim])
    return projected_registrations
