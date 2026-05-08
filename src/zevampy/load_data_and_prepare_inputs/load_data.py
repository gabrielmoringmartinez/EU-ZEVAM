# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

import pandas as pd
import warnings
from pathlib import Path

from src.zevampy.load_data_and_prepare_inputs.dimension_names import *


def load_data(input_dir, historical_validation_active=True, sensitivity_analysis_active=True,
              historical_csp_active=True, use_clusters_active=True, powertrains=None, survival_grouping=None):
    """
    Loads datasets required for modeling European BEV stock shares and performing CSP-based simulations.

    This function reads data from several CSV files stored in the `inputs` folder. The datasets include cluster groups,
    historical and projected vehicle registrations, survival rates, and other related parameters. If additional files
    should be loaded, it can be added a new csv file with data, and define in the dictionary a label for this data.

    Parameters:
        input_dir (str): Path to the directory containing input CSV files.

    Returns:
        tuple:
            - dict: A dictionary containing all loaded datasets, where:
                - Keys are descriptive dataset names (e.g., 'clusters', 'historical_registrations').
                - Values are pandas DataFrames containing the loaded data.
            - int: The maximum year found in the 'registrations_projected' dataset.
    """
    input_dir = Path(input_dir)
    # --- Check folder exists ---
    if not input_dir.exists():
        raise FileNotFoundError(
            f"Input directory '{input_dir}' does not exist.\n\n"
            "Fix this by:\n"
            "1) Updating 'input_path' in config.yaml (under 'data')\n"
            "2) Or passing a valid path via the CLI (--input-path)\n"
        )

    # --- Required files ---
    required_model_files = [
        "1_1_new_registrations_by_fuel_type_1970_2050_clusters.csv",
        "1_2_A_2_new_registrations_data_passenger_cars_eu_countries_1970_2021.csv",
        "1_3_new_registrations_2022_2050_projected.csv",
        "2_1_A_1_age_resolved_data_passenger_car_stock_fleet_eu_countries_2021.csv",
        "2_2_A_1_stock_year.csv",
    ]

    cluster_file = "0_country_clusters.csv"

    required_validation_files = [
        "4_1_eafo_ev_new_registration_shares.csv",
        "4_2_eafo_ev_stock_shares.csv",
    ]

    required_historical_csp_files = [
        "5_1_oguchi_2008_survival_rate_parameters.csv",
        "5_2_held_2016_survival_rates.csv",
    ]

    # --- Check files ---
    check_required_files(input_dir, required_model_files, "running the model")

    if historical_validation_active:
        check_required_files(
            input_dir,
            required_validation_files,
            "validation against historical data"
        )

    if sensitivity_analysis_active and historical_csp_active:
        check_required_files(
            input_dir,
            required_historical_csp_files,
            "historical CSP sensitivity analysis"
        )

    if use_clusters_active:
        check_required_files(input_dir, [cluster_file], "country clustering")
    if not use_clusters_active and (input_dir / cluster_file).exists():
        warnings.warn(
            f"'{cluster_file}' was found in '{input_dir}' but will not be used "
            "because 'use_clusters' is set to False.",
            UserWarning
        )

    # --- Load always-needed data ---
    if use_clusters_active:
        clusters = pd.read_csv(input_dir / cluster_file, sep=";", decimal=",")
    else:
        clusters = None
    registration_shares_by_cluster = pd.read_csv(
        input_dir / "1_1_new_registrations_by_fuel_type_1970_2050_clusters.csv",
        sep=";", decimal=","
    )
    if powertrains:
        validate_powertrains_in_data(
            registration_shares_by_cluster,
            powertrains,
            "registration shares by cluster"
        )

        registration_shares_by_cluster = add_rest_of_powertrains_from_selected_shares(
            registration_shares_by_cluster,
            powertrains,
            relative_sales_dim,
            "registration shares by cluster",
        )
    historical_registrations = pd.read_csv(
        input_dir / "1_2_A_2_new_registrations_data_passenger_cars_eu_countries_1970_2021.csv",
        sep=";", decimal=","
    )
    registrations_projected = pd.read_csv(
        input_dir / "1_3_new_registrations_2022_2050_projected.csv",
        sep=";", decimal=","
    )

    max_year = registrations_projected["time"].max()

    stock_by_age_2021 = pd.read_csv(
        input_dir / "2_1_A_1_age_resolved_data_passenger_car_stock_fleet_eu_countries_2021.csv",
        sep=";", decimal=","
    )

    if survival_grouping is None:
        survival_grouping = [country_dim]

    if survival_grouping == [country_dim] and powertrain_dim in stock_by_age_2021.columns:
        raise ValueError(
            "Invalid stock-by-age input data.\n\n"
            "The current configuration estimates survival rates only by country:\n"
            "survival_rates:\n"
            "  grouping:\n"
            "    - geo country\n\n"
            "However, the stock-by-age input file contains a 'powertrain' column.\n\n"
            "How to fix:\n"
            "- Remove the 'powertrain' column from the stock-by-age input file, and\n"
            "- provide total stock by country and vehicle age only:\n"
            "  geo country;vehicle age;number of registered vehicles\n\n"
            "If you want country- and powertrain-specific survival rates, use:\n"
            "survival_rates:\n"
            "  grouping:\n"
            "    - geo country\n"
            "    - powertrain"
        )

    required_stock_columns = set(
        survival_grouping + [age_dim, number_registered_vehicles_dim]
    )

    missing_columns = required_stock_columns - set(stock_by_age_2021.columns)

    if missing_columns:
        raise ValueError(
            "Invalid stock-by-age input data.\n\n"
            "The current configuration requires survival rates to be estimated by:\n"
            f"{survival_grouping}\n\n"
            "However, the stock-by-age input file does not contain all required columns.\n\n"
            f"Missing columns in 2_1 stock-by-age input file: {sorted(missing_columns)}\n\n"
            "How to fix:\n"
            "- If you want country-level survival rates only, use:\n"
            "  survival_rates:\n"
            "    grouping:\n"
            "      - geo country\n\n"
            "- If you want survival rates by country and powertrain, the 2_1 input file must contain:\n"
            "  geo country;vehicle age;powertrain;number of registered vehicles\n\n"
            "- If you later add vehicle size to the grouping, the 2_1 input file must also contain "
            "a corresponding vehicle size column."
        )

    if powertrains and survival_grouping and powertrain_dim in survival_grouping:
        stock_by_age_2021 = aggregate_stock_by_selected_powertrains(
            stock_by_age_2021,
            powertrains,
            "stock by age"
        )

    if powertrain_dim in survival_grouping:
        registration_powertrains = set(
            registration_shares_by_cluster[powertrain_dim].dropna().unique()
        )
        stock_powertrains = set(
            stock_by_age_2021[powertrain_dim].dropna().unique()
        )

        missing_stock_powertrains = registration_powertrains - stock_powertrains

        if missing_stock_powertrains:
            warnings.warn(
                "Some powertrain categories exist in the registration shares but not in the "
                "stock-by-age input data.\n\n"
                f"Missing from stock-by-age data: {sorted(missing_stock_powertrains)}\n\n"
                "Survival rates cannot be estimated for these categories, so stock will not "
                "be calculated for them. Total stock by country may therefore be incomplete.",
                UserWarning
            )

    if survival_grouping is None:
        survival_grouping = [country_dim]

    required_stock_columns = set(
        survival_grouping + [age_dim, number_registered_vehicles_dim]
    )

    missing_columns = required_stock_columns - set(stock_by_age_2021.columns)

    if missing_columns:
        raise ValueError(
            "Invalid stock-by-age input data.\n\n"
            f"Missing columns: {sorted(missing_columns)}\n\n"

            f"Survival rates are configured to be estimated by: {survival_grouping}\n"
            "However, the input data does not contain all required dimensions.\n\n"

            "Note:\n"
            "- Country-level survival rates can always be estimated.\n"
            "- Additional detail (e.g. powertrain) requires disaggregated stock-by-age data.\n\n"

            "How to fix:\n"
            f"- Remove {sorted(missing_columns)} from the survival grouping in config.yaml\n"
            "  OR\n"
            f"- Provide stock-by-age data including: {sorted(required_stock_columns)}\n"
        )

    stock_year = pd.read_csv(
        input_dir / "2_2_A_1_stock_year.csv",
        sep=";", decimal=","
    )

    data = {
        "clusters": clusters,
        "registration_shares_by_cluster": registration_shares_by_cluster,
        "historical_registrations": historical_registrations,
        "registrations_projected": registrations_projected,
        "stock_by_age_2021": stock_by_age_2021,
        "stock_year": stock_year,
    }

    # --- Optional: validation data ---
    if historical_validation_active:
        data["actual_bev_registration_shares"] = pd.read_csv(
            input_dir / "4_1_eafo_ev_new_registration_shares.csv",
            sep=";", decimal=","
        )
        data["actual_bev_stock_shares"] = pd.read_csv(
            input_dir / "4_2_eafo_ev_stock_shares.csv",
            sep=";", decimal=","
        )

    # --- Optional: sensitivity data ---
    if sensitivity_analysis_active and historical_csp_active:
        data["optimum_parameters_2008"] = pd.read_csv(
            input_dir / "5_1_oguchi_2008_survival_rate_parameters.csv",
            sep=";", decimal=","
        )
        data["survival_rates_2016"] = pd.read_csv(
            input_dir / "5_2_held_2016_survival_rates.csv",
            sep=";", decimal=","
        )

    return data, max_year


