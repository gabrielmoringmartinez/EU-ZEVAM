"""Update registration shares using observed BEV registration data."""

# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

from zevampy.part4_validate_model.use_bev_and_phev_actual_values import use_bev_and_phev_actual_values
from zevampy.part4_validate_model.update_other_powertrain_shares import update_other_powertrain_shares


def update_bev_registration_shares_with_real_values(registrations, actual_bev_registration_shares):
    """
    Update registration shares using observed BEV data.

    This function replaces modelled BEV registration shares with observed values and adjusts the remaining powertrain
    shares accordingly.

    Parameters:
        registrations (pandas.DataFrame):
            DataFrame containing modelled vehicle registrations.

        actual_bev_registration_shares (pandas.DataFrame):
            DataFrame containing observed BEV registration shares.

    Returns:
        pandas.DataFrame:
            Updated registration dataset containing adjusted powertrain shares.
    """
    registrations_with_real_bev_shares = use_bev_and_phev_actual_values(registrations, actual_bev_registration_shares)
    registrations_with_real_bev_shares = update_other_powertrain_shares(registrations_with_real_bev_shares)
    return registrations_with_real_bev_shares
