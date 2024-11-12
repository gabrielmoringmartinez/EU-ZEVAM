import pandas as pd


from src.part2_survival_rates.plot_survival_rates.setup_subplots import get_number_rows_and_columns, \
    setup_subplot_figure
from src.part2_survival_rates.plot_survival_rates.plot_subplot import plot_survival_rate_country
from src.part2_survival_rates.get_statistical_parameters import get_statistical_parameters, \
    get_statistical_parameters_of_each_country
from src.part2_survival_rates.get_function_values import get_weibull_function, \
    get_weibull_and_normal_function
from src.part2_survival_rates.get_distribution_function_discrete_points import \
    get_distribution_function_discrete_points
from src.part2_survival_rates.plot_survival_rates.save_figure import save_figure


def plot_csp_countries(survival_rates, country_names, pdf_parameters, plot_params, file_info,
                       activate_weibull=1, activate_weibull_and_normal=1):
    """
       Plots cumulative survival probability (CSP) curves for the specified countries with optional Weibull
       and/or Weibull-Gaussian fits.

       Parameters:
       - survival_rates (pd.DataFrame): Data containing survival rates for each country.
       - country_names (list): List of country names to be plotted.
       - pdf_parameters (pd.DataFrame): DataFrame containing the parameters for the Weibull and Gaussian distributions.
       - plot_params (dict): Dictionary containing the settings for the subplot, including font sizes,
                              spacing, figure size, and titles.
       - file_info (dict): Dictionary containing file information, such as file name and save options.
       - activate_weibull (int): If 1, includes Weibull fit in the plot; 0 excludes it.
       - activate_weibull_and_normal (int): If 1, includes Weibull-Gaussian fit in the plot; 0 excludes it.

       Returns:
       - survival_rates_weibull (pd.DataFrame): Updated DataFrame with fitted Weibull distribution data.
       - survival_rates_weibull_and_normal (pd.DataFrame): Updated DataFrame with fitted Weibull-Gaussian
        distribution data.
       """
    country_rows, country_columns = get_number_rows_and_columns(len(country_names))
    fig = setup_subplot_figure(plot_params)

    survival_rates_weibull = pd.DataFrame()
    survival_rates_weibull_and_normal = pd.DataFrame()
    i = 1
    for country_name in country_names:
        ax = fig.add_subplot(country_rows, country_columns, i)
        survival_rates_country = survival_rates[survival_rates["country label"] == country_name]
        plot_survival_rate_country(ax, "Data points", survival_rates_country[plot_params["x_column"]],
                                   survival_rates_country[plot_params["y_column"]], country_name, plot_params, i)

        pdf_df = pdf_parameters
        gamma, beta, k, mu, sigma = get_statistical_parameters(pdf_df)
        gamma_country, beta_country, k_country, mu_country, sigma_country = \
            get_statistical_parameters_of_each_country(gamma, beta, k, mu, sigma, country_name)
        weibull_values = get_weibull_function(gamma_country, beta_country)
        wg_values = get_weibull_and_normal_function(gamma_country, beta_country, k_country, mu_country, sigma_country)
        if activate_weibull:
            plot_survival_rate_country(ax, f"Weibull fit", survival_rates_country[plot_params["x_column"]],
                                       weibull_values, country_name, plot_params, i)
        if activate_weibull_and_normal:
            plot_survival_rate_country(ax, f"WG fit", survival_rates_country[plot_params["x_column"]],
                                       wg_values, country_name, plot_params, i)

        survival_rates_weibull = get_distribution_function_discrete_points(survival_rates_weibull,
                                                                           survival_rates_country, weibull_values)
        survival_rates_weibull_and_normal = get_distribution_function_discrete_points(survival_rates_weibull_and_normal,
                                                                                      survival_rates_country, wg_values)
        i = i + 1
    save_figure(fig, file_info, activate_weibull, activate_weibull_and_normal)
    return survival_rates_weibull, survival_rates_weibull_and_normal
