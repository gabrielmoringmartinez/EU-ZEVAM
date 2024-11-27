from src.load_data_and_prepare_inputs.dimension_names import *


def compute_stock_values(stock_df):
    """
    Computes stock values based on Weibull and Weibull-Gaussian survival rates.

    Parameters:
        stock_df (DataFrame): Data containing survival rates and registration data.

    Returns:
        DataFrame: Updated DataFrame with 'stock_weibull' and 'stock_wg' columns.
    """
    stock_df[stock_weibull_dim] = stock_df[survival_rate_weibull_dim] * stock_df[registrations_by_powertrain_dim]
    stock_df[stock_wg_dim] = stock_df[survival_rate_weibull_gaussian_dim] * stock_df[registrations_by_powertrain_dim]
    return stock_df
