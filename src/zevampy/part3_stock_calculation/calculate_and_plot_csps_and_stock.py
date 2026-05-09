# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

from src.zevampy.part1_transportation_model import calculate_registrations
from src.zevampy.part2_survival_rates.calculate_empirical_survival_rates import calculate_empirical_survival_rates
from src.zevampy.part3_stock_calculation.calculate_stock.compute_csp_values_and_compute_stock import \
    compute_csp_values_and_compute_stock
from src.zevampy.part2_survival_rates.plot_survival_rates import get_csp_plots
from src.zevampy.part3_stock_calculation.plot_stock import plot_stock_shares

from src.zevampy.load_data_and_prepare_inputs.dimension_names import *
import warnings


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
             - "stock_by_age" (pd.DataFrame): Vehicle stock data by age for 2021.
             - "registrations_projected" (pd.DataFrame): EU projected vehicle registration scenario data.
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
             - "empirical_survival_rates_label" (pd.DataFrame): 2021 empirical survival rates for vehicles by country.
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
    registrations = calculate_registrations(data[historical_registrations_label], inputs[countries_selected_label],
                                            data[registrations_projected_label], data[clusters_label],
                                            data[registration_shares_by_cluster_label], inputs[csp_data_ref_year_label],
                                            inputs[simulation_stock_years_label],
                                            inputs[initial_registration_year_label], inputs[use_clusters_label],
                                            inputs[output_path_label])
    registrations_for_survival = registrations.copy()

    if powertrain_dim in inputs[survival_grouping_label]:
        registrations_for_survival = (
            registrations
            .drop(columns=[new_registrations_dim])
            .rename(columns={registrations_by_powertrain_dim: new_registrations_dim})
        )
    else:
        registrations_for_survival = (
            registrations_for_survival
            .groupby([country_dim, time_dim], as_index=False)[registrations_by_powertrain_dim]
            .sum()
            .rename(columns={registrations_by_powertrain_dim: new_registrations_dim})
        )
    empirical_survival_rates = calculate_empirical_survival_rates(data[stock_by_age_label], registrations_for_survival,
                                                                  data[stock_year_label],
                                                                  inputs[countries_selected_label],
                                                                  inputs[output_path_label],
                                                                  inputs[survival_grouping_label])
    registration_powertrains = set(registrations[powertrain_dim].dropna().unique())

    survival_powertrains = (
        set(empirical_survival_rates[powertrain_dim].dropna().unique())
        if powertrain_dim in empirical_survival_rates.columns
        else registration_powertrains
    )

    missing_survival_powertrains = registration_powertrains - survival_powertrains
    stock_shares_are_valid = not missing_survival_powertrains

    empirical_survival_rates = empirical_survival_rates[empirical_survival_rates[age_dim] <=
                                                        inputs[csp_available_years_label]].copy()
    stock_values, stock_shares, optimum_parameters_wg, optimal_distribution_dict, fitted_csp_values = \
        compute_csp_values_and_compute_stock(empirical_survival_rates, registrations,
                                             inputs[simulation_stock_years_label],
                                             inputs[distribution_bounds_label], inputs[historical_csp_label],
                                             inputs[csp_available_years_label], inputs[countries_selected_label],
                                             inputs[survival_grouping_label], inputs[output_path_label],
                                             stock_shares_are_valid, inputs[save_options_stock_label],
                                             inputs[save_fitted_csp_values_label],
                                             )
    get_csp_plots(empirical_survival_rates, fitted_csp_values, inputs[config_all_label], inputs[config_group_label],
                  inputs[survival_grouping_label])
    if not stock_shares_are_valid:
        warnings.warn(
            "Stock shares will not be plotted because not all registration powertrains "
            "have corresponding survival rates.\n\n"
            f"Missing survival rates for: {sorted(missing_survival_powertrains)}\n\n"
            "Absolute stock can still be calculated for available powertrains, but stock "
            "shares would be misleading because the denominator would not include all "
            "powertrain categories.",
            UserWarning
        )
    else:
        plot_stock_shares(
            stock_shares,
            inputs[config_bev_reference_scenario_label],
            inputs[powertrain_dim]
        )

    return {
        registrations_label: registrations,
        empirical_survival_rates_label: empirical_survival_rates,
        stock_values_label: stock_values,
        stock_shares_label: stock_shares,
        optimum_parameters_wg_label: optimum_parameters_wg,
        optimal_distribution_dict_label: optimal_distribution_dict,
        fitted_csp_values_label: fitted_csp_values
    }