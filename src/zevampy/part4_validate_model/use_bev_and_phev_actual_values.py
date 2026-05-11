"""Replace modelled BEV and PHEV values with observed registration data."""

# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

from zevampy.load_data_and_prepare_inputs.dimension_names import *


def use_bev_and_phev_actual_values(df_model, df_actual, keys=[country_dim, time_dim, powertrain_dim],
                                   column_to_update=relative_sales_dim):
    """
    Update modelled values using observed BEV and PHEV data.

    This function replaces selected modelled values with observed
    values for rows matching the specified keys.

    Parameters:
        df_model (pandas.DataFrame):
            DataFrame containing modelled values.

        df_actual (pandas.DataFrame):
            DataFrame containing observed values used for updates.

        keys (list[str], optional):
            Columns used to match rows between both DataFrames.

        column_to_update (str, optional):
            Column name containing values to update.

    Returns:
        pandas.DataFrame:
            Updated DataFrame containing observed values where
            matches were found.
    """
    df1 = df_model.copy()
    df2 = df_actual.copy()

    df1.set_index(keys, inplace=True)
    df1.sort_index(inplace=True)

    df2.set_index(keys, inplace=True)
    df2.sort_index(inplace=True)

    df1.update(df2[[column_to_update]])
    df1.reset_index(inplace=True)
    return df1