# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

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
