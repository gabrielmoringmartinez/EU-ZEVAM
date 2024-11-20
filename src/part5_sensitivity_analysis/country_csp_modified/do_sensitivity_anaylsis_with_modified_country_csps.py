from src.part2_survival_rates.plot_survival_rates.plot_countries import plot_all_countries
from src.part3_stock_calculation.calculate_stock import calculate_stock
from src.part5_sensitivity_analysis.country_adjectives import country_adjectives
from src.part5_sensitivity_analysis.country_csp_modified.replace_survival_rates_with_country_specific_csp import replace_survival_rates_with_country_specific_csp
from src.part5_sensitivity_analysis.country_csp_modified.update_optimal_distribution import update_optimal_distribution_based_on_country_csp
from src.part5_sensitivity_analysis.country_csp_modified.generate_columns_to_plot import generate_columns_to_plot


def do_sensitivity_analysis_with_modified_country_csps(registrations, stock_shares, survival_rates,
                                                      optimal_distribution_dict, config):
    plot_params = config["plot_params"]
    columns_to_plot = {"share": "Share"}
    all_shares_df = stock_shares
    for country in plot_params["countries_selected"]:
        updated_survival_rates = replace_survival_rates_with_country_specific_csp(survival_rates.copy(), country)
        updated_opt_dist_dict = update_optimal_distribution_based_on_country_csp(country, optimal_distribution_dict)
        stock_values, stock_shares = calculate_stock(registrations, updated_survival_rates, updated_opt_dist_dict,
                                                     plot_params["stock_years"], plot_params["historical_csp"])
        stock_shares_country = stock_shares[['geo country', 'stock_year', 'powertrain', 'share']].copy()
        stock_shares_country.rename(columns={'share': f'share_{country}'}, inplace=True)
        if all_shares_df is None:
            all_shares_df = stock_shares_country
        else:
            all_shares_df = all_shares_df.merge(stock_shares_country,
                                                on=['geo country', 'stock_year', 'powertrain'],
                                                how='outer')
        columns_to_plot = generate_columns_to_plot(columns_to_plot, plot_params["countries_selected"], country_adjectives)
    bev_stock_shares = all_shares_df[all_shares_df['powertrain'] == 'BEV']
    plot_all_countries(bev_stock_shares, config, columns_to_plot, None)