"""Sensitivity analysis with increased and decreased CSP values."""

# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

from zevampy.part5_sensitivity_analysis.relative_increase_decrease_csp_modified.modify_csps import modify_csps
from zevampy.part2_survival_rates.get_fitted_csp_values import get_fitted_csp_values
from zevampy.part3_stock_calculation.calculate_stock.calculate_stock import calculate_stock
from zevampy.part5_sensitivity_analysis.relative_increase_decrease_csp_modified.generate_columns_to_plot import \
    generate_columns_to_plot
from zevampy.part2_survival_rates.plot_survival_rates.plot_all_countries import plot_all_countries
from zevampy.part5_sensitivity_analysis.update_stock_shares import update_stock_shares

from zevampy.load_data_and_prepare_inputs.dimension_names import *


def do_sensitivity_analysis_with_increased_decreased_csps(registrations, survival_rates, optimum_parameters_wg,
                                                          optimal_distribution_dict, config, csp_available_years,
                                                          countries_selected, output_path):
    """
    Perform sensitivity analysis with modified CSP parameters.

    This function adjusts cumulative survival probability (CSP) parameters by relative percentages, recalculates stock
    shares, and generates comparison plots for the selected powertrain.

    Parameters:
        registrations (pandas.DataFrame):
            Vehicle registration data.

        survival_rates (pandas.DataFrame):
            Empirical or fitted survival-rate data.

        optimum_parameters_wg (pandas.DataFrame):
            Optimized CSP parameters.

        optimal_distribution_dict (dict):
            Mapping between countries and selected CSP
            distributions.

        config (dict):
            Configuration settings for plotting and sensitivity analysis.

        csp_available_years (int):
            Number of CSP years used in the calculations.

        countries_selected (list[str]):
            Countries included in the simulation.

        output_path (str):
            Directory where outputs are saved.

    Returns:
        None
    """
    plot_params = config[plot_params_dim]
    columns_to_plot = {}
    stock_shares_df = None
    for percentage in plot_params[percentages_selected_label]:
        adjusted_parameters = modify_csps(optimum_parameters_wg, percentage)
        fitted_csp_values = get_fitted_csp_values(survival_rates, adjusted_parameters, csp_available_years, output_path,
                                                  [country_dim], False)
        stock_shares_are_valid = True
        stock_values, stock_shares = calculate_stock(registrations, fitted_csp_values,
                                                     plot_params[simulation_stock_years_label], 'non-historical_csp',
                                                     countries_selected, stock_shares_are_valid, output_path,
                                                     [country_dim])
        stock_shares_df = update_stock_shares(stock_shares_df, stock_shares, percentage)
    bev_stock_shares = stock_shares_df[stock_shares_df[powertrain_dim] == plot_params[powertrain_to_plot_label]]
    columns_to_plot = generate_columns_to_plot(columns_to_plot, plot_params[percentages_selected_label])
    plot_all_countries(bev_stock_shares, config, columns_to_plot, None)
    return



