from src.load_data_and_prepare_inputs.dimension_names import *


def get_statistical_parameters_of_each_country(gamma, beta, k, mu, sigma, country_name):
    """
       Extracts the statistical parameters for a specific country

       Parameters:
       - gamma (pd.DataFrame): Extracted gamma values for the Weibull distribution.
       - beta (pd.DataFrame): Extracted beta values for the Weibull distribution.
       - k (pd.DataFrame): Extracted k values for the Gaussian distribution.
       - mu (pd.DataFrame): Extracted mu values for the Gaussian distribution.
       - sigma (pd.DataFrame): Extracted sigma values for the Gaussian distribution.

       Returns:
       - gamma_country (float): The gamma parameter for the specified country.
       - beta_country (float): The beta parameter for the specified country.
       - k_country (float): The k parameter for the specified country.
       - mu_country (float): The mu parameter for the specified country.
       - sigma_country (float): The sigma parameter for the specified country.
       """
    gamma_country = gamma[gamma[country_dim] == country_name][gamma_weibull_dim]
    beta_country = beta[beta[country_dim] == country_name][beta_weibull_dim]
    k_country = k[k[country_dim] == country_name][k_weibull_gaussian_dim]
    mu_country = mu[mu[country_dim] == country_name][mu_weibull_gaussian_dim]
    sigma_country = sigma[sigma[country_dim] == country_name][sigma_weibull_gaussian_dim]
    return gamma_country, beta_country, k_country, mu_country, sigma_country
