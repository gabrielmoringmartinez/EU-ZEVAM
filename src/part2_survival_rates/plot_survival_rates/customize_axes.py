# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

import matplotlib.ticker as ticker
import matplotlib.pyplot as plt

from src.load_data_and_prepare_inputs.dimension_names import *


def customize_axes(ax, plot_params):
    """
    Customizes the grid, limits, and ticks for a given plot axis.

    Parameters:
    - ax (plt.Axes): Axis object to customize.
    - plot_params (dict): A dictionary containing plot settings such as grid visibility, axis limits, and
                          tick formatting.

    Returns:
    - ax (plt.Axes): Customized axis object.
    """
    ax.grid(plot_params[show_grid_dim])
    if share_dim in plot_params:
        ax.yaxis.set_major_formatter(ticker.PercentFormatter(xmax=1, decimals=plot_params[number_of_decimals_dim]))
    else:
        ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.1f'))
    ax.set_xlim(plot_params[x_lim_dim])
    ax.set_ylim(plot_params[y_lim_dim])
    y_ticks = ax.get_yticks()
    ax.set_yticks([0] + y_ticks[y_ticks != 0])
    x_ticks = ax.get_xticks()
    if x_ticks_dim in plot_params:
        plt.xticks(ticks=plot_params[x_ticks_dim])
    return ax
