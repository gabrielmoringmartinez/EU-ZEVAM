"""Update stock-share datasets for sensitivity-analysis comparisons."""

# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

from zevampy.part5_sensitivity_analysis.merge_stock_shares import merge_stock_shares

from zevampy.load_data_and_prepare_inputs.dimension_names import *


def update_stock_shares(stock_shares_df, new_stock_shares, column_suffix):
    """
    Update stock-share datasets with additional scenario results.

    This function renames stock-share columns for a new scenario and merges them into an existing stock-share dataset.

    Parameters:
        stock_shares_df (pandas.DataFrame):
            Existing stock-share dataset.

        new_stock_shares (pandas.DataFrame):
            Stock-share dataset containing updated scenario values.

        column_suffix (str):
            Suffix appended to the stock-share column name.

    Returns:
        pandas.DataFrame:
            Updated DataFrame containing merged stock-share results.
    """
    new_stock_shares = new_stock_shares[[country_dim, stock_year_dim, powertrain_dim, share_dim]].copy()
    new_stock_shares.rename(columns={share_dim: f'{share_dim}_{column_suffix}'}, inplace=True)
    return merge_stock_shares(stock_shares_df, new_stock_shares)
