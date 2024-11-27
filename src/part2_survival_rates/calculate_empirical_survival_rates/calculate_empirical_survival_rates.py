import pandas as pd

from src.load_data_and_prepare_inputs.dimension_names import *


def calculate_empirical_survival_rates(stock, registrations, stock_year):
    """
        Calculates the empirical survival rates for vehicles by merging and dividing stock data and registrations.

        Args:
            stock (pd.DataFrame): DataFrame containing vehicle stock data, including 'vehicle age' and
                                  number_registered_vehicles_dim.
            registrations (pd.DataFrame): DataFrame containing vehicle registration data with 'year' and
                                          new_registrations_dim.
            stock_year (pd.DataFrame): DataFrame containing the stock_year_dim information by country.

        Returns:
            pd.DataFrame: A DataFrame containing the calculated survival rates with columns ['geo country',
                          'vehicle age', 'survival rate'].
        """
    # Filter stock data for vehicle age range
    stock = filter_vehicle_age(stock)
    # Prepare registrations data and calculate survival rates
    registrations = prepare_registrations_data(registrations, stock_year)
    survival_rates = obtain_survival_rates(stock, registrations)
    # Save outputs
    save_dataframes(survival_rates)
    return survival_rates


def filter_vehicle_age(df, min_age=1, max_age=45):
    """
        Filters a DataFrame to retain only rows where vehicle age is within the specified range.

        Args:
            df (pd.DataFrame): DataFrame with a 'vehicle age' column to filter.
            min_age (int): Minimum vehicle age to retain (inclusive). Default is 1.
            max_age (int): Maximum vehicle age to retain (inclusive). Default is 45.

        Returns:
            pd.DataFrame: Filtered DataFrame with age_dim values between min_age and max_age.
        """
    return df[(df[age_dim] >= min_age) & (df[age_dim] <= max_age)]


def prepare_registrations_data(registrations, stock_year):
    """
        Merges registration data with stock year information, calculates vehicle age (age_dim), and filters the result.

        Args:
            registrations (pd.DataFrame): DataFrame containing vehicle registration data with 'year' and country_dim.
            stock_year (pd.DataFrame): DataFrame containing stock_year_dim information for each country_dim.

        Returns:
            pd.DataFrame: A DataFrame with added age_dim column, filtered to include only relevant ages.
        """
    # Merge to get stock year, calculate vehicle age, and filter
    registrations = pd.merge(registrations, stock_year, on=country_dim, how='left')
    # Calculates the vehicle age in a certain stock year based on the new registrations year
    registrations[age_dim] = registrations[stock_year_empirical_csp_data_dim] - registrations[time_dim] + 1
    # Keeps only values between 1 and 45
    registrations = filter_vehicle_age(registrations)
    return registrations


def obtain_survival_rates(stock, registrations):
    """
        Calculates survival rates by merging and dividing stock and registrations data on country_dim
        and age_dim.

        Args:
            stock (pd.DataFrame): DataFrame containing country_dim, age_dim, and number_registered_vehicles_dim.
            registrations (pd.DataFrame): DataFrame with country_dim,age_dim, and new_registrations dim.

        Returns:
            pd.DataFrame: A DataFrame containing country_dim, age_dim, and the empirical survival_rate_dim.
        """
    # Merge with selected columns and calculate survival rate
    survival_rates = pd.merge(stock, registrations[[country_dim, new_registrations_dim, age_dim]],
                              on=[age_dim, country_dim], how='left')
    # Divide stock of a certain vehicle age at a certain stock year by the new registrations at the vehicle age's year
    # to obtain the survival rate
    survival_rates[survival_rate_dim] = survival_rates[number_registered_vehicles_dim] / \
                                        survival_rates[new_registrations_dim]
    survival_rates = survival_rates[[country_dim, age_dim, survival_rate_dim]]

    return survival_rates


def save_dataframes(survival_rates):
    """Saves the empirical survival rates to CSV files."""
    survival_rates.to_csv('outputs/2_2_empirical_survival_rates_eu_countries_2021.csv', sep=';', index=False,
                          decimal=',')
