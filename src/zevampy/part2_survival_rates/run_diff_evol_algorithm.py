# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

from scipy.optimize import differential_evolution
import numpy as np
import pandas as pd

from src.zevampy.part2_survival_rates.loss_functions import loss_function_weibull, loss_function_weibull_and_normal
from src.zevampy.part2_survival_rates.append_optimum_parameters import append_optimum_parameters_weibull, \
    append_optimum_parameters_gaussian
from src.zevampy.part2_survival_rates.save_optimum_parameters import save_optimum_parameters_weibull, \
    save_optimum_parameters_gaussian
from src.zevampy.part2_survival_rates.get_value_countries import get_value_countries


from src.zevampy.load_data_and_prepare_inputs.dimension_names import *


def run_diff_evol_algorithm_weibull(bounds: list, survival_groups: np.ndarray, survival_rates, survival_grouping):
    """
    Runs the differential evolution optimization algorithm to fit Weibull distribution parameters (gamma and beta)

    Parameters:
        bounds (list): Bounds for the Weibull distribution parameters [gamma, beta]. Each element of the list
                       represents the range for a parameter: [(gamma_min, gamma_max), (beta_min, beta_max)].
        country_names_number (np.ndarray): Array of unique country labels
        survival_rates (pd.DataFrame): DataFrame containing survival rates for each country.

    Returns:
        pd.DataFrame: Optimized Weibull parameters for each country, including:
            - gamma: Scale parameter of the Weibull distribution.
            - beta: Shape parameter of the Weibull distribution.
            - r-squared: Measure of fit quality for the model.
            - country labels: The corresponding country identifier for the parameters.
        """
    optimum_gamma= []
    optimum_beta = []
    max_rsquared = []
    group_records = []

    for _, group in survival_groups.iterrows():
        mask = True
        for dim in survival_grouping:
            mask = mask & (survival_rates[dim] == group[dim])

        survival_rates_group = survival_rates.loc[mask, survival_rate_dim].to_numpy()

        result = differential_evolution(
            loss_function_weibull,
            bounds,
            args=(survival_rates_group,)
        )

        optimum_gamma.append(result.x[0])
        optimum_beta.append(result.x[1])
        max_rsquared.append(1 - result.fun)
        group_records.append(group.to_dict())

    result_df = pd.DataFrame(group_records)
    result_df[gamma_weibull_dim] = optimum_gamma
    result_df[beta_weibull_dim] = optimum_beta
    result_df[r_squared_weibull_dim] = max_rsquared

    return result_df


def run_diff_evol_algorithm_weibull_gaussian(bounds, survival_groups, survival_rates, optimum_parameters_weibull,
                                             survival_grouping):
    """
    Runs the differential evolution optimization algorithm to fit Weibull-Gaussian parameters (k, mu, sigma, delta)
    for each country. This builds upon the already optimized Weibull parameters.

    Parameters:
        bounds (list): Bounds for the Gaussian distribution parameters:
                      [(k_min, k_max), (mu_min, mu_max), (sigma_min, sigma_max)].
        country_names_number (np.ndarray): Array of unique country labels
        survival_rates (pd.DataFrame): DataFrame containing survival rates for each country.
        optimum_parameters_weibull (pd.DataFrame): DataFrame containing the optimized Weibull parameters
                                                   (gamma and beta) for each country.

    Returns:
        pd.DataFrame: Combined DataFrame containing:
            - Weibull parameters (gamma, beta).
            - Optimized Weibull-Gaussian parameters (k, mu, sigma, delta).
            - r-squared: Measure of fit quality for the Weibull-Gaussian model.
            - Country labels: Identifier for the parameters.
    """
    optimum_k = []
    optimum_mu = []
    optimum_sigma = []
    optimum_delta = []
    max_rsquared = []
    group_records = []

    for _, group in survival_groups.iterrows():
        mask = True
        for dim in survival_grouping:
            mask = mask & (survival_rates[dim] == group[dim])

        survival_rates_group = survival_rates.loc[mask, survival_rate_dim].to_numpy()

        param_mask = True
        for dim in survival_grouping:
            param_mask = param_mask & (optimum_parameters_weibull[dim] == group[dim])

        optimum_parameters_weibull_group = optimum_parameters_weibull.loc[param_mask]

        gamma_group = float(optimum_parameters_weibull_group[gamma_weibull_dim].iloc[0])
        beta_group = float(optimum_parameters_weibull_group[beta_weibull_dim].iloc[0])

        result = differential_evolution(
            loss_function_weibull_and_normal,
            bounds,
            args=(gamma_group, beta_group, survival_rates_group)
        )

        optimum_k.append(result.x[0])
        optimum_mu.append(result.x[1])
        optimum_sigma.append(result.x[2])
        optimum_delta.append(
            result.x[0] / (np.sqrt(np.pi * 2) * result.x[2])
        )
        max_rsquared.append(1 - result.fun)
        group_records.append(group.to_dict())

    result_df = pd.DataFrame(group_records)

    result_df[gamma_weibull_dim] = optimum_parameters_weibull[gamma_weibull_dim].values
    result_df[beta_weibull_dim] = optimum_parameters_weibull[beta_weibull_dim].values
    result_df[r_squared_weibull_dim] = optimum_parameters_weibull[r_squared_weibull_dim].values
    result_df[k_weibull_gaussian_dim] = optimum_k
    result_df[mu_weibull_gaussian_dim] = optimum_mu
    result_df[sigma_weibull_gaussian_dim] = optimum_sigma
    result_df[delta_weibull_gaussian_dim] = optimum_delta
    result_df[r_squared_weibull_gaussian_dim] = max_rsquared
    return result_df



