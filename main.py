from src.loader.loader import *
from src.part1_transportation_model.input_data import eu_countries_and_norway
from src.part1_transportation_model.calculate_registrations import calculate_registrations
from src.part2_survival_rates.calculate_empirical_survival_rates.calculate_empirical_survival_rates \
    import calculate_empirical_survival_rates
from src.part2_survival_rates.plot_survival_rates.get_csp_plots import get_csp_plots
from src.part2_survival_rates.plot_survival_rates.graph_inputs import config_all, config_group
from src.part3_stock_calculation.compute_csp_values_and_compute_stock import compute_csp_values_and_compute_stock
from src.part3_stock_calculation.input_data import stock_years, historical_csp, save_options_stock
from src.part3_stock_calculation.plot_stock.plot_bev_stock_share import plot_bev_stock_shares
from src.part3_stock_calculation.plot_stock.graph_inputs import config_bev_reference_scenario
from src.part4_validate_model.compare_model_and_actual_stock_results import compare_model_and_actual_stock_results
from src.part5_sensitivity_analysis.country_csp_modified.plot_with_modified_country_csps.graph_inputs import config_sensitivity_1
from src.part5_sensitivity_analysis.country_csp_modified.do_sensitivity_anaylsis_with_modified_country_csps import do_sensitivity_analysis_with_modified_country_csps
from src.part5_sensitivity_analysis.historical_csp_modified.do_sensitivity_analysis_with_historical_country_csps import do_sensitivity_analysis_with_historical_country_csps
from src.part5_sensitivity_analysis.relative_increase_decrease_csp_modified.do_sensitivity_analysis_with_increased_decreased_csps import do_sensitivity_analysis_with_increased_decreased_csps

registrations = calculate_registrations(historical_registrations, eu_countries_and_norway,
                                        registrations_eu_cam_scenario, clusters, registration_shares_by_cluster)
survival_rates_2021 = calculate_empirical_survival_rates(stock_by_age_2021, historical_registrations, stock_year)
stock_values, stock_shares, optimum_parameters_wg, optimal_distribution_dict, fitted_csp_values = \
    compute_csp_values_and_compute_stock(survival_rates_2021, registrations, 2021, stock_years,
                                         historical_csp, save_options_stock)
get_csp_plots(survival_rates_2021, fitted_csp_values, optimum_parameters_wg, config_all, config_group)
plot_bev_stock_shares(stock_shares, config_bev_reference_scenario)
compare_model_and_actual_stock_results(registrations, stock_shares, actual_bev_registration_shares,
                                       actual_bev_stock_shares, fitted_csp_values, optimal_distribution_dict,
                                       stock_years, historical_csp)
do_sensitivity_analysis_with_increased_decreased_csps(registrations, survival_rates_2021, stock_years,
                                                      optimum_parameters_wg, optimal_distribution_dict)
print('FINISH')

do_sensitivity_analysis_with_modified_country_csps(registrations, stock_shares, fitted_csp_values,
                                                   optimal_distribution_dict, config_sensitivity_1)
do_sensitivity_analysis_with_historical_country_csps(registrations, survival_rates_2021, survival_rates_2016,
                                                     stock_years, optimum_parameters_2008, optimal_distribution_dict)


