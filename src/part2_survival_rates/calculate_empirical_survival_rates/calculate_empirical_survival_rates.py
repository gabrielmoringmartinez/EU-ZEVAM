import pandas as pd

from src.part2_survival_rates.calculate_empirical_survival_rates.filter_vehicle_age import filter_vehicle_age
from src.part2_survival_rates.calculate_empirical_survival_rates.prepare_registrations_data import \
    prepare_registrations_data
from src.part2_survival_rates.calculate_empirical_survival_rates.obtain_survival_rates import obtain_survival_rates
from src.part2_survival_rates.calculate_empirical_survival_rates.save_dataframes import save_dataframes


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


