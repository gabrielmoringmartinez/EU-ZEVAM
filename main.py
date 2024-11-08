from src.loader.loader import *
from src.part1_transportation_model.input_data import eu_countries_and_norway
from src.part1_transportation_model.calculate_registrations import calculate_registrations


def calculate_csp_parameters(survival_rates, year):
    country_names = survival_rates['country label'].unique()
    bounds = [(5, 40), (2, 6)]
    optimum_parameters_weibull = run_diff_evol_algorithm_weibull(bounds, country_names, survival_rates)
    #title_excel = f'pdf_parameters_weibull_{year}_own_calculation'
    #optimum_parameters_weibull.to_excel(f'outputs/csp_and_stock/external_paper_results_replicated/{title_excel}.xlsx',
    #                                    index=False)

    k = [2, 100]
    mu = [5, 30]
    sigma = [5, 30]
    bounds = [k, mu, sigma]

    optimum_parameters_weibull_gaussian = run_diff_evol_algorithm_weibull_gaussian(bounds, country_names,
                                                                                     survival_rates,
                                                                                     optimum_parameters_weibull)

    #title_excel = 'pdf_parameters_WeibullGaussian_2016_own_calculation'
    #optimum_parameters_weibull_gaussian.to_excel(f'outputs/csp_and_stock/external_paper_results_replicated/'
    #                                              f'{title_excel}.xlsx', index=False)
    return optimum_parameters_weibull_gaussian

from scipy.optimize import differential_evolution
import numpy as np
def run_diff_evol_algorithm_weibull(bounds: list, country_names_number: np.ndarray, survival_rates):
    optimum_gamma_per_country = []
    optimum_beta_per_country = []
    max_rsquared_per_country = []
    for j in country_names_number:
        survival_rates_country = get_value_countries(survival_rates, j)
        result = differential_evolution(loss_function_weibull, bounds,survival_rates_country)
        optimum_gamma_per_country, optimum_beta_per_country, max_rsquared_per_country =save_optimum_parameters_weibull\
            (result, optimum_gamma_per_country, optimum_beta_per_country, max_rsquared_per_country)
    optimum_parameters_diff_evol_algorithm = get_df_optimum_parameters_weibull(optimum_gamma_per_country,
                                                                               optimum_beta_per_country,
                                                                               max_rsquared_per_country,
                                                                               country_names_number)
    return optimum_parameters_diff_evol_algorithm


def run_diff_evol_algorithm_weibull_gaussian(bounds, country_names_number, survival_rates, optimum_parameters_weibull):
    max_rsquared_per_country_weibull_gaussian = []
    optimum_k_per_country = []
    optimum_mu_per_country = []
    optimum_sigma_per_country = []
    optimum_delta_per_country = []
    parameters = [optimum_k_per_country, optimum_mu_per_country, optimum_sigma_per_country, optimum_delta_per_country, max_rsquared_per_country_weibull_gaussian]
    for j in country_names_number:
        survival_rates_country = get_value_countries(survival_rates, j)
        optimum_parameters_weibull_country = optimum_parameters_weibull[optimum_parameters_weibull["country label"] == j]
        gamma_country = optimum_parameters_weibull_country["gamma (Weibull)"].to_numpy()
        beta_country = optimum_parameters_weibull_country["beta (Weibull)"].to_numpy()
        args = (gamma_country, beta_country, survival_rates_country)
        result = differential_evolution(loss_function_weibull_and_normal, bounds, args)
        parameters =save_optimum_parameters_gaussian(result, optimum_k_per_country, optimum_mu_per_country, optimum_sigma_per_country, optimum_delta_per_country, max_rsquared_per_country_weibull_gaussian)
    optimum_parameters_diff_evol_algorithm = get_df_optimum_parameters_gaussian(optimum_parameters_weibull, parameters)
    return optimum_parameters_diff_evol_algorithm

import numpy as np
import math
def loss_function_weibull(x : list, *args) -> float:
    year = np.linspace(1, 45, 45)
    predict = np.exp(-(year/x[0])**x[1]*(math.gamma(1+1/x[1]))**x[1])
    actual = args
    return sum((predict-actual)**2)/sum((actual-np.average(actual))**2)


