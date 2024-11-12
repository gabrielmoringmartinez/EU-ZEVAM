from scipy.optimize import differential_evolution
import numpy as np
from src.part2_survival_rates.loss_functions import loss_function_weibull, loss_function_weibull_and_normal
from src.part2_survival_rates.append_optimum_parameters import append_optimum_parameters_weibull, \
    append_optimum_parameters_gaussian
from src.part2_survival_rates.save_optimum_parameters import save_optimum_parameters_weibull, \
    save_optimum_parameters_gaussian


def run_diff_evol_algorithm_weibull(bounds: list, country_names_number: np.ndarray, survival_rates):
    """
        Runs the differential evolution algorithm to fit Weibull parameters per country.

        Parameters:
            bounds (list): Bounds for the Weibull distribution parameters [gamma, beta].
            country_names_number (np.ndarray): List of unique country labels.
            survival_rates (DataFrame): Survival rates per country.

        Returns:
            DataFrame: Optimized Weibull parameters (gamma, beta, r-squared) per country.
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
       Runs the differential evolution algorithm to fit Weibull-Gaussian parameters per country.

       Parameters:
           bounds (list): Bounds for the Gaussian distribution parameters [k, mu, sigma].
           country_names_number (np.ndarray): List of unique country labels.
           survival_rates (DataFrame): Survival rates per country.
           optimum_parameters_weibull (DataFrame): Optimized Weibull parameters per country.

       Returns:
           DataFrame: Combined Weibull-Gaussian optimized parameters per country.
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
            optimum_parameters_weibull["country label"] == j]
        gamma_country = optimum_parameters_weibull_country["gamma (Weibull)"].to_numpy()
        beta_country = optimum_parameters_weibull_country["beta (Weibull)"].to_numpy()
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

        Parameters:
            survival_rates (DataFrame): Contains survival rate data.
            country_name (str): Name of the country.

        Returns:
            Series: Survival rates for the specified country.
    """
    values_country = survival_rates[survival_rates["country label"] == country_name]
    survival_rates_country = values_country["survival rate"]
    return survival_rates_country
