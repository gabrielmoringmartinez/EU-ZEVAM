# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

import matplotlib.pyplot as plt

from src.load_data_and_prepare_inputs.dimension_names import *


def setup_subplot_figure(plot_params):
    """
    Configures and sets up a subplot figure with the specified parameters, including figure size, spacing, and axis
    labels.

    Parameters:
    - plot_params (dict): A dictionary containing the settings for the subplot configuration, including:
        - 'tick_fontsize_dim': Font size for the tick labels.
        - 'space_between_plots_dim': Space between subplots (horizontal and vertical).
        - 'figure_height_dim': Height of the figure.
        - 'figure_width_dim': Width of the figure.
        - 'title_dim': Title for the entire figure.
        - 'title_font_dim': Font size for the title.
        - 'title_vertical_position_dim': Vertical position for the title.
        - 'x_label_dim': Label for the x-axis.
        - 'x_axis_title_vertical_position_dim': Vertical position for the x-axis label.
        - 'y_label_dim': Label for the y-axis.
        - 'y_axis_title_horizontal_position_dim': Horizontal position for the y-axis label.
        - 'axis_title_font_dim': Font size for the axis labels.

    Returns:
    - fig (plt.Figure): The configured Matplotlib figure object that contains the subplots.
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
