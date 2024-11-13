import pandas as pd


def compute_stock_shares(stock_df):
    """
    Computes the share of stock for each powertrain by country and year.

    Parameters:
        stock_df (DataFrame): Input DataFrame containing 'geo country', 'stock_year', 'vehicle age', 'powertrain',
        and 'stock' columns.

    Returns:
        DataFrame: DataFrame containing 'geo country', 'stock_year', 'powertrain', 'vehicle age' 'stock', and
                  'share' columns.
    """
    # Step 1: Aggregate stock by country, year, and powertrain
    stock_grouped = stock_df.groupby(['geo country', 'stock_year', 'powertrain']).sum().reset_index()

    # Step 2: Calculate the total stock by country and year
    stock_by_country_year = stock_grouped.groupby(['geo country', 'stock_year']).stock.sum().reset_index()

    # Step 3: Merge total stock back with the grouped data to calculate share per powertrain
    stock_merged = pd.merge(stock_grouped, stock_by_country_year, on=['geo country', 'stock_year'], suffixes=('', '_total'))
    stock_merged['share'] = stock_merged['stock'] / stock_merged['stock_total']

    # Step 4: Select relevant columns for output
    stock_share = stock_merged[['geo country', 'stock_year', 'powertrain', 'stock', 'share']]
    return stock_share