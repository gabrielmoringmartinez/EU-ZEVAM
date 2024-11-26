import pandas as pd


def load_data():
    """
    Loads datasets required for modeling European BEV stock shares and performing CSP-based simulations.

    This function reads data from several CSV files stored in the `inputs` folder. The datasets include country labels,
    historical and projected vehicle registrations, survival rates, and other related parameters.

    Returns:
        dict: A dictionary containing all loaded datasets, where:
            - Keys are descriptive dataset names (e.g., 'country_labels', 'historical_registrations').
            - Values are pandas DataFrames containing the loaded data.
    """
    country_labels = pd.read_csv('inputs/0_country_labels.csv', delimiter=';', decimal=',')
    clusters = pd.read_csv('inputs/0_country_clusters.csv', sep=';', decimal=',')
    registration_shares_by_cluster = pd.read_csv('inputs/1_1_new_registrations_by_fuel_type_1970_2050_clusters.csv', delimiter=';', decimal=',')
    historical_registrations = pd.read_csv('inputs/1_2_A_2_new_registrations_data_passenger_cars_eu_countries_1970_2021.csv', delimiter=';', decimal=',')
    registrations_eu_cam_scenario = pd.read_csv('inputs/1_3_new_registrations_2022_2050_cam_scenario.csv', delimiter=';', decimal=',')
    stock_by_age_2021 = pd.read_csv('inputs/2_1_A_1_age_resolved_data_passenger_car_stock_fleet_eu_countries_2021.csv', delimiter=';', decimal=',')
    survival_rates_2021 = pd.read_csv('inputs/2_1_A_3_empirical_survival_rates_eu_countries_2021.csv', delimiter=';', decimal=',')
    stock_year = pd.read_csv('inputs/2_2_A_1_stock_year.csv', delimiter=';', decimal=',')
    actual_bev_registration_shares = pd.read_csv('inputs/4_1_eafo_ev_new_registration_shares.csv', delimiter=';', decimal=',')
    actual_bev_stock_shares = pd.read_csv('inputs/4_2_eafo_ev_stock_shares.csv', delimiter=';', decimal=',')
    optimum_parameters_2008 = pd.read_csv('inputs/5_1_oguchi_2008_survival_rate_parameters.csv', delimiter=';', decimal=',')
    survival_rates_2016 = pd.read_csv('inputs/5_2_held_2016_survival_rates.csv', delimiter=';', decimal=',')
    # Return all the loaded data as a dictionary or as separate variables if needed
    data = {
        "country_labels": country_labels,
        "clusters": clusters,
        "registration_shares_by_cluster": registration_shares_by_cluster,
        "historical_registrations": historical_registrations,
        "registrations_eu_cam_scenario": registrations_eu_cam_scenario,
        "stock_by_age_2021": stock_by_age_2021,
        "survival_rates_2021": survival_rates_2021,
        "stock_year": stock_year,
        "actual_bev_registration_shares": actual_bev_registration_shares,
        "actual_bev_stock_shares": actual_bev_stock_shares,
        "optimum_parameters_2008": optimum_parameters_2008,
        "survival_rates_2016": survival_rates_2016
    }

    return data
