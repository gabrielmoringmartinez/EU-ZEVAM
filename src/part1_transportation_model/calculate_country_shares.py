# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

from src.load_data_and_prepare_inputs.dimension_names import time_dim, new_registrations_dim, share_dim, country_dim


def calculate_country_shares(data, year):
    """
        Calculates the share of vehicle registrations for each country for the last historical year available.

        Parameters:
        - data (pd.DataFrame): DataFrame containing the cleaned and processed historical registration data.
        - year (int): The year for which the share of registrations should be calculated. the last historical
        year available

        Returns:
        - pd.DataFrame: A DataFrame with country labels and their respective shares of vehicle registrations.
        """
    # Step 1: Filter for the given year
    data_year = data[data[time_dim] == year].copy()
    # Step 2: Calculate the total registrations for the given year
    total_registrations_year = data_year[new_registrations_dim].sum()
    # Step 3: Calculate the share of each country
    data_year[share_dim] = data_year[new_registrations_dim] / total_registrations_year
    # Return the relevant columns
    return data_year[[country_dim, share_dim]]
