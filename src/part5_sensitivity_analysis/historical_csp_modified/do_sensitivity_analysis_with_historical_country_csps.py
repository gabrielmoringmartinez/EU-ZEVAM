from src.part5_sensitivity_analysis.historical_csp_modified.process_historical_csp import process_stock_shares_with_historical_csps
from src.part5_sensitivity_analysis.historical_csp_modified.generate_columns_to_plot import generate_columns_to_plot
from src.part2_survival_rates.plot_survival_rates.plot_countries import plot_all_countries



def do_sensitivity_analysis_with_historical_country_csps(registrations, survival_rates_2021, survival_rates_2016,
                                                         stock_years, optimum_parameters_2008,
                                                         optimal_distribution_dict, config):
    plot_params = config["plot_params"]
    stock_shares_df = process_stock_shares_with_historical_csps(registrations, survival_rates_2021, survival_rates_2016,
                                                              stock_years, optimum_parameters_2008,
                                                              optimal_distribution_dict)
    bev_stock_shares = stock_shares_df[stock_shares_df['powertrain'] == plot_params["powertrain_to_plot"]]
    columns_to_plot = {}
    columns_to_plot = generate_columns_to_plot(columns_to_plot, plot_params["years_selected"])
    plot_all_countries(bev_stock_shares, config, columns_to_plot, None)

