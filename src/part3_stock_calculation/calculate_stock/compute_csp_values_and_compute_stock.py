from src.part2_survival_rates.calculate_csp_parameters import calculate_csp_parameters
from src.part2_survival_rates.get_fitted_csp_values import get_fitted_csp_values
from src.part3_stock_calculation.calculate_stock.calculate_stock import calculate_stock


def compute_csp_values_and_compute_stock(survival_rates, registrations, stock_years, bounds_distributions,
                                         historical_csp, csp_available_years, save_options=None):
    """
    Computes the Cumulative Survival Probability (CSP) values and stock estimates for a given set of survival rates,
    vehicle registrations, and other relevant parameters.

    This function performs the following:
        - Calculates optimal statistical parameters for the Weibull and Weibull-Gaussian (WG) distributions.
        - Computes the fitted CSP values based on the survival rates.
        - Calculates the stock values and stock shares for each year based on registrations and the fitted CSP values.

    Parameters:
        - survival_rates (pd.DataFrame): DataFrame containing survival rates for each country and year.
        - registrations (DataFrame): A DataFrame with vehicle registrations by powertrain, including historical
          and projected data.
        - stock_years (list): List of years over which to compute stock values.
        - bounds_distributions (dict): Dictionary defining the bounds for the distribution fitting process.
        - historical_csp (str): identifier for activating the historical CSP data.
        - csp_available_years (list): List of years for which CSP values are available or need to be computed.
        - save_options (dict, optional): Dictionary containing options for saving the results, such as file paths or flags. Default is None.

    Returns:
        - tuple: A tuple containing the following values:
            1. stock_values (pd.DataFrame): DataFrame with the computed stock values for each country and year.
            2. stock_shares (pd.DataFrame): DataFrame with the computed stock shares for each country and year.
            3. optimum_parameters_wg (dict): Dictionary containing the optimal parameters for the Weibull-Gaussian
                                            distribution.
            4. optimal_distribution_dict (dict): Dictionary with the distribution parameters used for fitting the CSP values.
            5. fitted_csp_values (pd.DataFrame): DataFrame with the fitted CSP values for each country and year.

    Notes:
        - If `save_options` is provided, the results (such as stock values or fitted CSP values) will be saved according to the specified options.
    """
    optimum_parameters_wg, optimal_distribution_dict = calculate_csp_parameters(survival_rates, bounds_distributions)
    fitted_csp_values = get_fitted_csp_values(survival_rates, optimum_parameters_wg, True, csp_available_years)
    stock_values, stock_shares = calculate_stock(registrations, fitted_csp_values, optimal_distribution_dict,
                                                 stock_years, historical_csp, save_options)
    return stock_values, stock_shares, optimum_parameters_wg, optimal_distribution_dict, fitted_csp_values
