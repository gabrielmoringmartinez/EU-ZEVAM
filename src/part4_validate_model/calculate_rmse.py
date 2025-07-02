# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

import pandas as pd
import numpy as np
from src.part4_validate_model.append_values import append_values
from src.load_data_and_prepare_inputs.dimension_names import *


def calculate_rmse(df, config):
    """
       Calculates the Root Mean Squared Error (RMSE) for the stock DataFrame based on the provided configuration.

       Parameters:
           df (pd.DataFrame): DataFrame containing the predicted and actual share values.
           config (dict): Configuration dictionary containing powertrains, timeframes, and title. Config can be edited
           in rmse_inputs.py

       Returns:
           None: Outputs the RMSE results to a CSV file.
       """
    df = df.copy()
    df['error'] = df[share_dim] - df[f'actual {share_dim}']
    df['squared_error'] = df['error'] ** 2
    # Collect RMSE results for each group
    rows_rmse = []
    countries = df[country_dim].unique()

    for powertrain in config[powertrains_rmse_label]:
        filtered_powertrain_df = df[df[powertrain_dim].isin(powertrain)]

        for timeframe in config[timeframes_rmse_label]:
            filtered_timeframe_df = filtered_powertrain_df[filtered_powertrain_df[stock_year_dim].between(timeframe[0],
                                                                                                          timeframe[1])]
            m = (timeframe[1] - timeframe[0])+1

            for country in countries:
                filtered_country_df = filtered_timeframe_df[filtered_timeframe_df[country_dim] == country]
                sum_squared_errors = filtered_country_df['squared_error'].sum()
                rmse = np.sqrt((1 / m) * sum_squared_errors)
                append_values(rows_rmse, country, timeframe, powertrain, 'real values', rmse)

    rmse_df = pd.DataFrame(rows_rmse)
    rmse_df.to_csv(f'outputs/{config[title_dim]}.csv', sep=';', index=False, decimal=',')
    return


