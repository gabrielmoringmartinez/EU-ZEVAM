from src.part1_transportation_model.input_data import eu_countries_and_norway
from src.part3_stock_calculation.calculate_stock.input_data import stock_years, historical_csp, save_options_stock, \
    csp_data_ref_year
from src.part2_survival_rates.plot_survival_rates.graph_inputs import config_all, config_group
from src.part3_stock_calculation.plot_stock.graph_inputs import config_bev_reference_scenario
from src.part4_validate_model.graph_inputs import config_validation_step1, config_validation_step2
from src.part4_validate_model.rmse_inputs import config_validation_rmse_step1, config_validation_rmse_step2
from src.part5_sensitivity_analysis.graph_inputs import config_sensitivity_1, config_sensitivity_2, \
    config_sensitivity_3, config_sensitivity_4

def prepare_inputs():
    # Simulation-related parameters
    inputs_simulation = {
        "eu_countries_and_norway": eu_countries_and_norway,
        "stock_years": stock_years,
        "csp_data_ref_year": csp_data_ref_year,
        "historical_csp": historical_csp,
        "save_options_stock": save_options_stock,
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