def check_required_files(input_dir, files, purpose):
    missing = [file for file in files if not (input_dir / file).exists()]

    if missing:
        raise FileNotFoundError(
            f"Missing input files for {purpose} in '{input_dir}':\n\n"
            + "\n".join(f"- {file}" for file in missing)
            + "\n\nCheck that the files exist and that their names are spelled correctly."
        )


def validate_powertrains_in_data(df, selected_powertrains, dataset_name):
    available_powertrains = set(df[powertrain_dim].dropna().unique())
    selected_powertrains = set(selected_powertrains)

    missing_powertrains = selected_powertrains - available_powertrains

    if missing_powertrains:
        raise ValueError(
            f"Invalid powertrain configuration for {dataset_name}.\n\n"
            f"Selected powertrains not found in input data: {sorted(missing_powertrains)}\n"
            f"Available powertrains are: {sorted(available_powertrains)}"
        )

    unused_powertrains = available_powertrains - selected_powertrains

    if unused_powertrains:
        warnings.warn(
            f"The following powertrains exist in {dataset_name} but are not selected "
            f"and will be ignored: {sorted(unused_powertrains)}",
            UserWarning
        )


REST_POWERTRAIN = "Rest of powertrains"
SHARE_TOLERANCE = 1e-3


def add_rest_of_powertrains_from_selected_shares(
    df,
    selected_powertrains,
    share_column,
    dataset_name,
):
    df = df.copy()
    selected_powertrains = list(selected_powertrains)

    available_powertrains = set(df[powertrain_dim].dropna().unique())
    missing_powertrains = set(selected_powertrains) - available_powertrains

    if missing_powertrains:
        raise ValueError(
            f"Invalid powertrain configuration for {dataset_name}.\n\n"
            f"Selected powertrains not found in input data: {sorted(missing_powertrains)}\n"
            f"Available powertrains are: {sorted(available_powertrains)}"
        )

    selected_df = df[df[powertrain_dim].isin(selected_powertrains)].copy()

    group_cols = [
        col for col in selected_df.columns
        if col not in [powertrain_dim, share_column]
    ]

    selected_sum = (
        selected_df
        .groupby(group_cols, as_index=False)[share_column]
        .sum()
        .rename(columns={share_column: "_selected_share_sum"})
    )

    rest_df = selected_sum.copy()
    rest_df[powertrain_dim] = REST_POWERTRAIN
    rest_df[share_column] = 1 - rest_df["_selected_share_sum"]

    if (rest_df[share_column] < -SHARE_TOLERANCE).any():
        raise ValueError(
            f"Invalid shares in {dataset_name}.\n\n"
            "Selected powertrain shares exceed 1 for at least one group."
        )

    rest_df[share_column] = rest_df[share_column].clip(lower=0)
    rest_df = rest_df[group_cols + [powertrain_dim, share_column]]

    result = pd.concat([selected_df, rest_df], ignore_index=True)

    return result


def aggregate_stock_by_selected_powertrains(df, selected_powertrains, dataset_name):
    df = df.copy()
    selected_powertrains = list(selected_powertrains)

    available_powertrains = set(df[powertrain_dim].dropna().unique())
    missing_powertrains = set(selected_powertrains) - available_powertrains

    if missing_powertrains:
        raise ValueError(
            f"Invalid powertrain configuration for {dataset_name}.\n\n"
            f"Selected powertrains not found in input data: {sorted(missing_powertrains)}\n"
            f"Available powertrains are: {sorted(available_powertrains)}"
        )

    df[powertrain_dim] = df[powertrain_dim].where(
        df[powertrain_dim].isin(selected_powertrains),
        REST_POWERTRAIN
    )

    group_cols = [
        col for col in df.columns
        if col != number_registered_vehicles_dim
    ]

    return (
        df.groupby(group_cols, as_index=False)[number_registered_vehicles_dim]
        .sum()
    )