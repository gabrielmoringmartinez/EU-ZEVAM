import pandas as pd


def replace_powertrain_share_registrations_with_country(registrations, country):
    year_country_replied = 2024
    registrations = registrations.copy()
    # Selecting rows for the specific country label
    country_data = registrations[registrations['geo country'] == country]
    # Split the country data into before 2024 and from 2024 onwards
    country_data_before_2024 = country_data[country_data['time'] < year_country_replied]
    country_data_from_2024 = country_data[country_data['time'] >= year_country_replied]

    # Select survival rates for the specified country from 2024 onwards
    country_registrations_share_from_2024 = country_data_from_2024[['time', 'powertrain', 'relative sales', 'registrations by powertrain']]

    # Merge survival rates from 2024 onwards with the original DataFrame for all countries
    registrations_merged = pd.merge(registrations, country_registrations_share_from_2024,
        on=['time', 'powertrain'], suffixes=('', f'_{country}'), how='left')

    # Replace values from 2024 onwards
    registrations_merged.loc[registrations_merged['time'] >= year_country_replied, 'relative sales'] = registrations_merged[
        f'relative sales_{country}']
    registrations_merged.loc[registrations_merged['time'] >= year_country_replied, 'registrations by powertrain'] \
        = registrations_merged[f'registrations by powertrain_{country}']

    # Drop the temporary columns
    registrations_merged.drop(columns=[f'relative sales_{country}', f'registrations by powertrain_{country}']
                              , inplace=True)
    registrations_merged['registrations by powertrain'] = registrations_merged['new vehicle registrations'] * registrations_merged['relative sales']
    return registrations_merged