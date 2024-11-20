from src.loader.loader import *
from src.part1_transportation_model.input_data import eu_countries_and_norway
from src.part1_transportation_model.calculate_registrations import calculate_registrations
from src.part2_survival_rates.calculate_csp_parameters import calculate_csp_parameters
from src.part2_survival_rates.calculate_empirical_survival_rates.calculate_empirical_survival_rates \
    import calculate_empirical_survival_rates
from src.part2_survival_rates.get_fitted_csp_values import get_fitted_csp_values
from src.part2_survival_rates.plot_survival_rates.get_csp_plots import get_csp_plots
from src.part2_survival_rates.plot_survival_rates.graph_inputs import config_all, config_group
from src.part3_stock_calculation.calculate_stock import calculate_stock
from src.part3_stock_calculation.input_data import stock_years, historical_csp, save_options_stock
from src.part3_stock_calculation.plot_stock.plot_bev_stock_share import plot_bev_stock_shares
from src.part3_stock_calculation.plot_stock.graph_inputs import config_bev_reference_scenario
from src.part4_validate_model.compare_model_and_actual_stock_results import compare_model_and_actual_stock_results

registrations = calculate_registrations(historical_registrations, eu_countries_and_norway,
                                        registrations_eu_cam_scenario, clusters, registration_shares_by_cluster)
optimum_parameters_wg, optimal_distribution_dict = calculate_csp_parameters(survival_rates_2021, 2021)
survival_rates_2021 = calculate_empirical_survival_rates(stock_by_age_2021, historical_registrations, stock_year)
fitted_csp_values = get_fitted_csp_values(survival_rates_2021, optimum_parameters_wg)
get_csp_plots(survival_rates_2021, fitted_csp_values, optimum_parameters_wg, config_all, config_group)
stock_values, stock_shares = calculate_stock(registrations, fitted_csp_values, optimal_distribution_dict, stock_years,
                                             historical_csp, save_options_stock)
plot_bev_stock_shares(stock_shares, config_bev_reference_scenario)
compare_model_and_actual_stock_results(registrations, stock_shares, actual_bev_registration_shares,
                                       actual_bev_stock_shares, fitted_csp_values, optimal_distribution_dict,
                                       stock_years, historical_csp)

print(fitted_csp_values)


import ast


def replace_survival_rates_with_country(survival_rates, country_label):
    # Selecting rows for the specific country label
    country_data = survival_rates[survival_rates['geo country'] == country_label]
    # Selecting survival rates for the specified country
    country_survival_rates = country_data[['vehicle age', 'survival rate Weibull', 'survival rate WG', 'distribution']]
    # Merge survival rates of the specified country with the original DataFrame for all countries
    survival_rates_merged = pd.merge(survival_rates, country_survival_rates, on='vehicle age', suffixes=(f'_{country_label}', ''))
    # Drop redundant columns
    survival_rates_merged.drop(columns=[f'survival rate Weibull_{country_label}', f'survival rate WG_{country_label}', f'distribution_{country_label}'], inplace=True)

    return survival_rates_merged


def update_opt_dist(country, opt_dist):
    weibull_countries = opt_dist['Weibull']
    wg_countries = opt_dist['WG']
    # Parse the string representations into lists
    #weibull_countries = ast.literal_eval(weibull_countries)
    #wg_countries = ast.literal_eval(wg_countries)
    # Checking if the provided country is present in weibull_countries and wg_countries
    if country in weibull_countries:
        weibull_countries.extend(wg_countries)
        wg_countries = []
    elif country in wg_countries:
        wg_countries.extend(weibull_countries)
        weibull_countries = []
    else:
        weibull_countries = []
        wg_countries = []

    # Combine the two lists into a single dictionary variable
    combined_countries = {
        'Weibull': weibull_countries,
        'WG': wg_countries
    }

    return combined_countries


stock_shares_dict = {}

countries_selected = ["Bulgaria", "Poland", "Italy", "Netherlands", "Germany", "Luxembourg"]
for country in countries_selected:
    updated_survival_rates = replace_survival_rates_with_country(fitted_csp_values.copy(), country)
    updated_survival_rates.to_csv(f'outputs/updated_survival_rates{country}.csv', sep=';', index=False, decimal=',')
    updated_opt_dist_dict = update_opt_dist(country, optimal_distribution_dict)
    stock_values, stock_shares = calculate_stock(registrations, updated_survival_rates, updated_opt_dist_dict,
                                                 stock_years, historical_csp)
    print(stock_shares)
    stock_shares_dict[country] = stock_shares

print(stock_shares_dict)



