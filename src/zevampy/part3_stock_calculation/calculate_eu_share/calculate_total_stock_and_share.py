"""Calculate aggregated stock shares for EU regions."""

# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

import numpy as np
from zevampy.load_data_and_prepare_inputs.dimension_names import share_dim, stock_dim, country_dim, powertrain_dim, \
    stock_year_dim


def calculate_total_stock_and_share(df, eu_region):
    """
    Calculate total stock and stock shares for an EU region.

    This function aggregates vehicle stock values across countries for a specified EU region and computes stock shares
    by powertrain and stock year.

    Parameters:
        df (pandas.DataFrame):
            Filtered stock-share DataFrame for the selected EU region.

        eu_region (str):
            Name of the EU region to assign to the aggregated results.

    Returns:
        pandas.DataFrame:
            Aggregated stock-share DataFrame containing stock values and calculated shares by powertrain and stock year.
    """
    df['total stock'] = np.where(df[share_dim] != 0, df[stock_dim] / df[share_dim], 0)
    df = df.groupby([powertrain_dim, stock_year_dim])[['total stock', stock_dim]].sum().reset_index()
    df[share_dim] = np.where(df['total stock'] != 0, df[stock_dim] / df['total stock'], 0)
    df[country_dim] = eu_region
    return df.drop(columns=['total stock'])
