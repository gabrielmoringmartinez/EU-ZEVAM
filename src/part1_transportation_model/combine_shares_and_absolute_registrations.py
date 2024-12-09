import pandas as pd
from src.load_data_and_prepare_inputs.dimension_names import country_dim, time_dim, cluster_dim, powertrain_dim, \
    relative_sales_dim, registrations_by_powertrain_dim, new_registrations_dim


def combine_shares_and_absolute_registrations(country_registrations, powertrain_share_registrations, clusters):
    """
        Combines the country-level vehicle registrations with the powertrain-specific share data, and calculates
        the registrations by powertrain for each country.

        Parameters:
        - country_registrations (pd.DataFrame): DataFrame containing the absolute registrations by country and year.
        - powertrain_share_registrations (pd.DataFrame): DataFrame containing the share of registrations for different
        powertrains for each cluster.
        - clusters (pd.DataFrame): DataFrame containing clusters assigned to each country.

        Returns:
        - pd.DataFrame: A DataFrame with the historical and projected registrations by powertrain
        for each country and year.
        """
    # A cluster is assigned to each country with its absolute registrations
    absolute_registrations = pd.merge(country_registrations, clusters[[country_dim, cluster_dim]],
                                      on=country_dim, how='left')
    # The absolute registrations for all EU countries and the powertrain shares estimated for each cluster are combined
    registrations = pd.merge(absolute_registrations, powertrain_share_registrations
    [[time_dim, cluster_dim, powertrain_dim, relative_sales_dim]], on=[time_dim, cluster_dim], how='left')
    # Sales by powertrain, vehicle size, year and country are obtained
    registrations[registrations_by_powertrain_dim] = (registrations[new_registrations_dim]
                                                      * registrations[relative_sales_dim])
    # Sales are saved and defined by scenario
    registrations = registrations.sort_values(by=[country_dim, time_dim, powertrain_dim])
    return registrations
