# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

from src.load_data_and_prepare_inputs.dimension_names import country_dim, time_dim


def preprocess_historical_registrations(historical_registrations, countries_to_keep, reference_year):
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
    # Step 2: Filter data for the countries in `eu_countries_and_norway`
    historical_registrations = historical_registrations[
        historical_registrations[country_dim].isin(countries_to_keep)]
    return historical_registrations
