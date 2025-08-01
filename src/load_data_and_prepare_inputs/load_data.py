# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

import pandas as pd

from src.load_data_and_prepare_inputs.dimension_names import *


def load_data(input_dir):
    """
    Loads datasets required for modeling European BEV stock shares and performing CSP-based simulations.

    This function reads data from several CSV files stored in the `inputs` folder. The datasets include cluster groups,
    historical and projected vehicle registrations, survival rates, and other related parameters. If additional files
    should be loaded, it can be added a new csv file with data, and define in the dictionary a label for this data.

    Parameters:
        input_dir (str): Path to the directory containing input CSV files.

    Returns:
        tuple:
            - dict: A dictionary containing all loaded datasets, where:
                - Keys are descriptive dataset names (e.g., 'clusters', 'historical_registrations').
                - Values are pandas DataFrames containing the loaded data.
            - int: The maximum year found in the 'registrations_eu_cam_scenario' dataset.
    """
    clusters = pd.read_csv(f'{input_dir}/0_country_clusters.csv', sep=';', decimal=',')
    registration_shares_by_cluster = pd.read_csv(f'{input_dir}/1_1_new_registrations_by_fuel_type_1970_2050_clusters.csv',
                                                 delimiter=';', decimal=',')
    historical_registrations = pd.read_csv(f'{input_dir}/1_2_A_2_new_registrations_data_passenger_cars_eu'
                                           '_countries_1970_2021.csv', delimiter=';', decimal=',')
    registrations_eu_cam_scenario = pd.read_csv(f'{input_dir}/1_3_new_registrations_2022_2050_cam_scenario.csv',
                                                delimiter=';', decimal=',')
    max_year = registrations_eu_cam_scenario['time'].max()

    stock_by_age_2021 = pd.read_csv(f'{input_dir}/2_1_A_1_age_resolved_data_passenger_car_stock_fleet_eu_countries_2021.csv',
                                    delimiter=';', decimal=',')
    stock_year = pd.read_csv(f'{input_dir}/2_2_A_1_stock_year.csv', delimiter=';', decimal=',')
    actual_bev_registration_shares = pd.read_csv(f'{input_dir}/4_1_eafo_ev_new_registration_shares.csv', delimiter=';',
                                                 decimal=',')
    actual_bev_stock_shares = pd.read_csv(f'{input_dir}/4_2_eafo_ev_stock_shares.csv', delimiter=';', decimal=',')
    optimum_parameters_2008 = pd.read_csv(f'{input_dir}/5_1_oguchi_2008_survival_rate_parameters.csv', delimiter=';',
                                          decimal=',')
    survival_rates_2016 = pd.read_csv(f'{input_dir}/5_2_held_2016_survival_rates.csv', delimiter=';', decimal=',')
    # Return all the loaded data as a dictionary or as separate variables if needed
    data = {
        clusters_label: clusters,
        registration_shares_by_cluster_label: registration_shares_by_cluster,
        historical_registrations_label: historical_registrations,
        registrations_eu_cam_scenario_label: registrations_eu_cam_scenario,
        stock_by_age_2021_label: stock_by_age_2021,
        stock_year_label: stock_year,
        actual_bev_registration_shares_label: actual_bev_registration_shares,
        actual_bev_stock_shares_label: actual_bev_stock_shares,
        optimum_parameters_2008_label: optimum_parameters_2008,
        survival_rates_2016_label: survival_rates_2016
    }

    return data, max_year
