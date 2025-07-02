# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

import matplotlib.pyplot as plt
from src.part2_survival_rates.plot_survival_rates.customize_axes import customize_axes
from src.load_data_and_prepare_inputs.dimension_names import *


def plot_survival_rate_country(ax, label, x, y, country_name, plot_params):
    """
        Plots survival rate data for a single country on a given subplot axis.

        Parameters:
        - ax (plt.Axes): The axis object where the plot will be drawn.
        - label (str): Label for the plot legend.
        - x (list or np.array): Data for the x-axis (e.g., vehicle age).
        - y (list or np.array): Data for the y-axis (e.g., survival rate).
        - country_name (str): Name of the country being plotted.
        - plot_params (dict): Dictionary containing the settings for the subplot, including font sizes,
                              spacing, figure size, and titles.

        Returns:
        - None
        """
    ax.plot(x, y, '-o', markersize=plot_params[marker_size_dim], linewidth=plot_params[line_width_dim], label=label)
    ax.set_title(country_name, fontsize=plot_params[title_fontsize_dim])
    plt.style.use('seaborn-v0_8-white')
    ax = plt.gca()
    customize_axes(ax, plot_params)



