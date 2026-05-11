"""Filter vehicle stock data by vehicle age."""

# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

from zevampy.load_data_and_prepare_inputs.dimension_names import age_dim


def filter_vehicle_age(df, min_age=1, max_age=45):
    """
    Filter rows by vehicle-age range.

    Parameters:
        df (pandas.DataFrame):
            DataFrame containing a vehicle-age column.

        min_age (int, optional):
            Minimum vehicle age to retain, inclusive.
            Defaults to 1.

        max_age (int, optional):
            Maximum vehicle age to retain, inclusive.
            Defaults to 45.

    Returns:
        pandas.DataFrame:
            Filtered DataFrame containing only rows within the
            specified vehicle-age range.
    """
    return df[(df[age_dim] >= min_age) & (df[age_dim] <= max_age)]
