# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

from src.zevampy.load_data_and_prepare_inputs.load_data import load_data
from src.zevampy.load_data_and_prepare_inputs.prepare_inputs import prepare_inputs


def load_data_and_prepare_inputs(input_path, config=None):
    """
    Combines the functionality of loading data and preparing inputs for the simulation and plot configurations.

    This function calls two sub-functions:
    1. `load_data`: Loads all required datasets from CSV files.
    2. `prepare_inputs`: Prepares and organizes simulation-related parameters and plot configurations.


    Parameters:
        input_dir (str): Path to the directory containing input CSV files.

    Returns:
        tuple:
            - `data` (dict): A dictionary containing loaded datasets with their names as keys.
            - `inputs` (dict): A dictionary containing simulation parameters and plot configurations.
    """
    model_config = config.get("model", {}) if config else {}
    geography_config = config.get("geography", {}) if config else {}

    historical_csp_active = model_config.get("historical_csp", False)
    historical_validation_active = model_config.get("historical_validation", True)
    sensitivity_analysis_active = model_config.get("sensitivity_analysis", True)
    use_clusters_active = geography_config.get("use_clusters", True)

    data, max_year = load_data(
        input_path,
        historical_validation_active=historical_validation_active,
        sensitivity_analysis_active=sensitivity_analysis_active,
        historical_csp_active=historical_csp_active,
        use_clusters_active=use_clusters_active,
    )
    inputs = prepare_inputs(max_year, config=config)
    return data, inputs
