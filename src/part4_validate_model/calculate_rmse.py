import pandas as pd
from itertools import islice
import numpy as np


def calculate_rmse(df, config):
    """
       Calculates the Root Mean Squared Error (RMSE) for the stock DataFrame based on the provided configuration.

       Parameters:
           df (pd.DataFrame): DataFrame containing the predicted and actual share values.
           config (dict): Configuration dictionary containing powertrains, timeframes, and title.

       Returns:
           None: Outputs the RMSE results to a CSV file.
       """
    df = df.copy()
    df['error'] = df['share'] - df['actual share']
    df['squared_error'] = df['error'] ** 2
    # Collect RMSE results for each group
    rows_rmse = []
    countries = df['geo country'].unique()

    for powertrain in config['powertrains']:
        filtered_powertrain_df = df[df['powertrain'].isin(powertrain)]

        for timeframe in config['timeframes']:
            filtered_timeframe_df = filtered_powertrain_df[filtered_powertrain_df['stock_year'].between(timeframe[0], timeframe[1])]
            m = (timeframe[1] - timeframe[0])+1

            for country in countries:
                filtered_country_df = filtered_timeframe_df[filtered_timeframe_df['geo country'] == country]
                sum_squared_errors = filtered_country_df['squared_error'].sum()
                rmse = np.sqrt((1 / m) * sum_squared_errors)
                append_values(rows_rmse, country, timeframe, powertrain, 'real values', rmse)

    rmse_df = pd.DataFrame(rows_rmse)
    rmse_df.to_csv(f'outputs/rmse_{config["title"]}.csv', sep=';', index=False, decimal=',')
    return


def append_values(rmse_rows, country, timeframe, powertrain, i, rmse):
    """
        Appends the RMSE result for a specific country, timeframe, and powertrain to the results list.

        Parameters:
            rmse_rows (list): The list to append the RMSE result to.
            country (str): The country name.
            timeframe (list): The timeframe (start year, end year).
            powertrain (str): The powertrain type.
            scenario (str): The scenario name (e.g., 'real values').
            rmse (float): The calculated RMSE value.

        Returns:
            None
        """
    rmse_rows.append({
        'Country': country,
        'Timeframe': timeframe,
        'Powertrain': powertrain,
        'Scenario': i,
        'RMSE': rmse,
    })
    return rmse_rows