from src.loader.loader import *
from src.part1_transportation_model.input_data import eu_countries_and_norway
from src.part1_transportation_model.calculate_registrations import calculate_registrations

registrations = calculate_registrations(historical_registrations, eu_countries_and_norway, country_labels,
                                                 registrations_eu_cam_scenario, clusters, registration_shares_by_cluster)