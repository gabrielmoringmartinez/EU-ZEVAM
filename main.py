from src.loader.loader import *
from src.part1_transportation_model.input_data import eu_countries_and_norway
from src.part1_transportation_model.calculate_registrations import calculate_registrations
from src.part2_survival_rates.calculate_csp_parameters import calculate_csp_parameters



optimum_parameters_wg = calculate_csp_parameters(survival_rates_2021, 2021)


def adapt_registrations_to_vehicle_stock_year(historical_registrations):
# This is necessary to afterwards calculate the stock!!!
    country_label = []
    vehicle_age = []
    new_registrations = []

    for index, row in historical_registrations.iterrows():
        if row['stock year'] >= row['time']:
            country_label.append(row['country label'])
            vehicle_age.append(row['stock year'] - row['time'] + 1)
            new_registrations.append(row['new vehicle registrations'])

    my_dict = {'country label': country_label, 'vehicle age': vehicle_age, 'new registrations': new_registrations}
    return my_dict




registrations = calculate_registrations(historical_registrations, eu_countries_and_norway, country_labels,
                                                 registrations_eu_cam_scenario, clusters, registration_shares_by_cluster)
historical_registrations = pd.merge(historical_registrations, stock_year, how='left')
historical_registrations = adapt_registrations_to_vehicle_stock_year(historical_registrations)