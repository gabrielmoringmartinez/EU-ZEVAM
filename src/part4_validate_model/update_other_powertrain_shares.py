# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

from src.load_data_and_prepare_inputs.dimension_names import *


def update_other_powertrain_shares(df):
    """
    Processes the 'registrations_with_real_bev_shares' DataFrame by:
    1. Setting 'relative sales' to 0 for excluded powertrains.
    2. Calculating the fraction of BEV and PHEV sales by 'geo country' and 'time'.
    3. Updating 'relative sales' for gasoline powertrain.
    4. Calculating 'registrations by powertrain' absolute value based on updated 'relative sales'.

    Parameters:
    - df (pd.DataFrame): The registrations DataFrame.
    Powertrains available are: ["BEV", "CNG", "D-HEV", "Diesel", "FCEV", "Gasoline", "G-HEV", "G-PHEV", "LPG"]

    Returns:
    - pd.DataFrame: Processed registrations DataFrame.
    """
    excluded_powertrains = ["CNG", "D-HEV", "Diesel", "FCEV", "G-HEV", "LPG"]
    # Step 1: Set 'relative sales' to 0 for excluded powertrains
    df.loc[df[powertrain_dim].isin(excluded_powertrains), relative_sales_dim] = 0
    # Step 2: Calculate BEV and PHEV relative sales fraction by group
    bev_phev_sales_sum = (
        df.groupby([country_dim, time_dim])
        .apply(lambda x: x.loc[x[powertrain_dim].isin(['BEV', 'G-PHEV']), relative_sales_dim].sum(),
               include_groups=False)
        .rename('bev_phev_sales_sum')
        .reset_index()
    )
    # Merge BEV and PHEV sales fraction back to the main DataFrame
    df = df.merge(bev_phev_sales_sum, on=[country_dim, time_dim], how='left')
    # Step 3: Update 'relative sales' for gasoline powertrain
    df.loc[df[powertrain_dim] == "Gasoline", relative_sales_dim] = 1 - df['bev_phev_sales_sum']
    # Step 4: Calculate 'registrations by powertrain'
    df[registrations_by_powertrain_dim] = df[new_registrations_dim] * df[relative_sales_dim]
    # Drop intermediate column
    df.drop(columns=['bev_phev_sales_sum'], inplace=True)
    return df
