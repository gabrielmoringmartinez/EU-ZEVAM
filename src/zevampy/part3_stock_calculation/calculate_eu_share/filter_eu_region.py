"""Filter stock-share data for predefined EU regions."""

# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

from zevampy.part3_stock_calculation.calculate_stock.input_data import eu_country_groups
from zevampy.load_data_and_prepare_inputs.dimension_names import country_dim


def filter_eu_region(df, eu_region):
    """
    Filter data for a predefined EU region.

    Parameters:
        df (pandas.DataFrame):
            DataFrame containing stock-share data.

        eu_region (str):
            Identifier of the EU region used for filtering.

    Returns:
        pandas.DataFrame:
            Filtered DataFrame containing only rows belonging
            to the selected EU region.
    """
    return df[df[country_dim].isin(eu_country_groups[eu_region])].copy()
