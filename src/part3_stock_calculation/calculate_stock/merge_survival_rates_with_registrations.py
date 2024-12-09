import pandas as pd

from src.load_data_and_prepare_inputs.dimension_names import country_dim, time_dim


def merge_survival_rates_with_registrations(survival_rates_df, registrations_df):
    """
    Merges survival rates with vehicle registration data based on common columns.

    Parameters:
        survival_rates_df (DataFrame): Survival rates data.
        registrations_df (DataFrame): Vehicle registration data.

    Returns:
        DataFrame: Merged DataFrame containing survival rates and new vehicle registration data by powertrain and
        country.
    """
    common_columns = [country_dim, time_dim]
    return pd.merge(survival_rates_df, registrations_df, on=common_columns, how='inner')
