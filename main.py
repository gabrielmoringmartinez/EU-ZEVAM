from src.loader.loader import *
from src.part1_transportation_model.input_data import eu_countries_and_norway
from src.part1_transportation_model.calculate_registrations import calculate_registrations
from src.part2_survival_rates.calculate_csp_parameters import calculate_csp_parameters
from src.part2_survival_rates.calculate_empirical_survival_rates.calculate_empirical_survival_rates \
    import calculate_empirical_survival_rates
from src.part2_survival_rates.get_fitted_csp_values import get_fitted_csp_values
from src.part2_survival_rates.plot_survival_rates.get_csp_plots import get_csp_plots
from src.part2_survival_rates.plot_survival_rates.graph_inputs import config_all, config_group
from src.part3_stock_calculation.calculate_stock import calculate_stock
from src.part3_stock_calculation.input_data import stock_years, historical_csp, save_options_stock
from src.part4_validate_model.use_bev_actual_values import use_bev_actual_values
from src.part4_validate_model.update_bev_registration_shares import update_bev_registration_shares_to_real_values
from src.part2_survival_rates.plot_survival_rates.plot_countries import plot_all_countries
from src.part4_validate_model.graph_inputs import config_validation_step1, config_validation_step2
from src.part4_validate_model.merge_dataframes_and_select_powertrain_and_years import merge_dataframes_and_select_powertrain_and_years

registrations = calculate_registrations(historical_registrations, eu_countries_and_norway,
                                        registrations_eu_cam_scenario, clusters, registration_shares_by_cluster)
optimum_parameters_wg, optimal_distribution_dict = calculate_csp_parameters(survival_rates_2021, 2021)
survival_rates_2021 = calculate_empirical_survival_rates(stock_by_age_2021, historical_registrations, stock_year)
fitted_csp_values = get_fitted_csp_values(survival_rates_2021, optimum_parameters_wg)
get_csp_plots(survival_rates_2021, fitted_csp_values, optimum_parameters_wg, config_all, config_group)
stock_values, stock_shares = calculate_stock(registrations, fitted_csp_values, optimal_distribution_dict, stock_years,
                                             historical_csp, save_options_stock)

registrations_with_real_bev_shares = update_bev_registration_shares_to_real_values(registrations, actual_bev_registration_shares)
stock_values_with_real_registrations, stock_shares_with_real_registrations = calculate_stock(registrations_with_real_bev_shares, fitted_csp_values,
                                                       optimal_distribution_dict, stock_years, historical_csp)

keys_columns_stock = ['geo country', 'stock_year', 'powertrain']
column_to_update_stock = 'share'
actual_stock_shares_2014_2023 = use_bev_actual_values(stock_shares_with_real_registrations, actual_bev_stock_shares, keys_columns_stock, column_to_update_stock)
validation_step1_df = merge_dataframes_and_select_powertrain_and_years(stock_shares_with_real_registrations, actual_stock_shares_2014_2023)
columns_to_plot = {'share': 'share', 'actual share': 'actual share'}
plot_all_countries(validation_step1_df, config_validation_step1, columns_to_plot, None)
validation_step2_df = merge_dataframes_and_select_powertrain_and_years(stock_shares, actual_stock_shares_2014_2023)
plot_all_countries(validation_step2_df, config_validation_step2, columns_to_plot, None)


