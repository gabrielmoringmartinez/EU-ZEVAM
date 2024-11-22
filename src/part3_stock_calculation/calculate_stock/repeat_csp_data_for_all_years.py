import pandas as pd


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
    years = pd.DataFrame({'stock_year': range(start_year, end_year + 1)})
    result_df = original_df.merge(years, how='cross')
    return result_df
