# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

import pandas as pd

from src.load_data_and_prepare_inputs.dimension_names import stock_year_dim


def repeat_csp_data_for_all_years(original_df, stock_years):
    """
        Expands CSP data for each year in a given range using a cross join.

        Parameters:
            original_df (DataFrame): Original CSP values DataFrame, indexed by 'geo country'.
            stock_years (list): List with start and end year for stock data expansion.

        Returns:
            DataFrame: Expanded DataFrame with 'stock_year' column for each year in the specified range.
        """
    start_year, end_year = stock_years
    years = pd.DataFrame({stock_year_dim: range(start_year, end_year + 1)})
    result_df = original_df.merge(years, how='cross')
    return result_df
