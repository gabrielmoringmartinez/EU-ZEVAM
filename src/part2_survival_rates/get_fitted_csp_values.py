import pandas as pd
from src.part2_survival_rates.get_statistical_parameters import get_statistical_parameters, \
    get_statistical_parameters_of_each_country
from src.part2_survival_rates.get_function_values import get_weibull_function, get_weibull_and_normal_function
from src.part2_survival_rates.get_distribution_function_discrete_points import get_distribution_function_discrete_points


def get_fitted_csp_values(survival_rates, pdf_parameters):
    country_names = survival_rates['country label'].unique()
    survival_rates_weibull = pd.DataFrame()
    survival_rates_weibull_and_normal = pd.DataFrame()
    for country_name in country_names:
        survival_rates_country = survival_rates[survival_rates["country label"] == country_name]
        gamma, beta, k, mu, sigma = get_statistical_parameters(pdf_parameters)
        gamma_country, beta_country, k_country, mu_country, sigma_country = \
            get_statistical_parameters_of_each_country(gamma, beta, k, mu, sigma, country_name)

        predicted_weibull_value = get_weibull_function(gamma_country, beta_country)
        predicted_weibull_and_normal_value = get_weibull_and_normal_function(gamma_country, beta_country, k_country,
                                                                             mu_country, sigma_country)
        survival_rates_weibull = get_distribution_function_discrete_points(survival_rates_weibull,
                                                                           survival_rates_country,
                                                                           predicted_weibull_value)

        survival_rates_weibull_and_normal = get_distribution_function_discrete_points(survival_rates_weibull_and_normal,
                                                                                      survival_rates_country,
                                                                                      predicted_weibull_and_normal_value)

    fitted_csp_values = pd.merge(survival_rates_weibull, survival_rates_weibull_and_normal,
                                    on=['country label', 'vehicle age'],
                                    suffixes=(' Weibull', ' WG'), how='inner')
    fitted_csp_values = pd.merge(fitted_csp_values, pdf_parameters[['country label', 'distribution']], on ='country label')

    #country_optimum_distribution = {dist: pdf_parameters.loc[pdf_parameters['distribution'] == dist, 'country label'].tolist()
    #                         for dist in pdf_parameters['distribution'].unique()}
    fitted_csp_values.to_csv(f'outputs/2_2_fitted_CSP_curves.csv', sep=';', index=False, decimal=',')
    return fitted_csp_values
