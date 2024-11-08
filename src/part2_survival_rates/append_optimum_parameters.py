import numpy as np


def append_optimum_parameters_weibull(result, optimum_gamma_per_country, optimum_beta_per_country,
                                      max_rsquared_per_country):
    """
        Appends optimal Weibull parameters from the result of the differential evolution algorithm.

        Args:
            result (OptimizeResult): Optimization result containing Weibull parameters [gamma, beta].
            optimum_gamma_per_country (list): List of gamma parameters for each country.
            optimum_beta_per_country (list): List of beta parameters for each country.
            max_rsquared_per_country (list): List of r-squared values for each country.

        Returns:
            tuple: Updated lists of gamma, beta, and r-squared values for each country.
        """
    optimum_gamma_per_country.append(result.x[0])
    optimum_beta_per_country.append(result.x[1])
    max_rsquared_per_country.append(1 - result.fun)
    return optimum_gamma_per_country, optimum_beta_per_country, max_rsquared_per_country


def append_optimum_parameters_gaussian(result, optimum_k_per_country, optimum_mu_per_country, optimum_sigma_per_country,
                                       optimum_delta_per_country, max_rsquared_per_country_weibull_gaussian):
    """
      Appends optimal Gaussian parameters from the result of the differential evolution algorithm.

      Args:
          result (OptimizeResult): Optimization result containing Gaussian parameters [k, mu, sigma].
          Lists to store Gaussian parameters (k, mu, sigma, delta, r-squared) per country.

      Returns:
          tuple: Updated lists of Gaussian parameters (k, mu, sigma, delta, r-squared) per country.
      """
    optimum_k_per_country.append(result.x[0])
    optimum_mu_per_country.append(result.x[1])
    optimum_sigma_per_country.append(result.x[2])
    max_rsquared_per_country_weibull_gaussian.append(1 - result.fun)
    delta = result.x[0] / (np.sqrt(2 * np.pi) * result.x[2])
    optimum_delta_per_country.append(delta)
    return optimum_k_per_country, optimum_mu_per_country, optimum_sigma_per_country, optimum_delta_per_country, \
        max_rsquared_per_country_weibull_gaussian
