"""Run CSP and registration sensitivity analyses for stock-share modelling."""

# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

# Functions
from zevampy.part5_sensitivity_analysis.country_csp_modified import do_sensitivity_analysis_with_modified_country_csps
from zevampy.part5_sensitivity_analysis.country_registrations_modified import \
    do_sensitivity_analysis_with_modified_country_registrations
from zevampy.part5_sensitivity_analysis.historical_csp_modified import do_sensitivity_analysis_with_historical_country_csps
from zevampy.part5_sensitivity_analysis.relative_increase_decrease_csp_modified import \
    do_sensitivity_analysis_with_increased_decreased_csps

from zevampy.load_data_and_prepare_inputs.dimension_names import *


def perform_sensitivity_analysis(data, calculated_data, inputs):
    """
    Perform sensitivity analyses for CSP and registration scenarios.

    This function evaluates the impact of modified cumulative survival probability (CSP) curves and registration
    scenarios on vehicle stock-share projections.

    The following sensitivity analyses are performed:
    - modified country-specific CSP curves,
    - historical CSP curves,
    - increased and decreased CSP values, and
    - modified country registrations.

    Parameters:
        data (dict):
            Dictionary containing historical survival-rate and CSP-related datasets.

        calculated_data (dict):
            Dictionary containing calculated registrations, stock shares, CSP values, and optimized parameters.

        inputs (dict):
            Dictionary containing configuration settings and simulation parameters for sensitivity analyses.

    Returns:
        None
    """
    # Extract the values from the calculated_data dictionary
    registrations = calculated_data[registrations_label]
    stock_shares = calculated_data[stock_shares_label]
    fitted_csp_values = calculated_data[fitted_csp_values_label]
    optimal_distribution_dict = calculated_data[optimal_distribution_dict_label]
    optimum_parameters_wg = calculated_data[optimum_parameters_wg_label]
    survival_rates_2021 = calculated_data[empirical_survival_rates_label]
    do_sensitivity_analysis_with_modified_country_csps(registrations, stock_shares, fitted_csp_values,
                                                       optimal_distribution_dict, inputs[config_sensitivity_1_label],
                                                       inputs[countries_selected_label], inputs[output_path_label])
    if inputs[historical_csp_label]:
        do_sensitivity_analysis_with_historical_country_csps(registrations, survival_rates_2021,
                                                             data[survival_rates_2016_label],
                                                             data[optimum_parameters_2008_label],
                                                             optimal_distribution_dict,
                                                             inputs[config_sensitivity_2_label],
                                                             inputs[distribution_bounds_label],
                                                             inputs[csp_available_years_label],
                                                             inputs[simulation_stock_years_label],
                                                             inputs[countries_selected_label],
                                                             inputs[output_path_label])
    do_sensitivity_analysis_with_increased_decreased_csps(registrations, survival_rates_2021, optimum_parameters_wg,
                                                          optimal_distribution_dict, inputs[config_sensitivity_3_label],
                                                          inputs[csp_available_years_label],
                                                          inputs[countries_selected_label], inputs[output_path_label])
    do_sensitivity_analysis_with_modified_country_registrations(registrations, stock_shares, fitted_csp_values,
                                                                optimal_distribution_dict,
                                                                inputs[config_sensitivity_4_label],
                                                                inputs[countries_selected_label],
                                                                inputs[output_path_label])
