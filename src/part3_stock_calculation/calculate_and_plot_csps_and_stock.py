# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

from src.part1_transportation_model import calculate_registrations
from src.part2_survival_rates.calculate_empirical_survival_rates import calculate_empirical_survival_rates
from src.part3_stock_calculation.calculate_stock.compute_csp_values_and_compute_stock import \
    compute_csp_values_and_compute_stock
from src.part2_survival_rates.plot_survival_rates import get_csp_plots
from src.part3_stock_calculation.plot_stock import plot_bev_stock_shares

from src.load_data_and_prepare_inputs.dimension_names import *


def calculate_and_plot_csps_and_stock(data, inputs):
    """
     Calculate and plot CSP curves and BEV stock shares.

     This function processes input data and configurations to compute and plot the cumulative survival probability
     (CSP) curves, vehicle stock values by country, stock year, vehicle age and powertrain, and BEV stock shares.
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
             - "registration_shares_by_cluster" (pd.DataFrame): Registration shares for each cluster.
             - "stock_year" (pd.DataFrame): Stock year information for each country.

         inputs (dict): Dictionary containing simulation parameters and plot configuration settings, such as:
             - "eu_countries_and_norway" (list): List of EU countries and Norway.
             - "csp_data_ref_year" (int): Reference year for CSP data (e.g., 2021).
             - "stock_years" (list[int]): List of years for which stock data is computed.
             - historical_csp (str): File path or identifier for the historical CSP data used for validation.
             - "save_options_stock" (dict): Options for saving computed stock data.
             - "config_all" (dict): Configuration for plotting CSP distributions across all countries.
             - "config_group" (dict): Configuration for plotting CSP distributions for specific groups.
             - "config_bev_reference_scenario" (dict): Configuration for plotting BEV stock shares under the reference
             scenario.

     Returns:
         dict: A dictionary containing calculated outputs, including:
             - "registrations" (pd.DataFrame): Calculated vehicle registrations by year, powertrain and country.
             - "survival_rates_2021" (pd.DataFrame): 2021 empirical survival rates for vehicles by country.
             - "stock_values" (pd.DataFrame): Calculated stock values over time by country, vehicle age and powertrain.
             - "stock_shares" (pd.DataFrame): Calculated stock shares over time.
             - "optimum_parameters_wg" (pd.DataFrame): Optimized CSP parameters for each country, including
                distribution type.
             - "optimal_distribution_dict" (dict): Dictionary specifying the optimal distribution per country (Weibull
                or Weibull Gaussian).
             - "fitted_csp_values" (pd.DataFrame): Fitted CSP values for each country and vehicle age.
     Raises:
         KeyError: If required keys are missing in the `data` or `inputs` dictionaries.
         ValueError: If the provided data dimensions or formats are invalid.
     """
    registrations = calculate_registrations(data[historical_registrations_label], inputs[eu_countries_and_norway_label],
                                            data[registrations_eu_cam_scenario_label], data[clusters_label],
                                            data[registration_shares_by_cluster_label], inputs[csp_data_ref_year_label])

    survival_rates_2021 = calculate_empirical_survival_rates(data[stock_by_age_2021_label],
                                                             data[historical_registrations_label],
                                                             data[stock_year_label])

    stock_values, stock_shares, optimum_parameters_wg, optimal_distribution_dict, fitted_csp_values = \
        compute_csp_values_and_compute_stock(survival_rates_2021, registrations, inputs[simulation_stock_years_label],
                                             inputs[distribution_bounds_label], inputs[historical_csp_label],
                                             inputs[csp_available_years_label], inputs[save_options_stock_label],
                                             inputs[save_fitted_csp_values_label])

    get_csp_plots(survival_rates_2021, fitted_csp_values, inputs[config_all_label], inputs[config_group_label])
    plot_bev_stock_shares(stock_shares, inputs[config_bev_reference_scenario_label])

    return {
        registrations_label: registrations,
        survival_rates_2021_label: survival_rates_2021,
        stock_values_label: stock_values,
        stock_shares_label: stock_shares,
        optimum_parameters_wg_label: optimum_parameters_wg,
        optimal_distribution_dict_label: optimal_distribution_dict,
        fitted_csp_values_label: fitted_csp_values
    }
