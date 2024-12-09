# Functions
from src.part4_validate_model.update_bev_registration_shares import update_bev_registration_shares_with_real_values
from src.part3_stock_calculation.calculate_stock.calculate_stock import calculate_stock
from src.part4_validate_model.use_bev_and_phev_actual_values import use_bev_and_phev_actual_values
from src.part4_validate_model.merge_dataframes_and_select_powertrain_and_years import \
    merge_dataframes_and_select_powertrain_and_years
from src.part2_survival_rates.plot_survival_rates.plot_all_countries import plot_all_countries
from src.part4_validate_model.calculate_rmse import calculate_rmse


from src.load_data_and_prepare_inputs.dimension_names import *


def compare_model_and_actual_stock_results(data, calculated_data, inputs):
    """
    Compares model-generated stock results with actual stock data and plots the comparison.

    Parameters:
        - data (dict): Dictionary containing actual BEV registration and stock shares.
            - actual_bev_registration_shares (pd.DataFrame): Actual BEV registration shares by country and year.
            - actual_bev_stock_shares (pd.DataFrame): Actual BEV stock shares by country and year.
        - calculated_data (dict): Dictionary containing model-generated data.
            - registrations (pd.DataFrame): Vehicle registrations by powertrain, including historical and
                                            projected data.
            - stock_shares (pd.DataFrame): Estimated stock data by country, powertrain, and vehicle age.
            - fitted_csp_values (pd.DataFrame): Fitted CSP values by country, vehicle age, and distribution type.
            - optimal_distribution_dict (dict): Optimal distribution type for each country (Weibull or Weibull-Gaussian).
    - inputs (dict): Configuration settings and additional inputs for stock calculations and plotting.
        - simulation_stock_years (list): Range of years for stock simulation.
        - historical_csp (str): Indicator for whether historical CSP data (e.g., from 2021) is used.
        - config_validation_step1 (dict): Plot configuration for validation step 1
        - config_validation_step2 (dict): Plot configuration for validation step 2
        - config_validation_rmse_step1 (dict): Settings for RMSE calculation in step 1.
        - config_validation_rmse_step2 (dict): Settings for RMSE calculation in step 2.
    Returns:
    - None: Outputs plots comparing model and actual data and RMSE calculations saved in CSV for validation purposes.
    """
    registrations = calculated_data[registrations_label]
    stock_shares = calculated_data[stock_shares_label]
    fitted_csp_values = calculated_data[fitted_csp_values_label]
    optimal_distribution_dict = calculated_data[optimal_distribution_dict_label]
    actual_bev_registration_shares = data[actual_bev_registration_shares_label]
    actual_bev_stock_shares = data[actual_bev_stock_shares_label]

    registrations_with_real_bev_shares = update_bev_registration_shares_with_real_values(registrations,
                                                                                         actual_bev_registration_shares)
    stock_values_with_real_registrations, stock_shares_with_real_registrations = calculate_stock\
        (registrations_with_real_bev_shares, fitted_csp_values, optimal_distribution_dict,
         inputs[simulation_stock_years_label], inputs[historical_csp_label])
    keys_columns_stock = [country_dim, stock_year_dim, powertrain_dim]
    column_to_update_stock = share_dim
    # Update stock shares with actual BEV values
    actual_stock_shares_2014_2023 = use_bev_and_phev_actual_values(stock_shares_with_real_registrations,
                                                                   actual_bev_stock_shares, keys_columns_stock,
                                                                   column_to_update_stock)
    # Validation Step 1: Compare updated stock shares
    validation_step1_df = merge_dataframes_and_select_powertrain_and_years(stock_shares_with_real_registrations,
                                                                           actual_stock_shares_2014_2023)
    # Create columns_to_plot, a dictionary to define column and legend values for the plot
    columns_to_plot = {col: col for col in validation_step1_df.columns if col in {share_dim, f'actual {share_dim}'}}
    plot_all_countries(validation_step1_df, inputs[config_validation_step1_label], columns_to_plot, None)
    # Validation Step 2: Compare original stock shares
    validation_step2_df = merge_dataframes_and_select_powertrain_and_years(stock_shares, actual_stock_shares_2014_2023)
    plot_all_countries(validation_step2_df, inputs[config_validation_step2_label], columns_to_plot, None)
    calculate_rmse(validation_step1_df, inputs[config_validation_rmse_step1_label])
    calculate_rmse(validation_step2_df, inputs[config_validation_rmse_step2_label])
    return





