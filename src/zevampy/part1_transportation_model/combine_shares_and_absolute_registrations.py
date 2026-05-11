"""Combine absolute registrations with powertrain registration shares."""

# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

import pandas as pd
from zevampy.load_data_and_prepare_inputs.dimension_names import country_dim, time_dim, cluster_dim, powertrain_dim, \
    relative_sales_dim, registrations_by_powertrain_dim, new_registrations_dim


def combine_shares_and_absolute_registrations(country_registrations, powertrain_share_registrations, clusters,
                                              use_clusters):
    """
    Combine absolute registrations with powertrain registration shares.

    The function assigns powertrain shares to country-level absolute registrations and calculates registrations by
    powertrain. If clustering is enabled, powertrain shares are matched through country clusters. If clustering is
    disabled, powertrain shares are matched directly by country.

    Parameters:
        country_registrations (pandas.DataFrame):
            DataFrame containing absolute vehicle registrations by country and year.

        powertrain_share_registrations (pandas.DataFrame):
            DataFrame containing powertrain registration shares by year and either cluster or country.

        clusters (pandas.DataFrame):
            DataFrame containing country-cluster assignments.

        use_clusters (bool):
            Whether powertrain shares should be matched by cluster instead of directly by country.

    Returns:
        pandas.DataFrame:
            DataFrame containing vehicle registrations by country, year, and powertrain.

    Raises:
        ValueError:
            If powertrain shares are missing for any required country, year, or powertrain combination.
    """
    if use_clusters:
        absolute_registrations = pd.merge(
            country_registrations,
            clusters[[country_dim, cluster_dim]],
            on=country_dim,
            how="left",
        )

        registrations = pd.merge(
            absolute_registrations,
            powertrain_share_registrations[
                [time_dim, cluster_dim, powertrain_dim, relative_sales_dim]
            ],
            on=[time_dim, cluster_dim],
            how="left",
        )
    else:
        registrations = pd.merge(
            country_registrations,
            powertrain_share_registrations[
                [time_dim, country_dim, powertrain_dim, relative_sales_dim]
            ],
            on=[time_dim, country_dim],
            how="left",
        )
    missing_share_rows = registrations[registrations[relative_sales_dim].isna()]

    if not missing_share_rows.empty:
        missing_keys = (
            missing_share_rows[[country_dim, time_dim]]
            .drop_duplicates()
            .sort_values([country_dim, time_dim])
        )

        raise ValueError(
            "Missing powertrain share registrations for some absolute registration rows.\n\n"
            f"use_clusters = {use_clusters}\n"
            f"Missing country/year combinations:\n"
            f"{missing_keys.to_string(index=False)}\n\n"
            "How to fix:\n"
            "- If use_clusters=True: make sure every selected country has a cluster assigned, "
            "and that the cluster has powertrain shares for all required years.\n"
            "- If use_clusters=False: provide country-specific powertrain shares for every selected "
            "country and year.\n"
        )
    expected_keys = registrations[
        [country_dim, time_dim]
    ].drop_duplicates()

    expected_powertrains = powertrain_share_registrations[
        [powertrain_dim]
    ].drop_duplicates()

    expected = expected_keys.merge(expected_powertrains, how="cross")

    actual = registrations[
        [country_dim, time_dim, powertrain_dim]
    ].drop_duplicates()

    missing_powertrain_rows = expected.merge(
        actual,
        on=[country_dim, time_dim, powertrain_dim],
        how="left",
        indicator=True,
    )

    missing_powertrain_rows = missing_powertrain_rows[
        missing_powertrain_rows["_merge"] == "left_only"
        ].drop(columns="_merge")

    if not missing_powertrain_rows.empty:
        raise ValueError(
            "Missing powertrain share registrations for some country/year/powertrain combinations.\n\n"
            f"use_clusters = {use_clusters}\n"
            f"Missing combinations:\n"
            f"{missing_powertrain_rows.to_string(index=False)}\n\n"
            "How to fix:\n"
            "- Add the missing powertrain share rows.\n"
            "- If use_clusters=True, check the cluster-level shares.\n"
            "- If use_clusters=False, check the country-level shares.\n"
        )
    # Sales by powertrain, vehicle size, year and country are obtained
    registrations[registrations_by_powertrain_dim] = (registrations[new_registrations_dim]
                                                      * registrations[relative_sales_dim])
    # Sales are saved and defined by scenario
    registrations = registrations.sort_values(by=[country_dim, time_dim, powertrain_dim])
    return registrations
