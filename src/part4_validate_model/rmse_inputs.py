POWERTRAINS = [["BEV"]]
TIMEFRAMES = [[2014, 2023]]
title_step1 = "validation_step_1_actual_new_bev_registrations_and_empirical_csp_curves_all_countries"
title_step2 = "validation_step_2_estimated_new_bev_registrations_and_empirical_csp_curves_all_countries"
# First dictionary for STEP1
config_rmse_validation_step1 = {
    "powertrains": POWERTRAINS,
    "timeframes": TIMEFRAMES,
    "title": title_step1
}

# Second dictionary for STEP2 (reuse and override title)
config_rmse_validation_step2 = {**config_rmse_validation_step1, "title": title_step2}