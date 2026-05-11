"""Merge survival-rate data with vehicle registrations."""

# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

import pandas as pd

from zevampy.load_data_and_prepare_inputs.dimension_names import country_dim, time_dim


def merge_survival_rates_with_registrations(survival_rates_df, registrations_df, survival_grouping):
    """
    Merge survival-rate data with vehicle registrations.

    Parameters:
        survival_rates_df (pandas.DataFrame):
            DataFrame containing survival-rate data.

        registrations_df (pandas.DataFrame):
            DataFrame containing vehicle registrations.

        survival_grouping (str or list[str]):
            Columns used to define the survival-rate grouping.

    Returns:
        pandas.DataFrame:
            Merged DataFrame containing survival rates and registration data.
    """
    if isinstance(survival_grouping, str):
        survival_grouping = [survival_grouping]

    merge_cols = survival_grouping + [time_dim]

    return pd.merge(survival_rates_df, registrations_df, on=merge_cols, how="inner")
