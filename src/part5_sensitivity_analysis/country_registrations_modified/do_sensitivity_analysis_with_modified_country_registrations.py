from src.part2_survival_rates.plot_survival_rates.plot_countries import plot_all_countries
from src.part3_stock_calculation.calculate_stock import calculate_stock
from src.part5_sensitivity_analysis.country_adjectives import country_adjectives
from src.part5_sensitivity_analysis.country_csp_modified.generate_columns_to_plot import generate_columns_to_plot
from src.part5_sensitivity_analysis.country_registrations_modified.replace_powertrain_share_registrations_with_country import replace_powertrain_share_registrations_with_country
from src.part5_sensitivity_analysis.update_stock_shares import update_stock_shares


def do_sensitivity_analysis_with_modified_country_registrations(registrations, stock_shares, survival_rates,
                                                                optimal_distribution_dict, config):
    plot_params = config["plot_params"]
    columns_to_plot = {"share": "Share"}
    stock_shares_df = stock_shares
    for country in plot_params["countries_selected"]:
        updated_registrations = replace_powertrain_share_registrations_with_country(registrations, country)
        stock_values, stock_shares = calculate_stock(updated_registrations, survival_rates, optimal_distribution_dict,
                                                     plot_params["stock_years"], plot_params["historical_csp"])
        stock_shares_df = update_stock_shares(stock_shares_df, stock_shares, country)
        columns_to_plot = generate_columns_to_plot(columns_to_plot, plot_params["countries_selected"], country_adjectives)
    bev_stock_shares = stock_shares_df[stock_shares_df['powertrain'] == plot_params["powertrain_to_plot"]]
    plot_all_countries(bev_stock_shares, config, columns_to_plot, None)

