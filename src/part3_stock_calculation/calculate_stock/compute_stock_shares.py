# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

import pandas as pd

from src.load_data_and_prepare_inputs.dimension_names import *


def compute_stock_shares(stock_df):
    """
    Computes the share of stock for each powertrain by country and year.

    Parameters:
        stock_df (DataFrame): Input DataFrame containing 'geo country', 'stock year', 'vehicle age', 'powertrain',
        and 'stock' columns.

    Returns:
        DataFrame: DataFrame containing 'geo country', 'stock_year', 'powertrain', 'vehicle age' 'stock', and
                  'share' columns.
    """
    # Step 1: Aggregate stock by country, year, and powertrain
    stock_grouped = stock_df.groupby([country_dim, stock_year_dim, powertrain_dim]).sum().reset_index()

    # Step 2: Calculate the total stock by country and year
    stock_by_country_year = stock_grouped.groupby([country_dim, stock_year_dim]).stock.sum().reset_index()

    # Step 3: Merge total stock back with the grouped data to calculate share per powertrain
    stock_merged = pd.merge(stock_grouped, stock_by_country_year, on=[country_dim, stock_year_dim],
                            suffixes=('', '_total'))
    stock_merged[share_dim] = stock_merged[stock_dim] / stock_merged[f'{stock_dim}_total']

    # Step 4: Select relevant columns for output
    stock_share = stock_merged[[country_dim, stock_year_dim, powertrain_dim, stock_dim, share_dim]]
    return stock_share
