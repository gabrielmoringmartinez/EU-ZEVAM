from src.part2_survival_rates.plot_survival_rates.plot_countries import plot_all_countries, plot_group_of_countries


def get_csp_plots(survival_rates, pdf_parameters, config_all, config_group):
    """
    Generates and displays CSP curves plots for all countries and specific groups of countries.

    Parameters:
    - survival_rates (pd.DataFrame): Data containing survival rates for each country.
    - pdf_parameters (pd.DataFrame): DataFrame containing the parameters for the Weibull and Gaussian distributions.
    and Weibull Gaussian curves.
    - config_all (dict): Configuration settings for plotting all countries.
    - config_group (dict): Configuration settings for plotting specific groups of countries.

    Returns:
    - None
    """
    plot_all_countries(pdf_parameters, survival_rates, config_all)
    country_group = 1
    plot_group_of_countries(pdf_parameters, survival_rates, country_group, config_group)
    country_group = 2
    plot_group_of_countries(pdf_parameters, survival_rates, country_group, config_group)
    plot_all_countries(pdf_parameters, survival_rates, config_all, activate_weibull=1, activate_weibull_and_normal=0)
    plot_all_countries(pdf_parameters, survival_rates, config_all, activate_weibull=0, activate_weibull_and_normal=1)
