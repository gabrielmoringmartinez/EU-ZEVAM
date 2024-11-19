from src.part2_survival_rates.plot_survival_rates.plot_csp_countries import plot_csp_countries


def plot_all_countries(merged_df, config, columns_to_plot_dict, distribution_type):
    """
       Plots cumulative survival probability (CSP) data for all countries, optionally with Weibull and/or
       Weibull-Gaussian fits.

       Parameters:
       - pdf_parameters (pd.DataFrame): DataFrame containing the parameters for the Weibull and Gaussian distributions.
        and Weibull Gaussian curves.
       - survival_rates (pd.DataFrame): Data containing survival rates for each country.
       - config (dict): Dictionary containing configuration settings for the plot.
       - own_calculation (bool): If True, indicates user calculation.
       - activate_weibull (int): If 1, includes Weibull fit in the plot; 0 excludes it.
       - activate_weibull_and_normal (int): If 1, includes Weibull-Gaussian fit in the plot; 0 excludes it.

       Returns:
       - None
       """
    plot_params = config["plot_params"]
    file_info = config["file_info"]
    country_names = merged_df['geo country'].unique()
    plot_csp_countries(merged_df, country_names, plot_params, file_info, columns_to_plot_dict, distribution_type)
    return


def plot_group_of_countries(merged_df, country_group, config, columns_to_plot_dict, distribution_type):
    """
      Plots CSP data for a specified group of countries, optionally with Weibull and/or Weibull-Gaussian fits.

      Parameters:
      - pdf_parameters (pd.DataFrame): PDataFrame containing the parameters for the Weibull and Gaussian distributions.
      - survival_rates (pd.DataFrame): Data containing survival rates for each country.
      - group_of_countries (int): Group number of countries to be plotted (e.g., 1 or 2).
      - config (dict): Dictionary containing configuration settings for the plot.
      - own_calculation (bool): If True, indicates user calculation.
      - activate_weibull (int): If 1, includes Weibull fit in the plot; 0 excludes it.
      - activate_weibull_and_normal (int): If 1, includes Weibull-Gaussian fit in the plot; 0 excludes it.

      Returns:
      - None
      """
    plot_params = config["plot_params"]
    file_info = config["file_info"].copy()
    country_names = merged_df['geo country'].unique()
    country_names = get_country_group_names(country_names, country_group, plot_params["number_of_countries_group"])
    file_info["group_info"] = f'group{country_group}_'
    plot_csp_countries(merged_df, country_names, plot_params, file_info, columns_to_plot_dict, distribution_type)
    return


def get_country_group_names(country_names, group_number, number_of_countries_group):
    """
    Selects country names based on the group number.

    Parameters:
    - merged_df (pd.DataFrame): The merged data frame containing country information.
    - group_number (int): The group number (1 or 2).
    - number_of_countries_group (int): Number of countries per group.

    Returns:
    - list: List of country names for the specified group.
    """
    if group_number == 1:
        return country_names[:number_of_countries_group]
    else:
        return country_names[number_of_countries_group:]