import pandas as pd

from src.load_data_and_prepare_inputs.dimension_names import *


def merge_dataframes_and_select_powertrain_and_years(df1, df2, powertrain=["BEV"], years=(2014, 2023)):
    """
    Filters two DataFrames by powertrain and year range, merges them on common columns,
    and prepares the resulting DataFrame.

    Args:
        df1 (pd.DataFrame): The first DataFrame containing model-generated data.
        df2 (pd.DataFrame): The second DataFrame containing actual observed data.

    Returns:
        pd.DataFrame: merged and filtered DataFrame that includes both model and actual data
                      for the specified powertrain and year range.
    """
    # Apply filtering conditions to both DataFrames
    df1 = df1[df1[powertrain_dim].isin(powertrain)]
    df1 = df1[df1[stock_year_dim].between(years[0], years[1])]

    df2 = df2[df2[powertrain_dim].isin(powertrain)]
    df2 = df2[df2[stock_year_dim].between(years[0], years[1])]

    # Identify the first three columns for the merge
    merge_columns = df1.columns[:3].tolist()

    # Drop 'stock' column from both DataFrames
    df1 = df1.drop(columns=[stock_dim], errors='ignore')
    df2 = df2.drop(columns=[stock_dim], errors='ignore')

    # Rename 'share' column in df2 to 'actual share'
    df2 = df2.rename(columns={'share': 'actual share'})

    # Merge the DataFrames on the first three columns
    merged_df = pd.merge(df1, df2, on=merge_columns, how='inner')

    return merged_df