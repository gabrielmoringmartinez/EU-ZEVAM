import os
def test_required_input_files_exist():
    # Define required input files by category
    essential_inputs = [
        "0_country_clusters.csv",
        "1_1_new_registrations_by_fuel_type_1970_2050_clusters.csv",
        "1_2_A_2_new_registrations_data_passenger_cars_eu_countries_1970_2021.csv",
        "1_3_new_registrations_2022_2050_cam_scenario.csv",
        "2_1_A_1_age_resolved_data_passenger_car_stock_fleet_eu_countries_2021.csv",
        "2_2_A_1_stock_year.csv",
    ]

    validation_inputs = [
        "4_1_eafo_ev_new_registration_shares.csv",
        "4_2_eafo_ev_stock_shares.csv"

    ]

    sensitivity_inputs = [
        "5_1_oguchi_2008_survival_rate_parameters.csv",
        "5_2_held_2016_survival_rates.csv"
    ]

    all_required_files = {
        "essential": essential_inputs,
        "validation": validation_inputs,
        "sensitivity": sensitivity_inputs
    }

    for category, files in all_required_files.items():
        for file in files:
            file_path = os.path.join("inputs", file)
            assert os.path.exists(file_path), f"Missing {category} input file: {file_path}"