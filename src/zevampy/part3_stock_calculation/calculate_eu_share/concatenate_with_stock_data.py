"""Combine stock-share data with aggregated EU-region results."""

# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

import pandas as pd


def concatenate_with_stock_data(stock_share, eu_data):
    """
    Concatenate stock-share data with aggregated EU-region data.

    Parameters:
        stock_share (pandas.DataFrame):
            Original stock-share DataFrame.

        eu_data (pandas.DataFrame):
            Aggregated EU-region stock-share data.

    Returns:
        pandas.DataFrame:
            Combined DataFrame containing country-level and EU-region stock-share results.
    """
    return pd.concat([stock_share, eu_data], ignore_index=True)
