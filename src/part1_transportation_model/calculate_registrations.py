import pandas as pd
time_dim = 'time'

def calculate_registrations(historical_registrations, eu_countries_and_norway, country_labels,
                            registrations_eu_cam_scenario, clusters, registration_shares_by_cluster):
    """
        Calculates and saves the absolute and powertrain-specific vehicle registrations for each country.
        The registrations are derived from historical data and projected future data, combined with powertrain shares.

        Parameters:
        - historical_registrations (pd.DataFrame): Historical vehicle registration data for EU countries.
        - eu_countries_and_norway (list): List of country labels (e.g., countries in the EU and Norway).
        - country_labels (pd.DataFrame): DataFrame containing country labels.
        - registrations_eu_cam_scenario (pd.DataFrame): Projected vehicle registrations scenario data
        for the EU countries.
        - clusters (pd.DataFrame): DataFrame containing clusters for each country (Möring et al., 2024).
        - registration_shares_by_cluster (pd.DataFrame): Share of registrations for each cluster and powertrain.

        Returns:
        - pd.DataFrame: A DataFrame with vehicle registrations by powertrain, including historical and projected data.
        Absolute sales and sales share is obtained.
        """
    historical_registrations = preprocess_historical_registrations(historical_registrations, eu_countries_and_norway,
                                                                   country_labels)
    country_registration_shares = calculate_country_shares(historical_registrations, 2021)
    projected_registrations = calculate_projected_registrations(country_registration_shares,
                                                                registrations_eu_cam_scenario)
    absolute_registrations = pd.concat([historical_registrations, projected_registrations], ignore_index=True)
    absolute_registrations.to_csv(f'outputs/1_1_absolute_registrations.csv', sep=';', index=False, decimal=',')
    registrations_by_powertrain = combine_shares_and_absolute_registrations(absolute_registrations,
                                                                            registration_shares_by_cluster, clusters,
                                                                            'scenario_ref')
    registrations_by_powertrain.to_csv(f'outputs/1_2_registrations_by_powertrain.csv', sep=';', index=False, decimal=',')
    return registrations_by_powertrain

def preprocess_historical_registrations(historical_registrations, countries_to_keep, country_labels):
    """
        Preprocesses the historical vehicle registration data by filtering, merging, and cleaning the data.

        Parameters:
        - historical_registrations (pd.DataFrame): DataFrame containing historical registration data.
        - countries_to_keep (list): List of countries to retain in the dataset.
        - country_labels (pd.DataFrame): DataFrame containing country labels.

        Returns:
        - pd.DataFrame: The cleaned and processed historical registration data.
        """
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
    data_year = data[data[time_dim] == year]
    # Step 2: Calculate the total registrations for the given year
    total_registrations_year = data_year['new vehicle registrations'].sum()
    # Step 3: Calculate the share of each country
    data_year['share'] = data_year['new vehicle registrations'] / total_registrations_year
    # Return the relevant columns
    return data_year[['geo country', 'share']]


def calculate_projected_registrations(country_registration_shares, registrations_eu_cam_scenario):
    """
        Calculates the projected vehicle registrations for each country based on the country shares
        and registration scenario.

        Parameters:
        - country_registration_shares (pd.DataFrame): DataFrame containing the share of vehicle registrations
        for each country.
        - registrations_eu_cam_scenario (pd.DataFrame): DataFrame containing projected registration data
        for various years.

        Returns:
        - pd.DataFrame: A DataFrame containing the projected vehicle registrations for each country and year.
        """
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
    """
        Combines the country-level vehicle registrations with the powertrain-specific share data, and calculates
        the registrations by powertrain for each country.

        Parameters:
        - country_registrations (pd.DataFrame): DataFrame containing the absolute registrations by country and year.
        - powertrain_share_registrations (pd.DataFrame): DataFrame containing the share of registrations for different
        powertrains for each cluster.
        - clusters (pd.DataFrame): DataFrame containing clusters assigned to each country.
        - scenario (str): The scenario for which the data is being calculated (e.g., 'scenario_ref').

        Returns:
        - pd.DataFrame: A DataFrame with the historical and projected registrations by powertrain
        for each country and year.
        """
    # A cluster is assigned to each country with its absolute registrations
    absolute_registrations = pd.merge(country_registrations, clusters[['geo country', 'cluster']],
                                      on='geo country', how='left')
    # The absolute registrations for all EU countries and the powertrain shares estimated for each cluster are combined
    registrations = pd.merge(absolute_registrations, powertrain_share_registrations
    [['time', 'cluster', 'powertrain', 'relative sales']], on=['time', 'cluster'], how='left')
    # Sales by powertrain, vehicle size, year and country are obtained
    registrations['registrations by powertrain'] = (registrations['new vehicle registrations']
                                                    * registrations['relative sales'])
    # Sales are saved and defined by scenario
    registrations = registrations.sort_values(by=['geo country', 'time', 'powertrain'])
    return registrations
