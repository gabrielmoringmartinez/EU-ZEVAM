from src.part4_validate_model.use_bev_actual_values import use_bev_actual_values
from src.part4_validate_model.update_other_powertrain_shares import update_other_powertrain_shares


def update_bev_registration_shares_with_real_values(registrations, actual_bev_registration_shares):
    """
        Updates registration shares with actual BEV registration data and adjusts other powertrain shares.
        Args:
            registrations (DataFrame): A DataFrame with vehicle registrations by powertrain, including historical
            and projected data.
            actual_bev_registration_shares (DataFrame): Actual BEV registration shares.
        Returns:
            registrations_with_real_bev_shares (DataFrame): registrations dataframe with the updated BEV and PHEV new registrations
            and also the other powertrains are updated
        """
    registrations_with_real_bev_shares = use_bev_actual_values(registrations, actual_bev_registration_shares)
    registrations_with_real_bev_shares = update_other_powertrain_shares(registrations_with_real_bev_shares)
    return registrations_with_real_bev_shares