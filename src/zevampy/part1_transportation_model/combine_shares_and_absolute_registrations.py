# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

import pandas as pd
from src.zevampy.load_data_and_prepare_inputs.dimension_names import country_dim, time_dim, cluster_dim, powertrain_dim, \
    relative_sales_dim, registrations_by_powertrain_dim, new_registrations_dim


def combine_shares_and_absolute_registrations(country_registrations, powertrain_share_registrations, clusters,
                                              use_clusters):
    """
        Combines the country-level vehicle registrations with the powertrain-specific share data, and calculates
        the registrations by powertrain for each country.
        If use_clusters=True, shares are matched by cluster.
        If use_clusters=False, shares are matched directly by country.

        Parameters:
        - country_registrations (pd.DataFrame): DataFrame containing the absolute registrations by country and year.
        - powertrain_share_registrations (pd.DataFrame): DataFrame containing the share of registrations for different
        powertrains for each cluster.
        - clusters (pd.DataFrame): DataFrame containing clusters assigned to each country.

        Returns:
        - pd.DataFrame: A DataFrame with the historical and projected registrations by powertrain
        for each country and year.
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
    # Sales by powertrain, vehicle size, year and country are obtained
    registrations[registrations_by_powertrain_dim] = (registrations[new_registrations_dim]
                                                      * registrations[relative_sales_dim])
    # Sales are saved and defined by scenario
    registrations = registrations.sort_values(by=[country_dim, time_dim, powertrain_dim])
    return registrations
