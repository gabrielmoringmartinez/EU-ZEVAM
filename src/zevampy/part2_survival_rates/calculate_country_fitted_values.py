# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

from src.zevampy.part2_survival_rates.get_statistical_parameters import get_statistical_parameters
from src.zevampy.part2_survival_rates.get_statistical_parameters_of_each_country import \
    get_statistical_parameters_of_each_country
from src.zevampy.part2_survival_rates.get_function_values import get_weibull_function, get_weibull_and_normal_function
from src.zevampy.part2_survival_rates.get_distribution_function_discrete_points import get_distribution_function_discrete_points

from src.zevampy.load_data_and_prepare_inputs.dimension_names import gamma_weibull_dim, beta_weibull_dim, \
    k_weibull_gaussian_dim, mu_weibull_gaussian_dim, sigma_weibull_gaussian_dim


def calculate_country_fitted_values(group, survival_rates, pdf_parameters, weibull_results, wg_results,
                                    csp_available_years, survival_grouping):
    """
    Helper function to calculate Weibull and Weibull-Gaussian fitted CSP values for a single country.

    Parameters:
    - country_name (str): Name of the country to calculate fitted values for.
    - survival_rates (pd.DataFrame): DataFrame with survival rates.
    - pdf_parameters (pd.DataFrame): DataFrame with distribution parameters.
    - weibull_results (pd.DataFrame): DataFrame to store Weibull CSP results.
    - wg_results (pd.DataFrame): DataFrame to store WG CSP results.
    - csp_available_years (int): Number of years (vehicle ages) for which CSP values are calculated.

    Returns:
    - tuple:
        - pd.DataFrame: Updated `weibull_results` with calculated Weibull CSP values.
        - pd.DataFrame: Updated `wg_results` with calculated WG CSP values.
    """
    parameter_mask = True
    for dim in survival_grouping:
        parameter_mask = parameter_mask & (pdf_parameters[dim] == group[dim])

    pdf_parameters_group = pdf_parameters.loc[parameter_mask]

    if pdf_parameters_group.empty:
        raise ValueError(
            "No fitted CSP parameters found for survival group:\n"
            f"{group.to_dict()}"
        )

    gamma_group = float(pdf_parameters_group[gamma_weibull_dim].iloc[0])
    beta_group = float(pdf_parameters_group[beta_weibull_dim].iloc[0])
    k_group = float(pdf_parameters_group[k_weibull_gaussian_dim].iloc[0])
    mu_group = float(pdf_parameters_group[mu_weibull_gaussian_dim].iloc[0])
    sigma_group = float(pdf_parameters_group[sigma_weibull_gaussian_dim].iloc[0])

    predicted_weibull_value = get_weibull_function(
        gamma_group,
        beta_group,
        csp_available_years,
    )

    predicted_weibull_and_normal_value = get_weibull_and_normal_function(
        gamma_group,
        beta_group,
        k_group,
        mu_group,
        sigma_group,
        csp_available_years,
    )

    weibull_results = get_distribution_function_discrete_points(
        weibull_results,
        survival_rates,
        predicted_weibull_value,
    )

    wg_results = get_distribution_function_discrete_points(
        wg_results,
        survival_rates,
        predicted_weibull_and_normal_value,
    )

    return weibull_results, wg_results