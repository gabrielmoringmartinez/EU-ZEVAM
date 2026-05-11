"""Clean and simplify calculated stock datasets."""

# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT


def cleanup_stock_data(stock_data, drop_columns):
    """
    Remove intermediate calculation columns from stock data.

    Parameters:
        stock_data (pandas.DataFrame):
            DataFrame containing calculated stock data.

        drop_columns (list[str]):
            Column names to remove.

    Returns:
        pandas.DataFrame:
            Cleaned stock DataFrame with intermediate columns removed.
    """
    return stock_data.drop(columns=drop_columns, errors="ignore")
