from src.part5_sensitivity_analysis.merge_stock_shares import merge_stock_shares

from src.load_data_and_prepare_inputs.dimension_names import *


def update_stock_shares(stock_shares_df, new_stock_shares, column_suffix):
    """
    Merges updated stock shares with the main stock shares DataFrame and renames columns.
    """
    new_stock_shares = new_stock_shares[[country_dim, stock_year_dim, powertrain_dim, share_dim]].copy()
    new_stock_shares.rename(columns={share_dim: f'{share_dim}_{column_suffix}'}, inplace=True)
    return merge_stock_shares(stock_shares_df, new_stock_shares)
