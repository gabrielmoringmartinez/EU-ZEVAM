import pandas as pd


def merge_survival_rates_with_registrations(survival_rates_df, registrations_df, merge_keys):
    """
    Merges survival rates with vehicle registration data based on common keys.

    Parameters:
        survival_rates_df (DataFrame): Survival rates data.
        registrations_df (DataFrame): Vehicle registration data.
        merge_keys (list): List of column names on which to merge the DataFrames, specifically time which represents
                           the year of first registration and country.

    Returns:
        DataFrame: Merged DataFrame containing survival rates and registration data.
    """
    return pd.merge(survival_rates_df, registrations_df, on=merge_keys, how='inner')