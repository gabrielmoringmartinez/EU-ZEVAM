"""Create subplot figures for CSP visualizations."""

# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

import matplotlib.pyplot as plt

from zevampy.load_data_and_prepare_inputs.dimension_names import *


def setup_subplot_figure(plot_params):
    """
    Create and configure a subplot figure.

    This function initializes a Matplotlib figure and applies global subplot formatting settings such as spacing,
    figure size, titles, and axis labels.

    Parameters:
        plot_params (dict):
            Dictionary containing figure and subplot formatting settings.

    Returns:
        matplotlib.figure.Figure:
            Configured Matplotlib figure object.
    """
    plt.rc('xtick', labelsize=plot_params[tick_fontsize_dim])
    plt.rc('ytick', labelsize=plot_params[tick_fontsize_dim])
    fig = plt.figure()
    fig.subplots_adjust(hspace=plot_params[space_between_plots_dim], wspace=plot_params[space_between_plots_dim])
    fig.set_figheight(plot_params[figure_height_dim])
    fig.set_figwidth(plot_params[figure_width_dim])
    plt.suptitle(plot_params[title_dim], fontsize=plot_params[title_font_dim], fontweight="bold",
                 y=plot_params[title_vertical_position_dim])
    fig.text(0.5, plot_params[x_axis_title_vertical_position_dim], plot_params[x_label_dim], ha='center',
             fontsize=plot_params[axis_title_font_dim], fontweight="bold")
    fig.text(plot_params[y_axis_title_horizontal_position_dim], 0.5, plot_params[y_label_dim], va='center',
             rotation='vertical', fontsize=plot_params[axis_title_font_dim], fontweight="bold")

    return fig
