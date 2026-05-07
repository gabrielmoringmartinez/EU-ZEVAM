# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

from src.zevampy.load_data_and_prepare_inputs.dimension_names import *


def select_optimum_distribution(row):
    """
    Determines the stock value based on the optimal distribution for each country.

    Parameters:
        row (Series): A row of stock data.
        optimal_distribution_dict (dict): Dictionary specifying which distribution (Weibull or WG)
                                              to use per country.

    Returns:
        float: Stock value based on the optimal distribution, or None if no match is found.
    """
    if row[distribution_dim] == weibull_label:
        return row[stock_weibull_dim]

    if row[distribution_dim] == weibull_gaussian_label:
        return row[stock_wg_dim]

    raise ValueError(
        f"Unknown distribution type: {row[distribution_dim]}"
    )
