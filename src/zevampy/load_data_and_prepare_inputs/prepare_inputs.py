# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

from src.zevampy.part1_transportation_model.input_data import eu_countries_and_norway, default_use_clusters
from src.zevampy.part2_survival_rates.input_data import distribution_bounds
from src.zevampy.part3_stock_calculation.calculate_stock.input_data import initial_simulation_stock_year, historical_csp, \
    save_options_stock, csp_data_ref_year, csp_available_years, save_fitted_csp_values, initial_registration_year
from src.zevampy.part2_survival_rates.plot_survival_rates.graph_inputs import config_all, config_group
from src.zevampy.part3_stock_calculation.plot_stock.graph_inputs import config_bev_reference_scenario
from src.zevampy.part4_validate_model.graph_inputs import config_validation_step1, config_validation_step2
from src.zevampy.part4_validate_model.rmse_inputs import config_validation_rmse_step1, config_validation_rmse_step2
from src.zevampy.part5_sensitivity_analysis.graph_inputs import config_sensitivity_1, config_sensitivity_2, \
    config_sensitivity_3, config_sensitivity_4

from src.zevampy.load_data_and_prepare_inputs.dimension_names import *
import warnings


def prepare_inputs(simulation_end_year, config=None):
    """
    Prepares the simulation-related parameters and plot configurations required for the modeling process.

    Organizes and combines simulation-related parameters (e.g., reference years, bounds distributions) and plot
    configuration parameters (e.g., settings for CSP and stock-related graphs).

     Parameters:
        simulation_end_year (int): The final year of the simulation period. Used together with a fixed initial year
                                   to define the simulation stock years range. The simulation end year is determined
                                    based on user inputs provided in CSV files.

    Returns:
        dict: A consolidated dictionary containing:
            - Simulation parameters (e.g., `eu_countries_and_norway`, `stock_years`, `bounds_distributions`).
            - Plot configuration settings for various steps of the analysis.
    """
    model_config = config.get("model", {})
    geography_config = config.get("geography", {})
    powertrains = config.get("powertrains", {})
    initial_stock_year = model_config.get("first_stock_year", initial_simulation_stock_year)
    initial_new_registrations_year = model_config.get("start_new_registration_year", initial_registration_year)
    end_year = model_config.get("end_year", simulation_end_year)
    simulation_stock_years = [initial_stock_year, end_year]
    countries = geography_config.get("countries") or eu_countries_and_norway
    use_clusters = geography_config.get("use_clusters", default_use_clusters)
    csp_ref_year = model_config.get("csp_reference_year", csp_data_ref_year)
    csp_avail_years = model_config.get("csp_available_years", csp_available_years)
    historical_csp_active = model_config.get("historical_csp", historical_csp)

    # Simulation-related parameters
    inputs_simulation = {
        countries_selected_label: countries,
        simulation_stock_years_label: simulation_stock_years,
        csp_data_ref_year_label: csp_ref_year,
        csp_available_years_label: csp_avail_years,
        historical_csp_label: historical_csp_active,
        save_options_stock_label: save_options_stock,
        save_fitted_csp_values_label: save_fitted_csp_values,
        distribution_bounds_label: distribution_bounds,
        powertrain_dim: powertrains,
        initial_registration_year_label: initial_new_registrations_year,
        use_clusters_label: use_clusters
    }
    # Plot configuration parameters
    inputs_plot_configuration = {
        config_all_label: config_all,
        config_group_label: config_group,
        config_bev_reference_scenario_label: config_bev_reference_scenario,
        config_validation_step1_label: config_validation_step1,
        config_validation_step2_label: config_validation_step2,
        config_validation_rmse_step1_label: config_validation_rmse_step1,
        config_validation_rmse_step2_label: config_validation_rmse_step2,
        config_sensitivity_1_label: config_sensitivity_1,
        config_sensitivity_2_label: config_sensitivity_2,
        config_sensitivity_3_label: config_sensitivity_3,
        config_sensitivity_4_label: config_sensitivity_4,
    }
    inputs = {
        **inputs_simulation,
        **inputs_plot_configuration
    }
    x_lim = tuple(simulation_stock_years)
    for plot_config_label in [
        config_bev_reference_scenario_label,
        config_sensitivity_1_label,
        config_sensitivity_2_label,
        config_sensitivity_3_label,
        config_sensitivity_4_label,
    ]:
        inputs[plot_config_label]["plot_params"]["x_lim"] = x_lim

    available_registration_history = (initial_stock_year - initial_new_registrations_year)+1
    if available_registration_history < csp_avail_years:
        if available_registration_history < csp_avail_years:
            raise ValueError(
                "Invalid model configuration: not enough historical registration data "
                "to calculate stock accurately.\n\n"

                f"start_new_registration_year = {initial_new_registrations_year}\n"
                f"first_stock_year = {initial_stock_year}\n"
                f"csp_available_years = {csp_avail_years}\n"
                f"available history = {available_registration_history} years\n\n"

                "Requirement:\n"
                "first_stock_year - start_new_registration_year >= csp_available_years\n\n"

                "How to fix:\n"
                f"- Set first_stock_year >= {initial_new_registrations_year + csp_avail_years-1}\n"
                f"- OR provide older start_new_registration_year <= {initial_stock_year-csp_avail_years+1}\n"
                "- OR reduce csp_available_years (⚠ may reduce accuracy of stock estimation)\n\n"

                "Note:\n"
                "Typical configuration uses ~45 years of CSP data. "
                "Using fewer years may undercount older vehicle stock."
            )
    if csp_avail_years < 45:
        warnings.warn(
            "csp_available_years is lower than the typical value of 45 years. "
            "This truncates the survival function and may lead to systematic "
            "underestimation of older vehicle cohorts. As a result, absolute "
            "vehicle stock levels are likely to be underestimated. The shorter "
            "the CSP time horizon, the stronger this bias becomes.",
            UserWarning
        )
    return inputs
