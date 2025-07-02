# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

from src.part5_sensitivity_analysis.merge_stock_shares import merge_stock_shares

from src.load_data_and_prepare_inputs.dimension_names import *


def update_stock_shares(stock_shares_df, new_stock_shares, column_suffix):
    """
    Updates the stock shares DataFrame by merging it with a new set of stock shares and renaming the share column.

    Parameters:
        - stock_shares_df (pd.DataFrame): The original DataFrame containing existing stock shares data.
        - new_stock_shares (pd.DataFrame):  A DataFrame containing updated stock shares for different conditions
        It should have the same column structure (same columns: country_dim, stock_year_dim, powertrain_dim, share_dim)
        as `stock_shares_df`.
        - column_suffix (str): A suffix to append to the `share_dim` column in the merged DataFrame
        to distinguish it from the original `share_dim` column.

    Returns:
        - pd.DataFrame: A merged DataFrame where the `new_stock_shares` are added as a new column
        with the name `{share_dim}_{column_suffix}`.
    """
    new_stock_shares = new_stock_shares[[country_dim, stock_year_dim, powertrain_dim, share_dim]].copy()
    new_stock_shares.rename(columns={share_dim: f'{share_dim}_{column_suffix}'}, inplace=True)
    return merge_stock_shares(stock_shares_df, new_stock_shares)
