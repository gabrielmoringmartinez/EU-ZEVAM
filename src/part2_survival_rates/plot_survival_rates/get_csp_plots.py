# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

import pandas as pd
from src.part2_survival_rates.plot_survival_rates.plot_all_countries import plot_all_countries
from src.part2_survival_rates.plot_survival_rates.plot_group_of_countries import plot_group_of_countries
from src.part2_survival_rates.plot_survival_rates.get_columns_to_plot import get_columns_to_plot

from src.load_data_and_prepare_inputs.dimension_names import *


def get_csp_plots(survival_rates, fitted_csp_values, config_all, config_group):
    """
    Generates and displays Cumulative Survival Probability (CSP) curve plots for all countries,
    as well as specific groups of countries, based on the given survival rates and fitted CSP values.
    The function produces three types of plots for all countries and then generates plots for
    groups of countries.

    Parameters:
    - survival_rates (pd.DataFrame): DataFrame containing survival rate data for each country,
                                      including vehicle age and survival rate values.
    - fitted_csp_values (pd.DataFrame): DataFrame containing the fitted CSP values based on Weibull
                                        and Weibull-Gaussian distributions.
    - config_all (dict): Dictionary containing configuration settings for plotting CSP curves for all countries.
                         This includes plot settings such as figure size, title, labels, etc.
    - config_group (dict): Dictionary containing configuration settings for plotting CSP curves for specific
                           groups of countries. Similar to `config_all` but used for group-specific plotting.

    Returns:
    - None: The function generates and saves the plots.
    """
    merged_df = pd.merge(survival_rates, fitted_csp_values, how='left')
    # Define column mappings for different distributions
    columns_to_plot_all = get_columns_to_plot()
    columns_to_plot_weibull = get_columns_to_plot(weibull_label)
    columns_to_plot_wg = get_columns_to_plot(weibull_gaussian_label)

    # Plot all countries
    plot_all_countries(merged_df, config_all, columns_to_plot_all, None)
    plot_all_countries(merged_df, config_all, columns_to_plot_weibull, weibull_label)
    plot_all_countries(merged_df, config_all, columns_to_plot_wg, weibull_gaussian_label)
    for country_group in [1, 2]:
        plot_group_of_countries(merged_df, country_group, config_group, columns_to_plot_all, None)

