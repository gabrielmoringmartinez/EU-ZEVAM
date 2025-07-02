# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

from src.load_data_and_prepare_inputs.dimension_names import *


def get_columns_to_plot(distribution_type=None):
    """
    Returns a dictionary mapping column names to legend labels based on the distribution type.

    Parameters:
    - distribution_type (str or None): Type of distribution ('Weibull', 'WG', or None for all).

    Returns:
    - dict: Mapping of column names to legend labels.
    """
    base_dict = {survival_rate_dim: data_points_plot_label}
    if distribution_type is None:
        base_dict.update({
            survival_rate_weibull_dim: weibull_plot_label,
            survival_rate_weibull_gaussian_dim: weibull_gaussian_plot_label
        })
    elif distribution_type == weibull_label:
        base_dict.update({survival_rate_weibull_dim: weibull_plot_label})
    elif distribution_type == weibull_label:
        base_dict.update({survival_rate_weibull_gaussian_dim: weibull_gaussian_plot_label})
    return base_dict
