def calculate_year_of_first_registration(survival_rates, time_dimension, stock_year_col='stock_year',
                                         age_col='vehicle age'):
    """
        Calculates the year of first registration for each entry in the DataFrame based on stock year and vehicle age.

        Parameters:
            survival_rates (DataFrame): Data containing stock year and vehicle age.
            time_dimension (str): Column name to store the calculated year of first registration.
            stock_year_col (str): Column name representing the year of stock (default: 'stock_year').
            age_col (str): Column name representing vehicle age (default: 'vehicle age').

        Returns:
            DataFrame: Updated DataFrame with calculated year of first registration.
        """
    survival_rates[time_dimension] = survival_rates[stock_year_col] - survival_rates[age_col] + 1
    return survival_rates
