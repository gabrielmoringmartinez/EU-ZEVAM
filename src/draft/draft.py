import pandas as pd

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


historical_registrations_ = pd.merge(historical_registrations, stock_year, how='left')
historical_registrations_ = adapt_registrations_to_vehicle_stock_year(historical_registrations_)