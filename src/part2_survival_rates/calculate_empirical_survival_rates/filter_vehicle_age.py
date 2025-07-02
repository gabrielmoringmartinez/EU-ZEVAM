# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

from src.load_data_and_prepare_inputs.dimension_names import age_dim


def filter_vehicle_age(df, min_age=1, max_age=45):
    """
        Filters a DataFrame to retain only rows where vehicle age is within the specified range.

        Args:
            df (pd.DataFrame): DataFrame with a 'vehicle age' column to filter.
            min_age (int): Minimum vehicle age to retain (inclusive). Default is 1.
            max_age (int): Maximum vehicle age to retain (inclusive). Default is 45.

        Returns:
            pd.DataFrame: Filtered DataFrame with age_dim values between min_age and max_age.
        """
    return df[(df[age_dim] >= min_age) & (df[age_dim] <= max_age)]
