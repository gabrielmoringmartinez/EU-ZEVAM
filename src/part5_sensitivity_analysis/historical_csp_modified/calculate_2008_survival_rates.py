from src.part2_survival_rates.get_fitted_csp_values import get_fitted_csp_values
from src.part3_stock_calculation.calculate_stock.calculate_stock import calculate_stock
from src.part3_stock_calculation.calculate_stock.input_data import stock_years, historical_csp

from src.load_data_and_prepare_inputs.dimension_names import *


def calculate_2008_survival_rates(optimum_parameters_2008, survival_rates_2021, optimal_distribution_dict,
                                  registrations, csp_available_years):
    country_names = optimum_parameters_2008[country_dim].unique()
    filtered_survival_rates_2021 = survival_rates_2021[survival_rates_2021[country_dim].isin(country_names)]
    fitted_csp_values_2008 = get_fitted_csp_values(filtered_survival_rates_2021, optimum_parameters_2008, False, csp_available_years)
    optimal_distribution_dict_2008 = prepare_optimal_distribution_dict(optimal_distribution_dict)
    stock_values_2008, stock_shares_2008 = calculate_stock(registrations, fitted_csp_values_2008,
                                                           optimal_distribution_dict_2008, stock_years, historical_csp)
    stock_shares_2008[country_dim] = stock_shares_2008[country_dim].replace(eu_27_plus_norway_label, eu_9_label)
    return stock_shares_2008


def prepare_optimal_distribution_dict(distribution_dict):
    """
    Prepare the optimal distribution dictionary for 2008 by combining Weibull and WG.
    """
    updated_dict = distribution_dict.copy()
    updated_dict[weibull_label] += updated_dict[weibull_gaussian_label]  # Add all elements from WG to Weibull
    updated_dict[weibull_gaussian_label] = []  # Clear WG list
    return updated_dict