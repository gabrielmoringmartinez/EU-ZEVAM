from src.load_data_and_prepare_inputs.dimension_names import *

POWERTRAINS = [["BEV"]]
TIMEFRAMES = [[2014, 2023]]
title_step1 = "4_1_rmse_validation_step_1_actual_new_bev_registrations_and_empirical_csp_curves_all_countries"
title_step2 = "4_2_rmse_validation_step_2_estimated_new_bev_registrations_and_empirical_csp_curves_all_countries"
# First dictionary for STEP1
config_validation_rmse_step1 = {
    powertrains_rmse_label: POWERTRAINS,
    timeframes_rmse_label: TIMEFRAMES,
    title_dim: title_step1
}

# Second dictionary for STEP2 (reuse and override title)
config_validation_rmse_step2 = {**config_validation_rmse_step1, title_dim: title_step2}