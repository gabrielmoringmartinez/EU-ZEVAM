def get_statistical_parameters(pdf_parameters):
    gamma_variable = pdf_parameters[["gamma (Weibull)", "country label"]]
    beta_variable = pdf_parameters[["beta (Weibull)", "country label"]]
    k_variable = pdf_parameters[["k (Import-Gaussian)", "country label"]]
    mu_variable = pdf_parameters[["mu (Import-Gaussian)", "country label"]]
    sigma_variable = pdf_parameters[["sigma (Import-Gaussian)", "country label"]]
    return gamma_variable, beta_variable, k_variable, mu_variable, sigma_variable


def get_statistical_parameters_of_each_country(gamma, beta, k, mu, sigma, country_name):
    gamma_country = gamma[gamma["country label"] == country_name]["gamma (Weibull)"]
    beta_country = beta[beta["country label"] == country_name]["beta (Weibull)"]
    k_country = k[k["country label"] == country_name]["k (Import-Gaussian)"]
    mu_country = mu[mu["country label"] == country_name]["mu (Import-Gaussian)"]
    sigma_country = sigma[sigma["country label"] == country_name]["sigma (Import-Gaussian)"]
    return gamma_country, beta_country, k_country, mu_country, sigma_country
