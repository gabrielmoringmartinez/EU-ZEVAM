import pandas as pd


def merge_dataframes_and_select_powertrain_and_years(df1, df2, powertrain=["BEV"], years=(2014, 2023)):
    """
    Filters two DataFrames for specific conditions, merges them on their first three identical columns,
    drops the 'stock' column, and renames 'share' in the second DataFrame to 'actual share'.

    Args:
        df1 (pd.DataFrame): The first DataFrame containing vehicle data.
        df2 (pd.DataFrame): The second DataFrame containing vehicle data.

    Returns:
        pd.DataFrame: A merged DataFrame with the specified adjustments.
    """
    # Apply filtering conditions to both DataFrames
    df1 = df1[df1['powertrain'].isin(powertrain)]
    df1 = df1[df1['stock_year'].between(years[0], years[1])]

    df2 = df2[df2['powertrain'].isin(powertrain)]
    df2 = df2[df2['stock_year'].between(years[0], years[1])]

    # Identify the first three columns for the merge
    merge_columns = df1.columns[:3].tolist()

    # Drop 'stock' column from both DataFrames
    df1 = df1.drop(columns=['stock'], errors='ignore')
    df2 = df2.drop(columns=['stock'], errors='ignore')

    # Rename 'share' column in df2 to 'actual share'
    df2 = df2.rename(columns={'share': 'actual share'})

    # Merge the DataFrames on the first three columns
    merged_df = pd.merge(df1, df2, on=merge_columns, how='inner')

    return merged_df