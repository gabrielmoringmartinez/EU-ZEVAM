from src.load_data_and_prepare_inputs.load_data import load_data
from src.load_data_and_prepare_inputs.prepare_inputs import prepare_inputs


def load_data_and_prepare_inputs():
    """
    Combines the functionality of loading data and preparing inputs for the simulation and plot configurations.

    This function calls two sub-functions:
    1. `load_data`: Loads all required datasets from CSV files.
    2. `prepare_inputs`: Prepares and organizes simulation-related parameters and plot configurations.

    Returns:
        tuple:
            - `data` (dict): A dictionary containing loaded datasets with their names as keys.
            - `inputs` (dict): A dictionary containing simulation parameters and plot configurations.
    """
    data = load_data()
    inputs = prepare_inputs()
    return data, inputs
