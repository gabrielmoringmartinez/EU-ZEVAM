from src.loader.loader import *
from src.part1_transportation_model.input_data import eu_countries_and_norway
from src.part1_transportation_model.calculate_registrations import calculate_registrations
from src.part2_survival_rates.calculate_csp_parameters import calculate_csp_parameters
from src.part2_survival_rates.get_fitted_csp_values import get_fitted_csp_values
from src.part2_survival_rates.plot_survival_rates.get_csp_plots import get_csp_plots
from src.part2_survival_rates.plot_survival_rates.graph_inputs import config_all, config_group


registrations = calculate_registrations(historical_registrations, eu_countries_and_norway,
                                        registrations_eu_cam_scenario, clusters, registration_shares_by_cluster)
optimum_parameters_wg, optimal_distribution_dict = calculate_csp_parameters(survival_rates_2021, 2021)
fitted_csp_values = get_fitted_csp_values(survival_rates_2021, optimum_parameters_wg)
get_csp_plots(survival_rates_2021, fitted_csp_values, optimum_parameters_wg, config_all, config_group)

print(registrations.columns)
print(fitted_csp_values.columns)



def repeat_data_for_years(original_df, stock_years):
    # Unpack the stock_years array to get the initial and end years
    initial_year, end_year = stock_years
    # Create the initial DataFrame with the constant year (initial_year)
    years = pd.DataFrame({'stock_year': range(initial_year, end_year)})
    # Use a cross join to duplicate original_df for each year
    result_df = original_df.merge(years, how='cross')
    return result_df


def select_column(row, **kwargs):
    optimal_distribution_dict = kwargs.get('optimal_distribution_dict', {})  # Retrieve the opt_dist_dict from kwargs
    if row['geo country'] in optimal_distribution_dict.get('Weibull', {}):
        return row['stock_weibull']
    elif row['geo country'] in optimal_distribution_dict.get('WG', {}):
        return row['stock_wg']
    else:
        return None  # You can handle the case when the country is not in any key


stock_years = [2014, 2050]
time_dim = 'time'
registrations_dim = 'registrations by powertrain'

survival_rates = repeat_data_for_years(fitted_csp_values, stock_years)
survival_rates_ = survival_rates.copy()
# Time represents the year of registration of the vehicle
survival_rates_[time_dim] = survival_rates_['stock_year'] - survival_rates_['vehicle age'] + 1
# Survival rates and registrations are merged
stock_data = pd.merge(survival_rates_, registrations, on=['geo country', time_dim], how='inner')
# Stock based on Weibull CSP parameters is obtained
stock_data['stock_weibull'] = stock_data['survival rate Weibull']*stock_data[registrations_dim]
# Stock based on Weibull-Gaussian parameters is obtained
stock_data['stock_wg'] = stock_data['survival rate WG'] * stock_data[registrations_dim]
# Stock based on the optimum distribution is obtained
stock_data['stock'] = stock_data.apply(select_column, axis=1, optimal_distribution_dict=optimal_distribution_dict)
stock_data = stock_data.rename(columns={time_dim: "year of first registration"})
stock_data = stock_data.drop(columns=['survival rate Weibull', 'survival rate WG', 'distribution', 'cluster', 'stock_weibull', 'stock_wg', 'new vehicle registrations', 'relative sales', registrations_dim])
stock_data.to_csv(f'outputs/stock_data_.csv', sep=';', index=False, decimal=',')