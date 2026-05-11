"""Compute vehicle stock values from survival rates and registrations."""

# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

from zevampy.load_data_and_prepare_inputs.dimension_names import *


def compute_stock_values(stock_df):
    """
    Calculate vehicle stock values using fitted survival rates.

    This function computes stock estimates based on Weibull and
    Weibull-Gaussian survival probabilities combined with vehicle
    registrations.

    Parameters:
        stock_df (pandas.DataFrame):
            DataFrame containing survival rates and vehicle
            registrations.

    Returns:
        pandas.DataFrame:
            Updated DataFrame containing calculated stock values
            for Weibull and Weibull-Gaussian distributions.
    """
    stock_df[stock_weibull_dim] = stock_df[survival_rate_weibull_dim] * stock_df[registrations_by_powertrain_dim]
    stock_df[stock_wg_dim] = stock_df[survival_rate_weibull_gaussian_dim] * stock_df[registrations_by_powertrain_dim]
    return stock_df
