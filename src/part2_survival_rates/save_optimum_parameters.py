import pandas as pd


def save_optimum_parameters_weibull(optimum_gamma_per_country, optimum_beta_per_country, max_rsquared_per_country,
                                      country_names):
    """
        Compiles the optimized Weibull parameters into a DataFrame.

        Parameters:
            Lists of optimized Weibull parameters per country and country labels.

        Returns:
            DataFrame: DataFrame with optimized Weibull parameters per country.
    """
    optimum_parameters_diff_evol_algorithm = pd.DataFrame()
    optimum_parameters_diff_evol_algorithm['country label'] = country_names
    optimum_parameters_diff_evol_algorithm["gamma (Weibull)"]= optimum_gamma_per_country
    optimum_parameters_diff_evol_algorithm["beta (Weibull)"] = optimum_beta_per_country
    optimum_parameters_diff_evol_algorithm["r squared (Weibull)"] = max_rsquared_per_country
    return optimum_parameters_diff_evol_algorithm


def save_optimum_parameters_gaussian(optimum_parameters_diff_evol_algorithm, parameters):
    """
    Compiles optimized Weibull-Gaussian parameters into a DataFrame.

    Parameters:
        optimum_parameters_diff_evol_algorithm (DataFrame): Contains the optimized Weibull parameters.
        parameters (list): Lists of Gaussian parameters (k, mu, sigma, delta, r-squared) per country.

    Returns:
        DataFrame: Combined Weibull-Gaussian optimized parameters per country.
    """
    optimum_parameters_diff_evol_algorithm["k (Import-Gaussian)"] = parameters[0]
    optimum_parameters_diff_evol_algorithm["mu (Import-Gaussian)"] = parameters[1]
    optimum_parameters_diff_evol_algorithm["sigma (Import-Gaussian)"]= parameters[2]
    optimum_parameters_diff_evol_algorithm["delta (Import-Gaussian)"]= parameters[3]
    optimum_parameters_diff_evol_algorithm["r squared (Weibull and Import-Gaussian)"] = parameters[4]
    return optimum_parameters_diff_evol_algorithm
