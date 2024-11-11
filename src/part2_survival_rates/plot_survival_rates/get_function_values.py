import numpy as np
import math


def get_weibull_function(gamma_variable, beta_variable):
    """
        Calculates the fitted Weibull survival probability values for a given set of parameters.

        Parameters:
        - gamma_variable (float): Gamma parameter for the Weibull distribution.
        - beta_variable (float): Beta parameter for the Weibull distribution.

        Returns:
        - csp (list): A list of cumulative survival probability values for ages 1 to 45.
        """
    year_a = np.linspace(1, 45, 45)
    csp = []
    for x in year_a:
        csp_value = np.exp(
            -(x / gamma_variable) ** beta_variable * (math.gamma(1 + 1 / beta_variable)) ** beta_variable)
        csp.append(float(csp_value))
    return csp


def get_weibull_and_normal_function(gamma_variable, beta_variable, k, mu, sigma):
    """
       Calculates the combined Weibull and Gaussian survival probability values for a given set of parameters.

       Parameters:
       - gamma_variable (float): Gamma parameter for the Weibull distribution.
       - beta_variable (float): Beta parameter for the Weibull distribution.
       - k (float): k parameter for the Gaussian distribution.
       - mu (float): mu parameter for the Gaussian distribution.
       - sigma (float): sigma parameter for the Gaussian distribution.

       Returns:
       - csp (list): A list of cumulative survival probability values from the combined fitted
       Weibull and Gaussian distributions.
       """
    year_a = np.linspace(1, 45, 45)
    csp = []
    for x in year_a:
        weibull = np.exp(-(x / gamma_variable) ** beta_variable * (math.gamma(1 + 1 / beta_variable)) ** beta_variable)
        delta = k / (np.sqrt(np.pi * 2) * sigma)
        normal = delta * np.exp(-0.5 * ((x - mu) / sigma) ** 2)
        csp_value = weibull + normal
        csp.append(float(csp_value))
    return csp
