def use_bev_actual_registrations(registrations, actual_bev_registrations, keys = ['geo country', 'time', 'powertrain'],
                                 column_to_update = 'relative sales'):
    """
    Updates the registrations with actual BEV registration values where rows match on the specified keys.

    Parameters:
    registrations_df (pd.DataFrame): The main DataFrame to update.
    actual_bev_registrations (pd.DataFrame): The DataFrame with actual values to update.
    keys (list): List of columns to match between the two DataFrames.
    column_to_update (str): The name of the column in registrations_df to update.

    Returns:
    pd.DataFrame: The updated registrations_df with values from new_sales_shares_df.
    """
    df1 = registrations.copy()
    df2 = actual_bev_registrations.copy()

    df1.set_index(keys, inplace=True)
    df2.set_index(keys, inplace=True)

    df1.update(df2[[column_to_update]])
    df1.reset_index(inplace=True)
    return df1
