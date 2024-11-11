import math
import numpy as np
import matplotlib.pyplot as plt


def get_number_rows_and_columns(number_of_countries):
    country_rows = math.ceil(np.sqrt(number_of_countries))  # Rows and columns are defined
    country_columns = country_rows
    return country_rows, country_columns


def setup_subplot_figure(plot_params):
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