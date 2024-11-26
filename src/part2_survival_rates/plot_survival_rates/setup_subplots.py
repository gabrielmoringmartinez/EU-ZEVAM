import math
import numpy as np
import matplotlib.pyplot as plt

from src.load_data_and_prepare_inputs.dimension_names import *


def get_number_rows_and_columns(number_of_countries, plot_params):
    """
    Determines the optimal number of rows and columns for the plot grid based on the number of countries to be plotted.

    Parameters:
    - number_of_countries (int): The total number of countries to be plotted.
    - plot_params (dict): A dictionary containing plot configuration parameters.
                          Expected keys: 'num_rows_dim' and 'num_columns_dim' which may specify
                          the number of rows and columns respectively.

    Returns:
    - tuple: A tuple containing two integers, (num_rows, num_columns), which specify the number of rows
             and columns for the plot grid. If no specific values are provided in `plot_params`,
             the function calculates a square grid based on the square root of the number of countries.
    """
    default_num_rows = None
    default_num_columns = None
    country_rows = plot_params.get(num_rows_dim, default_num_rows)  # Replace default_num_rows with a sensible default, e.g., 1
    country_columns = plot_params.get(num_columns_dim, default_num_columns)  # Replace default_num_columns with a sensible default, e.g., 1
    if country_rows is None and country_columns is None:
        country_rows = math.ceil(np.sqrt(number_of_countries))  # Rows and columns are defined
        country_columns = country_rows
    return country_rows, country_columns


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
