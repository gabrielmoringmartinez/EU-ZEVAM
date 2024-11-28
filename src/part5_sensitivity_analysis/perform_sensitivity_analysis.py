# Functions
from src.part5_sensitivity_analysis.country_csp_modified import do_sensitivity_analysis_with_modified_country_csps
from src.part5_sensitivity_analysis.country_registrations_modified import do_sensitivity_analysis_with_modified_country_registrations
from src.part5_sensitivity_analysis.historical_csp_modified import do_sensitivity_analysis_with_historical_country_csps
from src.part5_sensitivity_analysis.relative_increase_decrease_csp_modified import do_sensitivity_analysis_with_increased_decreased_csps
from src.part3_stock_calculation.calculate_stock.input_data import simulation_stock_years

from src.load_data_and_prepare_inputs.dimension_names import *


def perform_sensitivity_analysis(data, calculated_data, inputs):
    # Extract the values from the calculated_data dictionary
    registrations = calculated_data[registrations_label]
    stock_shares = calculated_data[stock_shares_label]
    fitted_csp_values = calculated_data[fitted_csp_values_label]
    optimal_distribution_dict = calculated_data[optimal_distribution_dict_label]
    optimum_parameters_wg = calculated_data[optimum_parameters_wg_label]
    survival_rates_2021 = calculated_data[survival_rates_2021_label]
    do_sensitivity_analysis_with_modified_country_csps(registrations, stock_shares, fitted_csp_values,
                                                       optimal_distribution_dict, inputs[config_sensitivity_1_label])
    do_sensitivity_analysis_with_historical_country_csps(registrations, survival_rates_2021,
                                                         data[survival_rates_2016_label],
                                                         simulation_stock_years,
                                                         data[optimum_parameters_2008_label],
                                                         optimal_distribution_dict,
                                                         inputs[config_sensitivity_2_label],
                                                         inputs[distribution_bounds_label],
                                                         inputs[csp_available_years_label])
    do_sensitivity_analysis_with_increased_decreased_csps(registrations, survival_rates_2021, simulation_stock_years,
                                                          optimum_parameters_wg, optimal_distribution_dict,
                                                          inputs[config_sensitivity_3_label],
                                                          inputs[csp_available_years_label])
    do_sensitivity_analysis_with_modified_country_registrations(registrations, stock_shares, fitted_csp_values,
                                                                optimal_distribution_dict,
                                                                inputs[config_sensitivity_4_label])
