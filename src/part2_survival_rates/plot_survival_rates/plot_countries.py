from src.part2_survival_rates.plot_survival_rates.plot_csp_countries import plot_csp_countries


def plot_all_countries(pdf_parameters, survival_rates, fitted_csp_values, config, own_calculation=False, activate_weibull=1,
                       activate_weibull_and_normal=1):
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
    country_names = survival_rates['country label'].unique()
    plot_csp_countries(survival_rates, fitted_csp_values, country_names, pdf_parameters, plot_params, file_info,
                       activate_weibull, activate_weibull_and_normal)
    return


def plot_group_of_countries(pdf_parameters, survival_rates, fitted_csp_values, group_of_countries, config, own_calculation=False,
                            activate_weibull=1, activate_weibull_and_normal=1):
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
    country_names = survival_rates['country label'].unique()
    if group_of_countries == 1:
        country_names = country_names[0:plot_params["number_of_countries_group"]]
    else:
        country_names = country_names[plot_params["number_of_countries_group"]:len(country_names)]
    file_info["group_info"] = f'group{group_of_countries}_'
    plot_csp_countries(survival_rates, fitted_csp_values, country_names, pdf_parameters, plot_params, file_info,
                       activate_weibull, activate_weibull_and_normal)
    return