"""Run differential-evolution optimization for CSP distribution fitting (Weibull)."""

# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

from scipy.optimize import differential_evolution
import numpy as np
import pandas as pd

from zevampy.part2_survival_rates.loss_functions import loss_function_weibull, loss_function_weibull_and_normal


from zevampy.load_data_and_prepare_inputs.dimension_names import *


def run_diff_evol_algorithm_weibull(bounds: list, survival_groups: np.ndarray, survival_rates, survival_grouping):
    """
    Fit Weibull distribution parameters using differential evolution.

    The function optimizes Weibull gamma and beta parameters for each survival-rate group and returns the fitted
    parameters together with the corresponding R-squared values.

    Parameters:
        bounds (list):
            Bounds for the Weibull parameters.

        survival_groups (pandas.DataFrame):
            Unique survival-rate groups used for parameter fitting.

        survival_rates (pandas.DataFrame):
            DataFrame containing empirical survival-rate values.

        survival_grouping (list[str]):
            Column names defining the survival-rate grouping.

    Returns:
        pandas.DataFrame:
            DataFrame containing optimized Weibull parameters and R-squared values for each survival-rate group.
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


"""
Run differential-evolution optimization for CSP distribution fitting. (Weibull-Gaussian)
"""


def run_diff_evol_algorithm_weibull_gaussian(bounds, survival_groups, survival_rates, optimum_parameters_weibull,
                                             survival_grouping):
    """
    Fit Weibull-Gaussian distribution parameters using differential evolution.

    The function uses previously optimized Weibull parameters and optimizes
    the Gaussian component for each survival-rate group.

    Parameters:
        bounds (list):
            Bounds for the Gaussian parameters.

        survival_groups (pandas.DataFrame):
            Unique survival-rate groups used for parameter fitting.

        survival_rates (pandas.DataFrame):
            DataFrame containing empirical survival-rate values.

        optimum_parameters_weibull (pandas.DataFrame):
            DataFrame containing previously optimized Weibull parameters.

        survival_grouping (list[str]):
            Column names defining the survival-rate grouping.

    Returns:
        pandas.DataFrame:
            DataFrame containing optimized Weibull and Weibull-Gaussian
            parameters and R-squared values for each survival-rate group.
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



