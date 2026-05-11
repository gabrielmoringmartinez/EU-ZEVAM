"""Calculate fitted CSP values for Weibull and Weibull-Gaussian models."""

# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT


from zevampy.part2_survival_rates.get_function_values import get_weibull_function, get_weibull_and_normal_function
from zevampy.part2_survival_rates.get_distribution_function_discrete_points import get_distribution_function_discrete_points

from zevampy.load_data_and_prepare_inputs.dimension_names import gamma_weibull_dim, beta_weibull_dim, \
    k_weibull_gaussian_dim, mu_weibull_gaussian_dim, sigma_weibull_gaussian_dim


def calculate_country_fitted_values(group, survival_rates, pdf_parameters, weibull_results, wg_results,
                                    csp_available_years, survival_grouping):
    """
    Calculate fitted CSP values for a survival-rate group.

    The function retrieves fitted distribution parameters for the selected survival group, calculates Weibull and
    Weibull-Gaussian CSP values, and appends the resulting discrete CSP curves to the corresponding result DataFrames.

    Parameters:
        group (dict or pandas.Series):
            Survival-group identifier containing grouping dimensions such as country or powertrain.

        survival_rates (pandas.DataFrame):
            DataFrame containing empirical survival-rate data.

        pdf_parameters (pandas.DataFrame):
            DataFrame containing fitted distribution parameters.

        weibull_results (pandas.DataFrame):
            DataFrame used to store fitted Weibull CSP values.

        wg_results (pandas.DataFrame):
            DataFrame used to store fitted Weibull-Gaussian CSP values.

        csp_available_years (int):
            Number of years for which CSP values are calculated.

        survival_grouping (list[str]):
            List of dimensions defining the survival-rate grouping.

    Returns:
        tuple:
            - pandas.DataFrame:
                Updated Weibull CSP results.

            - pandas.DataFrame:
                Updated Weibull-Gaussian CSP results.

    Raises:
        ValueError:
            If no fitted CSP parameters are found for the selected survival group.
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