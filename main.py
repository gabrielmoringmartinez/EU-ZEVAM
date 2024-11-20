from src.loader.loader import *
from src.part1_transportation_model.input_data import eu_countries_and_norway
from src.part1_transportation_model.calculate_registrations import calculate_registrations
from src.part2_survival_rates.calculate_empirical_survival_rates.calculate_empirical_survival_rates \
    import calculate_empirical_survival_rates
from src.part2_survival_rates.plot_survival_rates.get_csp_plots import get_csp_plots
from src.part2_survival_rates.plot_survival_rates.graph_inputs import config_all, config_group
from src.part3_stock_calculation.compute_csp_values_and_compute_stock import compute_csp_values_and_compute_stock
from src.part3_stock_calculation.input_data import stock_years, historical_csp, save_options_stock
from src.part3_stock_calculation.plot_stock.plot_bev_stock_share import plot_bev_stock_shares
from src.part3_stock_calculation.plot_stock.graph_inputs import config_bev_reference_scenario
from src.part4_validate_model.compare_model_and_actual_stock_results import compare_model_and_actual_stock_results
from src.part5_sensitivity_analysis.country_csp_modified.plot_with_modified_country_csps.graph_inputs import config_sensitivity_1
from src.part5_sensitivity_analysis.country_csp_modified.do_sensitivity_anaylsis_with_modified_country_csps import do_sensitivity_analysis_with_modified_country_csps
from src.part5_sensitivity_analysis.historical_csp_modified.calculate_2008_survival_rates import calculate_2008_survival_rates

registrations = calculate_registrations(historical_registrations, eu_countries_and_norway,
                                        registrations_eu_cam_scenario, clusters, registration_shares_by_cluster)
survival_rates_2021 = calculate_empirical_survival_rates(stock_by_age_2021, historical_registrations, stock_year)

stock_values, stock_shares, optimum_parameters_wg, optimal_distribution_dict, fitted_csp_values = \
    compute_csp_values_and_compute_stock(survival_rates_2021, registrations, 2021, stock_years,
                                         historical_csp, save_options_stock)
get_csp_plots(survival_rates_2021, fitted_csp_values, optimum_parameters_wg, config_all, config_group)
plot_bev_stock_shares(stock_shares, config_bev_reference_scenario)






compare_model_and_actual_stock_results(registrations, stock_shares, actual_bev_registration_shares,
                                       actual_bev_stock_shares, fitted_csp_values, optimal_distribution_dict,
                                       stock_years, historical_csp)
do_sensitivity_analysis_with_modified_country_csps(registrations, stock_shares, fitted_csp_values,
                                                  optimal_distribution_dict, config_sensitivity_1)


def merge_stock_shares(all_shares_df, stock_shares):
    """
    Merge the provided stock_shares DataFrame into all_shares_df on specified columns.

    Args:
        all_shares_df (pd.DataFrame or None): The main DataFrame to merge into. If None,
                                              this will be initialized with stock_shares.
        stock_shares (pd.DataFrame): The stock shares DataFrame to merge.

    Returns:
        pd.DataFrame: Updated DataFrame containing merged stock shares.
    """
    # Ensure stock_shares only contains relevant columns
    stock_shares = stock_shares.drop(columns=['stock'])

    # If all_shares_df is None, initialize it with stock_shares
    if all_shares_df is None:
        all_shares_df = stock_shares
    else:
        all_shares_df = all_shares_df.merge(stock_shares, on=['geo country', 'stock_year', 'powertrain'], how='outer')

    return all_shares_df


def generate_columns_to_plot(columns_to_plot, years_selected):
    """
    Generates the columns_to_plot dictionary for the plot legend.
    """
    for year in years_selected:
        column_name = f"share_{year}"
        columns_to_plot[column_name] = f"Share with CSP from {year}"
    return columns_to_plot





stock_values, stock_shares, optimum_parameters_wg, optimal_distribution_dict, fitted_csp_values = \
    compute_csp_values_and_compute_stock(survival_rates_2021, registrations, 2021, stock_years,
                                         'historical CSP', save_options_stock)
stock_values_2016, stock_shares_2016, x, y, z = compute_csp_values_and_compute_stock(survival_rates_2016, registrations,
                                                                                     2016, stock_years, 'historical CSP')
stock_shares_2008 = calculate_2008_survival_rates(optimum_parameters_2008, survival_rates_2021,
                                                  optimal_distribution_dict, registrations)
stock_shares.rename(columns={'share': f'share_{2021}'}, inplace=True)
stock_shares_2016.rename(columns={'share': f'share_{2016}'}, inplace=True)
stock_shares_2008.rename(columns={'share': f'share_{2008}'}, inplace=True)


all_shares_df =None
all_shares_df = merge_stock_shares(all_shares_df, stock_shares)
all_shares_df = merge_stock_shares(all_shares_df, stock_shares_2016)
all_shares_df = merge_stock_shares(all_shares_df, stock_shares_2008)

bev_stock_shares = all_shares_df[all_shares_df['powertrain'] == 'BEV']
columns_to_plot = {}
years_selected = [2021, 2016, 2008]
columns_to_plot = generate_columns_to_plot(columns_to_plot, years_selected)
print(all_shares_df)
from src.part2_survival_rates.plot_survival_rates.plot_countries import plot_all_countries
from src.part5_sensitivity_analysis.historical_csp_modified.plot_with_historical_csps.graph_inputs import config_sensitivity_2
plot_all_countries(bev_stock_shares, config_sensitivity_2, columns_to_plot, None)

