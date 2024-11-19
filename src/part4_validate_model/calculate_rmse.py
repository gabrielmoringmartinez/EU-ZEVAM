import pandas as pd
from itertools import islice
import numpy as np


def calculate_rmse(df, config):
    df = df.copy()
    df['error'] = df['share'] - df['actual share']
    df['squared_error'] = (df['share'] - df['actual share']) ** 2
    rows_rmse = []
    countries = df['geo country'].unique()
    for powertrain in config['powertrains']:
        # Filter the DataFrame
        filtered_powertrain_df = df[df['powertrain'].isin(powertrain)]
        for timeframe in config['timeframes']:
            filtered_timeframe_df = filtered_powertrain_df[filtered_powertrain_df['stock_year'].between(timeframe[0], timeframe[1])]
            m = (timeframe[1] - timeframe[0])+1
            for country in countries:
                filtered_country_df = filtered_timeframe_df[filtered_timeframe_df['geo country'] == country]
                sum_squared_errors = filtered_country_df['squared_error'].sum()
                average_error = abs(filtered_country_df['error']).mean()
                rmse = np.sqrt((1 / m) * sum_squared_errors)
                append_values(rows_rmse, country, timeframe, powertrain, 'real values', rmse)

    rmse_df = pd.DataFrame(rows_rmse)
    title = config['title']
    rmse_df.to_csv(f'outputs/rmse_{title}.csv', sep=';', index=False, decimal=',')
    return

def append_values(rows, country, timeframe, powertrain, i, rmse):
    rows.append({
        'Country': country,
        'Timeframe': timeframe,
        'Powertrain': powertrain,
        'Scenario': i,
        'RMSE': rmse,
    })
    return rows