def loss_function_weibull_and_normal(x: list, *args) -> float:
    gamma_country = args[0]
    beta_country = args[1]
    year = np.linspace(1, 45, 45)
    weibull = np.exp(-(year/gamma_country)**beta_country*(math.gamma(1+1/beta_country))**beta_country)
    delta = x[0]/(np.sqrt(np.pi*2)*x[2])
    normal = delta*np.exp(-0.5*((year-x[1])/x[2])**2)
    predict = weibull + normal
    actual = args[2]
    return sum((predict-actual)**2)/sum((actual-np.average(actual))**2)


def get_df_optimum_parameters_weibull(optimum_gamma_per_country, optimum_beta_per_country, max_rsquared_per_country,
                                      country_names):
    optimum_parameters_diff_evol_algorithm = pd.DataFrame()
    optimum_parameters_diff_evol_algorithm['country label'] = country_names
    optimum_parameters_diff_evol_algorithm["gamma (Weibull)"]= optimum_gamma_per_country
    optimum_parameters_diff_evol_algorithm["beta (Weibull)"] = optimum_beta_per_country
    optimum_parameters_diff_evol_algorithm["r squared (Weibull)"] = max_rsquared_per_country
    return optimum_parameters_diff_evol_algorithm


def get_df_optimum_parameters_gaussian(optimum_parameters_diff_evol_algorithm, parameters):
    optimum_parameters_diff_evol_algorithm["k (Import-Gaussian)"] = parameters[0]
    optimum_parameters_diff_evol_algorithm["mu (Import-Gaussian)"] = parameters[1]
    optimum_parameters_diff_evol_algorithm["sigma (Import-Gaussian)"]= parameters[2]
    optimum_parameters_diff_evol_algorithm["delta (Import-Gaussian)"]= parameters[3]
    optimum_parameters_diff_evol_algorithm["r squared (Weibull and Import-Gaussian)"] = parameters[4]
    return optimum_parameters_diff_evol_algorithm


def save_optimum_parameters_weibull(result, optimum_gamma_per_country, optimum_beta_per_country, max_rsquared_per_country):
    optimum_gamma_per_country.append(result.x[0])
    optimum_beta_per_country.append(result.x[1])
    max_rsquared_per_country.append(1-result.fun)
    return optimum_gamma_per_country, optimum_beta_per_country, max_rsquared_per_country


def save_optimum_parameters_gaussian(result, optimum_k_per_country, optimum_mu_per_country, optimum_sigma_per_country,
                                     optimum_delta_per_country, max_rsquared_per_country_weibull_gaussian):
    optimum_k_per_country.append(result.x[0])
    optimum_mu_per_country.append(result.x[1])
    optimum_sigma_per_country.append(result.x[2])
    max_rsquared_per_country_weibull_gaussian.append(1-result.fun)
    delta = result.x[0]/(np.sqrt(2*np.pi)*result.x[2])
    optimum_delta_per_country.append(delta)
    return optimum_k_per_country, optimum_mu_per_country, optimum_sigma_per_country, optimum_delta_per_country, \
        max_rsquared_per_country_weibull_gaussian


def get_value_countries(survival_rates, country_name):
    values_country = survival_rates[survival_rates["country label"] == country_name]
    survival_rates_country = values_country["survival rate"]
    return survival_rates_country


optimum_parameters_wg = calculate_csp_parameters(survival_rates_2021, 2021)
optimum_parameters_wg.to_csv(f'outputs/2_1_optimum_parameters_csp_curves.csv', sep=';', index=False, decimal=',')


def adapt_registrations_to_vehicle_stock_year(historical_registrations):
# This is necessary to afterwards calculate the stock!!!
    country_label = []
    vehicle_age = []
    new_registrations = []

    for index, row in historical_registrations.iterrows():
        if row['stock year'] >= row['time']:
            country_label.append(row['country label'])
            vehicle_age.append(row['stock year'] - row['time'] + 1)
            new_registrations.append(row['new vehicle registrations'])

    my_dict = {'country label': country_label, 'vehicle age': vehicle_age, 'new registrations': new_registrations}
    return my_dict




registrations = calculate_registrations(historical_registrations, eu_countries_and_norway, country_labels,
                                                 registrations_eu_cam_scenario, clusters, registration_shares_by_cluster)
historical_registrations = pd.merge(historical_registrations, stock_year, how='left')
historical_registrations = adapt_registrations_to_vehicle_stock_year(historical_registrations)