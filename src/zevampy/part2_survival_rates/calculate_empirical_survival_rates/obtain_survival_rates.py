# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

import pandas as pd
from zevampy.load_data_and_prepare_inputs.dimension_names import age_dim, country_dim, new_registrations_dim, \
    survival_rate_dim, number_registered_vehicles_dim


def obtain_survival_rates(stock, registrations, survival_grouping):
    """
        Calculates survival rates by merging and dividing stock and registrations data on country_dim
        and age_dim.

        Args:
            stock (pd.DataFrame): DataFrame containing country_dim, age_dim, and number_registered_vehicles_dim.
            registrations (pd.DataFrame): DataFrame with country_dim,age_dim, and new_registrations dim.

        Returns:
            pd.DataFrame: A DataFrame containing country_dim, age_dim, and the empirical survival_rate_dim.
        """
    # Merge with selected columns and calculate survival rate

    merge_cols = survival_grouping + [age_dim]
    survival_rates = pd.merge(stock, registrations[merge_cols + [new_registrations_dim]],
                              on=merge_cols, how='left')
    # Divide stock of a certain vehicle age at a certain stock year by the new registrations at the vehicle age's year
    # to obtain the survival rate
    survival_rates[survival_rate_dim] = survival_rates[number_registered_vehicles_dim] / \
                                        survival_rates[new_registrations_dim]

    survival_rates = survival_rates[
        merge_cols + [survival_rate_dim]
        ]

    return survival_rates

