# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

def save_dataframes(survival_rates):
    """Saves the empirical survival rates to CSV files."""
    survival_rates.to_csv('outputs/2_2_empirical_survival_rates_eu_countries_2021.csv', sep=';', index=False,
                          decimal=',')
