"""Define CSP plot columns and legend labels."""

# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

from zevampy.load_data_and_prepare_inputs.dimension_names import *


def get_columns_to_plot(distribution_type=None):
    """
    Return plot-column mappings for CSP visualizations.

    This function maps CSP-related dataframe columns to the legend labels used in plots. The returned mapping depends
    on the selected distribution type.

    Parameters:
        distribution_type (str or None, optional):
            Distribution type used for filtering plotted curves. Supported values are "Weibull", "WG", or None.
            Defaults to None.

    Returns:
        dict:
            Dictionary mapping dataframe column names to plot legend labels.
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
