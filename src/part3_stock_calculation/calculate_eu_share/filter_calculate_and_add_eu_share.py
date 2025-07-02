# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

from src.part3_stock_calculation.calculate_eu_share.filter_eu_region import filter_eu_region
from src.part3_stock_calculation.calculate_eu_share.calculate_total_stock_and_share import \
    calculate_total_stock_and_share
from src.part3_stock_calculation.calculate_eu_share.concatenate_with_stock_data import concatenate_with_stock_data


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
