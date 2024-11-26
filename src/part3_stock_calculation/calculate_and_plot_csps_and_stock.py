from src.part1_transportation_model import calculate_registrations
from src.part2_survival_rates.calculate_empirical_survival_rates import calculate_empirical_survival_rates
from src.part3_stock_calculation.calculate_stock.compute_csp_values_and_compute_stock import compute_csp_values_and_compute_stock
from src.part2_survival_rates.plot_survival_rates import get_csp_plots
from src.part3_stock_calculation.plot_stock import plot_bev_stock_shares


def calculate_and_plot_csps_and_stock(data, inputs):
    """
     Calculate and plot CSP curves and BEV stock shares.

     This function processes input data and configurations to compute and plot the cumulative survival probability (CSP) curves,
     vehicle stock values by country, stock year, vehicle age and powertrain, and BEV stock shares.
     It also generates plots for CSP distributions and BEV stock shares over time.

     Steps:
     1. Compute vehicle registrations based on historical and projected data.
     2. Calculate empirical survival rates using stock and registration data.
     3. Compute CSP distribution curves and vehicle stock using survival rates and registrations.
     4. Plot CSP distributions (both for all countries and specific groups of countries).
     5. Plot BEV stock shares based on computed stock data.

     Args:
         data (dict): Dictionary containing input datasets, such as:
             - "historical_registrations" (pd.DataFrame): Historical vehicle registration data for EU countries.
             - "stock_by_age_2021" (pd.DataFrame): Vehicle stock data by age for 2021.
             - "registrations_eu_cam_scenario" (pd.DataFrame): EU projected vehicle registration scenario data.
             - "clusters" (pd.DataFrame): Clustering labels for countries based on shared characteristics.
             - "registration_shares_by_cluster" (pd.DataFrame): Registration shares for each cluster and powertrain.
             - "stock_year" (pd.DataFrame): Stock year information for each country.

         inputs (dict): Dictionary containing simulation parameters and plot configuration settings, such as:
             - "eu_countries_and_norway" (list): List of EU countries and Norway.
             - "csp_data_ref_year" (int): Reference year for CSP data (e.g., 2021).
             - "stock_years" (list[int]): List of years for which stock data is computed.
             - "historical_csp" (pd.DataFrame): Historical CSP data for validation.
             - "save_options_stock" (dict): Options for saving computed stock data.
             - "config_all" (dict): Configuration for plotting CSP distributions across all countries.
             - "config_group" (dict): Configuration for plotting CSP distributions for specific groups.
             - "config_bev_reference_scenario" (dict): Configuration for plotting BEV stock shares under the reference
             scenario.

     Returns:
         dict: A dictionary containing calculated outputs, including:
             - "registrations" (pd.DataFrame): Calculated vehicle registrations by year, powertrain and country.
             - "survival_rates_2021" (pd.DataFrame): Empirical survival rates for vehicles by country.
             - "stock_values" (pd.DataFrame): Calculated stock values over time by country, vehicle age and powertrain.
             - "stock_shares" (pd.DataFrame): Calculated stock shares over time.
             - "optimum_parameters_wg" (pd.DataFrame): Optimal parameters for Weibull-Gaussian curves.
             - "optimal_distribution_dict" (dict): Distribution of CSP values for countries.
             - "fitted_csp_values" (pd.DataFrame): Fitted CSP values for validation.

     Raises:
         KeyError: If required keys are missing in the `data` or `inputs` dictionaries.
         ValueError: If the provided data dimensions or formats are invalid.
     """
    registrations = calculate_registrations(data["historical_registrations"], inputs["eu_countries_and_norway"],
                                            data["registrations_eu_cam_scenario"], data["clusters"],
                                            data["registration_shares_by_cluster"], inputs["csp_data_ref_year"])

    survival_rates_2021 = calculate_empirical_survival_rates(data["stock_by_age_2021"],
                                                             data["historical_registrations"],
                                                             data["stock_year"])

    stock_values, stock_shares, optimum_parameters_wg, optimal_distribution_dict, fitted_csp_values = \
        compute_csp_values_and_compute_stock(survival_rates_2021, registrations, inputs["stock_years"],
                                             inputs["distribution_bounds"], inputs["historical_csp"],
                                             inputs["csp_available_years"], inputs["save_options_stock"], )

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