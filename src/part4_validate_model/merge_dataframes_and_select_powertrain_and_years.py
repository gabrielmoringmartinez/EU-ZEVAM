import pandas as pd

from src.load_data_and_prepare_inputs.dimension_names import *


def merge_dataframes_and_select_powertrain_and_years(df1, df2, powertrain=["BEV"], years=(2014, 2023)):
    """
    Filters two DataFrames by powertrain and year range, merges them on common columns,
    and prepares the resulting DataFrame for analysis.

    Parameters:
       - df1 (pd.DataFrame): The first DataFrame containing model-generated data (e.g., stock shares).
       - df2 (pd.DataFrame): The second DataFrame containing actual observed data (e.g., actual stock shares).
       - powertrain (list, optional): List of powertrain types to filter by. Default is ["BEV"].
       - years (tuple, optional): A tuple specifying the start and end years for filtering. Default is (2014, 2023).

    Returns:
        pd.DataFrame: A merged and filtered DataFrame containing both model-generated and actual data for the specified
         powertrain and year range.
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
    df2 = df2.rename(columns={share_dim: f'actual {share_dim}'})

    # Merge the DataFrames on the first three columns
    merged_df = pd.merge(df1, df2, on=merge_columns, how='inner')

    return merged_df
