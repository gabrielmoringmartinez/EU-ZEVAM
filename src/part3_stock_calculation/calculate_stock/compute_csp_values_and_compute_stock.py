from src.part2_survival_rates.calculate_csp_parameters import calculate_csp_parameters
from src.part2_survival_rates.get_fitted_csp_values import get_fitted_csp_values
from src.part3_stock_calculation.calculate_stock.calculate_stock import calculate_stock


def compute_csp_values_and_compute_stock(survival_rates, registrations, stock_years, bounds_distributions,
                                         historical_csp, csp_available_years, save_options=None):

    optimum_parameters_wg, optimal_distribution_dict = calculate_csp_parameters(survival_rates, bounds_distributions)
    fitted_csp_values = get_fitted_csp_values(survival_rates, optimum_parameters_wg, True, csp_available_years)
    stock_values, stock_shares = calculate_stock(registrations, fitted_csp_values, optimal_distribution_dict,
                                                 stock_years, historical_csp, save_options)
    return stock_values, stock_shares, optimum_parameters_wg, optimal_distribution_dict, fitted_csp_values
