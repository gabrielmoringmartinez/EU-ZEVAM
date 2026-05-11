"""Merge stock-share datasets for comparative scenario analysis."""

# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

from zevampy.load_data_and_prepare_inputs.dimension_names import *


def merge_stock_shares(all_shares_df, stock_shares):
    """
    Merge stock-share datasets into a combined DataFrame.

    This function combines stock-share results from multiple scenarios using a shared set of merge columns.

    Parameters:
        all_shares_df (pandas.DataFrame or None):
            Existing combined stock-share DataFrame.

        stock_shares (pandas.DataFrame):
            Stock-share DataFrame to merge.

    Returns:
        pandas.DataFrame:
            Combined DataFrame containing merged stock-share results.
    """
    # Ensure stock_shares only contains relevant columns
    if stock_dim in stock_shares.columns:
        stock_shares = stock_shares.drop(columns=[stock_dim])
    # If all_shares_df is None, initialize it with stock_shares
    if all_shares_df is None:
        all_shares_df = stock_shares
    else:
        all_shares_df = all_shares_df.merge(stock_shares, on=[country_dim, stock_year_dim, powertrain_dim], how='outer')

    return all_shares_df
