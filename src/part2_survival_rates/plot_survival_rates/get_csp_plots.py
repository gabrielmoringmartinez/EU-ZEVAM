import pandas as pd
from src.part2_survival_rates.plot_survival_rates.plot_countries import plot_all_countries, plot_group_of_countries


def get_csp_plots(survival_rates, fitted_csp_values, pdf_parameters, config_all, config_group):
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
    merged_df = pd.merge(survival_rates, fitted_csp_values, how='left')
    # Define column mappings for different distributions
    columns_to_plot_all = get_columns_to_plot()
    columns_to_plot_weibull = get_columns_to_plot('Weibull')
    columns_to_plot_wg = get_columns_to_plot('WG')

    # Plot all countries
    plot_all_countries(merged_df, config_all, columns_to_plot_all, None)
    plot_all_countries(merged_df, config_all, columns_to_plot_weibull, 'Weibull')
    plot_all_countries(merged_df, config_all, columns_to_plot_wg, 'WG')
    for country_group in [1, 2]:
        plot_group_of_countries(merged_df, country_group, config_group, columns_to_plot_all, None)


def get_columns_to_plot(distribution_type=None):
    """
    Returns a dictionary mapping column names to legend labels based on the distribution type.

    Parameters:
    - distribution_type (str or None): Type of distribution ('Weibull', 'WG', or None for all).

    Returns:
    - dict: Mapping of column names to legend labels.
    """
    base_dict = {'survival rate': 'data points'}
    if distribution_type is None:
        base_dict.update({
            'survival rate Weibull': 'Weibull fit',
            'survival rate WG': 'WG fit'
        })
    elif distribution_type == 'Weibull':
        base_dict.update({'survival rate Weibull': 'Weibull fit'})
    elif distribution_type == 'WG':
        base_dict.update({'survival rate WG': 'WG fit'})
    return base_dict
