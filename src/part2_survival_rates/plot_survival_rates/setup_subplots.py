import math
import numpy as np
import matplotlib.pyplot as plt


def get_number_rows_and_columns(number_of_countries):
    """
        Determines the optimal number of rows and columns for plotting based on the number of countries.

        Parameters:
        - number_of_countries (int): Total number of countries to be plotted.

        Returns:
        - (int, int): Number of rows and columns for the plot grid.
        """
    country_rows = math.ceil(np.sqrt(number_of_countries))  # Rows and columns are defined
    country_columns = country_rows
    return country_rows, country_columns


def setup_subplot_figure(plot_params):
    """
        Configures and sets up a subplot figure with the specified parameters.

        Parameters:
        - plot_params (dict): Dictionary containing the settings for the subplot, including font sizes,
                              spacing, figure size, and titles.

        Returns:
        - fig (plt.Figure): Matplotlib figure object for the subplot.
        """
    plt.rc('xtick', labelsize=plot_params["tick_fontsize"])
    plt.rc('ytick', labelsize=plot_params["tick_fontsize"])
    fig = plt.figure()
    fig.subplots_adjust(hspace=plot_params["space_between_plots"], wspace=plot_params["space_between_plots"])
    fig.set_figheight(plot_params["figure_height"])
    fig.set_figwidth(plot_params["figure_width"])
    plt.suptitle("Empirical cumulative survival probability (CSP) curves of year 2021",
                 fontsize=plot_params["title_font"], fontweight="bold", y=plot_params["title_vertical_position"])
    fig.text(0.5, plot_params["axis_title_vertical_position"], plot_params["x_label"], ha='center',
             fontsize=plot_params["axis_title_font"], fontweight="bold")
    fig.text(plot_params["axis_title_vertical_position"], 0.5, plot_params["y_label"], va='center',
             rotation='vertical', fontsize=plot_params["axis_title_font"], fontweight="bold")
    return fig