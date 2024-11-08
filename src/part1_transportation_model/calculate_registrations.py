import pandas as pd
time_dim = 'time'

def calculate_registrations(historical_registrations, eu_countries_and_norway, country_labels,
                            registrations_eu_cam_scenario, clusters, registration_shares_by_cluster):
    historical_registrations = preprocess_historical_registrations(historical_registrations, eu_countries_and_norway,
                                                                   country_labels)
    country_registration_shares = calculate_country_shares(historical_registrations, 2021)
    projected_registrations = calculate_projected_registrations(country_registration_shares,
                                                                registrations_eu_cam_scenario)
    absolute_registrations = pd.concat([historical_registrations, projected_registrations], ignore_index=True)
    absolute_registrations.to_csv(f'outputs/1_1_absolute_registrations.csv', sep=';', index=False, decimal=',')
    registrations_by_powertrain = combine_shares_and_absolute_registrations(absolute_registrations,
                                                                            registration_shares_by_cluster, clusters,
                                                                            'scenario_test')
    registrations_by_powertrain.to_csv(f'outputs/1_2_registrations_by_powertrain.csv', sep=';', index=False, decimal=',')
    return registrations_by_powertrain

def preprocess_historical_registrations(historical_registrations, countries_to_keep, country_labels):
    # Step 1: Remove data for the year 2022
    historical_registrations = historical_registrations[historical_registrations[time_dim] != 2022]
    # Step 2: Filter data for the countries in `eu_countries_and_norway`
    historical_registrations = historical_registrations[
        historical_registrations['country label'].isin(countries_to_keep)]
    # Step 3: Merge with country labels
    historical_registrations = pd.merge(country_labels, historical_registrations, how='left')
    # Step 4: Drop the 'country label' column
    historical_registrations = historical_registrations.drop(columns=['country label'])
    # Return the processed DataFrame
    return historical_registrations


def calculate_country_shares(data, year):
    # Step 1: Filter for the given year
    data_year = data[data[time_dim] == year]
    # Step 2: Calculate the total registrations for the given year
    total_registrations_year = data_year['new vehicle registrations'].sum()
    # Step 3: Calculate the share of each country
    data_year['share'] = data_year['new vehicle registrations'] / total_registrations_year
    # Return the relevant columns
    return data_year[['geo country', 'share']]


def calculate_projected_registrations(country_registration_shares, registrations_eu_cam_scenario):
    # Perform cross join between country shares and vehicle registrations by year
    projected_registrations = pd.merge(country_registration_shares,
                                       registrations_eu_cam_scenario[[time_dim, 'new vehicle registrations']],
                                       how='cross')
    # Calculate projected registrations by multiplying share with total registrations
    projected_registrations['new vehicle registrations'] = projected_registrations['new vehicle registrations'] * \
                                                           projected_registrations['share']
    # Drop the 'share' column as it's no longer needed
    projected_registrations = projected_registrations.drop(columns=['share'])
    return projected_registrations


def combine_shares_and_absolute_registrations(country_registrations, powertrain_share_registrations, clusters, scenario):
    # A cluster is assigned to each country with its absolute registrations
    absolute_registrations = pd.merge(country_registrations, clusters[['geo country', 'cluster']], on='geo country', how='left')
    # The absolute registrations for all EU countries and the powertrain shares estimated for each cluster are combined
    registrations = pd.merge(absolute_registrations, powertrain_share_registrations
    [['time', 'cluster', 'powertrain', 'relative sales']], on=['time', 'cluster'], how='left')
    # Sales by powertrain, vehicle size, year and country are obtained
    registrations['registrations by powertrain'] = (registrations['new vehicle registrations'] * registrations['relative sales'])
    # Sales are saved and defined by scenario
    registrations = registrations.sort_values(by=['geo country', 'time', 'powertrain'])
    return registrations
