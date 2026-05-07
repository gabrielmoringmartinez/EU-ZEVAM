# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

import matplotlib.pyplot as plt


from src.zevampy.part2_survival_rates.plot_survival_rates.setup_subplot_figure import setup_subplot_figure
from src.zevampy.part2_survival_rates.plot_survival_rates.plot_subplot import plot_survival_rate_country
from src.zevampy.part2_survival_rates.plot_survival_rates.save_figure import save_figure
from src.zevampy.part2_survival_rates.plot_survival_rates.fill_area import fill_area_based_on_label
from src.zevampy.part2_survival_rates.plot_survival_rates.add_figure_legend import add_figure_legend
from src.zevampy.part2_survival_rates.plot_survival_rates.get_number_rows_and_columns import get_number_rows_and_columns

from src.zevampy.load_data_and_prepare_inputs.dimension_names import *


def plot_csp_countries(merged_df, groups, plot_params, file_info, columns_to_plot_dict, distribution_type,
                       group_column=country_dim):

    """
    Plots cumulative survival probability (CSP) curves for the specified countries with optional Weibull
    and/or Weibull-Gaussian fits.

    Parameters:
        - merged_df (pd.DataFrame): DataFrame containing columns to plot for all countries
        - country_names (list): List of country names to be plotted.
        - plot_params (dict): Dictionary containing the settings for the subplot, including font sizes,
                              spacing, figure size, and titles.
        - file_info (dict): Dictionary containing file information, such as file name and save options.
        - columns_to_plot_dict (dict): Name of the columns to be plotted and its corresponding name in the legend graph
        - distribution_type (string): It indicates the distribution type which is plot (None, Weibull, WG)
    Returns:
        None: Saves the figure to a file or performs visualization side effects.
    """
    if len(groups) == 0:
        return
    country_rows, country_columns = get_number_rows_and_columns(len(groups), plot_params)
    fig = setup_subplot_figure(plot_params)
    subplot_index = 1
    for group in groups:
        ax = fig.add_subplot(country_rows, country_columns, subplot_index)
        merged_df_group = merged_df[merged_df[group_column] == group]
        for column, legend in columns_to_plot_dict.items():
            plot_survival_rate_country(ax, legend, merged_df_group[plot_params[x_column_dim]],
                                       merged_df_group[column], group, plot_params)
        ax = fill_area_based_on_label(ax, merged_df_group, plot_params[x_column_dim],
                                      list(columns_to_plot_dict.keys()), plot_params[fill_between_dim])
        subplot_index = subplot_index + 1
    add_figure_legend(fig, ax, plot_params)
    save_figure(fig, file_info, distribution_type)
    plt.close(fig)
    return






