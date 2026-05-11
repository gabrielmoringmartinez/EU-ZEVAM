"""Append RMSE evaluation results to result collections."""

# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT


def append_values(rmse_rows, country, timeframe, powertrain, i, rmse):
    """
    Append RMSE evaluation results to a result list.

    Parameters:
        rmse_rows (list[dict]):
            List storing RMSE evaluation results.

        country (str):
            Country name.

        timeframe (list[int]):
            Evaluation timeframe defined by start and end year.

        powertrain (str):
            Powertrain category.

        i (str):
            Scenario identifier.

        rmse (float):
            Calculated RMSE value.

    Returns:
        list[dict]:
            Updated list containing appended RMSE results.
    """
    rmse_rows.append({
        'Country': country,
        'Timeframe': timeframe,
        'Powertrain': powertrain,
        'Scenario': i,
        'RMSE': rmse,
    })
    return rmse_rows
