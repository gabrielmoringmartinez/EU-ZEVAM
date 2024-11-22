from src.part2_survival_rates.get_fitted_csp_values import get_fitted_csp_values
from src.part3_stock_calculation.calculate_stock import calculate_stock
from src.part5_sensitivity_analysis.relative_increase_decrease_csp_modified.generate_columns_to_plot import generate_columns_to_plot
from src.part2_survival_rates.plot_survival_rates.plot_countries import plot_all_countries
from src.part5_sensitivity_analysis.update_stock_shares import update_stock_shares


def do_sensitivity_analysis_with_increased_decreased_csps(registrations, survival_rates, stock_years, optimum_parameters_wg, optimal_distribution_dict, config):
    plot_params = config["plot_params"]
    stock_shares_df = None
    for percentage in plot_params["percentages_selected"]:
        optimum_parameters = optimum_parameters_wg.copy()
        percentage_value = 1 + percentage
        optimum_parameters["gamma (Weibull)"] = optimum_parameters["gamma (Weibull)"] * percentage_value
        optimum_parameters["mu (Import-Gaussian)"] = optimum_parameters["mu (Import-Gaussian)"] * percentage_value
        fitted_csp_values = get_fitted_csp_values(survival_rates, optimum_parameters, True)
        stock_values, stock_shares = calculate_stock(registrations, fitted_csp_values, optimal_distribution_dict,
                                                     stock_years, 'non-historical_csp')
        stock_shares_df = update_stock_shares(stock_shares_df, stock_shares, percentage)
    bev_stock_shares = stock_shares_df[stock_shares_df['powertrain'] == plot_params["powertrain_to_plot"]]
    columns_to_plot = {}
    columns_to_plot = generate_columns_to_plot(columns_to_plot, plot_params["percentages_selected"])
    plot_all_countries(bev_stock_shares, config, columns_to_plot, None)
    return