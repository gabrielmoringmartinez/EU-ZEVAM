import numpy as np
import math
import pandas as pd


def get_weibull_function(gamma_variable, beta_variable, csp_available_years):
    """
        Calculates the fitted Weibull survival probability values for a given set of parameters.

        Parameters:
        - gamma_variable (float): Gamma parameter for the Weibull distribution.
        - beta_variable (float): Beta parameter for the Weibull distribution.
        - csp_available_years (int): Number of years (vehicle ages) for which CSP values are calculated.

        Returns:
        - csp (list): A list of cumulative survival probability values for ages 1 to 45.
        """
    # Extract scalar values if they are single-element Series
    if isinstance(gamma_variable, pd.Series):
        gamma_variable = gamma_variable.iloc[0]
    if isinstance(beta_variable, pd.Series):
        beta_variable = beta_variable.iloc[0]
    year_a = np.linspace(1, csp_available_years, csp_available_years)
    csp = []
    for x in year_a:
        csp_value = float(np.exp(-(x / gamma_variable) ** beta_variable * (math.gamma(1 + 1 / beta_variable)) ** beta_variable))
        csp.append(csp_value)
    return csp


def get_weibull_and_normal_function(gamma_variable, beta_variable, k, mu, sigma, csp_available_years):
    """
       Calculates the combined Weibull and Gaussian survival probability values for a given set of parameters.

       Parameters:
       - gamma_variable (float): Gamma parameter for the Weibull distribution.
       - beta_variable (float): Beta parameter for the Weibull distribution.
       - k (float): k parameter for the Gaussian distribution.
       - mu (float): mu parameter for the Gaussian distribution.
       - sigma (float): sigma parameter for the Gaussian distribution.
       - csp_available_years (int): Number of years (vehicle ages) for which CSP values are calculated.

       Returns:
       - csp (list): A list of cumulative survival probability values from the combined fitted
       Weibull and Gaussian distributions.
       """
    if isinstance(gamma_variable, pd.Series):
        gamma_variable = gamma_variable.iloc[0]
    if isinstance(beta_variable, pd.Series):
        beta_variable = beta_variable.iloc[0]
    if isinstance(k, pd.Series):
        k = k.iloc[0]
    if isinstance(mu, pd.Series):
        mu = mu.iloc[0]
    if isinstance(sigma, pd.Series):
        sigma = sigma.iloc[0]
    year_a = np.linspace(1, csp_available_years, csp_available_years)
    csp = []
    for x in year_a:
        weibull = np.exp(-(x / gamma_variable) ** beta_variable * (math.gamma(1 + 1 / beta_variable)) ** beta_variable)
        delta = k / (np.sqrt(np.pi * 2) * sigma)
        normal = delta * np.exp(-0.5 * ((x - mu) / sigma) ** 2)
        csp_value = weibull + normal
        csp.append(csp_value)
    return csp
