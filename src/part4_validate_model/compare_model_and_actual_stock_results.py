from src.part4_validate_model.update_bev_registration_shares import update_bev_registration_shares_with_real_values
from src.part3_stock_calculation.calculate_stock.calculate_stock import calculate_stock
from src.part4_validate_model.use_bev_actual_values import use_bev_actual_values
from src.part4_validate_model.merge_dataframes_and_select_powertrain_and_years import \
    merge_dataframes_and_select_powertrain_and_years
from src.part2_survival_rates.plot_survival_rates.plot_countries import plot_all_countries
from src.part4_validate_model.graph_inputs import config_validation_step1, config_validation_step2
from src.part4_validate_model.calculate_rmse import calculate_rmse
from src.part4_validate_model.rmse_inputs import config_rmse_validation_step1, config_rmse_validation_step2
from src.part3_stock_calculation.calculate_stock.input_data import stock_years, historical_csp

def compare_model_and_actual_stock_results(data, calculated_data):
    """
        Compares model results with actual stock results and plots the comparison.

        Args:
            registrations (DataFrame): A DataFrame with vehicle registrations by powertrain, including historical
            and projected data.
            stock_shares (DataFrame): Estimated stock data by country, powertrain and vehicle age
            actual_bev_registration_shares (DataFrame): Actual BEV registration shares.
            actual_bev_stock_shares (DataFrame): Actual BEV stock shares.
            fitted_csp_values (DataFrame): DataFrame containing fitted CSP values for each country by vehicle age,
            distribution model (Weibull and Weibull Gaussian), and distribution type.
            optimal_distribution_dict (Dict): Dictionary specifying the optimal distribution type per country.
            stock_years (list): List with start and end year, specifying the range of years to expand data.
            historical_csp (string): It indicates if 2021 csp data is used or a certain older year
    """
    registrations = calculated_data["registrations"]
    stock_shares = calculated_data["stock_shares"]
    fitted_csp_values = calculated_data["fitted_csp_values"]
    optimal_distribution_dict = calculated_data["optimal_distribution_dict"]
    actual_bev_registration_shares = data["actual_bev_registration_shares"]
    actual_bev_stock_shares = data["actual_bev_stock_shares"]

    registrations_with_real_bev_shares = update_bev_registration_shares_with_real_values(registrations,
                                                                                       actual_bev_registration_shares)
    stock_values_with_real_registrations, stock_shares_with_real_registrations = calculate_stock\
        (registrations_with_real_bev_shares, fitted_csp_values, optimal_distribution_dict, stock_years, historical_csp)
    keys_columns_stock = ['geo country', 'stock_year', 'powertrain']
    column_to_update_stock = 'share'
    # Update stock shares with actual BEV values
    actual_stock_shares_2014_2023 = use_bev_actual_values(stock_shares_with_real_registrations, actual_bev_stock_shares,
                                                          keys_columns_stock, column_to_update_stock)
    # Validation Step 1: Compare updated stock shares
    validation_step1_df = merge_dataframes_and_select_powertrain_and_years(stock_shares_with_real_registrations,
                                                                           actual_stock_shares_2014_2023)
    columns_to_plot = {'share': 'share', 'actual share': 'actual share'}
    plot_all_countries(validation_step1_df, config_validation_step1, columns_to_plot, None)
    # Validation Step 2: Compare original stock shares
    validation_step2_df = merge_dataframes_and_select_powertrain_and_years(stock_shares, actual_stock_shares_2014_2023)
    plot_all_countries(validation_step2_df, config_validation_step2, columns_to_plot, None)
    calculate_rmse(validation_step1_df, config_rmse_validation_step1)
    calculate_rmse(validation_step2_df, config_rmse_validation_step2)
    return





