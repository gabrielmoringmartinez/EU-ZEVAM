# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

def cleanup_stock_data(stock_data, drop_columns):
    """
    Removes calculation columns from the stock data.

    Parameters:
        stock_data (DataFrame): Stock data containing all calculations.
        drop_columns (list): List of column names to be removed from the DataFrame.

    Returns:
        DataFrame: Cleaned DataFrame with specified columns dropped.
    """
    return stock_data.drop(columns=drop_columns)
