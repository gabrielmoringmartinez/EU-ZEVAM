import pandas as pd

from src.load_data_and_prepare_inputs.dimension_names import survival_rate_dim


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
    # Get the unique geo country
    geo_country = survival_rates_country['geo country'].unique()[0]

    # Create a new DataFrame with years until 60 and survival_rate as 0
    data_extended = {
        "geo country": [geo_country] * 60,
        "vehicle age": list(range(1, 61)),
        "survival rate": [0] * 60
    }

    # Create the extended DataFrame
    survival_rates_country = pd.DataFrame(data_extended)

    survival_rates_country[survival_rate_dim] = predicted_function_value
    survival_rate_distribution_function = pd.concat([survival_rate_distribution_function, survival_rates_country],
                                                    ignore_index=True)
    return survival_rate_distribution_function
