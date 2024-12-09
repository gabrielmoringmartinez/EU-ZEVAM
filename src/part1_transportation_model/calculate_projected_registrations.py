import pandas as pd
from src.load_data_and_prepare_inputs.dimension_names import time_dim, new_registrations_dim, share_dim


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
                                       registrations_eu_cam_scenario[[time_dim, new_registrations_dim]], how='cross')

    # Calculate projected registrations by multiplying share with total registrations
    projected_registrations[new_registrations_dim] = projected_registrations[new_registrations_dim] * \
                                                     projected_registrations[share_dim]

    # Drop the share_dim column as it is no longer needed
    projected_registrations = projected_registrations.drop(columns=[share_dim])
    return projected_registrations
