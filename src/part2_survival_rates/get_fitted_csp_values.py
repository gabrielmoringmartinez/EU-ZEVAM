import pandas as pd
from src.part2_survival_rates.get_statistical_parameters import get_statistical_parameters, \
    get_statistical_parameters_of_each_country
from src.part2_survival_rates.get_function_values import get_weibull_function, get_weibull_and_normal_function
from src.part2_survival_rates.get_distribution_function_discrete_points import get_distribution_function_discrete_points


def get_fitted_csp_values(survival_rates, pdf_parameters):
    """
    Calculates fitted cumulative survival probability (CSP) values using Weibull and Weibull-Gaussian
    distribution optimum fitted parameters.

    Parameters:
    - survival_rates (pd.DataFrame): Data containing survival rates for each country.
    - pdf_parameters (pd.DataFrame): DataFrame containing the parameters for the Weibull and Gaussian distributions.
        and Weibull Gaussian curves.
    Returns:
    - pd.DataFrame: DataFrame containing fitted CSP values for each country by vehicle age, distribution model (Weibull
     and Weibull Gaussian), and distribution type.
    """
    country_names = survival_rates['geo country'].unique()
    weibull_results = pd.DataFrame()
    wg_results = pd.DataFrame()
    for country_name in country_names:
        survival_rates_country = survival_rates[survival_rates["geo country"] == country_name]
        weibull_results, wg_results = calculate_country_fitted_values(country_name, survival_rates_country,
                                                                      pdf_parameters, weibull_results, wg_results)
    fitted_csp_values = pd.merge(weibull_results, wg_results, on=['geo country', 'vehicle age'],
                                 suffixes=(' Weibull', ' WG'), how='inner')
    fitted_csp_values = pd.merge(fitted_csp_values, pdf_parameters[['geo country', 'distribution']], on = 'geo country')
    fitted_csp_values.to_csv(f'outputs/2_3_fitted_CSP_curves.csv', sep=';', index=False, decimal=',')
    return fitted_csp_values


def calculate_country_fitted_values(country_name, survival_rates, pdf_parameters, weibull_results, wg_results):
    """
    Helper function to calculate Weibull and Weibull-Gaussian fitted CSP values for a single country.

    Parameters:
    - country_name (str): Name of the country to calculate fitted values for.
    - survival_rates (pd.DataFrame): DataFrame with survival rates.
    - pdf_parameters (pd.DataFrame): DataFrame with distribution parameters.

    Returns:
    - tuple: Two lists of dictionaries for Weibull and Weibull-Gaussian CSP values.
    """
    survival_rates_country = survival_rates[survival_rates["geo country"] == country_name]
    gamma, beta, k, mu, sigma = get_statistical_parameters(pdf_parameters)
    gamma_country, beta_country, k_country, mu_country, sigma_country = \
        get_statistical_parameters_of_each_country(gamma, beta, k, mu, sigma, country_name)

    predicted_weibull_value = get_weibull_function(gamma_country, beta_country)
    predicted_weibull_and_normal_value = get_weibull_and_normal_function(gamma_country, beta_country, k_country,
                                                                         mu_country, sigma_country)
    weibull_results = get_distribution_function_discrete_points(weibull_results, survival_rates_country,
                                                                predicted_weibull_value)

    wg_results = get_distribution_function_discrete_points(wg_results, survival_rates_country,
                                                           predicted_weibull_and_normal_value)
    return weibull_results, wg_results
