from src.part2_survival_rates.get_fitted_csp_values import get_fitted_csp_values
from src.part3_stock_calculation.calculate_stock.calculate_stock import calculate_stock
from src.part3_stock_calculation.calculate_stock.input_data import stock_years, historical_csp


def calculate_2008_survival_rates(optimum_parameters_2008, survival_rates_2021, optimal_distribution_dict, registrations):
    country_names = optimum_parameters_2008['geo country'].unique()
    filtered_survival_rates_2021 = survival_rates_2021[survival_rates_2021['geo country'].isin(country_names)]
    fitted_csp_values_2008 = get_fitted_csp_values(filtered_survival_rates_2021, optimum_parameters_2008, False)
    optimal_distribution_dict_2008 = prepare_optimal_distribution_dict(optimal_distribution_dict)
    stock_values_2008, stock_shares_2008 = calculate_stock(registrations, fitted_csp_values_2008,
                                                           optimal_distribution_dict_2008, stock_years, historical_csp)
    stock_shares_2008['geo country'] = stock_shares_2008['geo country'].replace('EU-27+Norway', 'EU-9')
    #stock_values_2008['geo country'] = stock_values_2008['geo country'].replace('EU-27+Norway', 'EU-9')
    return stock_shares_2008

def prepare_optimal_distribution_dict(distribution_dict):
    """
    Prepare the optimal distribution dictionary for 2008 by combining Weibull and WG.
    """
    updated_dict = distribution_dict.copy()
    updated_dict['Weibull'] += updated_dict['WG']  # Add all elements from WG to Weibull
    updated_dict['WG'] = []  # Clear WG list
    return updated_dict