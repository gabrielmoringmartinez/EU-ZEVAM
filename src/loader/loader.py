import pandas as pd

country_labels = pd.read_csv('inputs/0_country_labels.csv', delimiter=';', decimal=',')
clusters = pd.read_csv('inputs/0_country_clusters.csv', sep=';', decimal=',')
registration_shares_by_cluster = pd.read_csv('inputs/1_1_new_registrations_by_fuel_type_1970_2050_clusters.csv', delimiter=';', decimal=',')
historical_registrations = pd.read_csv('inputs/1_2_A_2_new_registrations_data_passenger_cars_eu_countries_1970_2021.csv', delimiter=';', decimal=',')
registrations_eu_cam_scenario = pd.read_csv('inputs/1_3_new_registrations_2022_2050_cam_scenario.csv', delimiter=';', decimal=',')
