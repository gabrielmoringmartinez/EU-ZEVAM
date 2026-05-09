# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

def save_dataframes(survival_rates, output_path):
    """Saves the empirical survival rates to CSV files."""
    survival_rates.to_csv(f'{output_path}/2_2_empirical_survival_rates.csv', sep=';', index=False,
                          decimal=',')
