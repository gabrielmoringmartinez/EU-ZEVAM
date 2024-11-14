import pandas as pd

time_dim = 'time'


def calculate_empirical_survival_rates(stock, registrations, stock_year):
    """
        Calculates the empirical survival rates for vehicles by merging and dividing stock data and registrations.

        Args:
            stock (pd.DataFrame): DataFrame containing vehicle stock data, including 'vehicle age' and
                                  'number of registered vehicles'.
            registrations (pd.DataFrame): DataFrame containing vehicle registration data with 'year' and
                                          'new vehicle registrations'.
            stock_year (pd.DataFrame): DataFrame containing the 'stock year' information by country.

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
        Filters a DataFrame to retain only rows where 'vehicle age' is within the specified range.

        Args:
            df (pd.DataFrame): DataFrame with a 'vehicle age' column to filter.
            min_age (int): Minimum vehicle age to retain (inclusive). Default is 1.
            max_age (int): Maximum vehicle age to retain (inclusive). Default is 45.

        Returns:
            pd.DataFrame: Filtered DataFrame with 'vehicle age' values between min_age and max_age.
        """
    return df[(df['vehicle age'] >= min_age) & (df['vehicle age'] <= max_age)]


def prepare_registrations_data(registrations, stock_year):
    """
        Merges registration data with stock year information, calculates 'vehicle age', and filters the result.

        Args:
            registrations (pd.DataFrame): DataFrame containing vehicle registration data with 'year' and 'geo country'.
            stock_year (pd.DataFrame): DataFrame containing 'stock year' information for each 'geo country'.

        Returns:
            pd.DataFrame: A DataFrame with added 'vehicle age' column, filtered to include only relevant ages.
        """
    # Merge to get stock year, calculate vehicle age, and filter
    registrations = pd.merge(registrations, stock_year, on='geo country', how='left')
    # Calculates the vehicle age in a certain stock year based on the new registrations year
    registrations['vehicle age'] = registrations['stock year'] - registrations[time_dim] + 1
    # Keeps only values between 1 and 45
    registrations = filter_vehicle_age(registrations)
    return registrations


def obtain_survival_rates(stock, registrations):
    """
        Calculates survival rates by merging and dividing stock and registrations data on 'geo country'
        and 'vehicle age'.

        Args:
            stock (pd.DataFrame): DataFrame containing 'geo country', 'vehicle age', and
                                  'number of registered vehicles'.
            registrations (pd.DataFrame): DataFrame with 'geo country','vehicle age', and 'new vehicle registrations'.

        Returns:
            pd.DataFrame: A DataFrame containing 'geo country', 'vehicle age', and the empirical 'survival rate'.
        """
    # Merge with selected columns and calculate survival rate
    survival_rates = pd.merge(stock, registrations[['geo country', 'new vehicle registrations', 'vehicle age']],
                              on=['vehicle age', 'geo country'], how='left')
    # Divide stock of a certain vehicle age at a certain stock year by the new registrations at the vehicle age's year to obtain the survival rate
    survival_rates['survival rate'] = survival_rates['number of registered vehicles'] / survival_rates[
        'new vehicle registrations']
    survival_rates = survival_rates[['geo country', 'vehicle age', 'survival rate']]

    return survival_rates


def save_dataframes(survival_rates):
    """Saves the empirical survival rates to CSV files."""
    survival_rates.to_csv('outputs/2_2_empirical_survival_rates_eu_countries_2021.csv', sep=';', index=False, decimal=',')
