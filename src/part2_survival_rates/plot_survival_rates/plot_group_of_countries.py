from src.part2_survival_rates.plot_survival_rates.get_country_group_names import get_country_group_names
from src.part2_survival_rates.plot_survival_rates.plot_csp_countries import plot_csp_countries

from src.load_data_and_prepare_inputs.dimension_names import *


def plot_group_of_countries(merged_df, country_group, config, columns_to_plot_dict, distribution_type):
    """
    Plots data for a specified group of countries. When printing CSPs,
    optionally with Weibull and/or Weibull-Gaussian fits.

    Parameters:
       - merged_df (pd.DataFrame): DataFrame containing columns to plot for all countries
       - country_group (int): Group number of countries to be plotted (e.g., 1 or 2).
       - config (dict): Dictionary containing configuration settings for the plot.
       - columns_to_plot_dict (dict): Name of the columns to be plotted and its corresponding name in the legend graph
       - distribution_type (string): It indicates the distribution type which is plot (None, Weibull, WG)

    Returns:
      - None
    """
    plot_params = config[plot_params_dim]
    file_info = config[file_info_dim].copy()
    country_names = merged_df[country_dim].unique()
    country_names = get_country_group_names(country_names, country_group, plot_params[number_of_countries_group_dim])
    file_info[group_info_dim] = f'{group_suffix_for_saving_output}{country_group}_'
    plot_csp_countries(merged_df, country_names, plot_params, file_info, columns_to_plot_dict, distribution_type)
    return