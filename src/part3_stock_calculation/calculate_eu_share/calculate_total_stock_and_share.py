import numpy as np
from src.load_data_and_prepare_inputs.dimension_names import share_dim, stock_dim, country_dim, powertrain_dim, \
    stock_year_dim


def calculate_total_stock_and_share(df, eu_region):
    """
       Calculates the total stock and share for each powertrain and stock year within the specified EU region.

       Parameters:
       - df (pd.DataFrame): Filtered DataFrame for a specific EU region.
       - eu_region (str): The EU region identifier ('EU-9', 'EU-26+Norway' or 'EU-27+Norway') to filter and calculate.

       Returns:
       - pd.DataFrame: Grouped DataFrame with calculated new share values, labeled by EU region.

       Notes:
       - Sets 'total stock' to 0 if 'share' is 0 to avoid division errors.
       - Drops 'total stock' after calculating the share.
    """
    df['total stock'] = np.where(df[share_dim] != 0, df[stock_dim] / df[share_dim], 0)
    df = df.groupby([powertrain_dim, stock_year_dim])[['total stock', stock_dim]].sum().reset_index()
    df[share_dim] = np.where(df['total stock'] != 0, df[stock_dim] / df['total stock'], 0)
    df[country_dim] = eu_region
    return df.drop(columns=['total stock'])
