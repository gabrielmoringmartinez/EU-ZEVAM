

def update_other_powertrain_shares(df):
    """
    Processes the 'registrations_with_real_bev_shares' DataFrame by:
    1. Setting 'relative sales' to 0 for excluded powertrains.
    2. Calculating the fraction of BEV and PHEV sales by 'geo country' and 'time'.
    3. Updating 'relative sales' for gasoline powertrain.
    4. Calculating 'registrations by powertrain' absolute value based on updated 'relative sales'.

    Parameters:
    - df (pd.DataFrame): The registrations DataFrame.

    Returns:
    - pd.DataFrame: Processed registrations DataFrame.
    """
    excluded_powertrains = ["CNG", "D-HEV", "Diesel", "FCEV", "G-HEV", "LPG"]
    # Step 1: Set 'relative sales' to 0 for excluded powertrains
    df.loc[df['powertrain'].isin(excluded_powertrains), 'relative sales'] = 0
    # Step 2: Calculate BEV and PHEV relative sales fraction by group
    bev_phev_sales_sum = (
        df.groupby(['geo country', 'time'])
        .apply(lambda x: x.loc[x['powertrain'].isin(['BEV', 'G-PHEV']), 'relative sales'].sum())
        .rename('bev_phev_sales_sum')
        .reset_index()
    )
    # Merge BEV and PHEV sales fraction back to the main DataFrame
    df = df.merge(bev_phev_sales_sum, on=['geo country', 'time'], how='left')
    # Step 3: Update 'relative sales' for gasoline powertrain
    df.loc[df['powertrain'] == "Gasoline", 'relative sales'] = 1 - df['bev_phev_sales_sum']
    # Step 4: Calculate 'registrations by powertrain'
    df['registrations by powertrain'] = df['new vehicle registrations'] * df['relative sales']
    # Drop intermediate column
    df.drop(columns=['bev_phev_sales_sum'], inplace=True)
    return df
