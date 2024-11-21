from src.part5_sensitivity_analysis.historical_csp_modified.process_historical_csp import process_stock_shares_with_historical_csps
from src.part5_sensitivity_analysis.historical_csp_modified.generate_columns_to_plot import generate_columns_to_plot
from src.part2_survival_rates.plot_survival_rates.plot_countries import plot_all_countries
from src.part5_sensitivity_analysis.historical_csp_modified.plot_with_historical_csps.graph_inputs import \
    config_sensitivity_2


def do_sensitivity_analysis_with_historical_country_csps(registrations, survival_rates_2021, survival_rates_2016,
                                                         stock_years, optimum_parameters_2008,
                                                         optimal_distribution_dict):
    all_shares_df = process_stock_shares_with_historical_csps(registrations, survival_rates_2021, survival_rates_2016,
                                                              stock_years, optimum_parameters_2008,
                                                              optimal_distribution_dict)
    bev_stock_shares = all_shares_df[all_shares_df['powertrain'] == 'BEV']
    columns_to_plot = {}
    years_selected = [2021, 2016, 2008]
    columns_to_plot = generate_columns_to_plot(columns_to_plot, years_selected)
    plot_all_countries(bev_stock_shares, config_sensitivity_2, columns_to_plot, None)

