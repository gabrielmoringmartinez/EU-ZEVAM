from src.part2_survival_rates.plot_survival_rates.plot_csp_countries import plot_csp_countries

from src.load_data_and_prepare_inputs.dimension_names import *


def plot_all_countries(merged_df, config, columns_to_plot_dict, distribution_type):
    """
    Plots data for all countries. When printing CSPs, optionally with Weibull and/or Weibull-Gaussian fits.

    Parameters:
       - merged_df (pd.DataFrame): DataFrame containing columns to plot for all countries
       - config (dict): Dictionary containing configuration settings for the plot.
       - columns_to_plot_dict (dict): Name of the columns to be plot and its corresponding name in the legend graph
       - distribution_type (string): It indicates the distribution type which is plot (None, Weibull, WG)

    Returns:
       - None
    """
    plot_params = config[plot_params_dim]
    file_info = config[file_info_dim]
    country_names = merged_df[country_dim].unique()
    plot_csp_countries(merged_df, country_names, plot_params, file_info, columns_to_plot_dict, distribution_type)
    return
