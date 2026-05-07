# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

from src.zevampy.part2_survival_rates.plot_survival_rates.plot_all_countries import plot_all_countries
from src.zevampy.load_data_and_prepare_inputs.dimension_names import *


def plot_stock_shares(stock_shares, config_scenario, powertrains):
    columns_to_plot = {share_dim: share_dim.capitalize()}

    for pt in stock_shares[powertrain_dim].unique():

        stock_subset = stock_shares[
            stock_shares[powertrain_dim] == pt
            ]

        if stock_subset.empty:
            continue

        # Optional: add label for filename
        config_local = config_scenario.copy()
        config_local[file_info_dim] = config_local[file_info_dim].copy()
        pt_file = pt.replace(" ", "_")
        config_local[file_info_dim][additional_info_dim] = (
                config_local[file_info_dim].get(additional_info_dim, "") + f"_{pt_file}"
        )

        plot_all_countries(
            stock_subset,
            config_local,
            columns_to_plot,
            None
        )
