from src.part4_validate_model.update_bev_registration_shares import update_bev_registration_shares_to_real_values
from src.part3_stock_calculation.calculate_stock import calculate_stock
from src.part4_validate_model.use_bev_actual_values import use_bev_actual_values
from src.part4_validate_model.merge_dataframes_and_select_powertrain_and_years import \
    merge_dataframes_and_select_powertrain_and_years
from src.part2_survival_rates.plot_survival_rates.plot_countries import plot_all_countries
from src.part4_validate_model.graph_inputs import config_validation_step1, config_validation_step2


def compare_model_and_actual_stock_results(registrations, stock_shares, actual_bev_registration_shares,
                                           actual_bev_stock_shares, fitted_csp_values, optimal_distribution_dict,
                                           stock_years, historical_csp):
    registrations_with_real_bev_shares = update_bev_registration_shares_to_real_values(registrations,
                                                                                       actual_bev_registration_shares)
    stock_values_with_real_registrations, stock_shares_with_real_registrations = calculate_stock\
        (registrations_with_real_bev_shares, fitted_csp_values, optimal_distribution_dict, stock_years, historical_csp)
    keys_columns_stock = ['geo country', 'stock_year', 'powertrain']
    column_to_update_stock = 'share'
    actual_stock_shares_2014_2023 = use_bev_actual_values(stock_shares_with_real_registrations, actual_bev_stock_shares,
                                                          keys_columns_stock, column_to_update_stock)
    validation_step1_df = merge_dataframes_and_select_powertrain_and_years(stock_shares_with_real_registrations,
                                                                           actual_stock_shares_2014_2023)
    columns_to_plot = {'share': 'share', 'actual share': 'actual share'}
    plot_all_countries(validation_step1_df, config_validation_step1, columns_to_plot, None)
    validation_step2_df = merge_dataframes_and_select_powertrain_and_years(stock_shares, actual_stock_shares_2014_2023)
    plot_all_countries(validation_step2_df, config_validation_step2, columns_to_plot, None)
    return
