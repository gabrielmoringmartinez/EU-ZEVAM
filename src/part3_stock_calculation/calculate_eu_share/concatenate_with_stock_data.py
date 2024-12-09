import pandas as pd


def concatenate_with_stock_data(stock_share, eu_data):
    """
        Concatenates the main stock share DataFrame with calculated total EU region data.

        Parameters:
        - stock_share (pd.DataFrame): Original stock share DataFrame.
        - eu_data (pd.DataFrame): DataFrame containing calculated EU region stock data to append.

        Returns:
        - pd.DataFrame: Concatenated DataFrame containing both the original stock data and the EU region data.
        """
    return pd.concat([stock_share, eu_data], ignore_index=True)
