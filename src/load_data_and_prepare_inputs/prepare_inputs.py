from src.part1_transportation_model.input_data import eu_countries_and_norway
from src.part2_survival_rates.input_data import distribution_bounds
from src.part3_stock_calculation.calculate_stock.input_data import stock_years, historical_csp, save_options_stock, \
    csp_data_ref_year, csp_available_years
from src.part2_survival_rates.plot_survival_rates.graph_inputs import config_all, config_group
from src.part3_stock_calculation.plot_stock.graph_inputs import config_bev_reference_scenario
from src.part4_validate_model.graph_inputs import config_validation_step1, config_validation_step2
from src.part4_validate_model.rmse_inputs import config_validation_rmse_step1, config_validation_rmse_step2
from src.part5_sensitivity_analysis.graph_inputs import config_sensitivity_1, config_sensitivity_2, \
    config_sensitivity_3, config_sensitivity_4

def prepare_inputs():
    """
        Prepares the simulation-related parameters and plot configurations required for the modeling process.

        Organizes and combines simulation-related parameters (e.g., reference years, bounds distributions) and plot
        configuration parameters (e.g., settings for CSP and stock-related graphs).

        Returns:
            dict: A consolidated dictionary containing:
                - Simulation parameters (e.g., `eu_countries_and_norway`, `stock_years`, `bounds_distributions`).
                - Plot configuration settings for various steps of the analysis.
        """
    # Simulation-related parameters
    inputs_simulation = {
        "eu_countries_and_norway": eu_countries_and_norway,
        "stock_years": stock_years,
        "csp_data_ref_year": csp_data_ref_year,
        "csp_available_years": csp_available_years,
        "historical_csp": historical_csp,
        "save_options_stock": save_options_stock,
        "distribution_bounds": distribution_bounds
    }
    # Plot configuration parameters
    inputs_plot_configuration = {
        "config_all": config_all,
        "config_group": config_group,
        "config_bev_reference_scenario": config_bev_reference_scenario,
        "config_validation_step1": config_validation_step1,
        "config_validation_step2": config_validation_step2,
        "config_validation_rmse_step1": config_validation_rmse_step1,
        "config_validation_rmse_step2": config_validation_rmse_step2,
        "config_sensitivity_1": config_sensitivity_1,
        "config_sensitivity_2": config_sensitivity_2,
        "config_sensitivity_3": config_sensitivity_3,
        "config_sensitivity_4": config_sensitivity_4,
    }
    inputs = {
        **inputs_simulation,
        **inputs_plot_configuration
    }
    return inputs
