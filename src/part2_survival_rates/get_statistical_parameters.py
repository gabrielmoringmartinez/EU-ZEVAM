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
    gamma_variable = pdf_parameters[["gamma (Weibull)", "geo country"]]
    beta_variable = pdf_parameters[["beta (Weibull)", "geo country"]]
    k_variable = pdf_parameters[["k (Import-Gaussian)", "geo country"]]
    mu_variable = pdf_parameters[["mu (Import-Gaussian)", "geo country"]]
    sigma_variable = pdf_parameters[["sigma (Import-Gaussian)", "geo country"]]
    return gamma_variable, beta_variable, k_variable, mu_variable, sigma_variable


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
    gamma_country = gamma[gamma["geo country"] == country_name]["gamma (Weibull)"]
    beta_country = beta[beta["geo country"] == country_name]["beta (Weibull)"]
    k_country = k[k["geo country"] == country_name]["k (Import-Gaussian)"]
    mu_country = mu[mu["geo country"] == country_name]["mu (Import-Gaussian)"]
    sigma_country = sigma[sigma["geo country"] == country_name]["sigma (Import-Gaussian)"]
    return gamma_country, beta_country, k_country, mu_country, sigma_country
