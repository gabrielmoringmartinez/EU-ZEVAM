# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

import pandas as pd


from zevampy.part2_survival_rates.calculate_country_fitted_values import calculate_country_fitted_values
from zevampy.load_data_and_prepare_inputs.dimension_names import country_dim, age_dim, distribution_dim, weibull_label, \
    weibull_gaussian_label


def get_fitted_csp_values(survival_rates, pdf_parameters, csp_available_years, output_path, survival_grouping,
                          save_options=False):
    """
    Calculates fitted Cumulative Survival Probability (CSP) values for each country using Weibull and
    Weibull-Gaussian (WG) distribution parameters.

    Parameters:
    - survival_rates (pd.DataFrame): DataFrame containing survival rates by country and vehicle age.
    - pdf_parameters (pd.DataFrame): Parameters of Weibull and WG distributions for each country.
    - save_options (bool): If `True`, saves the fitted CSP values to a CSV file.
    - csp_available_years (int): Number of years (vehicle ages) for which CSP values are calculated.
    - save_options (bool, optional): Bool defining if results should be saved or not


    Returns:
    - pd.DataFrame: DataFrame containing fitted CSP values for each country by vehicle age, distribution model (Weibull
     and Weibull Gaussian), and the selected distribution type.
    """
    survival_groups = survival_rates[survival_grouping].drop_duplicates()
    weibull_results = pd.DataFrame()
    wg_results = pd.DataFrame()
    for _, group in survival_groups.iterrows():
        mask = True
        for dim in survival_grouping:
            mask = mask & (survival_rates[dim] == group[dim])

        survival_rates_group = survival_rates.loc[mask].copy()

        weibull_results, wg_results = calculate_country_fitted_values(
            group,
            survival_rates_group,
            pdf_parameters,
            weibull_results,
            wg_results,
            csp_available_years,
            survival_grouping
        )

    fitted_csp_values = pd.merge(
        weibull_results,
        wg_results,
        on=survival_grouping + [age_dim],
        suffixes=(f" {weibull_label}", f" {weibull_gaussian_label}"),
        how="inner"
    )

    fitted_csp_values = pd.merge(
        fitted_csp_values,
        pdf_parameters[survival_grouping + [distribution_dim]],
        on=survival_grouping,
        how="left"
    )

    if save_options:
        fitted_csp_values.to_csv(
            f"{output_path}/2_3_fitted_CSP_curves.csv",
            sep=";",
            index=False,
            decimal=","
        )

    return fitted_csp_values

