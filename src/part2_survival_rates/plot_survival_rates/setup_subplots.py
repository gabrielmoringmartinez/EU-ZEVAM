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
    return fig