from src.load_data_and_prepare_inputs.dimension_names import *


def get_statistical_parameters(pdf_parameters):
    """
       Extracts the statistical parameters for the Weibull and Gaussian distributions from the provided DataFrame.

       Parameters:
       - pdf_parameters (pd.DataFrame): DataFrame containing the parameters for the Weibull and Gaussian distributions.

       Returns:
       - gamma (pd.DataFrame): Extracted gamma values for the Weibull distribution.
       - beta (pd.DataFrame): Extracted beta values for the Weibull distribution.
       - k (pd.DataFrame): Extracted k values for the Gaussian distribution.
       - mu (pd.DataFrame): Extracted mu values for the Gaussian distribution.
       - sigma (pd.DataFrame): Extracted sigma values for the Gaussian distribution.
       """
    gamma_variable = pdf_parameters[[gamma_weibull_dim, country_dim]]
    beta_variable = pdf_parameters[[beta_weibull_dim, country_dim]]
    k_variable = pdf_parameters[[k_weibull_gaussian_dim, country_dim]]
    mu_variable = pdf_parameters[[mu_weibull_gaussian_dim, country_dim]]
    sigma_variable = pdf_parameters[[sigma_weibull_gaussian_dim, country_dim]]
    return gamma_variable, beta_variable, k_variable, mu_variable, sigma_variable



