"""Add aggregated EU-region stock shares to stock datasets."""

# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

from zevampy.part3_stock_calculation.calculate_eu_share.filter_eu_region import filter_eu_region
from zevampy.part3_stock_calculation.calculate_eu_share.calculate_total_stock_and_share import \
    calculate_total_stock_and_share
from zevampy.part3_stock_calculation.calculate_eu_share.concatenate_with_stock_data import concatenate_with_stock_data


def add_eu_stock_share(stock_share, eu_region):
    """
    Add aggregated stock shares for an EU region.

    This function filters stock-share data for a selected EU region, calculates aggregated stock shares, and appends
    the regional results to the original dataset.

    Parameters:
        stock_share (pandas.DataFrame):
            DataFrame containing vehicle stock-share data.

        eu_region (str):
            Identifier of the EU region to aggregate.

    Returns:
        pandas.DataFrame:
            DataFrame containing original and aggregated EU-region stock-share results.
    """
    regional_df = filter_eu_region(stock_share, eu_region)
    regional_df = calculate_total_stock_and_share(regional_df, eu_region)
    return concatenate_with_stock_data(stock_share, regional_df)
