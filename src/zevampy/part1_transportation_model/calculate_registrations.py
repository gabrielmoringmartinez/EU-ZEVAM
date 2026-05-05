# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

import pandas as pd

from src.zevampy.part1_transportation_model.preprocess_historical_registrations import preprocess_historical_registrations
from src.zevampy.part1_transportation_model.calculate_country_shares import calculate_country_shares
from src.zevampy.part1_transportation_model.calculate_projected_registrations import calculate_projected_registrations
from src.zevampy.part1_transportation_model.combine_shares_and_absolute_registrations import \
    combine_shares_and_absolute_registrations


def calculate_registrations(historical_registrations, countries_selected, registrations_projected,
                            clusters, registration_shares_by_cluster, reference_year, simulation_years,
                            start_registrations_year, use_clusters, output_path):
    """
        Calculates and saves the absolute and powertrain-specific vehicle registrations for each country.
        The registrations are derived from historical data and projected future data, combined with powertrain shares.

        Parameters:
        - historical_registrations (pd.DataFrame): Historical vehicle registration data for EU countries.
        - eu_countries_and_norway (list): List of country labels (e.g., countries in the EU and Norway).
        - registrations_projected (pd.DataFrame): Projected vehicle registrations scenario data
        for the EU countries.
        - clusters (pd.DataFrame): DataFrame containing clusters for each country (Möring et al., 2024).
        - registration_shares_by_cluster (pd.DataFrame): Share of registrations for each cluster and powertrain.
        - reference_year (int): The reference year used to calculate country-level EU registration shares
          (e.g., 2021 for historical data).


        Returns:
        - pd.DataFrame: A DataFrame with vehicle registrations by powertrain, including historical and projected data.
        Absolute sales and sales share is obtained.
        """
    end_year = simulation_years[1]
    absolute_registrations = preprocess_historical_registrations(historical_registrations, registrations_projected,
                                                                 reference_year, countries_selected,
                                                                 start_registrations_year, end_year)
    absolute_registrations.to_csv(f'{output_path}/1_1_absolute_registrations.csv', sep=';', index=False, decimal=',')
    registrations_by_powertrain = combine_shares_and_absolute_registrations(absolute_registrations,
                                                                            registration_shares_by_cluster, clusters,
                                                                            use_clusters)
    registrations_by_powertrain.to_csv(f'{output_path}/1_2_registrations_by_powertrain.csv', sep=';', index=False,
                                       decimal=',')
    return registrations_by_powertrain
