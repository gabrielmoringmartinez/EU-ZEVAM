"""Compute vehicle stock shares by country and powertrain."""

# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

import pandas as pd

from zevampy.load_data_and_prepare_inputs.dimension_names import *


def compute_stock_shares(stock_df):
    """
    Calculate vehicle stock shares by country and powertrain.

    This function aggregates vehicle stock values by country, stock year, and powertrain, and computes the corresponding
    stock shares.

    Parameters:
        stock_df (pandas.DataFrame):
            DataFrame containing calculated vehicle stock data.

    Returns:
        pandas.DataFrame:
            DataFrame containing stock values and stock shares by country, stock year, and powertrain.
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
