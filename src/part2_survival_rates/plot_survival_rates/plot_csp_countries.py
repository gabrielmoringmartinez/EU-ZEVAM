from src.part2_survival_rates.plot_survival_rates.setup_subplots import get_number_rows_and_columns, \
    setup_subplot_figure
from src.part2_survival_rates.plot_survival_rates.plot_subplot import plot_survival_rate_country
from src.part2_survival_rates.plot_survival_rates.save_figure import save_figure


def plot_csp_countries(survival_rates, fitted_csp_values, country_names, pdf_parameters, plot_params, file_info,
                       activate_weibull=1, activate_weibull_and_normal=1):
    """
       Plots cumulative survival probability (CSP) curves for the specified countries with optional Weibull
       and/or Weibull-Gaussian fits.

       Parameters:
       - survival_rates (pd.DataFrame): Data containing survival rates for each country.
       - fitted_csp_values (pd.DataFrame): DataFrame containing fitted CSP values for each country by vehicle age,
       distribution model (Weibull and Weibull Gaussian), and distribution type.
       - country_names (list): List of country names to be plotted.
       - pdf_parameters (pd.DataFrame): DataFrame containing the parameters for the Weibull and Gaussian distributions.
       - plot_params (dict): Dictionary containing the settings for the subplot, including font sizes,
                              spacing, figure size, and titles.
       - file_info (dict): Dictionary containing file information, such as file name and save options.
       - activate_weibull (int): If 1, includes Weibull fit in the plot; 0 excludes it.
       - activate_weibull_and_normal (int): If 1, includes Weibull-Gaussian fit in the plot; 0 excludes it.
       """
    country_rows, country_columns = get_number_rows_and_columns(len(country_names))
    fig = setup_subplot_figure(plot_params)
    i = 1
    for country_name in country_names:
        ax = fig.add_subplot(country_rows, country_columns, i)
        survival_rates_country = survival_rates[survival_rates["country label"] == country_name]
        fitted_csp_values_country = fitted_csp_values[fitted_csp_values["country label"] == country_name]
        weibull_values = list(fitted_csp_values_country['survival rate Weibull'])
        wg_values = list(fitted_csp_values_country['survival rate WG'])
        plot_survival_rate_country(ax, "Data points", survival_rates_country[plot_params["x_column"]],
                                   survival_rates_country[plot_params["y_column"]], country_name, plot_params, i)
        if activate_weibull:
            plot_survival_rate_country(ax, f"Weibull fit", survival_rates_country[plot_params["x_column"]],
                                       weibull_values, country_name, plot_params, i)
        if activate_weibull_and_normal:
            plot_survival_rate_country(ax, f"WG fit", survival_rates_country[plot_params["x_column"]],
                                       wg_values, country_name, plot_params, i)

        i = i + 1
    save_figure(fig, file_info, activate_weibull, activate_weibull_and_normal)
    return
