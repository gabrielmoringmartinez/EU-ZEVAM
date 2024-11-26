from scipy.optimize import differential_evolution
import numpy as np

from src.part2_survival_rates.loss_functions import loss_function_weibull, loss_function_weibull_and_normal
from src.part2_survival_rates.append_optimum_parameters import append_optimum_parameters_weibull, \
    append_optimum_parameters_gaussian
from src.part2_survival_rates.save_optimum_parameters import save_optimum_parameters_weibull, \
    save_optimum_parameters_gaussian


from src.load_data_and_prepare_inputs.dimension_names import *


def run_diff_evol_algorithm_weibull(bounds: list, country_names_number: np.ndarray, survival_rates):
    """
    Runs the differential evolution optimization algorithm to fit Weibull distribution parameters (gamma and beta)

    Parameters:
        bounds (list): Bounds for the Weibull distribution parameters [gamma, beta]. Each element of the list
                       represents the range for a parameter: [(gamma_min, gamma_max), (beta_min, beta_max)].
        country_names_number (np.ndarray): Array of unique country labels
        survival_rates (pd.DataFrame): DataFrame containing survival rates for each country.

    Returns:
        pd.DataFrame: Optimized Weibull parameters for each country, including:
            - gamma: Scale parameter of the Weibull distribution.
            - beta: Shape parameter of the Weibull distribution.
            - r-squared: Measure of fit quality for the model.
            - country labels: The corresponding country identifier for the parameters.
        """
    optimum_gamma_per_country = []
    optimum_beta_per_country = []
    max_rsquared_per_country = []
    for j in country_names_number:
        survival_rates_country = get_value_countries(survival_rates, j)
        result = differential_evolution(loss_function_weibull, bounds, survival_rates_country)
        optimum_gamma_per_country, optimum_beta_per_country, max_rsquared_per_country = append_optimum_parameters_weibull \
            (result, optimum_gamma_per_country, optimum_beta_per_country, max_rsquared_per_country)
    optimum_parameters_diff_evol_algorithm = save_optimum_parameters_weibull(optimum_gamma_per_country,
                                                                             optimum_beta_per_country,
                                                                             max_rsquared_per_country,
                                                                             country_names_number)
    return optimum_parameters_diff_evol_algorithm


def run_diff_evol_algorithm_weibull_gaussian(bounds, country_names_number, survival_rates, optimum_parameters_weibull):
    """
    Runs the differential evolution optimization algorithm to fit Weibull-Gaussian parameters (k, mu, sigma, delta)
    for each country. This builds upon the already optimized Weibull parameters.

    Parameters:
        bounds (list): Bounds for the Gaussian distribution parameters:
                      [(k_min, k_max), (mu_min, mu_max), (sigma_min, sigma_max)].
        country_names_number (np.ndarray): Array of unique country labels
        survival_rates (pd.DataFrame): DataFrame containing survival rates for each country.
        optimum_parameters_weibull (pd.DataFrame): DataFrame containing the optimized Weibull parameters
                                                   (gamma and beta) for each country.

    Returns:
        pd.DataFrame: Combined DataFrame containing:
            - Weibull parameters (gamma, beta).
            - Optimized Weibull-Gaussian parameters (k, mu, sigma, delta).
            - r-squared: Measure of fit quality for the Weibull-Gaussian model.
            - Country labels: Identifier for the parameters.
    """
    max_rsquared_per_country_weibull_gaussian = []
    optimum_k_per_country = []
    optimum_mu_per_country = []
    optimum_sigma_per_country = []
    optimum_delta_per_country = []
    parameters = [optimum_k_per_country, optimum_mu_per_country, optimum_sigma_per_country, optimum_delta_per_country,
                  max_rsquared_per_country_weibull_gaussian]
    for j in country_names_number:
        survival_rates_country = get_value_countries(survival_rates, j)
        optimum_parameters_weibull_country = optimum_parameters_weibull[
            optimum_parameters_weibull[country_dim] == j]
        gamma_country = optimum_parameters_weibull_country[gamma_weibull_dim].to_numpy()
        beta_country = optimum_parameters_weibull_country[beta_weibull_dim].to_numpy()
        args = (gamma_country, beta_country, survival_rates_country)
        result = differential_evolution(loss_function_weibull_and_normal, bounds, args)
        parameters = append_optimum_parameters_gaussian(result, optimum_k_per_country, optimum_mu_per_country,
                                                        optimum_sigma_per_country, optimum_delta_per_country,
                                                        max_rsquared_per_country_weibull_gaussian)
    optimum_parameters_diff_evol_algorithm = save_optimum_parameters_gaussian(optimum_parameters_weibull, parameters)
    return optimum_parameters_diff_evol_algorithm


def get_value_countries(survival_rates, country_name):
    """
    Retrieves survival rates for a specified country.

    This function filters the `survival_rates` DataFrame to extract survival rate values corresponding
    to the specified country.

    Parameters:
        survival_rates (DataFrame): Contains survival rate data.
        country_name (str): The name or label of the country for which to retrieve survival rates.

    Returns:
        Series: Survival rates for the specified country.
    """
    values_country = survival_rates[survival_rates[country_dim] == country_name]
    survival_rates_country = values_country[survival_rate_dim]
    return survival_rates_country
