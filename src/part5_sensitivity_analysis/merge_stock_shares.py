from src.load_data_and_prepare_inputs.dimension_names import *

def merge_stock_shares(all_shares_df, stock_shares):
    """
    Merge the provided stock_shares DataFrame into all_shares_df on specified columns.

    Args:
        all_shares_df (pd.DataFrame or None): The main DataFrame to merge into. If None,
                                              this will be initialized with stock_shares.
        stock_shares (pd.DataFrame): The stock shares DataFrame to merge.

    Returns:
        pd.DataFrame: Updated DataFrame containing merged stock shares.
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
