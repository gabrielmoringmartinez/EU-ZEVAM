import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

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
