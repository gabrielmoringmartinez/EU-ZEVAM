from src.part2_survival_rates.get_fitted_csp_values import get_fitted_csp_values
from src.part3_stock_calculation.calculate_stock import calculate_stock
from src.part5_sensitivity_analysis.historical_csp_modified.merge_stock_shares import merge_stock_shares
from src.part5_sensitivity_analysis.relative_increase_decrease_csp_modified.generate_columns_to_plot import generate_columns_to_plot
from src.part5_sensitivity_analysis.relative_increase_decrease_csp_modified.plot_with_increase_csps.graph_inputs import config_sensitivity_3
from src.part2_survival_rates.plot_survival_rates.plot_countries import plot_all_countries


def do_sensitivity_analysis_with_increased_decreased_csps(registrations, survival_rates, stock_years, optimum_parameters_wg, optimal_distribution_dict):
    stock_shares_df = None
    percentages_selected = [-0.4, -0.2, 0, 0.2, 0.4]
    for percentage in percentages_selected:
        optimum_parameters = optimum_parameters_wg.copy()
        percentage_value = 1 + percentage
        optimum_parameters["gamma (Weibull)"] = optimum_parameters["gamma (Weibull)"] * percentage_value
        optimum_parameters["mu (Import-Gaussian)"] = optimum_parameters["mu (Import-Gaussian)"] * percentage_value
        fitted_csp_values = get_fitted_csp_values(survival_rates, optimum_parameters, True)
        stock_values, stock_shares = calculate_stock(registrations, fitted_csp_values, optimal_distribution_dict,
                                                     stock_years, 'non-historical_csp')
        stock_shares.rename(columns={'share': f'share_{percentage}'}, inplace=True)
        stock_shares_df = merge_stock_shares(stock_shares_df, stock_shares)
    bev_stock_shares = stock_shares_df[stock_shares_df['powertrain'] == 'BEV']
    columns_to_plot = {}
    columns_to_plot = generate_columns_to_plot(columns_to_plot, percentages_selected)
    plot_all_countries(bev_stock_shares, config_sensitivity_3, columns_to_plot, None)
    return