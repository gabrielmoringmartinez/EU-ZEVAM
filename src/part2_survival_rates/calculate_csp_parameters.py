# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

from src.part2_survival_rates.run_diff_evol_algorithm import run_diff_evol_algorithm_weibull, \
    run_diff_evol_algorithm_weibull_gaussian
from src.part2_survival_rates.select_optimal_type_of_distribution import select_optimal_type_of_distribution

from src.load_data_and_prepare_inputs.dimension_names import *


def calculate_csp_parameters(survival_rates, bounds, save_options=False):
    """
    Optimizes CSP (Cumulative Survival Probability) parameters for country-specific survival curves
    using Weibull and Weibull-Gaussian (WG) distributions. The bounds for optimization are based on
    Held (2021) and can be found specifically in the Appendix F.

    This function performs the following steps:
    1. Optimize Weibull distribution parameters for each country using a differential evolution algorithm.
    2. Optimize Weibull-Gaussian distribution parameters using initial Weibull parameters.
    3. Select the optimal distribution type (Weibull or WG) for each country.
    4. Save the optimized parameters and distribution types to a CSV file.
    5. Return the optimized parameters and a dictionary mapping countries to their selected distribution types.

    Parameters:
        - survival_rates (DataFrame): Contains survival rate data by country with columns including country and
        survival rates.
        - bounds (dict): Dictionary defining optimization parameter bounds for 'weibull' and 'gaussian' distributions.
        - save_options (bool, optional): Bool defining if results should be saved or not

    Returns:
        tuple:
            - DataFrame: Optimized CSP parameters for each country, including distribution type.
            - dict: Dictionary where keys are distribution types ('Weibull' or 'WG') and values
                    are lists of countries categorized by their optimal distribution type.
    """
    # Extract bounds for Weibull and Gaussian distributions
    bounds_weibull = bounds[weibull_label]
    bounds_gaussian = bounds[weibull_gaussian_label]
    bounds_gaussian = [bounds_gaussian[k_weibull_gaussian_dim], bounds_gaussian[mu_weibull_gaussian_dim],
                       bounds_gaussian[sigma_weibull_gaussian_dim]]
    # Get the unique country names from the survival rates
    country_names = survival_rates[country_dim].unique()
    # Run the differential evolution algorithm to optimize the Weibull parameters for each country
    optimum_parameters_weibull = run_diff_evol_algorithm_weibull(bounds_weibull, country_names, survival_rates)
    # Run the differential evolution algorithm to optimize the Weibull-Gaussian parameters for each country
    optimum_parameters_weibull_gaussian = run_diff_evol_algorithm_weibull_gaussian(bounds_gaussian, country_names,
                                                                                   survival_rates,
                                                                                   optimum_parameters_weibull)
    # Select the optimal distribution type (Weibull or WG) based on the fitted parameters
    optimum_parameters_weibull_gaussian = select_optimal_type_of_distribution(optimum_parameters_weibull_gaussian)
    # Save the optimized parameters and distribution types to a CSV file
    if save_options:
        optimum_parameters_weibull_gaussian.to_csv(f'outputs/2_1_optimum_parameters_csp_curves.csv', sep=';',
                                                   index=False, decimal=',')
    # Create a dictionary mapping each distribution type to a list of countries
    country_opt_dist_dict = {dist: optimum_parameters_weibull_gaussian.loc[optimum_parameters_weibull_gaussian
                                                                           [distribution_dim] == dist, country_dim].tolist()
                             for dist in optimum_parameters_weibull_gaussian[distribution_dim].unique()}
    return optimum_parameters_weibull_gaussian, country_opt_dist_dict
