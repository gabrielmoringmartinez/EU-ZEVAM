from src.part5_sensitivity_analysis.merge_stock_shares import merge_stock_shares

def update_stock_shares(stock_shares_df, new_stock_shares, column_suffix):
    """
    Merges updated stock shares with the main stock shares DataFrame and renames columns.
    """
    new_stock_shares = new_stock_shares[['geo country', 'stock_year', 'powertrain', 'share']].copy()
    new_stock_shares.rename(columns={'share': f'share_{column_suffix}'}, inplace=True)
    return merge_stock_shares(stock_shares_df, new_stock_shares)
