from src.loader.loader import *
from src.part1_transportation_model.input_data import eu_countries_and_norway
from src.part1_transportation_model.calculate_registrations import calculate_registrations
from src.part2_survival_rates.calculate_csp_parameters import calculate_csp_parameters
from src.part2_survival_rates.get_fitted_csp_values import get_fitted_csp_values
from src.part2_survival_rates.plot_survival_rates.get_csp_plots import get_csp_plots
from src.part2_survival_rates.plot_survival_rates.graph_inputs import config_all, config_group
from src.part3_stock_calculation.calculate_stock import calculate_stock
from src.part3_stock_calculation.input_data import stock_years

registrations = calculate_registrations(historical_registrations, eu_countries_and_norway,
                                        registrations_eu_cam_scenario, clusters, registration_shares_by_cluster)
optimum_parameters_wg, optimal_distribution_dict = calculate_csp_parameters(survival_rates_2021, 2021)
fitted_csp_values = get_fitted_csp_values(survival_rates_2021, optimum_parameters_wg)
get_csp_plots(survival_rates_2021, fitted_csp_values, optimum_parameters_wg, config_all, config_group)
stock_values, stock_shares = calculate_stock(registrations, fitted_csp_values, optimal_distribution_dict, stock_years)




