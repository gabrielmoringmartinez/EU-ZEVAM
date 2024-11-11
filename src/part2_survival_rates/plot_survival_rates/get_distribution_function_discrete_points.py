import pandas as pd


def get_distribution_function_discrete_points(survival_rate_distribution_function, survival_rates_country,
                                              predicted_function_value):
    """
        Updates the distribution function DataFrame with the predicted values for a given country.

        Parameters:
        - survival_rate_distribution_function (pd.DataFrame): DataFrame of the the saved countries'
         survival probability values.
        - survival_rates_country (pd.DataFrame): DataFrame of the survival rates for a specific country.
        - predicted_function_value (list): List of predicted survival probability values.

        Returns:
        - survival_rate_distribution_function (pd.DataFrame): Updated DataFrame with the predicted values
        for the country.
        """
    survival_rates_country = survival_rates_country.reset_index()  # for reseting the index
    survival_rates_country = survival_rates_country.drop(['index'], axis=1)  # deleting the new column of index
    survival_rates_country['survival rate'] = predicted_function_value
    survival_rate_distribution_function = pd.concat([survival_rate_distribution_function, survival_rates_country],
                                                    ignore_index=True)
    return survival_rate_distribution_function
