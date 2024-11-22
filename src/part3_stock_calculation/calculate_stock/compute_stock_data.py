def compute_stock_values(stock_df, registrations_dimension):
    """
    Computes stock values based on Weibull and Weibull-Gaussian survival rates.

    Parameters:
        stock_df (DataFrame): Data containing survival rates and registration data.
        registrations_dimension (str): Column name for the number of registrations by year and powertrain.

    Returns:
        DataFrame: Updated DataFrame with 'stock_weibull' and 'stock_wg' columns.
    """
    stock_df['stock_weibull'] = stock_df['survival rate Weibull'] * stock_df[registrations_dimension]
    stock_df['stock_wg'] = stock_df['survival rate WG'] * stock_df[registrations_dimension]
    return stock_df
