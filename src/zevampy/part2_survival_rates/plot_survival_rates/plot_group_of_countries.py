"""Plot CSP curves for grouped survival-rate results."""

# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

from zevampy.part2_survival_rates.plot_survival_rates.get_country_group_names import get_country_group_names
from zevampy.part2_survival_rates.plot_survival_rates.plot_csp_countries import plot_csp_countries

from zevampy.load_data_and_prepare_inputs.dimension_names import *


def plot_group_of_countries(merged_df, group, config, columns_to_plot_dict, distribution_type):
    """
    Plot CSP curves for a selected group of survival-rate results.

    This function selects a subset of groups and generates CSP plots optionally including Weibull and Weibull-Gaussian
    fitted curves.

    Parameters:
        merged_df (pandas.DataFrame):
            DataFrame containing empirical and fitted CSP values.

        group (int):
            Group index to plot.

        config (dict):
            Plot configuration dictionary.

        columns_to_plot_dict (dict):
            Dictionary mapping dataframe column names to legend labels.

        distribution_type (str or None):
            Distribution type to plot. Supported values are "Weibull", "WG", or None.

    Returns:
        None
    """
    plot_params = config[plot_params_dim]
    file_info = config[file_info_dim].copy()
    group_names = merged_df[survival_grouping_label].unique()
    group_names = get_country_group_names(group_names, group, plot_params[number_of_countries_group_dim])
    file_info[group_info_dim] = f'{group_suffix_for_saving_output}{group}_'
    plot_csp_countries(merged_df, group_names, plot_params, file_info, columns_to_plot_dict, distribution_type)
    return
