import pandas as pd
import numpy as np
from src.part3_stock_calculation.calculate_stock.input_data import eu_country_groups

from src.load_data_and_prepare_inputs.dimension_names import *


def add_eu_stock_share(stock_share, eu_region):
    """
        Adds stock share data for a specified EU region to the main stock share DataFrame.

        Parameters:
        - stock_share (pd.DataFrame): DataFrame containing stock data with columns like 'geo country', 'stock',
                                      and 'share'.
        - share_label (str): Label for the share column to be added to the resulting DataFrame.
        - eu_region (str): The EU region identifier ('EU-9', 'EU-26+Norway' or 'EU-27+Norway') to filter and calculate.

        Returns:
        - pd.DataFrame: The original stock share data concatenated with the calculated EU region data.
        """
    regional_df = filter_eu_region(stock_share, eu_region)
    regional_df = calculate_total_stock_and_share(regional_df, eu_region)
    return concatenate_with_stock_data(stock_share, regional_df)


def filter_eu_region(df, eu_region):
    """
       Filters the input DataFrame to include only rows for the specified EU region.

       Parameters:
       - df (pd.DataFrame): DataFrame containing stock data with columns like 'geo country', 'stock',
                            and 'share'.
       - eu_region (str): The EU region identifier ('EU-9', 'EU-26+Norway' or 'EU-27+Norway') to filter and calculate.

       Returns:
       - pd.DataFrame: DataFrame containing only the rows that match the specified EU region.
       """
    return df[df[country_dim].isin(eu_country_groups[eu_region])].copy()


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


def concatenate_with_stock_data(stock_share, eu_data):
    """
        Concatenates the main stock share DataFrame with calculated total EU region data.

        Parameters:
        - stock_share (pd.DataFrame): Original stock share DataFrame.
        - eu_data (pd.DataFrame): DataFrame containing calculated EU region stock data to append.

        Returns:
        - pd.DataFrame: Concatenated DataFrame containing both the original stock data and the EU region data.
        """
    return pd.concat([stock_share, eu_data], ignore_index=True)
