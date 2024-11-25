from src.part1_transportation_model import calculate_registrations
from src.part2_survival_rates.calculate_empirical_survival_rates import calculate_empirical_survival_rates
from src.part3_stock_calculation.calculate_stock.compute_csp_values_and_compute_stock import compute_csp_values_and_compute_stock
from src.part2_survival_rates.plot_survival_rates import get_csp_plots
from src.part3_stock_calculation.plot_stock import plot_bev_stock_shares


def calculate_and_plot_csps_and_stock(data, inputs):
    registrations = calculate_registrations(data["historical_registrations"], inputs["eu_countries_and_norway"],
                                            data["registrations_eu_cam_scenario"], data["clusters"],
                                            data["registration_shares_by_cluster"])
    survival_rates_2021 = calculate_empirical_survival_rates(data["stock_by_age_2021"],
                                                             data["historical_registrations"],
                                                             data["stock_year"])
    stock_values, stock_shares, optimum_parameters_wg, optimal_distribution_dict, fitted_csp_values = \
        compute_csp_values_and_compute_stock(survival_rates_2021, registrations, inputs["csp_data_ref_year"],
                                             inputs["stock_years"], inputs["historical_csp"], inputs["save_options_stock"])
    get_csp_plots(survival_rates_2021, fitted_csp_values, optimum_parameters_wg, inputs["config_all"],
                  inputs["config_group"])
    plot_bev_stock_shares(stock_shares, inputs["config_bev_reference_scenario"])

    return {
        "registrations": registrations,
        "survival_rates_2021": survival_rates_2021,
        "stock_values": stock_values,
        "stock_shares": stock_shares,
        "optimum_parameters_wg": optimum_parameters_wg,
        "optimal_distribution_dict": optimal_distribution_dict,
        "fitted_csp_values": fitted_csp_values
    }