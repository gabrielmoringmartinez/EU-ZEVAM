"""Expand CSP datasets across simulation stock years."""

# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

import pandas as pd

from zevampy.load_data_and_prepare_inputs.dimension_names import stock_year_dim


def repeat_csp_data_for_all_years(original_df, stock_years):
    """
    Repeat CSP data for all simulation stock years.

    This function performs a cross join between CSP data and the simulation stock years to create a dataset covering
    all years.

    Parameters:
        original_df (pandas.DataFrame):
            DataFrame containing fitted CSP values.

        stock_years (list[int]):
            Simulation start and end years.

    Returns:
        pandas.DataFrame:
            Expanded DataFrame containing CSP values for all simulation stock years.
    """
    start_year, end_year = stock_years
    years = pd.DataFrame({stock_year_dim: range(start_year, end_year + 1)})
    result_df = original_df.merge(years, how='cross')
    return result_df
