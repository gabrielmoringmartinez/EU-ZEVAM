from src.part3_stock_calculation.calculate_stock.repeat_csp_data_for_all_years import repeat_csp_data_for_all_years
from src.part3_stock_calculation.calculate_stock.calculate_year_of_first_registration import \
    calculate_year_of_first_registration
from src.part3_stock_calculation.calculate_stock.merge_survival_rates_with_registrations import \
    merge_survival_rates_with_registrations
from src.part3_stock_calculation.calculate_stock.compute_stock_values import compute_stock_values
from src.part3_stock_calculation.calculate_stock.select_optimum_distribution import select_optimum_distribution
from src.part3_stock_calculation.calculate_stock.cleanup_stock_data import cleanup_stock_data
from src.part3_stock_calculation.calculate_stock.compute_stock_shares import compute_stock_shares
from src.part3_stock_calculation.calculate_eu_share.calculate_eu_share import calculate_eu_share
from src.part3_stock_calculation.calculate_stock.save_outputs import save_outputs

from src.load_data_and_prepare_inputs.dimension_names import *


def calculate_stock(registrations, csp_values, optimal_distribution_dict, stock_years, historical_csp,
                    save_options=None):
    """
    Calculates stock data for each country over a specified range of years.

    Parameters:
        - registrations (DataFrame): A DataFrame with vehicle registrations by powertrain, including historical
        - and projected data.
        - csp_values (DataFrame): DataFrame containing fitted CSP values for each country by vehicle age,
        - optimal_distribution_dict (dict): Dictionary specifying the optimal distribution type per country.
        - stock_years (list): List with start and end year, specifying the range of years to expand data.
        - historical_csp (str): identifier for activating the historical CSP data.
        - save_options (dict, optional): Dictionary containing paths for saving the results.

    Returns:
        DataFrame: Final stock data by country, powertrain and vehicle age with
         calculation columns (unnecessary) columns removed.
    """
    columns_to_drop = [survival_rate_weibull_dim, survival_rate_weibull_gaussian_dim, distribution_dim, cluster_dim,
                       stock_weibull_dim, stock_wg_dim, new_registrations_dim, relative_sales_dim,
                       registrations_by_powertrain_dim]

    survival_rates = repeat_csp_data_for_all_years(csp_values, stock_years)
    survival_rates = calculate_year_of_first_registration(survival_rates)
    stock_data = merge_survival_rates_with_registrations(survival_rates, registrations)
    stock_data = compute_stock_values(stock_data)
    stock_data[stock_dim] = stock_data.apply(select_optimum_distribution, axis=1, optimal_distribution_dict=optimal_distribution_dict)
    stock_data = stock_data.rename(columns={time_dim: year_of_first_registration_dim})
    stock_data = cleanup_stock_data(stock_data, columns_to_drop)
    stock_shares = compute_stock_shares(stock_data)
    stock_shares = calculate_eu_share(stock_shares, historical_csp)
    if save_options:
        save_outputs(stock_data, stock_shares, save_options)
    return stock_data, stock_shares














